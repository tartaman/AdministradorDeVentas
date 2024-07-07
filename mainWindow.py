from PyQt5 import QtCore, QtGui, QtWidgets
from RawInterfaces.MainWindow import Ui_MainWindow
from AgregarVenta import ventaInterface
from agregarCliente import ClienteInterface
from AbonarCliente import AbonarWindow
class MainWindowu(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
        self.AgregarVentasButton.clicked.connect(self.abrirVentas)
        self.AgregarClientesButton.clicked.connect(self.abrirClientes)
        self.AbonoClienteButton.clicked.connect(self.abrirAbonar)
    def abrirVentas(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ventaInterface()
        self.ui.setupUi(self.window)
        self.window.show()
    def abrirClientes(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ClienteInterface()
        self.ui.setupUi(self.window)
        self.window.show()
    def abrirAbonar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = AbonarWindow()
        self.ui.setupUi(self.window)
        self.window.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowu()
    ui.show()
    sys.exit(app.exec_())
