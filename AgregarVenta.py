from PyQt5 import QtCore, QtGui, QtWidgets
import conection
from RawInterfaces.agregarVenta import Ui_MainWindow
from Objetos.Cliente import Cliente
class ventaInterface(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_MainWindow.setupUi(self, self)
        self.Conector = conection.Conector()
        #Lista de los clientes llena de objetos cliente
        self.ListaClientes: list[Cliente] =[]
        self.LlenarComboCliente()
        #Cada vez que se cambie el cliente en la combobox se actualiza su id para subirlo a
        #la base de datos
        self.currentId = -1
        self.ClienteCombo.currentIndexChanged.connect(self.changeIndexCombo)

    def LlenarComboCliente(self):
        self.Conector.cursor.execute("SELECT * FROM cliente")
        resultados = self.Conector.cursor.fetchall()
        #crear un objeto cliente por cada uno de los clientes
        for cliente in resultados:
            clienteCreado = Cliente(cliente)
            #print(clienteCreado.id, clienteCreado.Nombre,clienteCreado.Edad,
            #      clienteCreado.Telefono, clienteCreado.SaldoPendiente)
            self.ListaClientes.append(clienteCreado)
        for cliente in self.ListaClientes:
            self.ClienteCombo.addItem(cliente.Nombre)
    def changeIndexCombo(self):
        for cliente in self.ListaClientes:
            if cliente.Nombre == str(self.ClienteCombo.currentText()):
                self.currentId = cliente.id
                print(self.currentId)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ventaInterface()
    ui.show()
    sys.exit(app.exec_())