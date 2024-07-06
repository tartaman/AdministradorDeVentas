from RawInterfaces.Abonar import Ui_AbonarWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import conection
from tkinter import messagebox

class AbonarWindow(Ui_AbonarWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_AbonarWindow.setupUi(self, self)
        self.Conector = conection.Conector()
