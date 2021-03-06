from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.pyplot import figure
from core import plot_all, set_axis_props


class Canvas(FigureCanvasQTAgg):
    def __init__(self, size=(20, 20)) -> None:
        self.figure = figure(figsize=size)
        self.axis = self.figure.add_subplot(111)
        set_axis_props(self.axis)
        super().__init__(self.figure)

    def plot_curve(self, alpha, beta, left, right, m, n):
        self.axis.cla()
        plot_all(self.axis, alpha, beta, left, right, m, n)
        self.figure.canvas.draw_idle()
        self.figure.tight_layout()
