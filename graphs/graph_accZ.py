import pyqtgraph as pg
import numpy as np


class graph_accelerationZ:

    def __init__(self, widget):
        self.widget = widget
        self.widget.getPlotItem().setTitle("AccelerationZ")
        #super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)

        self.widget.hideAxis('bottom')


        self.accZ_plot = self.widget.plot(pen=pg.mkPen((0, 0, 255), width=3), name="Z")


        self.accZ_data = np.linspace(0, 0)
        self.ptr = 0

    def update(self, az):

        self.accZ_data[:-1] = self.accZ_data[1:]
        self.accZ_data[-1] = float(az)
        self.ptr += 1
        self.accZ_plot.setData(self.accZ_data)
        self.accZ_plot.setPos(self.ptr, 0)