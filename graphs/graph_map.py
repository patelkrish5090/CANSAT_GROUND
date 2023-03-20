import pyqtgraph as pg
import numpy as np


class graph_temperature:
    
    def __init__(self, widget):
        #super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)

        self.widget = widget
        self.widget.getPlotItem().setTitle("Map")
        self.temp_plot = self.widget.plot(pen= pg.mkPen('b', width=3))
        self.temp_data = np.linspace(0, 0, 30)
        self.ptr = 0


    def update(self, value):
        self.temp_data[:-1] = self.temp_data[1:]
        self.temp_data[-1] = float(value)
        self.ptr += 1
        self.temp_plot.setData(self.temp_data)
        self.temp_plot.setPos(self.ptr, 0)
