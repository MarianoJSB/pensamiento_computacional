opcion = input("Ingrese una letra (V), (I), (P), (O): ")
def estacion(opcion):
    if opcion == "v":
        return "Verano"
    elif opcion == "i":
        return "Invierno"
    elif opcion == "p":
        return "primavera"
    elif opcion == "o":
        return "otoño"
    elif opcion != "v" or opcion != "i" or opcion != "p" or opcion != "o":
        return "error"
print(estacion(opcion))