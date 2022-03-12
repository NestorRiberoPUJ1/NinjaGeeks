from termcolor import colored, cprint


class auto:

    def __init__(self, marca, año, color, automatico, ventanas, sillas, airbags, puertas):
        self.marca = marca
        self.año = año
        self.color = color
        self.automatico = automatico
        self.ventanas = ventanas
        self.sillas = sillas
        self.airbags = airbags
        self.puertas = puertas


GabyMovil = auto("mercedes", 2019, "negro", True, 4, 6, 5, 6)
cprint(GabyMovil, "magenta")

GabyMovil2 = auto("audi", 2018, "blanco", True, 6, 7, 8, 6)
cprint(GabyMovil2, "blue")
