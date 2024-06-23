try:
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    try:
        print(dividendo/divisor)
    except ZeroDivisionError:
        print("No se puede dividir por 0")
except ValueError:
    print("Valor no validos")