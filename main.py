from Menu import Menu
from usuario import Usuario
from empresa import Empresa
from rol import Rol
import os

class Main():
    
    def __init__(self):
        pass
    
    def menu_main(self):
            opcion = self.menu(["1) ID", "2) Descripción", "3) Sueldo", "4) Salir"],"*"*20+" MENU ROLES "+"*"*21)
            os.system("cls")
            
            if opcion == "1":
                
                print("Hola")
                input("\nCONTINUAR..."), os.system("cls"),self.menu_main()
                
            elif opcion == "2":
                print(self.show())
                input("Ingrese la descripcion")
                input("\nCONTINUAR..."), os.system("cls"),self.menu_main()
                
            elif opcion == "3":
                input("Ingrese el sueldo")
                input("\nCONTINUAR..."), os.system("cls"),self.menu_main()

                
            elif opcion == "4":
                exit("FINAL DEL PROGRAMA")
            else:
                os.system("cls"),self.menu_main()
    
    def show(self):
        
                
opc = Main()
opc.menu_main()
