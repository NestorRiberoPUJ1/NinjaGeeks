import Funciones

def producto(a,b):
    res=0
    for x in range (abs(b)):
        if (b>0):
            res = Funciones.Suma(res,a)
        if (b<0):
            res = Funciones.Resta (res,a)
    return res

#####################################

import Funciones

operacion=input("Ingrese operacion")
index=0
for x in operacion :
    if(x=="+"):
        print("Es suma")
        N1=int(operacion[:index])
        N2=int(operacion[index+1:])
        print(Funciones.Suma(N1,N2))
    index=index+1
    
        
