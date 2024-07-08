from PyQt5 import QtCore, QtGui, QtWidgets
from RawInterfaces.MainWindow import Ui_MainWindow
from AgregarVenta import ventaInterface
from agregarCliente import ClienteInterface
from AbonarCliente import AbonarWindow
from VerClientes import VerClientesInterface
class MainWindowu(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
        self.AgregarVentasButton.clicked.connect(self.abrirVentas)
        self.AgregarClientesButton.clicked.connect(self.abrirClientes)
        self.AbonoClienteButton.clicked.connect(self.abrirAbonar)
        self.AbrirClientesVentasButton.clicked.connect(self.abrirVerVentasClientes)
    def abrirVentas(self):
        self.window = ventaInterface()
        self.window.show()
    def abrirClientes(self):
        self.window = ClienteInterface()
        self.window.show()
    def abrirAbonar(self):
        self.window = AbonarWindow()
        self.window.show()
    def abrirVerVentasClientes(self):
        self.window = VerClientesInterface()
        self.window.show()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowu()
    ui.show()
    sys.exit(app.exec_())
