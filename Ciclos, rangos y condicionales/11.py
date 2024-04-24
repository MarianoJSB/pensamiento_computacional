cobro = int(input("Ingrese lo que hay que cobrar: "))

def pagos(c):
    while c > 0:
        monto = int(input(f"falta para pagar {c}. Va a pagar: "))
        c -= monto
    return "todo pago"
print(pagos(cobro))