from termcolor import colored, cprint

class auto:
    def __init__(self, marca, modelo, año, color, automatico, ventanas, pais, puertas, sillas):
        self.marca= marca
        self.modelo= modelo
        self.año= año
        self.color= color
        self.automatico= automatico
        self.ventanas= ventanas
        self.pais= pais
        self.puertas= puertas
        self.sillas= sillas

    def mostrarAuto(self,color):
        color=color.lower()
        colores=["red","magenta","cyan","green"]
        if( color not in colores):
            color="gray"
        cprint(f"MARCA: {self.marca}",color)
        cprint(f"MODELO: {self.modelo}",color)
        cprint(f"AÑO: {self.año}",color)
        cprint(f"COLOR: {self.color}",color)
        cprint(f"AUTOMATICO: {self.automatico}",color)
        cprint(f"VENTANAS: {self.ventanas}",color)
        cprint(f"PAIS: {self.pais}",color)
        cprint(f"PUERTAS: {self.puertas}",color)
        cprint(f"SILLAS: {self.sillas}",color)


PaulaMovil = auto("BMW","gran copupé","2021","gris",True,5,"Alemania",4,5)
cprint(PaulaMovil, "red")

PaulaMovil.mostrarAuto("magenta")

LauraMovil = auto("ferrari","enzo","2016","negro",True,4,"Italia",2,4)
cprint(LauraMovil, "cyan")

LauraMovil.mostrarAuto("red")
