import pyqtgraph as pg
import numpy as np


class graph_accelerationX(pg.PlotItem):

    def __init__(self, widget):
        self.widget = widget
        self.widget.getPlotItem().setTitle("AccelerationX")
        #super().__init__(parent, name, labels, title, viewBox, axisItems, enableMenu, **kargs)
        self.widget.hideAxis('bottom')

        self.accX_plot = self.widget.plot(pen=pg.mkPen((255, 0, 0), width=3), name="X")
        self.accX_data = np.linspace(0, 0)
        self.ptr = 0

    def update(self, ax):
        self.accX_data[:-1] = self.accX_data[1:]
        self.accX_data[-1] = float(ax)
        self.ptr += 1
        self.accX_plot.setData(self.accX_data)
        self.accX_plot.setPos(self.ptr, 0)