def programa():
    try:
        n1 = int(input("Ingresa un numero entero: "))
        n2 = int(input("Ingresa otro numero entero: "))
        print(n1*n2)
    except ValueError:
        print("Uno o ambos valores no son numeros enteros")
programa()