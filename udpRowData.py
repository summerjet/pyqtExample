import socket
import time
import matplotlib.pyplot as plt
import numpy as np
import time
import threading
import Queue

HS_LIDAR_GT_SERIAL_UNIT_SIZE = 12 
HS_LIDAR_GT_Unit_Num         = 8
HS_LIDAR_GT_recevbuf_Size    = HS_LIDAR_GT_SERIAL_UNIT_SIZE*HS_LIDAR_GT_Unit_Num

myq = Queue.Queue(maxsize = 1)
threading_out = 0

port = 8083
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   
s.bind(("",port))  
time.sleep(0.1)
print 'waiting on port:',port,"\n"

def socket_putin():
        
        num =0
        breakout=1
        while breakout:
            data, addr = s.recvfrom(HS_LIDAR_GT_recevbuf_Size)
            myq.put(data)
            num +=1
            while myq.full() == 1:
                data, addr = s.recvfrom(HS_LIDAR_GT_recevbuf_Size)
                # print "queue full size = ",myq.qsize(), "qsize is full ! \n\n"
                # time.sleep(0.01)
                #if threading_out:
                    #exit()
                #put_flag=0
                #breakout=0
                #s.close()
                #break
                #print "unnormal ''''"
                #exit()
                num = 0

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

        self.ChannelId = []
        self.elevation = []
        self.azimuth = []
        self.refelctivity = []
        self.distance = []

    def wave_data_catch(self,channel=0):
        # print "before clearing myq.qsize() =",myq.qsize()
        myq.queue.clear() 
        recevbuf=[]
        self.width, self.distance = [], []
        self.width_buf, self.distance_buf = [], []
        self.ChannelId = []
        self.data_channel0_width, self.data_channel0_distance = [], []
        self.data_channel1_width, self.data_channel1_distance = [], []
        self.data_channel2_width, self.data_channel2_distance = [], []
        self.data_channel3_width, self.data_channel3_distance = [], []
        self.data_channel4_width, self.data_channel4_distance = [], []
        self.data_channel5_width, self.data_channel5_distance = [], []
        self.data_channel6_width, self.data_channel6_distance = [], []
        self.data_channel7_width, self.data_channel7_distance = [], []
        
        while myq.qsize()==0:
            waiting=[]
        
        recevbuf = myq.get()
        
        if len(recevbuf) != HS_LIDAR_GT_recevbuf_Size:
            return -1
        index = 0
        unit = 0 
        for unit in range(HS_LIDAR_GT_Unit_Num):
            self.ChannelId.append(ord(recevbuf[index])+ord(recevbuf[index+1])*256+\
            ord(recevbuf[index+2])*256*256+ord(recevbuf[index+3])*256*256*256)
            
            self.distance_buf.append((ord(recevbuf[index+4])+ord(recevbuf[index+5])*256+\
            ord(recevbuf[index+6])*256*256+ord(recevbuf[index+7])*256*256*256)*0.15/256)

            self.width_buf.append((ord(recevbuf[index+8])+ord(recevbuf[index+9])*256+\
            ord(recevbuf[index+10])*256*256+ord(recevbuf[index+11])*256*256*256)*0.15/256)
            
            index += HS_LIDAR_GT_SERIAL_UNIT_SIZE

        for k in range(8):
            if self.ChannelId[k] == 1:
                self.data_channel0_width.append(self.width_buf[k])
                self.data_channel0_distance.append(self.distance_buf[k])
                
            elif self.ChannelId[k] == 2:
                self.data_channel1_width.append(self.width_buf[k])
                self.data_channel1_distance.append(self.distance_buf[k])
                
            elif self.ChannelId[k] == 3:
                self.data_channel2_width.append(self.width_buf[k])
                self.data_channel2_distance.append(self.distance_buf[k])
                
            elif self.ChannelId[k] == 4:
                self.data_channel3_width.append(self.width_buf[k])
                self.data_channel3_distance.append(self.distance_buf[k])
                
            elif self.ChannelId[k] == 5:
                self.data_channel4_width.append(self.width_buf[k])
                self.data_channel4_distance.append(self.distance_buf[k])
                
            elif self.ChannelId[k] == 6:
                self.data_channel5_width.append(self.width_buf[k])
                self.data_channel5_distance.append(self.distance_buf[k])
                
            elif self.ChannelId[k] == 7:
                self.data_channel6_width.append(self.width_buf[k])
                self.data_channel6_distance.append(self.distance_buf[k])

            elif self.ChannelId[k] == 8:
                self.data_channel7_width.append(self.width_buf[k])
                self.data_channel7_distance.append(self.distance_buf[k])

        #print self.ChannelId
        #print self.data_channel7_width
        #print self.data_channel7_distance
        #plt.plot(self.data_channel_all[0:500],'r.--')  
        #plt.show()  
        if self.data_channel0_width or self.data_channel1_width or \
            self.data_channel2_width or self.data_channel3_width:
            self.data_channel4_width, self.data_channel4_distance = [0],[0]
            self.data_channel5_width, self.data_channel5_distance = [0],[0]
            self.data_channel6_width, self.data_channel6_distance = [0],[0]
            self.data_channel7_width, self.data_channel7_distance = [0],[0]
        else:
            self.data_channel0_width, self.data_channel0_distance = [0],[0]
            self.data_channel1_width, self.data_channel1_distance = [0],[0]
            self.data_channel2_width, self.data_channel2_distance = [0],[0]
            self.data_channel3_width, self.data_channel3_distance = [0],[0]
        if channel == 0:
            self.width = self.data_channel0_width[0]
            self.distance = self.data_channel0_distance[0]
        elif channel == 1:
            self.width = self.data_channel1_width[0]
            self.distance = self.data_channel1_distance[0]
        elif channel == 2:
            self.width = self.data_channel2_width[0]
            self.distance = self.data_channel2_distance[0]
        elif channel == 3:
            self.width = self.data_channel3_width[0]
            self.distance = self.data_channel3_distance[0]
        elif channel == 4:
            self.width = self.data_channel4_width[0]
            self.distance = self.data_channel4_distance[0]
        elif channel == 5:
            self.width = self.data_channel5_width[0]
            self.distance = self.data_channel5_distance[0]
        elif channel == 6:
            self.width = self.data_channel6_width[0]
            self.distance = self.data_channel6_distance[0]
        elif channel == 7:
            self.width = self.data_channel7_width[0]
            self.distance = self.data_channel7_distance[0]
        #print "id = ",self.ChannelId
        #print "width = ", self.width_buf,"\n", "distance = ", self.distance_buf
        print "dataSel : ","width = ",self.width," distance = ", self.distance
        #print "recbuf = ",self.data_channel0_width[0], self.data_channel0_distance[0]
        return self.width, self.distance
        

