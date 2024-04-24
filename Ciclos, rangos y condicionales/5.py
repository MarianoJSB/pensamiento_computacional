jugada = input("¡Juguemos! Ingresá piedra (R), papel (P) o tijera (T): ")
def juego(opcion):
    if opcion == "r":
        return "Papel, gana bot"
    elif opcion == "p":
        return "Tijera, gana bot"
    elif opcion == "t":
        return "piedra, gana bot"
    elif opcion != "t" or opcion != "r" or opcion != "p":
        return "no vale"
print(juego(jugada))