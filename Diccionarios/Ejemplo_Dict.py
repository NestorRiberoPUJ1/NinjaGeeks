from termcolor import cprint

nestor = {
    "nombre": "Nestor",
    "apellido": "Ribero",
    "estatura": 1.80,
    "color favorito": "naranja",
    "edad": 24,
    "materia favorita": "python"
}

cprint(nestor, "red")

nestor.update({"edad": 25})

cprint(nestor, "blue")

nestor.update({"color favorito": "orange", "carro": "A4"})

cprint(nestor, "green")

for x in nestor:
    print(f"{x} : {nestor[x]}") 


texto= "no sE EsCrIbIr NoRmAl"

cprint(f"Orginal : {texto}","grey")
cprint(f"Mayusculas: {texto.upper()}","blue")
cprint(f"Minusculas: {texto.lower()}","red")
cprint(f"Titulo: {texto.title()}","magenta")