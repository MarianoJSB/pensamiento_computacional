def control_calidad(dic):
    tupla = []
    for i in dic:
        if not i["chequeo"]:
            tupla.append(i)
    nuevo_diccionario = [i for i in diccionario if i["chequeo"]]
    cantidad_lista = len(nuevo_diccionario)
    return tuple(tupla),f"Productos aprobados: {cantidad_lista}"

diccionario = [
    {
        "codigo": 00,
        "vencimiento": "12-05-2024",
        "chequeo": True
    },
    {
        "codigo": 1,
        "vencimiento": "12-05-2025",
        "chequeo": False
    },
    {
        "codigo": 5,
        "vencimiento": "12-04-2024",
        "chequeo": False
    }
]

print(control_calidad(diccionario))