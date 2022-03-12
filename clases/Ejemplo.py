from termcolor import cprint
# CLASE
class auto:

    def __init__(self, marca, modelo, año, color, automatico):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.automatico = automatico


NestorMovil = auto("Audi","Q3",2018,"Negro",True)  # INSTACIA
cprint(NestorMovil,"green")
BernieMovil= auto("Ford","Escape",2017,"Blanco",True)
cprint(BernieMovil,"red")