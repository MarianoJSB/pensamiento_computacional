total = 0

opciones={ 
        1:"hamburguesas",
        2:"milanesas",
        3:"gaseosa",
        4:"alfajor",
        5:"papasfritas",
        6:"agua" 
}

valores={
    1:1000,
    2:1500,
    3:500,
    4:300,
    5:600,
    6:350
}

for i in opciones:
    opcion = opciones[i]
    precio = valores.get(i)
    print(f"{i}: {opcion} -> {precio}")
try:
    eleccion = int(input("Ingrese la opcion: "))
    if eleccion < 1 or eleccion > 6:
        raise Exception("Valor no disponible")
    seleccionado = valores.get(eleccion)
    cantidad = int(input("Ingrese la cantidad a comprar: "))
    total = seleccionado * cantidad
    print(total)
except ValueError:
    print("Valor no valido")