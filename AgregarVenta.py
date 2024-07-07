from PyQt5 import QtCore, QtGui, QtWidgets
import conection
from RawInterfaces.agregarVenta import Ui_VentaWindow
from Objetos.Cliente import Cliente
from tkinter import messagebox
class ventaInterface(Ui_VentaWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_VentaWindow.setupUi(self, self)
        self.Conector = conection.Conector()
        #Lista de los clientes llena de objetos cliente
        self.ListaClientes: list[Cliente] =[]
        self.LlenarComboCliente()
        #Cada vez que se cambie el cliente en la combobox se actualiza su id para subirlo a
        #la base de datos
        self.currentId = -1
        self.CostoLine.setValidator(QtGui.QIntValidator(1, 9999, self))
        self.AbonoLine.setValidator(QtGui.QIntValidator(1, 9999, self))
        self.ClienteCombo.currentIndexChanged.connect(self.changeIndexCombo)
        self.AgregarVentaButton.clicked.connect(self.agregarVenta)
        self.LimpiarVentaButton.clicked.connect(self.Limpiar)
        self.RecargarClientesButton.clicked.connect(self.LlenarComboCliente)
        self.AbonoLine.textChanged.connect(self.calcularSaldo)

    def LlenarComboCliente(self):
        self.ClienteCombo.clear()
        self.Conector.conection.reconnect()
        self.Conector.cursor.execute("SELECT * FROM cliente")
        resultados = self.Conector.cursor.fetchall()
        #crear un objeto cliente por cada uno de los clientes
        for cliente in resultados:
            clienteCreado = Cliente(cliente)
            print(clienteCreado.id, clienteCreado.Nombre,clienteCreado.Edad,
                  clienteCreado.Telefono, clienteCreado.SaldoPendiente)
            self.ListaClientes.append(clienteCreado)
        for cliente in self.ListaClientes:
            self.ClienteCombo.addItem(cliente.Nombre)
    def changeIndexCombo(self):
        for cliente in self.ListaClientes:
            if cliente.Nombre == str(self.ClienteCombo.currentText()):
                self.currentId = cliente.id
                print(self.currentId)
    def agregarVenta(self):
        #devuelve arreglo de fechas con formato YYYY/MM/DD
        fecha = self.CalendarioHoy.selectedDate().getDate()
        #extraer los parametros de la venta para poder crear el objeto venta
        idCliente = self.currentId
        modeloLentes = self.ModeloLine.text()
        tipoMica = self.MicaLine.text()
        costo = float(self.CostoLine.text())
        abono = float(self.AbonoLine.text())
        saldo = float(self.SaldoLine.text())
        self.Conector.cursor.execute("CALL agregarVenta(%s,%s,%s,%s,%s,%s,%s)",
                                     [f"{fecha[0]}/{fecha[1]}/{fecha[2]}",
                                      idCliente,
                                      modeloLentes.title(),
                                      tipoMica.title(),
                                      costo,
                                      abono,
                                      saldo])
        messagebox.showinfo("Exito", "Se ha agregado la venta con exito")
        self.actualizarSaldoPendiente()
        self.Limpiar()
    def calcularSaldo(self):
        try:
            if self.CostoLine.text() != "" and self.AbonoLine.text() != "":
                costo = float(self.CostoLine.text())
                abono = float(self.AbonoLine.text())
            self.saldo = costo - abono
            self.SaldoLine.setText(f"{self.saldo}")
        except:
            print("hubo un error al calcular el saldo")
    def actualizarSaldoPendiente(self):
        self.Conector.cursor.execute("SELECT saldoPendiente FROM cliente WHERE id_cliente = %s",
                                     [self.currentId])
        result = self.Conector.cursor.fetchone()
        self.Conector.cursor.execute("CALL actualizarSaldoPendiente(%s,%s,%s)",
                                     [self.saldo, self.currentId, result[0]])
        self.Conector.conection.commit()
        messagebox.showinfo("Exito", "Se ha subido la venta con éxito")
    def Limpiar(self):
        self.AbonoLine.setText("")
        self.CostoLine.setText("")
        self.MicaLine.setText("")
        self.SaldoLine.setText("")
        self.ModeloLine.setText("")
        self.ClienteCombo.setCurrentText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ventaInterface()
    ui.show()
    sys.exit(app.exec_())