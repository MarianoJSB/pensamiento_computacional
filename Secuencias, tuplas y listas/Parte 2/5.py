lista = []

cant = int(input("¿Cuantas cartas vas a agregar? "))

for i in range(cant):
    carta = int(input("Ingrese el valor de la carta: "))
    lista.append(carta)
lista.sort()
print(f"Lista de cartas ordenada de menor a mayor: {lista}")