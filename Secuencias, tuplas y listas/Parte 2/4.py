lista = []

i = ''
while i != 'x':
    i = input("Ingrese un ingrediente - (X) para salir: ")
    if i == 'x':
        break
    if i not in lista:
        lista.append(i)
print(f"Ingredientes: {lista}")