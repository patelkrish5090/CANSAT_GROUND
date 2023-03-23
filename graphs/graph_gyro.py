import pyqtgraph as pg
import numpy as np


class graph_gyro:
    def __init__(self, widget):
        self.widget = widget
        self.widget.getPlotItem().setTitle("Gyro")

        # self.widget.hideAxis("bottom")
        self.scatter = pg.ScatterPlotItem(pxmode=False)
        self.widget.addItem(self.scatter)
        self.old = []
        # self.widget.plotItem.showGrid(True, True, 0.7)
        # self.widget.addLine(y=0, pen=pg.mkPen((255, 0, 0), width=1))
        # self.widget.addLine(x=0, pen=pg.mkPen((255, 0, 0), width=1))
        # self.widget.setXRange(-10, 10)
        # self.widget.setYRange(-10, 10)
        # adding legend
        # self.widget.addLegend()
        # self.pitch_plot = self.widget.plot(pen= pg.mkPen((255, 0, 0), width=3), name="Pitch")
        # self.roll_plot = self.widget.plot(pen= pg.mkPen((0, 255, 0), width=3), name="Roll")
        # self.yaw_plot = self.widget.plot(pen= pg.mkPen((0, 0, 255), width=3), name="Yaw")
        #
        # self.pitch_data = np.linspace(0, 0)
        # self.roll_data = np.linspace(0, 0)
        # self.yaw_data = np.linspace(0, 0)
        # self.ptr = 0






    def update(self, x, y):
        self.scatter.setData(self.old)
        x = np.pi / 180 * x
        self.scatter.addPoints(
            [
                {
                    "pos": (np.cos(x), np.sin(x)),
                    "size": 15,
                    "pen": {"color": "red", "width": 5},
                    "brush": pg.mkBrush(0, 0, 255),
                }
            ]
        )
        self.old.append(
            {
                    "pos": (np.cos(x), np.sin(x)),
                "size": 5,
                "pen": {"color": "blue", "width": 1},
                "brush": pg.mkBrush(0, 0, 255),
            }
        )

        self.old = self.old[-30:]

    # def update(self, pitch, roll, yaw):
    #
    # self.pitch_data[:-1] = self.pitch_data[1:]
    # self.roll_data[:-1] = self.roll_data[1:]
    # self.yaw_data[:-1] = self.yaw_data[1:]
    #
    # self.pitch_data[-1] = float(pitch)
    # self.roll_data[-1] = float(roll)
    # self.yaw_data[-1] = float(yaw)
    #
    # self.ptr += 1
    #
    # self.pitch_plot.setData(self.pitch_data)
    # self.roll_plot.setData(self.roll_data)
    # self.yaw_plot.setData(self.yaw_data)
    #
    # self.pitch_plot.setPos(self.ptr, 0)
    # self.roll_plot.setPos(self.ptr, 0)
    # self.yaw_plot.setPos(self.ptr, 0)
