class Rol:
    _codigo = 0
    def __init__(self,desp,sueldo):
        Rol._codigo += 1
        self.codigo = Rol._codigo
        self.descripcion = desp
        self.sueldo = sueldo
        
        
    def mostrarRol(self):
        print("Codigo: {} - Rol: {} - Sueldo: {}".format(self.codigo,self.descripcion,self.sueldo))
        
rol1 = Rol("Jefe",1000)
rol1.mostrarRol()
rol1 = Rol("Gerente",800.5)
rol1.mostrarRol()
rol1 = Rol("Cliente",800.5)
rol1.mostrarRol()