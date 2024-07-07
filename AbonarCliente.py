from RawInterfaces.Abonar import Ui_AbonarWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import conection
from tkinter import messagebox
from Objetos.Cliente import Cliente
class AbonarWindow(Ui_AbonarWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_AbonarWindow.setupUi(self, self)
        self.Conector = conection.Conector()
        self.ClienteComboBox.currentIndexChanged.connect(self.changeIndexCombo)
        self.ListaClientes = []
        self.LlenarComboClientee()
        self.AgregarAbonoButton.clicked.connect(self.abonar)
        self.MontoAbonoLine.textChanged.connect(self.validarAbono)
    def LlenarComboClientee(self):
        self.ClienteComboBox.clear()
        self.Conector.conection.reconnect()
        self.Conector.cursor.execute("SELECT * FROM cliente")
        resultados = self.Conector.cursor.fetchall()
        #crear un objeto cliente por cada uno de los clientes
        for cliente in resultados:
            clienteCreado = Cliente(cliente)
            #print(clienteCreado.id, clienteCreado.Nombre,clienteCreado.Edad,
            #      clienteCreado.Telefono, clienteCreado.SaldoPendiente)
            self.ListaClientes.append(clienteCreado)
        for cliente in self.ListaClientes:
            self.ClienteComboBox.addItem(cliente.Nombre)
    def changeIndexCombo(self):
        for cliente in self.ListaClientes:
            if cliente.Nombre == str(self.ClienteComboBox.currentText()):
                self.currentId = cliente.id
                print(self.currentId)
                self.currentSaldoPendiente = cliente.SaldoPendiente
                self.LabelDebe.setText(f"Este cliente debe: {cliente.SaldoPendiente}")
    def abonar(self):
        self.cantidaddeabono = float(self.MontoAbonoLine.text())
        self.Conector.cursor.execute("SELECT saldoPendiente FROM cliente WHERE id_cliente = %s",
                                     [self.currentId])
        result = self.Conector.cursor.fetchone()
        self.Conector.cursor.execute("CALL actualizarSaldoPendiente(%s,%s,%s)",
                                     [-self.cantidaddeabono, self.currentId, result[0]])
        self.Conector.conection.commit()
        messagebox.showinfo("Éxito", "Se ha abonado con éxito")
    def validarAbono(self):
        try:
            if (self.MontoAbonoLine.text() != ""):
                abonoline = float(self.MontoAbonoLine.text())
            if abonoline > self.currentSaldoPendiente:
                messagebox.showerror("Cantidad innecesaria", "La cantidad de abono es mayor a lo que debe el cliente")
        except:
            pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = AbonarWindow()
    ui.show()
    sys.exit(app.exec_())