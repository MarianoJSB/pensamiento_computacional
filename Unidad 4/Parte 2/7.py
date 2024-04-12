lista = [1,2,56,82,9,78,12,11,10,99,35]
def par(x):
    if x % 2 == 0:
        return True
    else:
        return False
filtro = list(filter(par,lista))
print(f"Lista de pares: {filtro}")