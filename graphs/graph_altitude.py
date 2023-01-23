import pyqtgraph as pg
import numpy as np

class graph_altitude:

    def __init__(self, widget):
        self.widget = widget
        self.widget.getPlotItem().setTitle("Altitude")
        # super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)
        self.altitude_plot = self.widget.plot(pen= pg.mkPen('b', width=3))
        self.altitude_data = np.linspace(0, 0, 30)
        self.ptr1 = 0

    def update(self, value):
        self.altitude_data[:-1] = self.altitude_data[1:]
        self.altitude_data[-1] = float(value)
        self.ptr1 += 1
        self.altitude_plot.setData(self.altitude_data)
        self.altitude_plot.setPos(self.ptr1, 0)