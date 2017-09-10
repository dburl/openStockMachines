from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("OpenStockMachines - Home Dashboard")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window=MainWindow()
    window.show()

    app.exec_()
