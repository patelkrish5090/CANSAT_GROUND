import pyqtgraph as pg
import numpy as np


class graph_accelerationY:

    def __init__(self, widget):
        self.widget = widget
        self.widget.getPlotItem().setTitle("AccelerationY")
        #super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)

        self.widget.hideAxis('bottom')
        self.accY_plot = self.widget.plot(pen=pg.mkPen((0, 255, 0), width=3), name="Y")
        self.accY_data = np.linspace(0, 0)
        self.ptr = 0

    def update(self, ay):
        self.accY_data[:-1] = self.accY_data[1:]
        self.accY_data[:-1] = self.accY_data[1:]
        self.accY_data[-1] = float(ay)
        self.ptr += 1
        self.accY_plot.setData(self.accY_data)
        self.accY_plot.setPos(self.ptr, 0)
