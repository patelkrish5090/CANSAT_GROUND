import pyqtgraph as pg
import numpy as np


class graph_gyro_z:
    
    def __init__(self, widget):
        self.widget = widget
        self.widget.getPlotItem().setTitle("Gyro Z")

        self.gyro_plot = self.widget.plot(pen= pg.mkPen('b', width=3))
        self.gyro_data = np.linspace(0, 0, 30)
        self.ptr = 0


    def update(self, value):
        self.gyro_data[:-1] = self.gyro_data[1:]
        self.gyro_data[-1] = float(value)
        self.ptr += 1
        self.gyro_plot.setData(self.gyro_data)
        self.gyro_plot.setPos(self.ptr, 0)
