#suma   params: x->num  y->num
def Suma(sumando1:int,sumando2:int):
    resultado=sumando1+sumando2
    return resultado 

#resta      params: x->num  y->num
def Resta(minuendo:int,sustraendo:int):
    resultado=minuendo-sustraendo
    return resultado

#multiplicacion params: x->num  y->num
def Multiplicacion(factor1:int,factor2:int):
    resultado=factor1*factor2
    return resultado

#division   params: a->num  b->num
def division(dividendo:int,divisor:int):
    resultado= dividendo/divisor
    return resultado 


#sumatoria  params: lista-> list[num]
def sumatoria (lista:list):
    resultado=0
    for index in lista:
        resultado= resultado+index 
    return int(resultado)