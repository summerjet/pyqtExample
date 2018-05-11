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
from optparse import OptionParser
import sys





if __name__ == '__main__':
	parser = OptionParser(usage="%prog [-v]", version="%prog 1.0")

	parser.add_option(
		"-d", "--plotDistance",help="setting plotDistance",default="12.5"
	)

	(options, args) = parser.parse_args(sys.argv)

	pDistance = float(options.plotDistance)

	app = QApplication(sys.argv)
	window = QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(window)
	ui.initialAll(pDistance)

	window.show()
	sys.exit(app.exec_())

