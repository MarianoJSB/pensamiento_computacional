def promedioNotas(dic,intento):
    suma = 0
    promedio = 0
    cant = 0

    for i in dic:
        if i["intento"] == intento:
            cant += 1
            suma += i["nota"]
            promedio = suma / cant
    return promedio

diccionario = [
    {
        "nombre": 'mariano',
        "apellido": 'aguiar',
        "intento": 1,
        "nota": 9
    },
    {
        "nombre": 'alex',
        "apellido": 'rodriguez',
        "intento": 1,
        "nota": 3
    },
    {
        "nombre": 'jose',
        "apellido": 'lopez',
        "intento": 3,
        "nota": 5
    }
]

print(promedioNotas(diccionario,3))