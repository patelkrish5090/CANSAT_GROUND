# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 325)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        #Menubar
        #-----------------------
        self.menubar = self.menuBar()
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 840, 22))

        self.menuStart = self.menubar.addMenu('Start')
        self.actionStart = QAction("Start", MainWindow)
        self.menuStart.addAction(self.actionStart)

        self.menuStop = self.menubar.addMenu('Stop')
        self.actionStop = QAction("Stop", MainWindow)
        self.menuStop.addAction(self.actionStop)

        self.menuCalibrate = self.menubar.addMenu('Calibrate')
        self.actionCalibrate = QAction("Calibrate", MainWindow)
        self.menuCalibrate.addAction(self.actionCalibrate)


        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        #--------------------
        self.Pressure = PlotWidget(self.centralwidget)
        self.Pressure.setObjectName(u"Pressure")
        self.Pressure.setGeometry(QRect(10, 10, 121, 121))
        self.Pressure.setMaximumSize(QSize(200, 200))
        self.Pressure.setStyleSheet(u"background-color: black")
        self.Altitude = PlotWidget(self.centralwidget)
        self.Altitude.setObjectName(u"Altitude")
        self.Altitude.setGeometry(QRect(10, 160, 121, 121))
        self.Altitude.setMaximumSize(QSize(121, 121))
        self.Altitude.setStyleSheet(u"background-color: black")
        self.Speed = PlotWidget(self.centralwidget)
        self.Speed.setObjectName(u"Speed")
        self.Speed.setGeometry(QRect(150, 10, 121, 121))
        self.Speed.setMaximumSize(QSize(121, 121))
        self.Speed.setStyleSheet(u"background-color: black")
        self.Temperature = PlotWidget(self.centralwidget)
        self.Temperature.setObjectName(u"Temperature")
        self.Temperature.setGeometry(QRect(150, 160, 121, 121))
        self.Temperature.setMaximumSize(QSize(121, 121))
        self.Temperature.setStyleSheet(u"background-color:black")
        self.AccelerationX = PlotWidget(self.centralwidget)
        self.AccelerationX.setObjectName(u"AccelerationX")
        self.AccelerationX.setGeometry(QRect(290, 10, 121, 121))
        self.AccelerationX.setMaximumSize(QSize(121, 121))
        self.AccelerationX.setStyleSheet(u"background-color:black")
        self.AccelerationY = PlotWidget(self.centralwidget)
        self.AccelerationY.setObjectName(u"AccelerationY")
        self.AccelerationY.setGeometry(QRect(290, 160, 121, 121))
        self.AccelerationY.setMaximumSize(QSize(121, 121))
        self.AccelerationY.setStyleSheet(u"background-color: black")
        self.AccelerationZ = PlotWidget(self.centralwidget)
        self.AccelerationZ.setObjectName(u"AccelerationZ")
        self.AccelerationZ.setGeometry(QRect(430, 10, 121, 121))
        self.AccelerationZ.setMaximumSize(QSize(121, 121))
        self.AccelerationZ.setStyleSheet(u"background-color: black")
        self.Map = PlotWidget(self.centralwidget)
        self.Map.setObjectName(u"Map")
        self.Map.setGeometry(QRect(430, 160, 121, 121))
        self.Map.setMaximumSize(QSize(121, 121))
        self.Map.setStyleSheet(u"background-color: black")
        self.RawData = QTableWidget(self.centralwidget)
        self.RawData.setObjectName(u"RawData")
        self.RawData.setGeometry(QRect(580, 140, 256, 141))
        self.Gyro = PlotWidget(self.centralwidget)
        self.Gyro.setObjectName(u"Gyro")
        self.Gyro.setGeometry(QRect(580, 10, 251, 121))
        self.Gyro.setStyleSheet(u"background-color: black")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuStart.setTitle(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuStop.setTitle(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.menuCalibrate.setTitle(QCoreApplication.translate("MainWindow", u"Calibrate", None))
    # retranslateUi
        
    def start(self):
        print("You Clicked Start Button")

    def stop(self):
        print("You Clicked Start Button")

    def calibrate(self):
        print("You Clicked Start Button")