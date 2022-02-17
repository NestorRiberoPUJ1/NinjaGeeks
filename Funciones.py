#resta      params: x->num  y->num
def Resta(x,y):
    resultado=x-y
    return resultado

#multiplicacion params: x->num  y->num
def Multiplicacion(x,y):
    resultado=x*y
    return resultado

#division   params: a->num  b->num
def division(a,b):
    resultado= a/b
    return resultado 

#suma   params: x->num  y->num
def Suma(x,y):
    resultado=x+y
    return resultado

#sumatoria  params: lista-> list[num]
def sumatoria (lista):
    resultado=0
    for index in lista:
        resultado= resultado+index 
    return resultado