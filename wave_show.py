import socket  
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import Queue
import time
import numpy

global myq

myq = Queue.Queue(maxsize = 1200+1)
'''
fig1 = plt.figure(1)
ax = plt.subplot(5,1,1,xlim=(0, 13500), ylim=(0,255))
line, = ax.plot([],[],'.-',lw=2)

ax0=plt.subplot(5,1,2,xlim=(0, 3500), ylim=(0,255))
line0, = ax0.plot([],[],'b.-',lw=2)

ax1=plt.subplot(5,1,3,xlim=(0, 3500), ylim=(0,255))
line1, = ax1.plot([],[],'r.-',lw=2)

ax2=plt.subplot(5,1,4,xlim=(0, 3500), ylim=(0,255))
line2, = ax2.plot([],[],'k.-',lw=2)

ax3=plt.subplot(5,1,5,xlim=(0, 3500), ylim=(0,255))
line3, = ax3.plot([],[],'y.-',lw=2)
'''




class socket_receive:
    
    def __init__(self):
        self.data_o=[]
        self.breakout =1#socket receive flag
        self.data_channel0=[]
        self.data_channel1=[]
        self.data_channel2=[]
        self.data_channel3=[]
        self.put_flag =1


        #self.signal_rms=[]

    '''
    def init(self):
        line.set_data([],[])
        return line,
    '''


    def socket_putin(self):
        time.sleep(0.05)
        port = 8081
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
        s.bind(("",port))  
        time.sleep(0.1)
        print 'waiting on port:',port,"\n"
        num =0
        index=0
        while self.breakout:
            data, addr = s.recvfrom(202)
            if ord(data[200])==1:
                #print "starting catching...",ord(data[200])
                #myq.put(data)
                #print "qsize =",myq.qsize(),"flag =", ord(data[200])
                self.put_flag=1
                while self.put_flag:
                    data, addr = s.recvfrom(202)
                    myq.put(data)
                    num +=1

                    #print ord(data[200])
                    if ord(data[200])==1:
                        #print "number of udp in queue: ", num 
                        num =0
                        index+=1

                    while myq.full() == 1:
                        print "queue full size = ",myq.qsize(), "exit out of threading !\n"
                        time.sleep(0.2)
                        self.put_flag=0
                        self.breakout=0
                        #s.close()
                        #break
                        exit()
                        
                    
                    

    def wave_data_catch(self,channel):
        #print "before clearing myq.qsize() =",myq.qsize()
        myq.queue.clear() 
        data_temp=[]
        data_get=[]
        self.data_o[:] = []
        self.data_channel0=[]
        self.data_channel1=[]
        self.data_channel2=[]
        self.data_channel3=[]
        time.sleep(0.1)

        breakout_get=1
        data_handle_flag=1
        num_data=0
        while myq.qsize()<=70:
            waiting=[]
        print "qsize = ", myq.qsize()

        while breakout_get:
            #time.sleep(0.01)
            
            data_get = myq.get()
            #print "starting catching data ... myq.qsize()=", myq.qsize()
            if ord(data_get[200])>0:
                print "here*************************************************"
                while data_handle_flag:
                    if int(myq.qsize())>=70:
                        data_get = myq.get()
                        num_data+=1
                        for k in range(len(data_get)-1):
                            data_temp.append(ord(data_get[k]))
                            self.data_o.append(ord(data_get[k]))
                        
                        #try:    
                        #print ord(data_get[200])
                        if ord(data_get[200])==1 and num_data == 67:
                            print "size of data_temp1 = ",len(data_temp) ,"num_data =", num_data,"-------------"
                            print "lenght = ",len(data_temp)
                            breakout_get=0
                            data_handle_flag=0
                            num_data=0
                                                           
                            for z1 in range(320):
                                for z2 in range(8):
                                    #self.data_o.append(data_temp[z1*32+channel*8+z2])
                                    self.data_channel0.append(data_temp[z1*32+0*8+z2])
                                    self.data_channel1.append(data_temp[z1*32+1*8+z2])
                                    self.data_channel2.append(data_temp[z1*32+2*8+z2])
                                    self.data_channel3.append(data_temp[z1*32+3*8+z2])
                            
                            print "end==============================================="
                            data_temp =[]
                            self.data_o=[]
                            break
                            
                        else:
                            data_get=[]
                            data_o=[]
                            self.data_channel0=[]
                            self.data_channel1=[]
                            self.data_channel2=[]
                            self.data_channel3=[]
                            #print "number of datacatch =",num_data,"myqsize =", myq.qsize()
                            #break
                        '''    
                        except:
                            print "excetion size of data_temp = ",len(data_temp) 
                            data_temp=[]
                            self.data_o=[]
                            data_get=[]
                            num_data =0
                            data_handle_flag=0
                            self.data_channel0[:]=[]
                        '''
            
            data_get=[]
               
        #print self.data_o
        #plt.plot(self.data_channel1[0:500],'.--')  
        #plt.show()  
        return self.data_channel1
'''
    def animate_wave(self,i):
        self.wave_data_catch(channel_opt)
        x = range(len(self.data_o))
        line.set_data(x,self.data_o)
        
        x4 = range(len(self.data_channel0))
        line0.set_data(x4,self.data_channel0)
        line1.set_data(x4,self.data_channel1)
        line2.set_data(x4,self.data_channel2)
        line3.set_data(x4,self.data_channel3)
'''
class wave_receive_thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        #print "starting receiving ...","\n"
        socket_receive().socket_putin()

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
    try:
        thread_catch.start()
        #class_anim1 = animation.FuncAnimation(fig1, socket_receive().animate_wave, init_func=socket_receive().init,interval=100)
        plt.show()
        socket_receive().breakout =0
        exit()
    except:
        print 'animation error!!'