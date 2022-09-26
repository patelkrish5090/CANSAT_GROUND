import sys
from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import pyqtgraph as pg
from communication import Communication
from dataBase import data_base

from graphs.graph_acceleration import graph_acceleration
from graphs.graph_altitude import graph_altitude
from graphs.graph_gyro import graph_gyro
from graphs.graph_pressure import graph_pressure
from graphs.graph_speed import graph_speed
from graphs.graph_temperature import graph_temperature
from graphs.graph_accX import graph_accelerationX
from graphs.graph_accY import graph_accelerationY
from graphs.graph_accZ import graph_accelerationZ



pg.setConfigOption('background', (244, 244, 244))
pg.setConfigOption('foreground','black')


app = QtWidgets.QApplication(sys.argv)
view = pg.GraphicsView()
Layout = pg.GraphicsLayout()
view.setCentralItem(Layout)
view.show()
view.setWindowTitle('Flight Data')
view.resize(1400, 1000)


ser = Communication()
data_base = data_base()
font = QtGui.QFont('Arial', 1)
font.setPixelSize(150)


# Create buttons
styleStop = "background-color:rgb(255, 51, 51);" \
            "color:rgb(0,0,0);" \
            "font-size:14px;"
styleStart = "background-color:rgb(29, 185, 84);" \
             "color:rgb(0,0,0);" \
             "font-size:14px;"
styleCali = "background-color:rgb(0, 128, 255);" \
             "color:rgb(0,0,0);" \
             "font-size:14px;"

start = QtWidgets.QGraphicsProxyWidget()
btn1 = QtWidgets.QPushButton('Start Data Collection')
btn1.setStyleSheet(styleStart)
btn1.clicked.connect(data_base.start)
start.setWidget(btn1)

stop = QtWidgets.QGraphicsProxyWidget()
btn2 = QtWidgets.QPushButton('Stop Data Collection')
btn2.resize(150, 50)
btn2.setStyleSheet(styleStop)
btn2.clicked.connect(data_base.stop)
stop.setWidget(btn2)

cali = QtWidgets.QGraphicsProxyWidget()
btn3 = QtWidgets.QPushButton('Calibrate Sensors')
btn3.setStyleSheet(styleCali)
btn3.clicked.connect(data_base.stop)
cali.setWidget(btn3)


# Import graphs

altitude = graph_altitude()

speed = graph_speed()

acceleration = graph_acceleration()
accelerationX = graph_accelerationX()
accelerationY = graph_accelerationY()
accelerationZ= graph_accelerationZ()

gyro = graph_gyro()

pressure = graph_pressure()

temperature = graph_temperature()




text="""Cansat Project BITS Goa"""
Layout.addLabel(text, col=0, colspan=2)
Layout.nextCol()
Layout.addItem(start)
Layout.nextCol()
Layout.addItem(stop)
Layout.nextCol()
Layout.addItem(cali)

Layout.nextRow()

l1 = Layout.addLayout(colspan=20, rowspan=2)
l11 = l1.addLayout(rowspan=1, colspan=20, border='black')

# Altitude, speed
l11.addItem(altitude)
l11.nextCol()
l11.addItem(speed)
l11.nextCol()
l11.addItem(temperature)
l11.nextCol()
l11.addItem(pressure)


l1.nextRow()


l12 = l1.addLayout(rowspan=1, colspan=20, border='black')

l12.addItem(accelerationX)
l12.nextCol()
l12.addItem(accelerationY)
l12.nextCol()
l12.addItem(accelerationZ)
l12.nextCol()
l12.addItem(gyro)




def update():
    try:
        data = []
        data = ser.getData()
        altitude.update(data[1])
        speed.update(data[8], data[9], data[10])
        accelerationX.update(data[8])
        accelerationY.update(data[9])
        accelerationZ.update(data[10])
        gyro.update(data[5], data[6], data[7])
        pressure.update(data[4])
        temperature.update(data[3])
        data_base.guardar(data)
    except IndexError:
        print('starting, please wait a moment')


if(ser.isOpen()) or (ser.dummyMode()):
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(500)
else:
    print("UPDATE CALL ERROR")


if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()
