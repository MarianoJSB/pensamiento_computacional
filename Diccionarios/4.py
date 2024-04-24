def peliculas(dic,nueva):
    for i in dic:
        if i["puntaje"] > 7:
            nueva.append(i)
    return nueva

diccionario = [
    {
        "nombre": 'toy story',
        "anio": 1995,
        "puntaje": 6
    },
    {
        "nombre": 'batman',
        "anio": 2005,
        "puntaje": 1
    },
    {
        "nombre": 'joker',
        "anio": 2019,
        "puntaje": 8
    }
]

nueva = []

print(peliculas(diccionario,nueva))