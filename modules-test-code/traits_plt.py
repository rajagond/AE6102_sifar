from traits.api import HasTraits, Instance
from traitsui.api import View, Item, InstanceEditor
from traitsui.editors import ImageEditor
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtGui

class MatplotlibPlot(HasTraits):
    figure = Instance(Figure, ())
    
    traits_view = View(
        Item('canvas', editor=ImageEditor(), show_label=False),
        resizable=True, title="Matplotlib Figure"
    )

    def _init_(self):
        super(MatplotlibPlot, self)._init_()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        
    def plot(self, x, y):
        self.ax.plot(x, y)
        self.canvas.draw()

class MyGUI(HasTraits):
    plot = Instance(MatplotlibPlot)
    
    view = View(
        Item('plot', editor=InstanceEditor(), show_label=False),
        resizable=True, title="My GUI"
    )

    def _init_(self):
        super(MyGUI, self)._init_()
        self.plot = MatplotlibPlot()
        
        # Example data
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]
        
        # Plot the data
        self.plot.plot(x, y)

if __name__ == '__main__':
    app = QtGui.QGuiApplication([])
    gui = MyGUI()
    gui.configure_traits()