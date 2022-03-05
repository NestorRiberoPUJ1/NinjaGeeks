from termcolor import colored, cprint

paula= {
    "nombre": "Paula",
    "apellido": "Garcia",
    "estatura": 1.60,
    "edad": 13,
    "cumpleaños": "abril 18",
    "color": "no definido",
    "materia": "ingles",
    "cancion favorita": "solas",
}

cprint(paula,"cyan")

paula.update({"color": "negro"})

cprint(paula,"magenta")

paula.update({"cancion favorita": "ninguna"})

cprint(paula,"red")

paula.update({"estatura": 1.61, "comida": "pasta"})

cprint(paula,"green")

for x in paula:
    cprint(f"{x} : {paula[x]}","yellow")

hola= "tUmBa lA cAsA mAmI"

cprint(f"original : {hola}","white")
cprint(f"MAYUSCULAS : {hola.upper()}","cyan")
cprint(f"minusculas : {hola.lower()}","magenta")
cprint(f"Normal : {hola.title()}","red")
