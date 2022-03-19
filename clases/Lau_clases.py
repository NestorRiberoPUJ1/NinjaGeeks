from termcolor import colored, cprint
##clase
class auto:

    def __init__(self,marca,modelo,año,color,sunrorf):
        self.marca= marca
        self.modelo= modelo
        self.año= año
        self.color= color
        self.sunrorf= sunrorf


    def mostrarAuto(self):
        print(f"marca:  {self.marca}")
        print(f"self.modelo")
        print(f"self.año")
        print(f"self.color")
        print(f"self.sunrorf")

        @classmethod
        def mostrarGarje (cls)
            for carro in cls.garajeAutos:
                

LauMovil= auto("audi","a4",2021,"negro","true")
cprint (LauMovil, "blue")
LauMovil.mostrarAuto()
PauMovil= auto("jeep","Wagoneer",2021,"blanco","flase")
cprint (LauMovil, "red")
PauMovil.mostrarAuto()