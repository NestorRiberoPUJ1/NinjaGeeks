from termcolor import colored, cprint

Gaby= {
    "nombre": "Gabriela",
    "apellido": "Morales",
    "segundo apellido": "lemus",
    "edad": 13,
    "estatura": 1.63,
    "color favorito": "beige y negro",
    "materia favorita": "quimica",
    "peor materia": "sociales",
    "cumpleaños": 12-8,
    "color menos favorito": "azul oscuro o neon",
    "comida favorita": "pasta carbonara",
    "fruta favorita":"maracuya",
    "numero favorito":8
}

cprint (Gaby,"cyan")

cprint ("x", "white", "on_white")

Gaby.update({"edad": 13.7, "comida favorita": "pasta carbonara con pan"})
cprint (Gaby, "magenta")
cprint ("x", "white", "on_white")

Gaby.update({"color menos favorito": "azul y verde oscuro o neon", "materia favorita":"math y quimica" })
cprint (Gaby, "red")
cprint ("x", "white", "on_white")

for x in Gaby:
    cprint (f"{x} : {Gaby[x]})", "cyan", attrs=["bold"])
cprint ("x", "white", "on_white")
cprint ("x", "white", "on_white")

texto= "nO sE EscrIbRir NorMal"
cprint (f"originial  : {texto}", "red")
cprint (f"mayusculas: {texto.upper()}","yellow")
cprint (f"minusculas: {texto.lower()}","magenta")
cprint (f"titulo: {texto.title()}","blue")
