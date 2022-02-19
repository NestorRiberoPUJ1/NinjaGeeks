from cgi import print_directory
import Funciones


operacion=input("Ingrese operacion ")
index=0
for x in operacion:
    if(x=="+"):
        print("ES SUMA")
        N1=int(operacion[:index])
        N2=int(operacion[index+1:])
        print(Funciones.Suma(N1,N2))
    index=index+1

#################################

