import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget, QVBoxLayout,QTabWidget, QWidget
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.animation as animation

from ui_mainwindow import Ui_MainWindow
#from wave_pulse_algorithm import distannce_parse, wave_receive_thread
import time
import csv
import random
import numpy

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
'''
######################width##############################
channel_opt = 2
ret1 = wave_receive_thread()
ret1.start()
width_list =[]
distance_list=[]

try:
	widthhandle = distannce_parse()
	for i in range(1 ):
	    time.sleep(0.01)
	    pSignal=widthhandle.wave_data_catch(0)
	    widthhandle.pulseSignal()
	    w_d = widthhandle.widthGet()
	    if w_d[0]:
	        width_list.append(w_d[0])
	        distance_list.append(w_d[1])
	    #widthhandle.widthGet()
	#plt.plot(pSignal[1],pSignal[0],'o-')
	ret1.stop()
	ret1.join()

except:
    print "creating treading failed !!!"



width = []
distance_delta = []
for i in range(100):
    rd_w = random.random()*5+i/20
    width.append(rd_w)
for j in range(100):
	rd_d = random.random()*0.2+width[j]/5
	distance_delta.append(rd_d)

width_max = max(width)
width_min = min(width)
step = 10
step_value = (width_max - width_min)/step

cal_distance = []
cal_width=[]
for r in range(step):
	cal_width.append(r*step_value+0.5*step_value)
for k in range(step):
	dis_av_pt = []
	for m in range(len(width)):
		#if width[m]>=(k+0.5)*step_value-step_value*0.2 and width[m]<=(k+0.5)*step_value+step_value*0.2:
		if width[m]>=(k+0.5)*step_value-step_value*0.2 and width[m]<=(k+0.5)*step_value+step_value*0.2:
			dis_av_pt.append(distance_delta[m])
	if dis_av_pt:
		cal_distance.append(numpy.mean(dis_av_pt))
	else:
		cal_distance.append(0)

#print "len of calwidth =", len(cal_width)," step_value =", step_value,"len(cal_dis) =", len(cal_distance)


distance_show = []
distance_show = []
distance_real = 20
width_show = width
x=cal_width
y=cal_distance

for h in range(len(width_show)):
	if width_show[h] < cal_width[0]:
		distance_show_temp = float((y[1]-y[0])*(width_show[h]-x[0]))/float(x[1]-x[0])+float(y[0])
	elif width_show[h] >=cal_width[len(cal_width)-1]:
		distance_show_temp = float((y[step-1]-y[step-2])*(width_show[h]-x[step-1]))/float(x[step-1]-x[step-2])+float(y[step-1])
	else:
		for s in range(len(cal_width)-1):
			if width_show[h] >=cal_width[s] and width_show[h] < cal_width[s+1]:
				distance_show_temp = float((y[s+1]-y[s])*(width_show[h]-x[s]))/float(x[s+1]-x[s])+float(y[s])
		if not distance_show_temp:
			distance_show_temp = 0
			print "wrong data"
	distance_show.append(distance_show_temp-distance_delta[h]+distance_real)
print "len(distance_show =",len(distance_show)
########################################################

#x=[1,2,3]
Fig1 = plt.Figure(figsize=(8,8))
plt =  Fig1.add_subplot(211)
plt.plot(width,distance_delta,'.',lw=2)
plt.plot(cal_width,cal_distance,'ro--',lw=2)
plt.grid()

plt = Fig1.add_subplot(212)
#plt.plot(x,'ro--',lw=2)
plt.plot(width_show,distance_show,'bo')


canvas1 = FigureCanvasQTAgg(Fig1)
canvas1.setParent(ui.pyplotWidget)
'''
window.show()
sys.exit(app.exec_())
