import socket
import time
import matplotlib.pyplot as plt
import numpy as np
import time
import threading
import Queue


myq = Queue.Queue(maxsize = 5200+1)


port = 8081
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
s.bind(("",port))  
time.sleep(0.1)
print 'waiting on port:',port,"\n"

def socket_putin():
        
        num =0
        index=0
        breakout=1
        put_flag=1
        while breakout:
            data, addr = s.recvfrom(202)
            if ord(data[200])==1:
                #print "starting catching...",ord(data[200])
                #myq.put(data)
                #print "qsize =",myq.qsize(),"flag =", ord(data[200])
                put_flag=1
                while put_flag:
                    data, addr = s.recvfrom(202)
                    myq.put(data)
                    num +=1

                    #print ord(data[200])
                    if ord(data[200])==1:
                        #print "number of udp in queue: ", num 
                        num =0
                        index+=1

                    while myq.full() == 1:
                        print "queue full size = ",myq.qsize(), "qsize is full ! \n\n"
                        time.sleep(1)
                        #put_flag=0
                        #breakout=0
                        #s.close()
                        #break
                        #print "unnormal ''''"
                        #exit()



class wave_receive_thread(threading.Thread):
    def __init__(self, thread_num=0, timeout=1.0):
        threading.Thread.__init__(self)
        self.thread_num = thread_num

        self.stopped = False
        self.timeout = timeout

    def run(self):
        #print "starting receiving ...","\n"
        #socket_putin()

        subthread = threading.Thread(target=socket_putin, args=())
        subthread.setDaemon(True)
        subthread.start()

        while not self.stopped:
            subthread.join(self.timeout)

        #print('Thread stopped')

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped


