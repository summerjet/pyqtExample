import socket  
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import Queue
import time
import numpy
import csv

myq = Queue.Queue(maxsize = 67*40+1)

fig1 = plt.figure(1)
#ax = plt.subplot(5,1,1,xlim=(0, 13500), ylim=(0,255))
#line, = ax.plot([],[],'.-',lw=2)

ax0=plt.subplot(2,2,1,xlim=(0, 3500), ylim=(0,255))
line0, = ax0.plot([],[],'b.-',lw=2)

ax1=plt.subplot(2,2,2,xlim=(0, 3500), ylim=(0,255))
line1, = ax1.plot([],[],'r.-',lw=2)

ax2=plt.subplot(2,2,3,xlim=(0, 3500), ylim=(0,255))
line2, = ax2.plot([],[],'k.-',lw=2)

ax3=plt.subplot(2,2,4,xlim=(0, 3500), ylim=(0,255))
line3, = ax3.plot([],[],'y.-',lw=2)


port = 8081
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
s.bind(("",port))  
time.sleep(0.1)
print 'waiting on port:',port  

class socket_receive:
    
    def __init__(self):
        self.data_o=[]
        self.breakout =1#socket receive flag
        self.data_channel0=[]
        self.data_channel1=[]
        self.data_channel2=[]
        self.data_channel3=[]
        self.data_get=[1]
        #self.signal_rms=[]

    
    def init(self):
        line0.set_data([],[])
        return line0,

    def socket_putin(self):
        put_flag =1
        while self.breakout:
            data, addr = s.recvfrom(201)
            if ord(data[200])==1:
                myq.put(data)
                print "qsize =",myq.qsize(),"flag =", ord(data[200])
                put_flag=1
                while put_flag:
                    data, addr = s.recvfrom(201)
                    #print "qsize_in	 =",myq.qsize(),"flag =", ord(data[200])
                    if myq.full() == 1:
                        #print "queue full size = ",myq.qsize()
                        time.sleep(0.2)
                        put_flag=0
                        exit()
                        break
                    else:
                        myq.put(data)

    def wave_data_catch(self,channel):
        data_temp=[]
        #channel =int(channel_opt)
        #print "before clearing myq.qsize() =",myq.qsize()
        myq.queue.clear() 
        self.data_o[:] = []
        self.data_channel0[:]=[]
        self.data_channel1[:]=[]
        self.data_channel2[:]=[]
        self.data_channel3[:]=[]
        breakout_get=1
        #print "channel ===================",channel,"==========================="
        
        while breakout_get:
            a=[]
            if int(myq.qsize())>=80:
                self.data_get = myq.get()
                #print "starting catching data ... myq.qsize()=", myq.qsize()
                #print ord(self.data_get[200])
                if ord(self.data_get[200])==1:
                    while True:
                        if not myq.empty():
                            self.data_get = myq.get()
                            for k in range(len(self.data_get)-1):
                                data_temp.append(ord(self.data_get[k]))
                                self.data_o.append(ord(self.data_get[k]))
                                
                            if ord(self.data_get[200])==1:
                                breakout_get=0
                                #print "size of data_temp = ",len(data_temp)                                
                                for z1 in range(414):
                                    for z2 in range(8):
                                        #self.data_o.append(data_temp[z1*32+channel*8+z2])
                                        self.data_channel0.append(data_temp[z1*32+0*8+z2])
                                        self.data_channel1.append(data_temp[z1*32+1*8+z2])
                                        self.data_channel2.append(data_temp[z1*32+2*8+z2])
                                        self.data_channel3.append(data_temp[z1*32+3*8+z2])
                                
                                data_temp[:] =[]
                                
                            
                                break
                        else:
                            pass
                else:
                    pass 
        return self.data_o

    def animate_wave(self,i):
        self.wave_data_catch(channel_opt)
        #x = range(len(self.data_o))
        #line.set_data(x,self.data_o)
        
        x4 = range(len(self.data_channel0))
        line0.set_data(x4,self.data_channel0)
        line1.set_data(x4,self.data_channel1)
        line2.set_data(x4,self.data_channel2)
        line3.set_data(x4,self.data_channel3)
        # data=[]
        # data.append(self.data_channel0)
        # with open ("./waveData.csv","wb") as csvfile:
        #     writer = csv.writer(csvfile)
        #     writer.writerows(data)
        # exit()




class wave_receive_thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        print "starting receiving ...","\n"
        socket_receive().socket_putin()

'''
class wave_show_tread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):  
        print "Starting showing ..."
'''

if __name__ == '__main__':
    
    from optparse import OptionParser
    import sys

    parser = OptionParser(usage="%prog [-v]", version="%prog 1.0")

    parser.add_option(
        "-c", "--channel",help="channel selection",default="0"
    )
    parser.add_option(
        "-n", "--pointNum",help="number of points showed",default="2000"
    )
    parser.add_option(
        "-m", "--multiplotSelect",help="selcting mode of showing",default="1"
    )

    (options, args) = parser.parse_args(sys.argv)

    try:
        thread_catch = wave_receive_thread()

    except:
        print "creating treading failed !!!"

    global channel_opt
    channel_opt = int(options.channel)

    plt.title("channel %d"%int(channel_opt))
    plt.xlabel("time /ns")
    plt.ylabel("ADC signal /bit")
    # try:
    thread_catch.start()
    class_anim1 = animation.FuncAnimation(fig1, socket_receive().animate_wave, init_func=socket_receive().init,interval=100)
    plt.show()

    # socket_receive().breakout =0
    # exit()
    # except:
    #     print 'animation error!!'
