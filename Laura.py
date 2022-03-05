
from operator import truediv
from sys import flags


operacion=input("ingrese operacion\t")
for x in operacion:
    if(x=="-"):
        print("ES RESTA")
    if(x=="+"):
        print("ES SUMA")
    if(x=="/"):
        print("ES DIVISION")
    if (x=="*"):
        print("ES MULTIPLICACION")
      
########################################################
flag=False
num1=""
num2=""
operador=""
for x in operacion:
    if (x=="+"):
        operador="+"
        flag=True
    elif (x=="-"):
        print("-")
        flag=True
    elif (x=="*"):
        operador= "*"
        flag=True
    elif (x=="/"):
        operador= "/"
        flag=True
    else : 
        if (flag == False):
            num1 = num1 + x
        elif (flag == True):
            num2 = num2 + x
print (num1)
num1= float (num1)
print (operador)
print (num2)
num2= float (num2)

if (operador == "+"):
    print ("-" + str (num1 + num2))
elif (operador == "-"):
    print ("=" + str (num1 - num2))
elif (operador == "*"):
    print ("-" + str (num1 * num2))
elif (operador == "/"):
    print ("=" + str (num1 / num2))


