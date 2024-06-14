import sys

from pyqtgraph.Qt import QtCore, QtWidgets
import pyqtgraph as pg
from PySide6 import QtWidgets
from PyQt5.QtWidgets import QAction, QMenuBar, QMenu
from PyQt5.uic import loadUi


from communication import Communication
from dataBase import data_base

from graphs.graph_altitude import graph_altitude
from graphs.graph_gyro import graph_gyro
from graphs.graph_gyro_z import graph_gyro_z
from graphs.graph_pressure import graph_pressure

# from graphs.graph_humidity import graph_humidity
from graphs.graph_temperature import graph_temperature

# from graphs.graph_heat_index import graph_heat_index
# from graphs.graph_map import graph_map
# from graphs.graph_accX import graph_accelerationX
# from graphs.graph_accY import graph_accelerationY
# from graphs.graph_accZ import graph_accelerationZ
#

pg.setConfigOption("background", (244, 244, 244))
pg.setConfigOption("foreground", "black")


uiclass, baseclass = pg.Qt.loadUiType("graphs/main.ui")


class Window(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Flight Data")
        self.RawData.setColumnCount(11)
        self.altitude = graph_altitude(self.Altitude)
        self.pressure = graph_pressure(self.Pressure)
        self.temperature = graph_temperature(self.Temperature, "Temperature")
        # self.humidity = graph_humidity(self.Humidity)
        self.gyro = graph_gyro(self.Gyro)
        self.gyro_z = graph_gyro_z(self.Gyro_Z)
        # self.heatIndex = graph_heat_index(self.HeatIndex)
        # self.map = graph_map(self.Map)
        # self.accelerationZ = graph_accelerationZ(self.AccelerationZ)
        # self.accelerationY = graph_accelerationY(self.AccelerationY)
        # self.accelerationX = graph_accelerationX(self.AccelerationX)
        
        self.actionStart.triggered.connect(self.start)
        self.actionStop.triggered.connect(self.stop)
        self.actionCalibrate.triggered.connect(self.calibrate)

    def update_console(self, text):
        print("updating, {}".format(text))
        self.RawData.setRowCount(self.RawData.rowCount() + 1)
        print(len(text))
        for i, item in enumerate(text):
            item = QtWidgets.QTableWidgetItem(str(item))
            self.RawData.setItem(self.RawData.rowCount() - 1, i, item)

    def start(self):
        self.lastCommand = "Last Command Sent: Start"
        print(self.lastCommand)

    def stop(self):
        print("Last Command Sent: Stop")

    def calibrate(self):
        print("Last Command Sent: Calibrate")


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()

ser = Communication()
data_base = data_base()
# altitude = graph_altitude()
# speed = graph_speed()

# acceleration = graph_acceleration()
# accelerationX = graph_accelerationX()
# accelerationY = graph_accelerationY()
# accelerationZ = graph_accelerationZ()
# gyro = graph_gyro()
# pressure = graph_pressure()
# temperature = graph_temperature()


def update():
    try:
        data = []
        data = ser.getData()
        # TODO: Use telemetry string format to parse data
        # TODO: Check data integrity
        # DATA FORMAT: TEAM_ID, TIMESTAMP, PACKET_COUNT, ALTITUDE, PRESSURE,
        # TEMP, VOLTAGE, GNSS_TIME, GNSS_LATITUDE, GNSS_LONGITUDE,
        # GNSS_ALTITUDE, GNSS_SATS, ACCELEROMETER_DATA, GYRO_SPIN_RATE,
        # FLIGHT_SOFTWARE_STATE, OPTIONAL_DATA
        window.altitude.update(float(data[-1]))
        # window.humidity.update(float(data[2]))
        window.pressure.update(float(data[0]))
        window.temperature.update(float(data[1]))
        window.gyro.update(float(data[2]), float(data[3]))
        window.gyro_z.update(float(data[4]))
        # window.gnss_temperature.update(data[7])
        # window.accelerationZ.update(data[10])
        # window.accelerationY.update(data[9])
        # window.accelerationX.update(data[8])

        data_base.guardar(data)
        window.update_console(data)
    except IndexError:
        print("starting, please wait a moment")
    except KeyboardInterrupt:
        exit()


if (ser.isOpen()) or (ser.dummyMode()):
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(500)
else:
    print("UPDATE CALL ERROR")

def start(self):
    self.lastCommand = "Last Command Sent: Start"
    print(self.lastCommand)

def stop(self):
    print("Last Command Sent: Stop")

def calibrate(self):
    print("Last Command Sent: Calibrate")


if __name__ == "__main__":
    if (sys.flags.interactive != 1) or not hasattr(QtCore, "PYQT_VERSION"):
        QtWidgets.QApplication.instance().exec_()
