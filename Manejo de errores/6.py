def jugadores(num):
    return num
try:
    numero = int(input("Ingrese el numero de jugadores"))
    if numero > 4:
        raise Exception("Se puede un maximo de 4 jugadores")
    elif numero < 2:
        raise Exception("Se puede un minimo de 2 jugadores")
    print(jugadores(numero))
except ValueError:
    print("Valor no valido")