from termcolor import cprint

Dany = {"Nombre": "Daniela",
        "Apellido": "Espitia",
        "Edad": 14,
        "Estatura": 1.53,
        "Color favorito": "Verde y cafe",
        "materia favorita": "Matematcas",
        "Lugar favorita": "Mi casa",
        "Nacionalidad": "Colombia,Bogota",
        "Dia de nacimiento": "04 de mayo del 2007",
        "numero de la suerte": 16,
        }

cpirnt(Dany, "red") 

Dany. update({"Edad":15})

cpirnt(Dany, "yellow") 

Dany. update({"Aapellido": "Gonzalez"})

cpirnt(Dany, "cyan") 

Dany. update({"Lugar favorito":"cocina", "Celular": "huawei"})

cprint(Dany, "green")

for x in Dany:
    print(f"{x} : {Dany[x]}") 


texto= "no sE EsCrIbIr NoRmAl"

cprint(f"Orginal : {texto}","grey")
cprint(f"Mayusculas: {texto.upper()}","blue")
cprint(f"Minusculas: {texto.lower()}","red")
cprint(f"Titulo: {texto.title()}","magenta")

