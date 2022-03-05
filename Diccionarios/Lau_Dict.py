from termcolor import cprint


laura= {
    "nombre": "laura",
    "apellido": "garcia",
    "edad": 15,
    "estatura": 1.65,
    "pasatiempo":"bailar",
    "cumpleaños ": "11-mayo",
    "color favorito": "azul",
    "materia favorita" : "español y matematicas",
    "cancion favorita" : "no tengo",
    "usuario de ig" : "pr33ty.lau",
        
}
cprint(laura, "blue")

laura.update({"materia favorita": "matematicas"})

cprint(laura, "red")

laura.update({"cancion favorita": "lloraras"})

for x in laura:
    cprint(f"{x} : {laura[x]}")
    


hi= "QuieRE Que LE BaIlE"

cprint(f"original : {hi}","white")
cprint(f"MAYUSCULAS : {hi.upper()}","green")
cprint(f"minusculas : {hi.lower()}","magenta")
cprint(f"Normal : {hi.title()}","blue")
