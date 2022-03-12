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

PaulaMovil = auto("BMW","gran copupé","2021","gris",True,5,"Alemania",4,5)
cprint(PaulaMovil, "red")

LauraMovil = auto("ferrari","enzo","2016","negro",True,4,"Italia",2,4)
cprint(LauraMovil, "cyan")

