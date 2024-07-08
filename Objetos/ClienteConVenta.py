class ClienteConVenta:
    def __init__(self, params: list):
        self.idCliente = params[0]
        self.Nombre = params[1]
        self.idVenta = params[2]
        self.ProductoVendido = params[3] + " " + params[4]
        self.costo = params[5]
        self.fechaVisita = params[6]
        self.fechaLiquidacion = params[7]
    def read(self):
        print(self.idCliente, self.Nombre,self.idVenta,self.ProductoVendido,self.costo, self.fechaVisita, self.fechaLiquidacion)