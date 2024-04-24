def guardar_plantas(plantas, informacion):
    planta = {
        'especie': informacion[0],
        'luz_solar': informacion[1],
        'precio': informacion[2]
    }
    
    plantas.append(planta)
    return plantas

# Informacion de la planta ingresada por el usuario
especie = input("Ingrese el nombre de la especie: ")
luz = input("¿Necesita luz solar? S/N ")
if luz.lower() == 's':
    luz = True
else:
    luz = False
precio = int(input("Ingrese el precio: "))
lista_informacion = [especie,luz,precio]

#Lista de plantas
plantas = []
print(guardar_plantas(plantas, lista_informacion))
