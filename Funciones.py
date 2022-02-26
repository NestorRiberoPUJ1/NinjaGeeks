#suma   params: sumando1->num  sumando2->num
def Suma(sumando1:int,sumando2:int):
    resultado=sumando1+sumando2
    return resultado 

#resta  params: minuendo->num  sustraendo->num
def Resta(minuendo:int,sustraendo:int):
    resultado=minuendo-sustraendo
    return resultado

#multiplicacion params: factor1->num  factor2->num
def Multiplicacion(factor1:int,factor2:int):
    resultado=factor1*factor2
    return resultado

#division   params: dividendo->num  divisor->num
def Division(dividendo:int,divisor:int):
    resultado= dividendo/divisor
    return resultado 


#sumatoria  params: lista-> list[num]
def Sumatoria (lista:list):
    resultado=0
    for index in lista:
        resultado= resultado+index 
    return int(resultado)

#promedio 
def Promedio (lista:list):
    promedio=0
    longitud=len(lista)
    promedio=Sumatoria(lista)/longitud
    return promedio     
    