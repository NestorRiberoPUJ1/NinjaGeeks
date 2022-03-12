from enum import Flag
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


operacion=input("ingrese operacion\t")

flag= False
num1=""
num2=""
operador= ""
for x in operacion:
    if (x=="+"):
        operador="+"
        flag=True
    elif (x=="-"):
        operador="-"
        flag=True
    elif (x=="*"):
        operador="*"
        flag=True
    elif (x== "/"):
        operador="/"
        flag=True
    else:
        if (flag == False):
            num1 = num1 + x
        elif (flag == True):
            num2 = num2 + x

import sys
from termcolor import colored, cprint



cprint (num1,"red")
num1= float (num1)
cprint (operador,"white")
cprint (num2,"red")
num2= float (num2)

if (operador == "+"):
    cprint("="+ str(num1+num2),"white")
elif(operador == "-"):
    cprint("="+str(num1-num2),"white","on_blue")
elif(operador == "*"):
    cprint("="+str(num1*num2),"white","on_yellow")
elif(operador == "/"):
    cprint("/"+str(num1/num2),"white","on_red")
    



    
        