class distannce_parse():

    def __init__(self):
        
        self.distance = 0
        self.treshold = 65
        self.delay = 0
        self.allChannelData = []
        self.ptIndex =[]

        self.data_channel_all = []
        self.data_channel0=[]
        self.data_channel1=[]
        self.data_channel2=[]
        self.data_channel3=[]

    def wave_data_catch(self,channel=0):
        #print "before clearing myq.qsize() =",myq.qsize()
        myq.queue.clear() 
        data_temp=[]
        data_get=[]
        self.data_channel_all = []
        self.data_channel0=[]
        self.data_channel1=[]
        self.data_channel2=[]
        self.data_channel3=[]
        time.sleep(0.02)

        breakout_get=1
        data_handle_flag=1
        num_data=0
        while myq.qsize()<=70:
            waiting=[]
        #print "qsize = ", myq.qsize()

        while breakout_get:
            #time.sleep(0.01)
            
            data_get = myq.get()
            #print "starting catching data ... myq.qsize()=", myq.qsize()
            if ord(data_get[200])>0:
                #print "here*************************************************"
                while data_handle_flag:
                    if int(myq.qsize())>=70:
                        data_get = myq.get()
                        num_data+=1
                        for k in range(len(data_get)-1):
                            data_temp.append(ord(data_get[k]))
                            #self.data_channel_all.append(ord(data_get[k]))
                        
                        #try:    
                        #print ord(data_get[200])
                        if ord(data_get[200])==1 and num_data == 67:
                            #print "size of data_temp1 = ",len(data_temp) ,"num_data =", num_data,"-------------"
                            #print "lenght = ",len(data_temp)
                            breakout_get=0
                            data_handle_flag=0
                            num_data=0
                                                           
                            for z1 in range(320):
                                for z2 in range(8):
                                    self.data_channel_all.append(data_temp[z1*32+int(channel)*8+z2])
                                    self.data_channel0.append(data_temp[z1*32+0*8+z2])
                                    self.data_channel1.append(data_temp[z1*32+1*8+z2])
                                    self.data_channel2.append(data_temp[z1*32+2*8+z2])
                                    self.data_channel3.append(data_temp[z1*32+3*8+z2])
                            
                            #print "oneframe_data completed ==============================================="
                            data_temp =[]
                            self.data_channel_all=[]
                            break
                            
                        else:
                            data_get=[]
                            data_channel_all=[]
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
                            self.data_channel_all=[]
                            data_get=[]
                            num_data =0
                            data_handle_flag=0
                            self.data_channel0[:]=[]
                        '''
            
            data_get=[]
               
        #print self.data_channel_all
        #plt.plot(self.data_channel2[0:500],'r.--')  
        #plt.show()  
        return self.data_channel_all

    def pulseSignal(self):

        self.allChannelData = self.data_channel_all

        Id = []
        pulseData_temp = []
        for i in range(len(self.allChannelData)):
            if int(self.allChannelData[i]) >= self.treshold and i >=self.delay and i<=2000:
                Id.append(i)
        
        
        for k in range(len(Id)):
            pulseData_temp.append(self.allChannelData[Id[k]])
        
        #print pulseData
        #print Id
        self.ptIndex = Id
        self.pulseData = pulseData_temp 
        
        #plt.plot(self.ptIndex,self.pulseData,'.--')
        #plt.show()
        return self.pulseData, self.ptIndex
    
    def widthGet(self):
        threshold = 85+75
        y =[arr for arr in self.pulseData]
        x =[arr for arr in self.ptIndex]

        #plt.plot(x,y,'o--')
        #plt.show()
        #print "x=" ,"  len(x)=", len(x)
        #print "y=" ,"  len(y)=", len(y)

        wave=[]
        Id = []

        #print "max(y)=", max(y)
        max_index = y.index(max(y))
        for dis in range(len(y)) :
            if y[dis] >=threshold and x[dis] <= x[max_index]+30:
                Id.append(dis)
        #print "index =",Id
        
        if len(Id)>1 and not(x[Id[0]]==x[0]) and not(y[Id[0]]==y[0]) :  
            #print "len id =", len(Id), " ", Id[0]," ",x[Id[0]]," ", x[0], "x=", x," y=",y
            #Id.insert(0,Id[0]-1)
            Id.insert(0,Id[0]-1)
       
            #Id.append(Id[len(Id)-1]+1)
            Id.append(Id[len(Id)-1]+1)
            Id = np.array(Id)
            x=np.array(x)
            y=np.array(y) 

            #print "len id =", len(Id), " ", Id[0]," ",x[Id[0]]," ", x[0], "x=", x," y=",y
            a=np.array(x[Id])
            b=np.array(y[Id])
            #print "====",a, "   " ,b 
            #print "new index =",    Id

        else:
            Id=[]
            a=[]
            b=[]
            print 'posedge <0 ns,\n'
    
        z = Id
        width_left=0
        width_right=0
        if len(Id)>=3  :
            if float(y[z[1]]-y[z[0]]) and (y[z[-2]]-y[z[-1]]):
                #print float(y[z[-2]]-y[z[-1]]), float(y[z[1]]-y[z[0]])

                width_left = float((x[z[1]]-x[z[0]])*(threshold-y[z[0]]))/float(y[z[1]]-y[z[0]])+float(x[z[0]])
                #print "width_left=", width_left 
                #print "out of size =", len(x),
                width_right = float((y[z[-2]]-threshold)*(x[z[-1]]-x[z[-2]]))/float(y[z[-2]]-y[z[-1]])+float(x[z[-2]])
            
                width = width_right-width_left
                l=[width_left,width_right]
                #print width_left,"ddadf =", width_right
            else:
                width_right=0
                width_left=0
                #print "divided by zero ...."
                #print "x=",x," y=",y

            
        else:
            width = 0
            peak=0
            print 'peak < width-threshold'
    

        #plt.plot(x,y,'*--')
        #plt.plot([width_left,width_right],[threshold,threshold],'ro--')
        #plt.show()
        
        distance = []
        width =round(width_right-width_left,4)
        distance = round(width_left,4)
        print "width = ", width, "  distance = ",distance    

        return width,distance


        

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

    channel_opt = int(options.channel)
    
    #socketReceiv = wave_show.socket_receive()
   
    ret1 = wave_receive_thread()
    ret1.start()
    width_list =[]
    distance_list=[]

    try:
        datahandle = distannce_parse()
        for i in range(100 ):
            time.sleep(0.01)
            pSignal=datahandle.wave_data_catch(0)
            datahandle.pulseSignal()
            w_d = datahandle.widthGet()
            if w_d[0]:

                width_list.append(w_d[0])
                distance_list.append(w_d[1])
            #datahandle.widthGet()
        #plt.plot(pSignal[1],pSignal[0],'o-')
        ret1.stop()
        ret1.join()

    except:
        print "creating treading failed !!!"
        
    #print "threding is over !"
    try:
        print "congratulation to you !"
        #plt.show()
        print width_list, "len(width_list) =", len(width_list)
        print distance_list, "len(distance_list) =", len(distance_list)
        print "width std =", np.std(width_list)," distance std =", np.std(distance_list)
        plt.plot(distance_list,width_list,'bo')
        plt.xlabel(" posedge_of_pulse /ns")
        plt.ylabel(" width_of_pulse /bit")
        plt.title("divergence_of_signal")
        plt.show()

    except:
        print 'widthGetting error!!'

