from termcolor import cprint
# CLASE
class auto:

    garajeAutos=[]

    def __init__(self, marca, modelo, año, color, automatico):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.automatico = automatico

        auto.garajeAutos.append(self)


    def mostrarAuto(self,color):
        color=color.lower()
        colores=["red","blue","green","magenta","grey","cyan"]
        if( color not in colores):
            color="grey"
        cprint(f"MARCA: {self.marca}",color)
        cprint(f"MODELO: {self.modelo}",color)
        cprint(f"AÑO: {self.año}",color)
        cprint(f"COLOR: {self.color}",color)
        cprint(f"AUTOMATICO: {self.automatico}",color)

    @classmethod
    def mostrarGaraje(cls,color):
        
        for carro in cls.garajeAutos:

            carro.mostrarAuto(color)
            print("---------------------------")

NestorMovil = auto("Audi","Q3",2018,"Negro",True)  # INSTACIA
cprint(NestorMovil,"green")
NestorMovil.mostrarAuto("red")
BernieMovil= auto("Ford","Escape",2017,"Blanco",True)
cprint(BernieMovil,"magenta")
BernieMovil.mostrarAuto("blue")

print(auto.garajeAutos)
print("---------------------------")
auto.mostrarGaraje("cyan")
PerroMovil= auto("Honda","NSX",2022,"Naranja",True)
auto.mostrarGaraje("green")