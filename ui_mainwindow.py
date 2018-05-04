# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import qrc_rc
from wave_pulse_algorithm import distannce_parse, wave_receive_thread
import time
import random
import numpy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.animation as animation
import matplotlib.pyplot 
import csv

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1800, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pyplotWidget = QtWidgets.QWidget(self.centralwidget)
        self.pyplotWidget.setGeometry(QtCore.QRect(400, 20, 1400, 921))
        self.pyplotWidget.setObjectName("pyplotWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 20, 390, 641))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.PT_Slider_distance_6 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_6.setMaximum(1000)
        self.PT_Slider_distance_6.setProperty("value", 0)
        self.PT_Slider_distance_6.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_6.setObjectName("PT_Slider_distance_6")
        self.gridLayout.addWidget(self.PT_Slider_distance_6, 10, 1, 1, 1)
        self.PT_Slider_distance_10 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_10.setMaximum(1000)
        self.PT_Slider_distance_10.setProperty("value", 0)
        self.PT_Slider_distance_10.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_10.setObjectName("PT_Slider_distance_10")
        self.gridLayout.addWidget(self.PT_Slider_distance_10, 14, 1, 1, 1)
        self.PT_Slider_distance_8 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_8.setMaximum(1000)
        self.PT_Slider_distance_8.setProperty("value", 0)
        self.PT_Slider_distance_8.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_8.setObjectName("PT_Slider_distance_8")
        self.gridLayout.addWidget(self.PT_Slider_distance_8, 12, 1, 1, 1)
        self.PT_Slider_distance_5 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_5.setMaximum(1000)
        self.PT_Slider_distance_5.setProperty("value", 0)
        self.PT_Slider_distance_5.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_5.setObjectName("PT_Slider_distance_5")
        self.gridLayout.addWidget(self.PT_Slider_distance_5, 9, 1, 1, 1)
        self.label1_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label1_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_5.setFont(font)
        self.label1_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_5.setObjectName("label1_5")
        self.gridLayout.addWidget(self.label1_5, 9, 0, 1, 1)
        self.PT_Slider8 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider8.setMaximum(1000)
        self.PT_Slider8.setProperty("value", 0)
        self.PT_Slider8.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider8.setObjectName("PT_Slider8")
        self.gridLayout.addWidget(self.PT_Slider8, 12, 2, 1, 1)
        self.label1_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label1_7.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_7.setFont(font)
        self.label1_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_7.setObjectName("label1_7")
        self.gridLayout.addWidget(self.label1_7, 11, 0, 1, 1)
        self.PT_Slider3 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider3.setMaximum(1000)
        self.PT_Slider3.setProperty("value", 0)
        self.PT_Slider3.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider3.setObjectName("PT_Slider3")
        self.gridLayout.addWidget(self.PT_Slider3, 7, 2, 1, 1)
        self.PT_Slider9 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider9.setMaximum(1000)
        self.PT_Slider9.setProperty("value", 0)
        self.PT_Slider9.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider9.setObjectName("PT_Slider9")
        self.gridLayout.addWidget(self.PT_Slider9, 13, 2, 1, 1)
        self.change_calibration_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.change_calibration_3.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/pic/rotate.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.change_calibration_3.setIcon(icon)
        self.change_calibration_3.setIconSize(QtCore.QSize(30, 30))
        self.change_calibration_3.setObjectName("change_calibration_3")
        self.gridLayout.addWidget(self.change_calibration_3, 4, 2, 1, 1)
        self.PT_Slider4 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider4.setMaximum(1000)
        self.PT_Slider4.setProperty("value", 0)
        self.PT_Slider4.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider4.setObjectName("PT_Slider4")
        self.gridLayout.addWidget(self.PT_Slider4, 8, 2, 1, 1)
        self.PT_Slider10 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider10.setMaximum(1000)
        self.PT_Slider10.setProperty("value", 0)
        self.PT_Slider10.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider10.setObjectName("PT_Slider10")
        self.gridLayout.addWidget(self.PT_Slider10, 14, 2, 1, 1)
        self.label1_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label1_9.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_9.setFont(font)
        self.label1_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_9.setObjectName("label1_9")
        self.gridLayout.addWidget(self.label1_9, 13, 0, 1, 1)
        self.channel0 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel0.setFont(font)
        self.channel0.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/pic/off.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/pic/fresh.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.channel0.setIcon(icon1)
        self.channel0.setIconSize(QtCore.QSize(28, 28))
        self.channel0.setObjectName("channel0")
        self.gridLayout.addWidget(self.channel0, 0, 2, 1, 1)
        self.PT_Slider6 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider6.setMaximum(1000)
        self.PT_Slider6.setProperty("value", 0)
        self.PT_Slider6.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider6.setObjectName("PT_Slider6")
        self.gridLayout.addWidget(self.PT_Slider6, 10, 2, 1, 1)
        self.PT_Slider_distance_4 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_4.setMaximum(1000)
        self.PT_Slider_distance_4.setProperty("value", 0)
        self.PT_Slider_distance_4.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_4.setObjectName("PT_Slider_distance_4")
        self.gridLayout.addWidget(self.PT_Slider_distance_4, 8, 1, 1, 1)
        self.PT_Slider2 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider2.setEnabled(True)
        self.PT_Slider2.setMaximum(1000)
        self.PT_Slider2.setProperty("value", 0)
        self.PT_Slider2.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider2.setObjectName("PT_Slider2")
        self.gridLayout.addWidget(self.PT_Slider2, 6, 2, 1, 1)
        self.label1_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label1_8.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_8.setFont(font)
        self.label1_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_8.setObjectName("label1_8")
        self.gridLayout.addWidget(self.label1_8, 12, 0, 1, 1)
        self.label1_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label1_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_3.setFont(font)
        self.label1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_3.setObjectName("label1_3")
        self.gridLayout.addWidget(self.label1_3, 7, 0, 1, 1)
        self.PT_Slider5 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider5.setMaximum(1000)
        self.PT_Slider5.setProperty("value", 0)
        self.PT_Slider5.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider5.setObjectName("PT_Slider5")
        self.gridLayout.addWidget(self.PT_Slider5, 9, 2, 1, 1)
        self.label1_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label1_6.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_6.setFont(font)
        self.label1_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_6.setObjectName("label1_6")
        self.gridLayout.addWidget(self.label1_6, 10, 0, 1, 1)
        self.label1_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label1_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_2.setFont(font)
        self.label1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_2.setObjectName("label1_2")
        self.gridLayout.addWidget(self.label1_2, 6, 0, 1, 1)
        self.PT_Slider_distance_2 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_2.setMaximum(1000)
        self.PT_Slider_distance_2.setProperty("value", 0)
        self.PT_Slider_distance_2.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_2.setObjectName("PT_Slider_distance_2")
        self.gridLayout.addWidget(self.PT_Slider_distance_2, 6, 1, 1, 1)
        self.PT_Slider_distance_9 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_9.setMaximum(1000)
        self.PT_Slider_distance_9.setProperty("value", 0)
        self.PT_Slider_distance_9.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_9.setObjectName("PT_Slider_distance_9")
        self.gridLayout.addWidget(self.PT_Slider_distance_9, 13, 1, 1, 1)
        self.channel2 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel2.setFont(font)
        self.channel2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel2.setIcon(icon1)
        self.channel2.setIconSize(QtCore.QSize(28, 28))
        self.channel2.setObjectName("channel2")
        self.gridLayout.addWidget(self.channel2, 2, 2, 1, 1)
        self.label1_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_10.setFont(font)
        self.label1_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_10.setObjectName("label1_10")
        self.gridLayout.addWidget(self.label1_10, 14, 0, 1, 1)
        self.channel3 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel3.setFont(font)
        self.channel3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel3.setIcon(icon1)
        self.channel3.setIconSize(QtCore.QSize(28, 28))
        self.channel3.setObjectName("channel3")
        self.gridLayout.addWidget(self.channel3, 3, 2, 1, 1)
        self.PT_Slider_distance_1 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_1.setAutoFillBackground(False)
        self.PT_Slider_distance_1.setMaximum(1000)
        self.PT_Slider_distance_1.setProperty("value", 0)
        self.PT_Slider_distance_1.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_1.setObjectName("PT_Slider_distance_1")
        self.gridLayout.addWidget(self.PT_Slider_distance_1, 5, 1, 1, 1)
        self.channel1 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel1.setFont(font)
        self.channel1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel1.setIcon(icon1)
        self.channel1.setIconSize(QtCore.QSize(28, 28))
        self.channel1.setObjectName("channel1")
        self.gridLayout.addWidget(self.channel1, 1, 2, 1, 1)
        self.label1 = QtWidgets.QLabel(self.layoutWidget)
        self.label1.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 5, 0, 1, 1)
        self.PT_Slider_distance_7 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_7.setMaximum(1000)
        self.PT_Slider_distance_7.setProperty("value", 0)
        self.PT_Slider_distance_7.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_7.setObjectName("PT_Slider_distance_7")
        self.gridLayout.addWidget(self.PT_Slider_distance_7, 11, 1, 1, 1)
        self.PT_Slider7 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider7.setMaximum(1000)
        self.PT_Slider7.setProperty("value", 0)
        self.PT_Slider7.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider7.setObjectName("PT_Slider7")
        self.gridLayout.addWidget(self.PT_Slider7, 11, 2, 1, 1)
        self.PT_Slider_distance_3 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_3.setMaximum(1000)
        self.PT_Slider_distance_3.setProperty("value", 0)
        self.PT_Slider_distance_3.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_3.setObjectName("PT_Slider_distance_3")
        self.gridLayout.addWidget(self.PT_Slider_distance_3, 7, 1, 1, 1)
        self.label1_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label1_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_4.setFont(font)
        self.label1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_4.setObjectName("label1_4")
        self.gridLayout.addWidget(self.label1_4, 8, 0, 1, 1)
        self.PT_Slider1 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider1.setMaximum(1000)
        self.PT_Slider1.setSingleStep(1)
        self.PT_Slider1.setProperty("value", 0)
        self.PT_Slider1.setSliderPosition(0)
        self.PT_Slider1.setTracking(True)
        self.PT_Slider1.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider1.setObjectName("PT_Slider1")
        self.gridLayout.addWidget(self.PT_Slider1, 5, 2, 1, 1)
        self.catchWave = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.catchWave.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/pic/import.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.catchWave.setIcon(icon2)
        self.catchWave.setIconSize(QtCore.QSize(30, 30))
        self.catchWave.setObjectName("catchWave")
        self.gridLayout.addWidget(self.catchWave, 0, 1, 1, 1)
        self.clearAndClose = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clearAndClose.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/pic/clear.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.clearAndClose.setIcon(icon3)
        self.clearAndClose.setIconSize(QtCore.QSize(30, 30))
        self.clearAndClose.setObjectName("clearAndClose")
        self.gridLayout.addWidget(self.clearAndClose, 1, 1, 1, 1)
        self.simulation_on = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.simulation_on.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/pic/add.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.simulation_on.setIcon(icon4)
        self.simulation_on.setIconSize(QtCore.QSize(30, 30))
        self.simulation_on.setObjectName("simulation_on")
        self.gridLayout.addWidget(self.simulation_on, 2, 1, 1, 1)
        self.change_calibration = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.change_calibration.setFont(font)
        self.change_calibration.setIcon(icon1)
        self.change_calibration.setIconSize(QtCore.QSize(30, 30))
        self.change_calibration.setObjectName("change_calibration")
        self.gridLayout.addWidget(self.change_calibration, 3, 1, 1, 1)
        self.change_calibration_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.change_calibration_2.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/pic/move.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.change_calibration_2.setIcon(icon5)
        self.change_calibration_2.setIconSize(QtCore.QSize(30, 30))
        self.change_calibration_2.setObjectName("change_calibration_2")
        self.gridLayout.addWidget(self.change_calibration_2, 4, 1, 1, 1)
        self.calibration_out = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.calibration_out.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/pic/output.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.calibration_out.setIcon(icon6)
        self.calibration_out.setIconSize(QtCore.QSize(30, 30))
        self.calibration_out.setObjectName("calibration_out")
        self.gridLayout.addWidget(self.calibration_out, 15, 1, 1, 1)
        self.rmse_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.rmse_message.setGeometry(QtCore.QRect(10, 700, 161, 41))
        self.rmse_message.setObjectName("rmse_message")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 670, 48, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.average_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.average_message.setGeometry(QtCore.QRect(180, 700, 161, 41))
        self.average_message.setObjectName("average_message")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 670, 78, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionDistancePlus = QtWidgets.QAction(MainWindow)
        self.actionDistancePlus.setObjectName("actionDistancePlus")
        self.actionWidthPlus = QtWidgets.QAction(MainWindow)
        self.actionWidthPlus.setCheckable(False)
        self.actionWidthPlus.setEnabled(True)
        self.actionWidthPlus.setObjectName("actionWidthPlus")
        self.actionDistanceMinus = QtWidgets.QAction(MainWindow)
        self.actionDistanceMinus.setObjectName("actionDistanceMinus")
        self.actionWidthMinus = QtWidgets.QAction(MainWindow)
        self.actionWidthMinus.setObjectName("actionWidthMinus")
        self.actionCalPtSelectLeft = QtWidgets.QAction(MainWindow)
        self.actionCalPtSelectLeft.setObjectName("actionCalPtSelectLeft")
        self.actionCalPtSelectRight = QtWidgets.QAction(MainWindow)
        self.actionCalPtSelectRight.setObjectName("actionCalPtSelectRight")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#########################################edit by summerjet#################################
       
        self.simu_data()
        self.simu_plot_setup()
        self.catchWave.clicked.connect(self.width_distance_calibration_data_get)
        self.clearAndClose.clicked.connect(self.clearAndCloseFunc)
        self.simulation_on.clicked.connect(self.plt_animation)

        self.channel0.clicked.connect(self.wave_channel_sel)
        self.channel1.clicked.connect(self.wave_channel_sel)
        self.channel2.clicked.connect(self.wave_channel_sel)
        self.channel3.clicked.connect(self.wave_channel_sel)

        self.PT_Slider1.valueChanged.connect(self.sliderFunc_w1)
        self.PT_Slider2.valueChanged.connect(self.sliderFunc_w2)
        self.PT_Slider3.valueChanged.connect(self.sliderFunc_w3)
        self.PT_Slider4.valueChanged.connect(self.sliderFunc_w4)
        self.PT_Slider5.valueChanged.connect(self.sliderFunc_w5)
        self.PT_Slider6.valueChanged.connect(self.sliderFunc_w6)
        self.PT_Slider7.valueChanged.connect(self.sliderFunc_w7)
        self.PT_Slider8.valueChanged.connect(self.sliderFunc_w8)
        self.PT_Slider9.valueChanged.connect(self.sliderFunc_w9)
        self.PT_Slider10.valueChanged.connect(self.sliderFunc_w10)

        self.PT_Slider_distance_1.valueChanged.connect(self.sliderFunc_d1)
        self.PT_Slider_distance_2.valueChanged.connect(self.sliderFunc_d2)
        self.PT_Slider_distance_3.valueChanged.connect(self.sliderFunc_d3)
        self.PT_Slider_distance_4.valueChanged.connect(self.sliderFunc_d4)
        self.PT_Slider_distance_5.valueChanged.connect(self.sliderFunc_d5)
        self.PT_Slider_distance_6.valueChanged.connect(self.sliderFunc_d6)
        self.PT_Slider_distance_7.valueChanged.connect(self.sliderFunc_d7)
        self.PT_Slider_distance_8.valueChanged.connect(self.sliderFunc_d8)
        self.PT_Slider_distance_9.valueChanged.connect(self.sliderFunc_d9)
        self.PT_Slider_distance_10.valueChanged.connect(self.sliderFunc_d10)

        self.calibration_out.clicked.connect(self.csv_write)
        
        self.value_set()
        self.ptSelect = 0

    def pointSelectRight(self):
        self.ptSelect +=1
        self.ptSelect=self.ptSelect%10
        print "pt =", self.ptSelect
    def pointSelectLeft(self):
        self.ptSelect -=1
        self.ptSelect=self.ptSelect%10
        print "pt=", self.ptSelect
    
    def setShortcut_fun_d_plus(self):
        self.cal_distance[self.ptSelect] += 0.1
    def setShortcut_fun_d_minus(self):
        self.cal_distance[self.ptSelect] -= 0.1
    def setShortcut_fun_w_plus(self):
        self.cal_width[self.ptSelect] += 0.1
    def setShortcut_fun_w_minus(self):
        self.cal_width[self.ptSelect] -= 0.1

    def value_set(self):
        
        width_max = max(self.width)
        width_min = min(self.width)
        step = 10
        step_value = (width_max - width_min)/step

        self.cal_distance_set_1 = []
        self.cal_width_set_1=[]
        for r in range(step):
            self.cal_width_set_1.append(r*step_value+0.5*step_value)
        for k in range(step):
            dis_av_pt = []
            for m in range(len(self.width)):
                #if self.width[m]>=(k+0.5)*step_value-step_value*0.2 and self.width[m]<=(k+0.5)*step_value+step_value*0.2:
                if self.width[m]>=(k+0.5)*step_value-step_value*0.2 and self.width[m]<=(k+0.5)*step_value+step_value*0.2:
                    dis_av_pt.append(self.distance_delta[m])
            if dis_av_pt:
                self.cal_distance_set_1.append(float(numpy.mean(dis_av_pt)))
            else:
                self.cal_distance_set_1.append(0)

        #print "cal_distance_set_1 = ",self.cal_distance_set_1
        self.scale_distance = 100.0
        self.scale_width = 100.0
        #print "config before =", self.cal_width_set_1, "s ", self.cal_width_set_1[1]
        self.PT_Slider1.setValue(self.cal_width_set_1[0]*self.scale_width)
        self.PT_Slider2.setValue(self.cal_width_set_1[1]*self.scale_width)
        self.PT_Slider3.setValue(self.cal_width_set_1[2]*self.scale_width)
        self.PT_Slider4.setValue(self.cal_width_set_1[3]*self.scale_width)
        self.PT_Slider5.setValue(self.cal_width_set_1[4]*self.scale_width)
        self.PT_Slider6.setValue(self.cal_width_set_1[5]*self.scale_width)
        self.PT_Slider7.setValue(self.cal_width_set_1[6]*self.scale_width)
        self.PT_Slider8.setValue(self.cal_width_set_1[7]*self.scale_width)
        self.PT_Slider9.setValue(self.cal_width_set_1[8]*self.scale_width)
        self.PT_Slider10.setValue(self.cal_width_set_1[9]*self.scale_width)

        

        self.PT_Slider_distance_1.setValue(self.cal_distance_set_1[0]*self.scale_distance)
        self.PT_Slider_distance_2.setValue(self.cal_distance_set_1[1]*self.scale_distance)
        self.PT_Slider_distance_3.setValue(self.cal_distance_set_1[2]*self.scale_distance)
        self.PT_Slider_distance_4.setValue(self.cal_distance_set_1[3]*self.scale_distance)
        self.PT_Slider_distance_5.setValue(self.cal_distance_set_1[4]*self.scale_distance)
        self.PT_Slider_distance_6.setValue(self.cal_distance_set_1[5]*self.scale_distance)
        self.PT_Slider_distance_7.setValue(self.cal_distance_set_1[6]*self.scale_distance)
        self.PT_Slider_distance_8.setValue(self.cal_distance_set_1[7]*self.scale_distance)
        self.PT_Slider_distance_9.setValue(self.cal_distance_set_1[8]*self.scale_distance)
        self.PT_Slider_distance_10.setValue(self.cal_distance_set_1[9]*self.scale_distance)

        #print "============", self.cal_width_set_1,"==============", self.cal_distance_set_1
        #print self.PT_Slider1.value()," ", self.PT_Slider2.value()
        
    def sliderFunc_w1(self):
        self.cal_width_set[0] = self.PT_Slider1.value()/self.scale_width
        self.plt_animation()
    def sliderFunc_w2(self):
        self.cal_width_set[1] = self.PT_Slider2.value()/self.scale_width
        self.plt_animation()
    def sliderFunc_w3(self):
        self.cal_width_set[2] = self.PT_Slider3.value()/self.scale_width
        self.plt_animation()
    def sliderFunc_w4(self):
        self.cal_width_set[3] = self.PT_Slider4.value()/self.scale_width
        self.plt_animation()
    def sliderFunc_w5(self):
        self.cal_width_set[4] = self.PT_Slider5.value()/self.scale_width
        self.plt_animation()
    def sliderFunc_w6(self):
        self.cal_width_set[5] = self.PT_Slider6.value()/self.scale_width
        self.plt_animation()
    def sliderFunc_w7(self):
        self.cal_width_set[6] = self.PT_Slider7.value()/self.scale_width
        self.plt_animation()
    def sliderFunc_w8(self):
        self.cal_width_set[7] = self.PT_Slider8.value()/self.scale_width
        self.plt_animation()
    def sliderFunc_w9(self):
        self.cal_width_set[8] = self.PT_Slider9.value()/self.scale_width
        self.plt_animation()
    def sliderFunc_w10(self):
        self.cal_width_set[9] = self.PT_Slider10.value()/self.scale_width
        self.plt_animation()

    def sliderFunc_d1(self):
        self.cal_distance_set[0] = self.PT_Slider_distance_1.value()/self.scale_distance
        self.plt_animation()
    def sliderFunc_d2(self):
        self.cal_distance_set[1] = self.PT_Slider_distance_2.value()/self.scale_distance
        self.plt_animation()
    def sliderFunc_d3(self):
        self.cal_distance_set[2] = self.PT_Slider_distance_3.value()/self.scale_distance
        self.plt_animation()
    def sliderFunc_d4(self):
        self.cal_distance_set[3] = self.PT_Slider_distance_4.value()/self.scale_distance
        self.plt_animation()
    def sliderFunc_d5(self):
        self.cal_distance_set[4] = self.PT_Slider_distance_5.value()/self.scale_distance
        self.plt_animation()
    def sliderFunc_d6(self):
        self.cal_distance_set[5] = self.PT_Slider_distance_6.value()/self.scale_distance
        self.plt_animation()
    def sliderFunc_d7(self):
        self.cal_distance_set[6] = self.PT_Slider_distance_7.value()/self.scale_distance
        self.plt_animation()
    def sliderFunc_d8(self):
        self.cal_distance_set[7] = self.PT_Slider_distance_8.value()/self.scale_distance
        self.plt_animation()
    def sliderFunc_d9(self):
        self.cal_distance_set[8] = self.PT_Slider_distance_9.value()/self.scale_distance
        self.plt_animation()
    def sliderFunc_d10(self):
        self.cal_distance_set[9] = self.PT_Slider_distance_10.value()/self.scale_distance
        self.plt_animation()

    def calculation_cal_show(self):
        step = 10
        self.cal_distance = self.cal_distance_set
        self.cal_width=self.cal_width_set
        
        self.distance_show = []
        distance_real = 20
        self.width_show = self.width
        x=self.cal_width
        y=self.cal_distance
        
        for h in range(len(self.width_show)):
            if self.width_show[h] < self.cal_width[0]:
                distance_show_temp = float((y[1]-y[0])*(self.width_show[h]-x[0]))/float(x[1]-x[0])+float(y[0])
            elif self.width_show[h] >=self.cal_width[len(self.cal_width)-1]:
                distance_show_temp = float((y[step-1]-y[step-2])*(self.width_show[h]-x[step-1]))/float(x[step-1]-x[step-2])+float(y[step-1])
            else:
                for s in range(len(self.cal_width)-1):
                    if self.width_show[h] >=self.cal_width[s] and self.width_show[h] < self.cal_width[s+1]:
                        distance_show_temp = float((y[s+1]-y[s])*(self.width_show[h]-x[s]))/float(x[s+1]-x[s])+float(y[s])
                if not distance_show_temp:
                    distance_show_temp = 0
                    print "wrong data"
            self.distance_show.append(distance_show_temp-self.distance_delta[h]+distance_real)
        
    def clearAll(self):
        self.width_udp = []
        self.distance_udp = []

    def clearAndCloseFunc(self):
        self.clearAll()
        self.ret1.stop()
        self.ret1.join()

    def wave_channel_sel(self):
        if self.channel0.isChecked():
            self.channel_opt = 0
            print "channel0 is checked ====",self.channel_opt
            print "testing !"
        elif self.channel1.isChecked():
            self.channel_opt = 1
            print "channel1 is checked ====",self.channel_opt
        elif self.channel2.isChecked():
            self.channel_opt = 2
            print "channel2 is checked ====",self.channel_opt
        elif self.channel3.isChecked():
            self.channel_opt =3
            print "channel3 is checked ====",self.channel_opt
        else:
            self.channel_opt = 0
            print "default setting !",self.channel_opt
        return self.channel_opt

    def width_distance_get(self, points_num=10):
        self.channel_opt = 0
        self.ret1 = wave_receive_thread()
        self.ret1.start()
        width_list =[]
        distance_list=[]
        channel_sel = self.wave_channel_sel()
        try:
            datahandle = distannce_parse()
            for i in range(points_num):
                time.sleep(0.01)
                pSignal=datahandle.wave_data_catch(channel_sel)
                datahandle.pulseSignal()
                width_distance = datahandle.widthGet()
                if width_distance[0]:
                    width_list.append(width_distance[0])
                    distance_list.append(width_distance[1])
                #datahandle.widthGet()
            #matplotlib.pyplot.plot(pSignal[1],pSignal[0],'o-')
            self.ret1.stop()
            self.ret1.join()
        except:
            print "creating treading failed !!!"
        return width_list, distance_list
    def width_distance_calibration_data_get(self):
        temp_width,temp_distance = self.width_distance_get()
        self.width_udp += temp_width
        self.distance_udp += temp_distance
    def width_distance_calibration(self):
        width,distance_delta = self.width_udp, self.distance_udp
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
        #print "len(distance_show =",len(distance_show)

        return width,distance_delta,cal_width,cal_distance,width_show,distance_show

        print "calibration here ========"

    def simu_data(self):
        
        self.width = []
        self.distance_delta = []
        for i in range(100):
            rd_w = random.random()*5+i/20
            self.width.append(rd_w)
        for j in range(100):
            rd_d = random.random()*0.2+self.width[j]/5
            self.distance_delta.append(rd_d)

        width_max = max(self.width)
        width_min = min(self.width)
        step = 10
        step_value = (width_max - width_min)/step

        self.cal_distance = []
        self.cal_width=[]
        for r in range(step):
            self.cal_width.append(r*step_value+0.5*step_value)
        for k in range(step):
            dis_av_pt = []
            for m in range(len(self.width)):
                #if self.width[m]>=(k+0.5)*step_value-step_value*0.2 and self.width[m]<=(k+0.5)*step_value+step_value*0.2:
                if self.width[m]>=(k+0.5)*step_value-step_value*0.2 and self.width[m]<=(k+0.5)*step_value+step_value*0.2:
                    dis_av_pt.append(self.distance_delta[m])
            if dis_av_pt:
                self.cal_distance.append(numpy.mean(dis_av_pt))
            else:
                self.cal_distance.append(0)

        #print "len of calwidth =", len(self.cal_width)," step_value =", step_value,"len(cal_dis) =", len(self.cal_distance)
        self.cal_width_set = self.cal_width
        self.cal_distance_set = self.cal_distance

        self.distance_show = []
        distance_real = 20
        self.width_show = self.width
        x=self.cal_width
        y=self.cal_distance

        for h in range(len(self.width_show)):
            if self.width_show[h] < self.cal_width[0]:
                distance_show_temp = float((y[1]-y[0])*(self.width_show[h]-x[0]))/float(x[1]-x[0])+float(y[0])
            elif self.width_show[h] >=self.cal_width[len(self.cal_width)-1]:
                distance_show_temp = float((y[step-1]-y[step-2])*(self.width_show[h]-x[step-1]))/float(x[step-1]-x[step-2])+float(y[step-1])
            else:
                for s in range(len(self.cal_width)-1):
                    if self.width_show[h] >=self.cal_width[s] and self.width_show[h] < self.cal_width[s+1]:
                        distance_show_temp = float((y[s+1]-y[s])*(self.width_show[h]-x[s]))/float(x[s+1]-x[s])+float(y[s])
                if not distance_show_temp:
                    distance_show_temp = 0
                    print "wrong data"
            self.distance_show.append(distance_show_temp-self.distance_delta[h]+distance_real)
        #print "len(self.distance_show =",len(self.distance_show)

    def simu_plot_setup(self):
        #self.width,self.distance_delta = self.simu_data()#simulation is on
        #self.width,self.distance_delta,self.cal_width,self.cal_distance,self.width_show,\
        #self.distance_show = self.width_distance_calibration()#socket data source
        self.Fig1 = matplotlib.pyplot.Figure(figsize=(10,8))#matplotlib.pyplot.Figure(figsize=(8,8))
        matplotlib.pyplot =  self.Fig1.add_subplot(211,xlim=(0, 10), ylim=(0,3), facecolor ="w")
        self.line1, = matplotlib.pyplot.plot(self.width,self.distance_delta,'.',lw=2)
        self.line2, = matplotlib.pyplot.plot(self.cal_width,self.cal_distance,'ro--',lw=2)
        #matplotlib.pyplot.grid()

        matplotlib.pyplot = self.Fig1.add_subplot(212,xlim=(0, 10), ylim=(18,22))
        #matplotlib.pyplot.plot(x,'ro--',lw=2)
        self.line3, = matplotlib.pyplot.plot(self.width_show,self.distance_show,'bo')
        matplotlib.pyplot.grid()
        self.canvas1 = FigureCanvasQTAgg(self.Fig1)
        self.canvas1.setParent(self.pyplotWidget)

    def plt_animation(self):
        self.calculation_cal_show()
        self.line1.set_data(self.width,self.distance_delta)
        self.line2.set_data(self.cal_width,self.cal_distance)
        self.line3.set_data(self.width_show, self.distance_show)
        self.canvas1.draw()
        #print "ok"

    def csv_write(self):
        data_read = []
        with open ("./dataTemp/calibration.csv","rb") as f1:
            reader = csv.reader(f1)
            for row in reader:
                data_read.append(row)

        data_read.append(self.cal_width)
        data_read.append(self.cal_distance)
        
        print data_read

        with open ("./dataTemp/calibration.csv","wb") as csvfile:
            writer = csv.writer(csvfile)
            
            writer.writerows(data_read)
        print "write successful!"






