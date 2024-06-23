list = [1,2,3,56,7]
def ejercicio(lista, indice):
    return lista[indice]
try:
    index = int(input("Ingrese el indice del elemento: "))
    print(ejercicio(list,index))
except IndexError:
    print("El valor esta fuera del rango")