class Venta:
    def __init__(self, id, fechaVisita, idCliente, modeloLentes, tipoDeMica, costo, abono, saldo, fechadeliquidacion):
        self.fechadeliquidacion = fechadeliquidacion
        self.saldo = saldo
        self.abono = abono
        self.costo = costo
        self.tipoDeMica = tipoDeMica
        self.modeloLentes = modeloLentes
        self.idCliente = idCliente
        self.fechaVisita = fechaVisita
        self.id = id

    def __init__(self, params: list):
        self.fechadeliquidacion = params[8]
        self.saldo = params[7]
        self.abono = params[6]
        self.costo = params[5]
        self.tipoDeMica = params[4]
        self.modeloLentes = params[3]
        self.idCliente = params[2]
        self.fechaVisita = params[1]
        self.id = params[0]