###########################################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1_5.setText(_translate("MainWindow", "Pt5"))
        self.label1_7.setText(_translate("MainWindow", "Pt7"))
        self.change_calibration_3.setText(_translate("MainWindow", "cal_distance"))
        self.label1_9.setText(_translate("MainWindow", "Pt9"))
        self.channel0.setText(_translate("MainWindow", "channel0"))
        self.label1_8.setText(_translate("MainWindow", "Pt8"))
        self.label1_3.setText(_translate("MainWindow", "Pt3"))
        self.label1_6.setText(_translate("MainWindow", "Pt6"))
        self.label1_2.setText(_translate("MainWindow", "Pt2"))
        self.channel2.setText(_translate("MainWindow", "channel2"))
        self.label1_10.setText(_translate("MainWindow", "Pt10"))
        self.channel3.setText(_translate("MainWindow", "channel3"))
        self.channel1.setText(_translate("MainWindow", "channel1"))
        self.label1.setText(_translate("MainWindow", "Pt1"))
        self.label1_4.setText(_translate("MainWindow", "Pt4"))
        self.catchWave.setText(_translate("MainWindow", "Catch wave"))
        self.clearAndClose.setText(_translate("MainWindow", "clear and close"))
        self.simulation_on.setText(_translate("MainWindow", "simulation_on"))
        self.change_calibration.setText(_translate("MainWindow", "change_calib"))
        self.change_calibration_2.setText(_translate("MainWindow", "cal_width"))
        self.calibration_out.setText(_translate("MainWindow", "calib_output"))
        self.label.setText(_translate("MainWindow", "rmse"))
        self.label_2.setText(_translate("MainWindow", "average"))
        self.menuFile.setTitle(_translate("MainWindow", "file"))
        self.actionOpen.setText(_translate("MainWindow", "open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+C, Ctrl+L"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "save as"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionDistancePlus.setText(_translate("MainWindow", "distancePlus"))
        self.actionDistancePlus.setShortcut(_translate("MainWindow", "Up"))
        self.actionWidthPlus.setText(_translate("MainWindow", "widthPlus"))
        self.actionWidthPlus.setShortcut(_translate("MainWindow", "Shift+Up"))
        self.actionDistanceMinus.setText(_translate("MainWindow", "distanceMinus"))
        self.actionDistanceMinus.setShortcut(_translate("MainWindow", "Down"))
        self.actionWidthMinus.setText(_translate("MainWindow", "widthMinus"))
        self.actionWidthMinus.setShortcut(_translate("MainWindow", "Shift+Down"))
        self.actionCalPtSelectLeft.setText(_translate("MainWindow", "calPtSelectLeft"))
        self.actionCalPtSelectLeft.setShortcut(_translate("MainWindow", "Left"))
        self.actionCalPtSelectRight.setText(_translate("MainWindow", "calPtSelectRight"))
        self.actionCalPtSelectRight.setShortcut(_translate("MainWindow", "Right"))

import qrc_rc
