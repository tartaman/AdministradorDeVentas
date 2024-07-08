from RawInterfaces.VerClientes import Ui_ClienteViewWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from conection import Conector
from Objetos.ClienteConVenta import ClienteConVenta
from EditarVentaCliente import EditarVentaClienteInterface
import re
class VerClientesInterface(Ui_ClienteViewWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_ClienteViewWindow.setupUi(self, self)
        self.Conector = Conector()
        self.ClientesConVentas:list[ClienteConVenta] = []
        self.LlenarTablaDeClientes()
        self.BusquedaLine.textChanged.connect(self.find)
        self.BuscarButton.clicked.connect(self.find)
        self.TablaClientesConVentas.itemClicked.connect(self.Edit)
    def LlenarTablaDeClientes(self):
        self.Conector.cursor.execute("SELECT id_cliente, nombre, v.id_venta, v.modeloLentes, v.tipoDeMica, v.costo, v.fechaVisita, v.fechaLiquidacion FROM cliente c INNER JOIN venta v ON c.id_cliente = v.IdCliente;")
        results = self.Conector.cursor.fetchall()
        for result in results:
            clienteconventa = ClienteConVenta(result)
            clienteconventa.read()
            self.ClientesConVentas.append(clienteconventa)
        row = 0
        self.TablaClientesConVentas.setRowCount(len(self.ClientesConVentas))
        for cliente in self.ClientesConVentas:
            self.TablaClientesConVentas.setItem(row, 0, QtWidgets.QTableWidgetItem(str(cliente.idCliente)))
            self.TablaClientesConVentas.setItem(row, 1, QtWidgets.QTableWidgetItem(str(cliente.Nombre)))
            self.TablaClientesConVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(cliente.idVenta)))
            self.TablaClientesConVentas.setItem(row, 3, QtWidgets.QTableWidgetItem(str(cliente.ProductoVendido)))
            self.TablaClientesConVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(cliente.costo)))
            self.TablaClientesConVentas.setItem(row, 5, QtWidgets.QTableWidgetItem(str(cliente.fechaVisita)))
            self.TablaClientesConVentas.setItem(row, 6, QtWidgets.QTableWidgetItem(str(cliente.fechaLiquidacion)))
            row = row + 1

    def find(self):
        matches = self.TablaClientesConVentas.findItems(self.BusquedaLine.text(),Qt.MatchFlag.MatchContains)
        for match in matches:
            self.TablaClientesConVentas.selectRow(match.row())
    def Edit(self):
        self.selectedClientId = int(self.TablaClientesConVentas.item(self.TablaClientesConVentas.currentRow(),0).text())
        self.selectedSaleId = int(self.TablaClientesConVentas.item(self.TablaClientesConVentas.currentRow(),2).text())
        self.openEditWindow(self.selectedClientId,self.selectedSaleId)

    def openEditWindow(self, ClientId, SaleId):
        self.window = EditarVentaClienteInterface(ClientId,SaleId)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = VerClientesInterface()
    ui.show()
    sys.exit(app.exec_())