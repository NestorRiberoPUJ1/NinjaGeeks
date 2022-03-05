from termcolor import cprint

cata = {"nombre": "catalina",
        "apellido": "guevara",
        "estatura": 1.58,
        "color favorito": "agua marina",
        "edad": 14,
        "materia favorita": "danzas",
        "profesor mas rata": "maop", }
cata.update({"profesor favorito": "ninguno"})


cprint(cata["nombre"], "magenta")
cprint(cata["edad"], "blue")
cprint(cata["profesor mas rata"], "red")
cprint(cata["profesor favorito"], "blue")

for x in cata:
    print(f"{x}:{cata[x]}")

hola = "HoLa a ToDos LlEgUe Yo La DiVaZa"
cprint(hola.upper(), "blue")
cprint(hola.lower(), "magenta")
cprint(hola.title(), "cyan")

for x in cata:
    cprint(f"{x}:{str(cata[x]).upper()}", "blue")
for x in cata:
    cprint(f"{x}:{str(cata[x]).lower()}", "cyan")
for x in cata:
    cprint(f"{x}:{str(cata[x]).title()}", "green")


malala = {"nombre": "alejandra",
          "apellido": "avila",
          "estatura": 1.61,
          "color favorito": "nose",
          "edad": 14,
          "materia favorita": "danzas",
          "profesor mas rata": "maop", }

contactos = []
contactos.append(cata)
contactos.append(malala)
print(contactos)
cprint(contactos[0], "green")
cprint(contactos[0]["nombre"], "red")

diccionario = {"cata": cata}
diccionario.update({"malala": malala})
print(diccionario)
cprint(diccionario["cata"], "green")
cprint(diccionario["malala"]["nombre"], "red")
