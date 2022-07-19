class Usuario:
    def __init__(self,ced,nom,telf,dir,correo):
        self.cedula = ced
        self.nombre = nom
        self.telf = telf
        self.dir = dir
        self.correo = correo
        
    def ValidaCedula(self):
        if len(self.cedula) == 10:
            return self.cedula
        else:
            return "9999999999"
       
    def mostrarCliente(self):
        print("Cliente: {} - {} - {}".format(self.cedula,self.nombre,self.correo))
        