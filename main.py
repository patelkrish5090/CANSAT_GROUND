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
from graphs.graph_time import graph_time



pg.setConfigOption('background', (244, 244, 2444))
pg.setConfigOption('foreground','black')


app = QtWidgets.QApplication(sys.argv)
view = pg.GraphicsView()
Layout = pg.GraphicsLayout()
view.setCentralItem(Layout)
view.show()
view.setWindowTitle('Flight Data')
view.resize(1400, 1000)

# declare object for serial Communication
ser = Communication()
# declare object for storage in CSV
data_base = data_base()
# Fonts for text items
font = QtGui.QFont('Arial', 1)
font.setPixelSize(150)

# Declare graphs

# Altitude graph
altitude = graph_altitude()
# Speed graph
speed = graph_speed()
# Acceleration graph
acceleration = graph_acceleration()
# Gyro graph
gyro = graph_gyro()
# Pressure Graph
pressure = graph_pressure()
# Temperature graph
temperature = graph_temperature()
# Time graph
time = graph_time(font=font)



text="""Cansat Project BITS Goa"""
Layout.addLabel(text, col=2, colspan=10)
Layout.nextRow()


l1 = Layout.addLayout(colspan=20, rowspan=2)
l11 = l1.addLayout(rowspan=1, colspan=5, border='black')

# Altitude, speed
l11.addItem(altitude)
l11.addItem(speed)
l11.addItem(temperature)
l11.addItem(pressure)


l1.nextRow()


l12 = l1.addLayout(rowspan=1, colspan=7, border='black')
l12.addItem(acceleration)
l12.addItem(gyro)
l12.addItem(time)


def update():
    try:
        value_chain = []
        value_chain = ser.getData()
        altitude.update(value_chain[1])
        speed.update(value_chain[8], value_chain[9], value_chain[10])
        time.update(value_chain[0])
        acceleration.update(value_chain[8], value_chain[9], value_chain[10])
        gyro.update(value_chain[5], value_chain[6], value_chain[7])
        pressure.update(value_chain[4])
        temperature.update(value_chain[3])
        data_base.guardar(value_chain)
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
