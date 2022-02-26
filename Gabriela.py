import numbers
from pickle import FALSE
from xmlrpc.client import FastParser
import Funciones

def producto(a,b):
    res=0
    for x in range (abs(b)):
        if (b>0):
            res = Funciones.Suma(res,a)
        if (b<0):
            res = Funciones.Resta (res,a)
    return res


###################

operacion=input("ingrese operacion\t")

flag= False
num1=""
num2=""
operador= ""
for x in operacion:
    if (x=="+"):
        operador= "+"
        flag=True
    elif (x=="-"):
        operador ="-"
        flag=True
    elif (x=="*"):
        operador ="*"
        flag=True
    elif (x== "/"):
        operador = "/"
        flag=True
    else :
        if (flag == False):
            num1  = num1 + x  
        elif (flag == True):
            num2 = num2 + x
print (num1)
num1= float (num1)
print (operador)
print (num2)
num2= float (num2)

if (operador == "+"):
    print ("="+ str (num1 +num2))
elif (operador == "-"):
    print ("=" + str  (num1-num2))
elif (operador == "*"):
    print ("=" + str  (num1*num2))
elif (operador == "/"):
    print ("=" + str  (num1/num2))



