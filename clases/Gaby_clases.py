from termcolor import colored, cprint


class auto:
    
    garajeAutos=[]

    def __init__(self, marca, año, color, automatico, ventanas, sillas, airbags, puertas):
        self.marca = marca
        self.año = año
        self.color = color
        self.automatico = automatico
        self.ventanas = ventanas
        self.sillas = sillas
        self.airbags = airbags
        self.puertas = puertas
        auto.garajeAutos.append(self)

    def mostrarauto(self, color):
        color=color.lower()
        colores=["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        if (color not in colores):
            color ="grey"
        cprint(f"MARCA:{self.marca}",color)
        cprint(f"AÑO:{self.año}",color)
        cprint(f"COLOR:{self.color}",color)
        cprint(f"AUTOMATICO:{self.automatico}",color)
        cprint(f"VENTANAS:{self.ventanas}",color)
        cprint(f"SILLAS:{self.sillas}",color)
        cprint(f"AIRBAGS:{self.airbags}",color)
        cprint(f"PUERTAS:{self.puertas}",color)
    
    @classmethod
    def mostrargaraje(cls,color):
        
        for carro in cls.garajeAutos:

            carro.mostrarauto(color)
            print("---------------------------")


GabyMovil = auto("mercedes", 2019, "negro", True, 4, 6, 5, 6)
cprint(GabyMovil, "red")
GabyMovil.mostrarauto("magenta")

GabyMovil2 = auto("audi", 2018, "blanco", True, 6, 7, 8, 6)
cprint(GabyMovil2, "blue")
GabyMovil2.mostrarauto("cyan")

print(auto.garajeAutos)
print("---------------------------")
auto.mostrargaraje("blue")
xMovil= auto("toyota",2017,"rojo", True, 4, 6, 5, 6)
auto.mostrargaraje("yellow")
