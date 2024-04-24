def supermercado(tickets,informacion):
    ticket = {
        'nombre': informacion[0],
        'precio por unidad': informacion[1],
        'cantidad': informacion[2]
    }
    total = ticket['precio por unidad'] * ticket['cantidad']
    tickets.append(ticket)
    return f'El total a pagar es: {total}'

nombre = input("Ingrese el nombre del producto: ")
precio = int(input("Ingrese el precio x unidad: "))
cantidad = int(input("Ingrese la cantidad: "))

informacion = [nombre,precio,cantidad]

tickets = []
print(supermercado(tickets, informacion))