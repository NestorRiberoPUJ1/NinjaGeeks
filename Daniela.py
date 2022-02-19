import Funciones

def producto(a,b):
    res=0 
    for x in range (abs(b)):
        if (b>0):
            res+= Funciones.Suma(res,a)
        if (b<0):
            res+= Funciones.Resta (res,a)
    return res 
print (producto(5,4))

#############################################

operacion=input("Ingresa operacion ")

for x in operacion:
    if(x=="+"):
        print("ES SUMA")
    if(x=="-"):
        print("ES RESTA")
    if(x=="*"):
        print("ES MULTIPLICACION")
    if (x=="/"):
        print("ES DIVISION")
