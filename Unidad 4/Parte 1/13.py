lista = [
        [("Detergente", 123), ("Jabón Líquido", 456)],[("Cloro", 103), ("Coca cola", 222)]
        ]

def supermercado(lista):
    total = 0
    for i in lista:
        total += i[0][1] + i[1][1]
    return f"El total de la compra es {total}"
print(supermercado(lista))