if __name__ == '__main__':

    from optparse import OptionParser
    import sys

    parser = OptionParser(usage="%prog [-v]", version="%prog 1.0")

    parser.add_option(
        "-c", "--channel",help="channel selection",default="0"
    )
  

    (options, args) = parser.parse_args(sys.argv)

    channel_opt = int(options.channel)
    
    ret1 = wave_receive_thread()
    ret1.start()
    try:
    
        datahandle = distannce_parse()
        width_list, distance_list = [], []

        for i in range(128*100):
            width_temp, distance_temp = [], []
            width_temp, distance_temp = datahandle.wave_data_catch(channel_opt)
            if distance_temp:
                width_list.append(width_temp)
                distance_list.append(distance_temp)
        ret1.stop()
        ret1.join()
    
        
    except:
        print "creating treading failed !!!"
    print "channel %d"%channel_opt,"\n",len(width_list),"", len(distance_list),"\n\n"
    #print "threding is over !"
    try:
        print "congratulation to you !"
        #plt.show()
        # print width_list, "len(width_list) =", len(width_list)
        # print distance_list, "len(distance_list) =", len(distance_list)
        # print "width std =", np.std(width_list)," distance std =", np.std(distance_list)
        # plt.plot(distance_list,'b.--')
        plt.plot(width_list,distance_list,'bo')
        plt.ylabel(" distance /m")
        plt.xlabel(" width_of_pulse /m")
        plt.title("width --- distance ")
        plt.show()

    except:
        print 'widthGetting error!!'

    #ret1.stop()
    #ret1.join()
    #threading_out=1
    
