# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import qrc_rc
#from wave_pulse_algorithm import distannce_parse, wave_receive_thread
from udpRowData import distannce_parse, wave_receive_thread

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
        MainWindow.resize(1800, 1100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pyplotWidget = QtWidgets.QWidget(self.centralwidget)
        self.pyplotWidget.setGeometry(QtCore.QRect(550, 20, 1300, 1100))
        self.pyplotWidget.setObjectName("pyplotWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(8, 10, 464, 791))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addWidget(self.change_calibration_3, 9, 2, 1, 1)
        self.PT_Slider7 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider7.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider7.setMouseTracking(False)
        self.PT_Slider7.setMaximum(5000)
        self.PT_Slider7.setProperty("value", 0)
        self.PT_Slider7.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider7.setObjectName("PT_Slider7")
        self.gridLayout.addWidget(self.PT_Slider7, 16, 2, 1, 1)
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
        self.gridLayout.addWidget(self.label1, 10, 0, 1, 1)
        self.change_calibration_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.change_calibration_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/pic/move.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.change_calibration_2.setIcon(icon1)
        self.change_calibration_2.setIconSize(QtCore.QSize(30, 30))
        self.change_calibration_2.setObjectName("change_calibration_2")
        self.gridLayout.addWidget(self.change_calibration_2, 9, 1, 1, 1)
        self.PT_Slider_distance_1 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_1.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_1.setMouseTracking(False)
        self.PT_Slider_distance_1.setAutoFillBackground(False)
        self.PT_Slider_distance_1.setMaximum(5000)
        self.PT_Slider_distance_1.setProperty("value", 0)
        self.PT_Slider_distance_1.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_1.setObjectName("PT_Slider_distance_1")
        self.gridLayout.addWidget(self.PT_Slider_distance_1, 10, 1, 1, 1)
        self.PT_Slider_distance_2 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_2.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_2.setMouseTracking(False)
        self.PT_Slider_distance_2.setMaximum(5000)
        self.PT_Slider_distance_2.setProperty("value", 0)
        self.PT_Slider_distance_2.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_2.setObjectName("PT_Slider_distance_2")
        self.gridLayout.addWidget(self.PT_Slider_distance_2, 11, 1, 1, 1)
        self.PT_Slider_distance_7 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_7.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_7.setMouseTracking(False)
        self.PT_Slider_distance_7.setMaximum(5000)
        self.PT_Slider_distance_7.setProperty("value", 0)
        self.PT_Slider_distance_7.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_7.setObjectName("PT_Slider_distance_7")
        self.gridLayout.addWidget(self.PT_Slider_distance_7, 16, 1, 1, 1)
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
        self.gridLayout.addWidget(self.label1_9, 18, 0, 1, 1)
        self.PT_Slider_distance_9 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_9.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_9.setMouseTracking(False)
        self.PT_Slider_distance_9.setMaximum(5000)
        self.PT_Slider_distance_9.setProperty("value", 0)
        self.PT_Slider_distance_9.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_9.setObjectName("PT_Slider_distance_9")
        self.gridLayout.addWidget(self.PT_Slider_distance_9, 18, 1, 1, 1)
        self.PT_Slider9 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider9.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider9.setMouseTracking(False)
        self.PT_Slider9.setMaximum(5000)
        self.PT_Slider9.setProperty("value", 0)
        self.PT_Slider9.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider9.setObjectName("PT_Slider9")
        self.gridLayout.addWidget(self.PT_Slider9, 18, 2, 1, 1)
        self.label1_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label1_10.setFont(font)
        self.label1_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_10.setObjectName("label1_10")
        self.gridLayout.addWidget(self.label1_10, 19, 0, 1, 1)
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
        self.gridLayout.addWidget(self.label1_6, 15, 0, 1, 1)
        self.PT_Slider3 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider3.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider3.setMouseTracking(False)
        self.PT_Slider3.setMaximum(5000)
        self.PT_Slider3.setProperty("value", 0)
        self.PT_Slider3.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider3.setObjectName("PT_Slider3")
        self.gridLayout.addWidget(self.PT_Slider3, 12, 2, 1, 1)
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
        self.gridLayout.addWidget(self.label1_5, 14, 0, 1, 1)
        self.PT_Slider_distance_8 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_8.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_8.setMouseTracking(False)
        self.PT_Slider_distance_8.setMaximum(5000)
        self.PT_Slider_distance_8.setProperty("value", 0)
        self.PT_Slider_distance_8.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_8.setObjectName("PT_Slider_distance_8")
        self.gridLayout.addWidget(self.PT_Slider_distance_8, 17, 1, 1, 1)
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
        self.gridLayout.addWidget(self.label1_4, 13, 0, 1, 1)
        self.channel4 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel4.setFont(font)
        self.channel4.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/pic/off.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icon/pic/fresh.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.channel4.setIcon(icon2)
        self.channel4.setIconSize(QtCore.QSize(28, 28))
        self.channel4.setObjectName("channel4")
        self.gridLayout.addWidget(self.channel4, 1, 2, 1, 1)
        self.PT_Slider1 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider1.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider1.setMouseTracking(False)
        self.PT_Slider1.setMaximum(5000)
        self.PT_Slider1.setSingleStep(1)
        self.PT_Slider1.setProperty("value", 0)
        self.PT_Slider1.setSliderPosition(0)
        self.PT_Slider1.setTracking(True)
        self.PT_Slider1.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider1.setObjectName("PT_Slider1")
        self.gridLayout.addWidget(self.PT_Slider1, 10, 2, 1, 1)
        self.PT_Slider_distance_4 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_4.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_4.setMouseTracking(False)
        self.PT_Slider_distance_4.setMaximum(5000)
        self.PT_Slider_distance_4.setProperty("value", 0)
        self.PT_Slider_distance_4.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_4.setObjectName("PT_Slider_distance_4")
        self.gridLayout.addWidget(self.PT_Slider_distance_4, 13, 1, 1, 1)
        self.PT_Slider4 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider4.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider4.setMouseTracking(False)
        self.PT_Slider4.setMaximum(5000)
        self.PT_Slider4.setProperty("value", 0)
        self.PT_Slider4.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider4.setObjectName("PT_Slider4")
        self.gridLayout.addWidget(self.PT_Slider4, 13, 2, 1, 1)
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
        self.gridLayout.addWidget(self.label1_7, 16, 0, 1, 1)
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
        self.gridLayout.addWidget(self.label1_2, 11, 0, 1, 1)
        self.PT_Slider_distance_3 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_3.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_3.setMouseTracking(False)
        self.PT_Slider_distance_3.setMaximum(5000)
        self.PT_Slider_distance_3.setProperty("value", 0)
        self.PT_Slider_distance_3.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_3.setObjectName("PT_Slider_distance_3")
        self.gridLayout.addWidget(self.PT_Slider_distance_3, 12, 1, 1, 1)
        self.PT_Slider8 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider8.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider8.setMouseTracking(False)
        self.PT_Slider8.setMaximum(5000)
        self.PT_Slider8.setProperty("value", 0)
        self.PT_Slider8.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider8.setObjectName("PT_Slider8")
        self.gridLayout.addWidget(self.PT_Slider8, 17, 2, 1, 1)
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
        self.gridLayout.addWidget(self.label1_3, 12, 0, 1, 1)
        self.PT_Slider_distance_6 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_6.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_6.setMouseTracking(False)
        self.PT_Slider_distance_6.setMaximum(5000)
        self.PT_Slider_distance_6.setProperty("value", 0)
        self.PT_Slider_distance_6.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_6.setObjectName("PT_Slider_distance_6")
        self.gridLayout.addWidget(self.PT_Slider_distance_6, 15, 1, 1, 1)
        self.PT_Slider6 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider6.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider6.setMouseTracking(False)
        self.PT_Slider6.setMaximum(5000)
        self.PT_Slider6.setProperty("value", 0)
        self.PT_Slider6.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider6.setObjectName("PT_Slider6")
        self.gridLayout.addWidget(self.PT_Slider6, 15, 2, 1, 1)
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
        self.gridLayout.addWidget(self.label1_8, 17, 0, 1, 1)
        self.PT_Slider_distance_10 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_10.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_10.setMouseTracking(False)
        self.PT_Slider_distance_10.setMaximum(5000)
        self.PT_Slider_distance_10.setProperty("value", 0)
        self.PT_Slider_distance_10.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_10.setObjectName("PT_Slider_distance_10")
        self.gridLayout.addWidget(self.PT_Slider_distance_10, 19, 1, 1, 1)
        self.PT_Slider10 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider10.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider10.setMouseTracking(False)
        self.PT_Slider10.setMaximum(5000)
        self.PT_Slider10.setProperty("value", 0)
        self.PT_Slider10.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider10.setObjectName("PT_Slider10")
        self.gridLayout.addWidget(self.PT_Slider10, 19, 2, 1, 1)
        self.PT_Slider2 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider2.setEnabled(True)
        self.PT_Slider2.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider2.setMouseTracking(False)
        self.PT_Slider2.setMaximum(5000)
        self.PT_Slider2.setProperty("value", 0)
        self.PT_Slider2.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider2.setObjectName("PT_Slider2")
        self.gridLayout.addWidget(self.PT_Slider2, 11, 2, 1, 1)
        self.PT_Slider_distance_5 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider_distance_5.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider_distance_5.setMouseTracking(False)
        self.PT_Slider_distance_5.setMaximum(5000)
        self.PT_Slider_distance_5.setProperty("value", 0)
        self.PT_Slider_distance_5.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider_distance_5.setObjectName("PT_Slider_distance_5")
        self.gridLayout.addWidget(self.PT_Slider_distance_5, 14, 1, 1, 1)
        self.PT_Slider5 = QtWidgets.QSlider(self.layoutWidget)
        self.PT_Slider5.setCursor(QtGui.QCursor(QtCore.Qt.SplitHCursor))
        self.PT_Slider5.setMouseTracking(False)
        self.PT_Slider5.setMaximum(5000)
        self.PT_Slider5.setProperty("value", 0)
        self.PT_Slider5.setOrientation(QtCore.Qt.Horizontal)
        self.PT_Slider5.setObjectName("PT_Slider5")
        self.gridLayout.addWidget(self.PT_Slider5, 14, 2, 1, 1)
        self.calibration_out = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.calibration_out.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/pic/output.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.calibration_out.setIcon(icon3)
        self.calibration_out.setIconSize(QtCore.QSize(40, 40))
        self.calibration_out.setObjectName("calibration_out")
        self.gridLayout.addWidget(self.calibration_out, 21, 1, 1, 2)
        self.clearAndClose = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clearAndClose.setFont(font)
        self.clearAndClose.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/pic/clear.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.clearAndClose.setIcon(icon4)
        self.clearAndClose.setIconSize(QtCore.QSize(30, 30))
        self.clearAndClose.setObjectName("clearAndClose")
        self.gridLayout.addWidget(self.clearAndClose, 6, 1, 1, 1)
        self.change_calibration = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.change_calibration.setFont(font)
        self.change_calibration.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/pic/import.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.change_calibration.setIcon(icon5)
        self.change_calibration.setIconSize(QtCore.QSize(30, 30))
        self.change_calibration.setObjectName("change_calibration")
        self.gridLayout.addWidget(self.change_calibration, 5, 2, 1, 1)
        self.channel5 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel5.setFont(font)
        self.channel5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel5.setIcon(icon2)
        self.channel5.setIconSize(QtCore.QSize(28, 28))
        self.channel5.setObjectName("channel5")
        self.gridLayout.addWidget(self.channel5, 2, 2, 1, 1)
        self.channel6 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel6.setFont(font)
        self.channel6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel6.setIcon(icon2)
        self.channel6.setIconSize(QtCore.QSize(28, 28))
        self.channel6.setObjectName("channel6")
        self.gridLayout.addWidget(self.channel6, 3, 2, 1, 1)
        self.channel1 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel1.setFont(font)
        self.channel1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel1.setIcon(icon2)
        self.channel1.setIconSize(QtCore.QSize(28, 28))
        self.channel1.setObjectName("channel1")
        self.gridLayout.addWidget(self.channel1, 2, 1, 1, 1)
        self.catchWave = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.catchWave.setFont(font)
        self.catchWave.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/pic/file-open.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.catchWave.setIcon(icon6)
        self.catchWave.setIconSize(QtCore.QSize(30, 30))
        self.catchWave.setObjectName("catchWave")
        self.gridLayout.addWidget(self.catchWave, 5, 1, 1, 1)
        self.channel3 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel3.setFont(font)
        self.channel3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel3.setIcon(icon2)
        self.channel3.setIconSize(QtCore.QSize(28, 28))
        self.channel3.setObjectName("channel3")
        self.gridLayout.addWidget(self.channel3, 4, 1, 1, 1)
        self.channel0 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel0.setFont(font)
        self.channel0.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel0.setIcon(icon2)
        self.channel0.setIconSize(QtCore.QSize(28, 28))
        self.channel0.setObjectName("channel0")
        self.gridLayout.addWidget(self.channel0, 1, 1, 1, 1)
        self.channel2 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel2.setFont(font)
        self.channel2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel2.setIcon(icon2)
        self.channel2.setIconSize(QtCore.QSize(28, 28))
        self.channel2.setObjectName("channel2")
        self.gridLayout.addWidget(self.channel2, 3, 1, 1, 1)
        self.saveOriginUdpData = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.saveOriginUdpData.setFont(font)
        self.saveOriginUdpData.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/pic/add.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.saveOriginUdpData.setIcon(icon7)
        self.saveOriginUdpData.setIconSize(QtCore.QSize(30, 30))
        self.saveOriginUdpData.setObjectName("saveOriginUdpData")
        self.gridLayout.addWidget(self.saveOriginUdpData, 6, 2, 1, 1)
        self.channel7 = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.channel7.setFont(font)
        self.channel7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.channel7.setIcon(icon2)
        self.channel7.setIconSize(QtCore.QSize(28, 28))
        self.channel7.setObjectName("channel7")
        self.gridLayout.addWidget(self.channel7, 4, 2, 1, 1)
        self.rmse_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.rmse_message.setGeometry(QtCore.QRect(91, 887, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.rmse_message.setFont(font)
        self.rmse_message.setObjectName("rmse_message")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(141, 924, 48, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.average_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.average_message.setGeometry(QtCore.QRect(261, 887, 160, 40))
        self.average_message.setObjectName("average_message")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(311, 924, 78, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(90, 950, 331, 61))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 1021, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.realDistance = QtWidgets.QTextEdit(self.centralwidget)
        self.realDistance.setGeometry(QtCore.QRect(91, 812, 160, 40))
        self.realDistance.setObjectName("realDistance")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 852, 128, 23))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAction = QtWidgets.QMenu(self.menubar)
        self.menuAction.setObjectName("menuAction")
        self.menuPointsAction = QtWidgets.QMenu(self.menubar)
        self.menuPointsAction.setObjectName("menuPointsAction")
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
        self.actionCatchWave = QtWidgets.QAction(MainWindow)
        self.actionCatchWave.setObjectName("actionCatchWave")
        self.actionClearAndClose = QtWidgets.QAction(MainWindow)
        self.actionClearAndClose.setObjectName("actionClearAndClose")
        self.actionSaveOriginUdpData = QtWidgets.QAction(MainWindow)
        self.actionSaveOriginUdpData.setObjectName("actionSaveOriginUdpData")
        self.actionCalibrationFileOutput = QtWidgets.QAction(MainWindow)
        self.actionCalibrationFileOutput.setObjectName("actionCalibrationFileOutput")
        self.actionDistancePlus = QtWidgets.QAction(MainWindow)
        self.actionDistancePlus.setObjectName("actionDistancePlus")
        self.actionDistanceMinus = QtWidgets.QAction(MainWindow)
        self.actionDistanceMinus.setObjectName("actionDistanceMinus")
        self.actionWidthPlus = QtWidgets.QAction(MainWindow)
        self.actionWidthPlus.setObjectName("actionWidthPlus")
        self.actionWidthMinus = QtWidgets.QAction(MainWindow)
        self.actionWidthMinus.setObjectName("actionWidthMinus")
        self.actionPointSelect = QtWidgets.QAction(MainWindow)
        self.actionPointSelect.setObjectName("actionPointSelect")
        self.actionPointSelectLeft = QtWidgets.QAction(MainWindow)
        self.actionPointSelectLeft.setObjectName("actionPointSelectLeft")
        self.actionDistanceWidthScaleTab = QtWidgets.QAction(MainWindow)
        self.actionDistanceWidthScaleTab.setObjectName("actionDistanceWidthScaleTab")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuAction.addAction(self.actionCatchWave)
        self.menuAction.addAction(self.actionClearAndClose)
        self.menuAction.addAction(self.actionSaveOriginUdpData)
        self.menuAction.addAction(self.actionCalibrationFileOutput)
        self.menuPointsAction.addAction(self.actionDistancePlus)
        self.menuPointsAction.addAction(self.actionDistanceMinus)
        self.menuPointsAction.addAction(self.actionWidthPlus)
        self.menuPointsAction.addAction(self.actionWidthMinus)
        self.menuPointsAction.addAction(self.actionPointSelect)
        self.menuPointsAction.addAction(self.actionPointSelectLeft)
        self.menuPointsAction.addAction(self.actionDistanceWidthScaleTab)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menubar.addAction(self.menuPointsAction.menuAction())

        self.retranslateUi(MainWindow)
        self.actionClose.triggered.connect(MainWindow.close)
        self.actionCatchWave.triggered.connect(self.catchWave.click)
        self.actionClearAndClose.triggered.connect(self.clearAndClose.click)
        self.actionSaveOriginUdpData.triggered.connect(self.saveOriginUdpData.click)
        self.actionCalibrationFileOutput.triggered.connect(self.calibration_out.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.channel0, self.channel1)
        MainWindow.setTabOrder(self.channel1, self.channel2)
        MainWindow.setTabOrder(self.channel2, self.channel3)
        MainWindow.setTabOrder(self.channel3, self.channel4)
        MainWindow.setTabOrder(self.channel4, self.channel5)
        MainWindow.setTabOrder(self.channel5, self.channel6)
        MainWindow.setTabOrder(self.channel6, self.channel7)
        MainWindow.setTabOrder(self.channel7, self.catchWave)
        MainWindow.setTabOrder(self.catchWave, self.change_calibration)
        MainWindow.setTabOrder(self.change_calibration, self.clearAndClose)
        MainWindow.setTabOrder(self.clearAndClose, self.saveOriginUdpData)
        MainWindow.setTabOrder(self.saveOriginUdpData, self.change_calibration_2)
        MainWindow.setTabOrder(self.change_calibration_2, self.change_calibration_3)
        MainWindow.setTabOrder(self.change_calibration_3, self.PT_Slider_distance_1)
        MainWindow.setTabOrder(self.PT_Slider_distance_1, self.PT_Slider_distance_2)
        MainWindow.setTabOrder(self.PT_Slider_distance_2, self.PT_Slider_distance_3)
        MainWindow.setTabOrder(self.PT_Slider_distance_3, self.PT_Slider_distance_4)
        MainWindow.setTabOrder(self.PT_Slider_distance_4, self.PT_Slider_distance_5)
        MainWindow.setTabOrder(self.PT_Slider_distance_5, self.PT_Slider_distance_6)
        MainWindow.setTabOrder(self.PT_Slider_distance_6, self.PT_Slider_distance_7)
        MainWindow.setTabOrder(self.PT_Slider_distance_7, self.PT_Slider_distance_8)
        MainWindow.setTabOrder(self.PT_Slider_distance_8, self.PT_Slider_distance_9)
        MainWindow.setTabOrder(self.PT_Slider_distance_9, self.PT_Slider_distance_10)
        MainWindow.setTabOrder(self.PT_Slider_distance_10, self.PT_Slider1)
        MainWindow.setTabOrder(self.PT_Slider1, self.PT_Slider2)
        MainWindow.setTabOrder(self.PT_Slider2, self.PT_Slider3)
        MainWindow.setTabOrder(self.PT_Slider3, self.PT_Slider4)
        MainWindow.setTabOrder(self.PT_Slider4, self.PT_Slider5)
        MainWindow.setTabOrder(self.PT_Slider5, self.PT_Slider6)
        MainWindow.setTabOrder(self.PT_Slider6, self.PT_Slider7)
        MainWindow.setTabOrder(self.PT_Slider7, self.PT_Slider8)
        MainWindow.setTabOrder(self.PT_Slider8, self.PT_Slider9)
        MainWindow.setTabOrder(self.PT_Slider9, self.PT_Slider10)
        MainWindow.setTabOrder(self.PT_Slider10, self.calibration_out)
        MainWindow.setTabOrder(self.calibration_out, self.realDistance)
        MainWindow.setTabOrder(self.realDistance, self.rmse_message)
        MainWindow.setTabOrder(self.rmse_message, self.average_message)
#########################################edit by summerjet#################################
        #initial clear all
    def initialAll(self,pDistance):
        self.pDistance=0
        self.DWScale = 0
        self.scale_distance = 200.0
        self.scale_width = 200.0
        self.distance_real = 8.5
        self.pDistance = pDistance
        self.width_udp, self.distance_udp, self.width, self.distance_delta, self.cal_width, self.cal_distance, self.width_show, self.distance_show = [],[],[],[],[],[],[],[]
        self.cal_width = [0,0,0,0,0,0,0,0,0,0]
        self.cal_distance = [0,0,0,0,0,0,0,0,0,0]
        self.ptSelect = 0
        self.ret = wave_receive_thread()
        self.ret.start()
        self.rdData_calcu_data_gen()
        self.botton_init_value_set()
        self.plot_setup()
        
        
        #set up slots and signals
        self.catchWave.clicked.connect(self.width_distance_udp_sum)
        self.change_calibration.clicked.connect(self.width_distance_calculate)
        self.clearAndClose.clicked.connect(self.clearAndCloseFunc)
        self.saveOriginUdpData.clicked.connect(self.csv_save_udp_sum)
        self.calibration_out.clicked.connect(self.calibration_csv_write)

        self.actionDistancePlus.triggered.connect(self.setShortcut_fun_d_plus)
        self.actionDistanceMinus.triggered.connect(self.setShortcut_fun_d_minus)
        self.actionWidthPlus.triggered.connect(self.setShortcut_fun_w_plus)
        self.actionWidthMinus.triggered.connect(self.setShortcut_fun_w_minus)
        self.actionPointSelectLeft.triggered.connect(self.pointSelectLeft)
        self.actionPointSelect.triggered.connect(self.pointSelectRight)
        self.actionDistanceWidthScaleTab.triggered.connect(self.distanceWidthScale)



        self.channel0.clicked.connect(self.wave_channel_sel)
        self.channel1.clicked.connect(self.wave_channel_sel)
        self.channel2.clicked.connect(self.wave_channel_sel)
        self.channel3.clicked.connect(self.wave_channel_sel)
        self.channel4.clicked.connect(self.wave_channel_sel)
        self.channel5.clicked.connect(self.wave_channel_sel)
        self.channel6.clicked.connect(self.wave_channel_sel)
        self.channel7.clicked.connect(self.wave_channel_sel)

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

    def pointSelectRight(self):
        self.ptSelect +=1
        self.ptSelect=self.ptSelect%10
        print "pt =", self.ptSelect
        self.plt_animation()
    def pointSelectLeft(self):
        self.ptSelect -=1
        self.ptSelect=self.ptSelect%10
        print "pt=", self.ptSelect
        self.plt_animation()
    def setShortcut_fun_d_plus(self):
        if self.DWScale:
            self.cal_distance[self.ptSelect] += 0.5
        else:        
            self.cal_distance[self.ptSelect] += 0.01
        self.plt_animation()
    def setShortcut_fun_d_minus(self):
        if self.DWScale:
            self.cal_distance[self.ptSelect] -= 0.5
        else:        
            self.cal_distance[self.ptSelect] -= 0.01
        self.plt_animation()
    def setShortcut_fun_w_plus(self):
        if self.DWScale:
            self.cal_width[self.ptSelect] += 0.5
        else:    
            self.cal_width[self.ptSelect] += 0.05
        self.plt_animation()
    def setShortcut_fun_w_minus(self):
        if self.DWScale:
            self.cal_width[self.ptSelect] -= 0.5
        else:    
            self.cal_width[self.ptSelect] -= 0.05
        self.plt_animation()
    def distanceWidthScale(self):
        if self.DWScale:
            self.DWScale = 0
        else:
            self.DWScale = 1



    def botton_init_value_set(self):
        self.cal_distance_set_init = []
        self.cal_width_set_init=[]
        width_max = max(self.width)
        width_min = min(self.width)
        step = 10
        step_value = (width_max - width_min)/step

        for r in range(step):
            self.cal_width_set_init.append(r*step_value+0.5*step_value+width_min)
        for k in range(step):
            dis_av_pt = []
            for m in range(len(self.width)):
                #if self.width[m]>=(k+0.5)*step_value-step_value*0.2 and self.width[m]<=(k+0.5)*step_value+step_value*0.2:
                if self.width[m]>=(k+0.5)*step_value-step_value*0.2 and self.width[m]<=(k+0.5)*step_value+step_value*0.2:
                    dis_av_pt.append(self.distance_delta[m])
            if dis_av_pt:
                self.cal_distance_set_init.append(float(numpy.mean(dis_av_pt)))
            else:
                self.cal_distance_set_init.append(0)

        #print "cal_distance_set_init = ",self.cal_distance_set_init
        #print "config before =", self.cal_width_set_init, "s ", self.cal_width_set_init[1]
        self.PT_Slider1.setValue(self.cal_width_set_init[0]*self.scale_width)
        self.PT_Slider2.setValue(self.cal_width_set_init[1]*self.scale_width)
        self.PT_Slider3.setValue(self.cal_width_set_init[2]*self.scale_width)
        self.PT_Slider4.setValue(self.cal_width_set_init[3]*self.scale_width)
        self.PT_Slider5.setValue(self.cal_width_set_init[4]*self.scale_width)
        self.PT_Slider6.setValue(self.cal_width_set_init[5]*self.scale_width)
        self.PT_Slider7.setValue(self.cal_width_set_init[6]*self.scale_width)
        self.PT_Slider8.setValue(self.cal_width_set_init[7]*self.scale_width)
        self.PT_Slider9.setValue(self.cal_width_set_init[8]*self.scale_width)
        self.PT_Slider10.setValue(self.cal_width_set_init[9]*self.scale_width)

        self.PT_Slider_distance_1.setValue(self.cal_distance_set_init[0]*self.scale_distance)
        self.PT_Slider_distance_2.setValue(self.cal_distance_set_init[1]*self.scale_distance)
        self.PT_Slider_distance_3.setValue(self.cal_distance_set_init[2]*self.scale_distance)
        self.PT_Slider_distance_4.setValue(self.cal_distance_set_init[3]*self.scale_distance)
        self.PT_Slider_distance_5.setValue(self.cal_distance_set_init[4]*self.scale_distance)
        self.PT_Slider_distance_6.setValue(self.cal_distance_set_init[5]*self.scale_distance)
        self.PT_Slider_distance_7.setValue(self.cal_distance_set_init[6]*self.scale_distance)
        self.PT_Slider_distance_8.setValue(self.cal_distance_set_init[7]*self.scale_distance)
        self.PT_Slider_distance_9.setValue(self.cal_distance_set_init[8]*self.scale_distance)
        self.PT_Slider_distance_10.setValue(self.cal_distance_set_init[9]*self.scale_distance)
        
        #print "============", self.cal_width_set_init,"==============", self.cal_distance_set_init
        #print self.PT_Slider1.value()," ", self.PT_Slider2.value()
    def botton_value_set(self):
        #print "cal_distance_set_init = ",self.cal_distance_set_init
        
        #print "config before =", self.cal_width_set_init, "s ", self.cal_width_set_init[1]
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
        #print "============", self.cal_width_set_init,"==============", self.cal_distance_set_init
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
    ######## botton setting end
    def calculation_showData_gen(self):
        step = 10
        self.cal_distance = self.cal_distance_set
        self.cal_width=self.cal_width_set
        
        self.distance_show = []
        self.width_show = self.width
        x=self.cal_width
        y=self.cal_distance
        #print "llll = ", x,"\n\n", y, "\n\n"
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
                    #print "wrong data"
            self.distance_show.append(distance_show_temp-self.distance_delta[h]+self.distance_real)
        return self.width_show, self.distance_show
        
    def clearAndCloseFunc(self):
        self.width_udp, self.distance_udp = [], []
        self.distance_udp = []
        self.ret.stop()
        self.ret.join()

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
        elif self.channel4.isChecked():
            self.channel_opt =4
            print "channel3 is checked ====",self.channel_opt
        elif self.channel5.isChecked():
            self.channel_opt =5
            print "channel3 is checked ====",self.channel_opt
        elif self.channel6.isChecked():
            self.channel_opt =6
            print "channel3 is checked ====",self.channel_opt
        elif self.channel7.isChecked():
            self.channel_opt =7
            print "channel3 is checked ====",self.channel_opt
        else:
            self.channel_opt = 7
            print "default setting !",self.channel_opt
        return self.channel_opt
    '''
    def waveAlgorithm_width_distance_catch_func(self):
        points_num=600
        self.channel_opt = 0
        #ret = wave_receive_thread()
        #ret.start()
        
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
                if width_distance[1]:
                    width_list.append(width_distance[0])
                    distance_list.append(width_distance[1])
                #datahandle.widthGet()
            #matplotlib.pyplot.plot(pSignal[1],pSignal[0],'o-')
            #ret.stop()
            #ret.join()
            
            
        except:
            print "creating treading failed !!!"
        print len(width_list)
        return width_list, distance_list
    '''
    def udpRowData_width_distance_catch_func(self):
        points_num=100
        self.channel_opt = 0
        channel_sel = self.wave_channel_sel()
        
        datahandle = distannce_parse()
        width_list, distance_list = [], []

        for i in range(points_num):
            #time.sleep(0.01)
            width_temp, distance_temp = [], []
            width_temp, distance_temp = datahandle.wave_data_catch(channel_sel)
            if width_temp:
                width_list.append(width_temp)
                distance_list.append(distance_temp)
        return width_list, distance_list
    def width_distance_udp_sum(self):
        #temp_width,temp_distance = self.waveAlgorithm_width_distance_catch_func()
        temp_width,temp_distance = self.udpRowData_width_distance_catch_func()
        self.width_udp += temp_width
        self.distance_udp += temp_distance
        print "data_lenth =", len(self.width_udp), " ", len(self.distance_udp )
    def width_distance_calculate(self):
        self.width,self.distance_delta,self.cal_width,self.cal_distance,self.width_show,self.distance_show = [],[],[],[],[],[]
        self.width_distance_udp_sum()
        width,distance_delta = self.width_udp, self.distance_udp
        width_max = max(width)
        width_min = min(width)
        step = 10
        step_value = (width_max - width_min)/step

        cal_distance = []
        cal_width=[]
        for r in range(step):
            cal_width.append(r*step_value+0.2*step_value+width_min)
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
        
        self.width,self.distance_delta,self.cal_width,self.cal_distance = width,distance_delta,cal_width,cal_distance
        #self.cal_width_set_init , self.cal_distance_set_init= cal_width, cal_distance
        self.cal_width_set_1 , self.cal_distance_set_1= cal_width, cal_distance
        self.botton_value_set()
        print self.width[0:50],"\n\n",self.distance_delta[0:50]#,"\n\n",self.cal_width,"\n\n",self.cal_distance,"\n\n",self.width_show,"\n\n",self.distance_show,"\n","\n",
        self.cal_width_set, self.cal_distance_set = self.cal_width,  self.cal_distance
        
        self.plt_animation()
        self.ret.stop()
        self.ret.join()
        #self.rdData_calcu_data_gen()
        return width,distance_delta,cal_width,cal_distance#,width_show,distance_show

    def simu_data_gen(self):
        width, distance_delta = [], []
        for i in range(100):
            rd_w = random.random()*5+i/20
            width.append(rd_w)
        for j in range(100):
            rd_d = random.random()*0.2+self.width[j]/5
            distance_delta.append(rd_d)
        return 
    def rdData_calcu_data_gen(self): #input self.width and self.distance_delta
        self.width, self.distance_delta = self.csvRead()

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

        self.distance_show = []
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
                    #print "wrong data"
            self.distance_show.append(distance_show_temp-self.distance_delta[h]+self.distance_real)

        self.cal_width_set = self.cal_width
        self.cal_distance_set = self.cal_distance

        return self.cal_width, self.cal_distance, self.width_show, self.distance_show,
        #print "len(self.distance_show =",len(self.distance_show)
    def plot_setup(self):
        self.Fig1 = matplotlib.pyplot.Figure(figsize=(12,10))#matplotlib.pyplot.Figure(figsize=(8,8))
        matplotlib.pyplot =  self.Fig1.add_subplot(211,xlim=(0, 8),\
         ylim=(self.pDistance-0.5,self.pDistance+0.8), facecolor ="w")
        self.line1, = matplotlib.pyplot.plot(self.width,self.distance_delta,'.',lw=2)
        self.line2, = matplotlib.pyplot.plot(self.cal_width,self.cal_distance,'ro--',lw=2)
        self.line4, = matplotlib.pyplot.plot(self.cal_width[self.ptSelect],self.cal_distance[self.ptSelect],'kx',markersize =20,mew=2)
        #matplotlib.pyplot.grid()

        matplotlib.pyplot = self.Fig1.add_subplot(212,xlim=(0, 8),\
         ylim=(self.distance_real-0.1,self.distance_real+0.1))
        #matplotlib.pyplot.plot(x,'ro--',lw=2)
        self.line3, = matplotlib.pyplot.plot(self.width_show,self.distance_show,'bo')
        matplotlib.pyplot.grid()

        self.canvas1 = FigureCanvasQTAgg(self.Fig1)
        self.canvas1.setParent(self.pyplotWidget)
    def plt_animation(self):
        self.calculation_showData_gen()
        self.line1.set_data(self.width,self.distance_delta)
        self.line2.set_data(self.cal_width,self.cal_distance)
        self.line3.set_data(self.width_show, self.distance_show)
        self.line4.set_data(self.cal_width[self.ptSelect],self.cal_distance[self.ptSelect])
        self.canvas1.draw()
        self.propertyCaculate()
        #print "ok"
    def testfunc(self):
        matplotlib.pyplot =  self.Fig1.add_subplot(211,xlim=(0, 10), ylim=(50,200), facecolor ="w")
        self.line1, = matplotlib.pyplot.plot(self.width,self.distance_delta,'.',lw=5)
        self.canvas1.draw()
        #self.line2, = matplotlib.pyplot.plot(self.cal_width,self.cal_distance,'ro--',lw=2)
    
    def calibration_csv_write(self):
        data_read = []
        with open ("./dataTemp/calibration.csv","rb") as f1:
            reader = csv.reader(f1)
            for row in reader:
                data_read.append(row)
        data_read.append(self.cal_width)
        data_read.append(self.cal_distance)

        #print data_read
        with open ("./dataTemp/calibration.csv","wb") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_read)
        print "write successful!"
    def csv_save_udp_sum(self):
        data_read = []
        with open ("./dataTemp/originUdpSumData.csv","rb") as f1:
            reader = csv.reader(f1)
            for row in reader:
                data_read.append(row)
        print  "first=",self.width_udp
        wr_width = self.width_udp
        wr_width.append(self.channel_opt)
        wr_distance = self.distance_udp
        wr_distance.append(self.channel_opt)
        
        data_read.append(wr_width)
        data_read.append(wr_distance)
        #print data_read
        
        with open ("./dataTemp/originUdpSumData.csv","wb") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_read)
        print "write successful!"
        
    def csvRead(self):
        data_handle= []
        width = []
        distance_delta=[]
        
        with open ("./dataTemp/data.csv","rb") as f1:
            reader = csv.reader(f1)
            for row in reader:
                data_handle.append(row)
        print type(data_handle[0][0])
        
        for k in range(len(data_handle)):
            width.append(float(data_handle[k][0]))
            distance_delta.append(float(data_handle[k][1]))
        print "length of import = ",len(width), " ", len(distance_delta)
        return width, distance_delta
    def propertyCaculate(self):
        width_mean = numpy.mean(self.width_show)
        distance_mean = numpy.mean(self.distance_show)
        rmseOfdivergence = numpy.std(self.distance_show)
        self.rmse_message.setText("%f"%round(rmseOfdivergence,4))
        self.average_message.setText("%f"%round(distance_mean,4))
        self.lcdNumber.display(len(self.width_show))
        return width_mean

###########################################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.change_calibration_3.setText(_translate("MainWindow", "cal_distance"))
        self.label1.setText(_translate("MainWindow", "Pt1"))
        self.change_calibration_2.setText(_translate("MainWindow", "cal_width"))
        self.label1_9.setText(_translate("MainWindow", "Pt9"))
        self.label1_10.setText(_translate("MainWindow", "Pt10"))
        self.label1_6.setText(_translate("MainWindow", "Pt6"))
        self.label1_5.setText(_translate("MainWindow", "Pt5"))
        self.label1_4.setText(_translate("MainWindow", "Pt4"))
        self.channel4.setText(_translate("MainWindow", "channel4"))
        self.label1_7.setText(_translate("MainWindow", "Pt7"))
        self.label1_2.setText(_translate("MainWindow", "Pt2"))
        self.label1_3.setText(_translate("MainWindow", "Pt3"))
        self.label1_8.setText(_translate("MainWindow", "Pt8"))
        self.calibration_out.setText(_translate("MainWindow", "calibration_file_output"))
        self.clearAndClose.setText(_translate("MainWindow", "clear / close"))
        self.change_calibration.setText(_translate("MainWindow", "state_calib"))
        self.channel5.setText(_translate("MainWindow", "channel5"))
        self.channel6.setText(_translate("MainWindow", "channel6"))
        self.channel1.setText(_translate("MainWindow", "channel1"))
        self.catchWave.setText(_translate("MainWindow", "Catch wave"))
        self.channel3.setText(_translate("MainWindow", "channel3"))
        self.channel0.setText(_translate("MainWindow", "channel0"))
        self.channel2.setText(_translate("MainWindow", "channel2"))
        self.saveOriginUdpData.setText(_translate("MainWindow", "saveOriginUdpData"))
        self.channel7.setText(_translate("MainWindow", "channel7"))
        self.rmse_message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1230</p></body></html>"))
        self.label.setText(_translate("MainWindow", "rmse"))
        self.average_message.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">1230</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "average"))
        self.label_3.setText(_translate("MainWindow", "Number of Points"))
        self.label_4.setText(_translate("MainWindow", "real_distance"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAction.setTitle(_translate("MainWindow", "Action"))
        self.menuPointsAction.setTitle(_translate("MainWindow", "pointsAction"))
        self.actionOpen.setText(_translate("MainWindow", "open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionClose.setText(_translate("MainWindow", "close"))
        self.actionClose.setShortcut(_translate("MainWindow", "Ctrl+C, Ctrl+L"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_as.setText(_translate("MainWindow", "save as"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionCatchWave.setText(_translate("MainWindow", "catchWave"))
        self.actionCatchWave.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionClearAndClose.setText(_translate("MainWindow", "clearAndClose"))
        self.actionClearAndClose.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSaveOriginUdpData.setText(_translate("MainWindow", "saveOriginUdpData"))
        self.actionSaveOriginUdpData.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCalibrationFileOutput.setText(_translate("MainWindow", "calibrationFileOutput"))
        self.actionCalibrationFileOutput.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionDistancePlus.setText(_translate("MainWindow", "distancePlus"))
        self.actionDistancePlus.setShortcut(_translate("MainWindow", "Up"))
        self.actionDistanceMinus.setText(_translate("MainWindow", "distanceMinus"))
        self.actionDistanceMinus.setShortcut(_translate("MainWindow", "Down"))
        self.actionWidthPlus.setText(_translate("MainWindow", "widthPlus"))
        self.actionWidthPlus.setShortcut(_translate("MainWindow", "Right"))
        self.actionWidthMinus.setText(_translate("MainWindow", "widthMinus"))
        self.actionWidthMinus.setShortcut(_translate("MainWindow", "Left"))
        self.actionPointSelect.setText(_translate("MainWindow", "pointSelectRight"))
        self.actionPointSelect.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.actionPointSelectLeft.setText(_translate("MainWindow", "pointSelectLeft"))
        self.actionPointSelectLeft.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.actionDistanceWidthScaleTab.setText(_translate("MainWindow", "distanceWidthScaleTab"))
        self.actionDistanceWidthScaleTab.setShortcut(_translate("MainWindow", "M"))

import qrc_rc
