
def calculadora (operacion):
    contador=0
    operador=""
    num1=""
    num2=""
    flag=False
    for x in operacion:
        if (x=="+"):
            operador="suma"
            flag=True
        elif (x=="-"):
            operador="resta"
            flag=True
        elif (x=="*"):
            operador="multiplicacion"
            flag=True
        elif (x=="/"):
            operador="division"
            flag=True
        else: 
            if(flag==False):
                num1=num1+x
            if(flag==True):
                num2=num2+x
        contador=contador+1

    if (operador=="suma"):
        resultado=float(num1)+float(num2)
    elif (operador=="resta"):
        resultado=float(num1)-float(num2)
    elif (operador=="multiplicacion"):
        resultado=float(num1)*float(num2)
    elif (operador=="division"):
        resultado=float(num1)/float(num2)

    print ("[INFO]\t"+str(operador))
    print ("[NUM1]\t"+str(num1))
    print ("[NUM2]\t"+str(num2))
    print ("[RESULTADO]\t"+str(resultado))

while (True):

    operacion=input("ingrese su operacion\t")
    try:
        calculadora (operacion)
    except:
        print ("syntax error >:(")

