n1 = int(input("ingrese un numero: "))
n2 = int(input("ingrese otro numero: "))
limite = int(input("ingrese un numero limite: "))

suma = n1 + n2

if suma < limite:
    print(f"para llegar a {limite} falta {abs(suma - limite)}")
elif suma > limite:
    print(f"llega a {limite}")
