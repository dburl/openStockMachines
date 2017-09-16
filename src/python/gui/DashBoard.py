from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random

import sys

from gui.CandlePlot import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.initUI()
        self.drawPlot()
    def initUI(self):
        self.setWindowTitle("OpenStockMachines - Home Dashboard")
        self.statusBar().showMessage('Ready')
        self.setGeometry(50,50,650,650)
    def drawPlot(self):
        m = CandlePlot(self, width=5, height=4)
        m.move(0, 0)

        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This s an example button')
        button.move(500, 0)
        button.resize(140, 100)


class RemittanceDashBoard:
    def exec(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
