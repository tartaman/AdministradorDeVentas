class Cliente:
    #Encajar en la sociedad
    def __init__(self, id, Nombre, Edad, Telefono, SaldoPendiente):
        self.id = id
        self.Nombre = Nombre
        self.Edad = Edad
        self.Telefono = Telefono
        self.SaldoPendiente = SaldoPendiente
    #ser feliz
    def __init__(self, params:list):
        self.id = params[0]
        self.Nombre = params[1]
        self.Edad = params[2]
        self.Telefono = params[3]
        self.SaldoPendiente = params[4]