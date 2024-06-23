try:
    user = int(input("Ingresa un numero entero: "))
    print(user)
except ValueError:
    print("El valor no es un numero entero")