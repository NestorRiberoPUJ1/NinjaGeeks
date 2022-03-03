import Funciones
from termcolor import cprint


cprint('Hello, World!', 'blue')
cprint('Hello, World!', 'blue',attrs=["bold","underline"])
cprint('Hello, World!', 'blue')


#operacion=input("Ingrese operacion ")

def nombreFuncion(operacion):
    index=0
    for x in operacion:
        if(x=="+"):
            print("ES SUMA")
            N1=int(operacion[:index])
            N2=int(operacion[index+1:])
            print(Funciones.Suma(N1,N2))
        index=index+1

#################################
