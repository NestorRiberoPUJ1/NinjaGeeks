

class auto: 
    listaAutos= []
    def __init__(self,marca,modelo,año,automatico):
        self.marca=marca 
        self.modelo=modelo
        self.año= año
        self.automatico=automatico
        auto.listaAutos.append(self)

    def imprimirAuto(self):
        print (f"[marca]: {self.marca}")
        print (f"[modelo]: {self.modelo}")
        print (f"[año]: {self.año}")
        print (f"[automatico]: {self.automatico}")
        print ("_____________________________________")

    @classmethod
    def imprimirGaraje (cls):
        for x in cls.listaAutos:
            x.imprimirAuto

catamovil=auto ("audi", "a4",2022,True)
catamovil.imprimirAuto()

nestormovil=auto ("audi","q3",2018, True)
nestormovil.imprimirAuto() 

blazermovil=auto ("chevrolet","blazer rs",2020,True)
blazermovil.imprimirAuto()