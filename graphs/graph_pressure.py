import pyqtgraph as pg
import numpy as np


class graph_pressure:
    
    def __init__(self, widget):
        self.widget = widget
        self.widget.getPlotItem().setTitle("Gyro height")

        self.pressure_plot = self.widget.plot(pen= pg.mkPen('b', width=3))
        self.pressure_data = np.linspace(0, 0, 30)
        self.ptr = 0


    def update(self, value):
        self.pressure_data[:-1] = self.pressure_data[1:]
        self.pressure_data[-1] = float(value)
        self.ptr += 1
        self.pressure_plot.setData(self.pressure_data)
        self.pressure_plot.setPos(self.ptr, 0)
