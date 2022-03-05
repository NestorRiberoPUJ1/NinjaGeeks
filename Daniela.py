from re import X
from statistics import _NumberT
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
flag= False
Num1=""
Num2=""
for x in operacion:
    if(x=="+"):
        operador = "SUMA"
        flag=True
    elif(x=="-"):
        operador = "RESTA"
        flag=True
    elif(x=="*"):
        operador = "MULTIPLICACION"
        flag=True
    elif (x=="/"):
        operador = "DIVISION"
        flag=True
    else:
        if(flag == False):
           Num1 = Num1 + X
        elif (flag == True):
           Num2 = Num2 + X
print (Num1,"on_red")
Num1= float (Num1)
print (operador)
print (Num2,"on_green")
Num2= float (Num2)

if (operador == "+"):
    print ("="+ str (Num1 +Num2, "on_grey"))
elif (operador == "-"):
    print ("=" + str  (Num1-Num2, "on_blue"))
elif (operador == "*"):
    print ("=" + str  (Num1*Num2, "on_cyan"))
elif (operador == "/"):
    print ("=" + str  (Num1/Num2, "on_ white"))