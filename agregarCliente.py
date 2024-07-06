from PyQt5 import QtCore, QtGui, QtWidgets
import conection
from RawInterfaces.AgregarCliente import Ui_ClienteWindow
from tkinter import messagebox
class ClienteInterface(Ui_ClienteWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        Ui_ClienteWindow.setupUi(self, self)
        self.Conector = conection.Conector()

        #retringir la edad
        self.EdadLine.setValidator(QtGui.QIntValidator(1, 999, self))
        #Agregar la funcion a los botones
        self.AgregarClienteButton.clicked.connect(self.SubirCliente)
        self.LimpiarButton.clicked.connect(self.Limpiar)

    def SubirCliente(self):
        nombre = self.NombreLine.text()
        edad = self.EdadLine.text()
        telefono = self.TelefonoLine.text()
        self.Conector.cursor.execute("CALL agregarCliente(%s,%s,%s)",
                                     [nombre, int(edad), telefono])
        self.Conector.conection.commit()
        messagebox.showinfo("Exito", "Se ha añadido el registro con exito")
    def Limpiar(self):
        self.NombreLine.setText("")
        self.EdadLine.setText("")
        self.TelefonoLine.setText("")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ClienteInterface()
    ui.show()
    sys.exit(app.exec_())