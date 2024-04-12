precio = int(input("Ingrese el precio de la maquina: "))

def fichas(precio):
    while precio > 0:
        opcion = input(f"Ingrese {precio} fichas para comenzar: ")
        if opcion.lower() == "f":
            precio -= 1
        elif opcion.lower != "f":
            print("Por favor solamente ingrese fichas reales (f)")
    return "¡A jugar!"
print(fichas(precio))