francia = ("Francia", "París", "Europa")
argentina = ("Argentina", "Buenos Aires", "América del Sur")
japon = ("Japón", "Tokio", "Asia")
alemania = ("Alemania", "Berlín", "Europa")
peru = ("Perú", "Lima", "América del Sur")

paises = [francia , argentina , japon , alemania , peru]

def informacion(lista):
    for i in lista:
        print(f"Pais: {i[0]}")
        print(f"Capital: {i[1]}")
        print(f"Continente: {i[2]}\n")
informacion(paises)