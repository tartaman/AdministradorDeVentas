from PyQt5 import QtCore, QtGui, QtWidgets
from RawInterfaces.EditarVentaCliente import Ui_EditarVentaClienteWindow
import conection
from Objetos.Cliente import Cliente
from Objetos.Venta import Venta
from tkinter import messagebox

class EditarVentaClienteInterface(Ui_EditarVentaClienteWindow,QtWidgets.QMainWindow):
    def __init__(self,idCliente,idVenta):
        super().__init__()
        Ui_EditarVentaClienteWindow.setupUi(self,self)
        self.Conector = conection.Conector()
        self.idCliente = idCliente
        self.idVenta = idVenta
        self.EditarCamposButton.clicked.connect(self.editar)
        print(idCliente,idVenta)
        self.LlenarDatosInicio()
    def LlenarDatosInicio(self):
        self.Conector.cursor.execute("SELECT * FROM cliente c INNER JOIN venta v WHERE id_cliente = %s AND id_venta = %s", [self.idCliente,self.idVenta])
        result = self.Conector.cursor.fetchone()
        self.NombreLineEdit.setText(str(result[1]))
        self.EdadLineEdit.setText(str(result[2]))
        self.TelefonoLineEdit.setText(str(result[3]))
        self.SaldoPendienteLineEdit.setText(str(result[4]))
    def editar(self):
        cliente = Cliente(self.idCliente,self.NombreLineEdit.text(),self.EdadLineEdit.text(),
                          self.TelefonoLineEdit.text(),self.SaldoPendienteLineEdit.text())
        fechavisita = self.CalendarioVisita.selectedDate().getDate()
        fechaLiquidacion = self.CalendarioLiquidacion.selectedDate().getDate()
        venta = Venta(self.idVenta, f"{fechavisita[0]}/{fechavisita[1]}/{fechavisita[2]}",self.idCliente
                      ,self.ProductoLineEdit.text(),
                      self.MicaLineEdit.text(),
                      self.CostoTotalLineEdit.text(),
                      self.AbonoVentaLineEdit.text(),
                      self.SaldoPendienteLineEdit.text(),
                      f"{fechaLiquidacion[0]}/{fechaLiquidacion[1]}/{fechaLiquidacion[2]}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = EditarVentaClienteInterface()
    ui.show()
    sys.exit(app.exec_())