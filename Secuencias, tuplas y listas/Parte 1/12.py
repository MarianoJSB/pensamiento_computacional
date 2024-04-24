def facultad():
    lista = []
    materia = 's'
    while materia != 'x':
        materia = input("Ingrese el nombre de la materia (X) para salir: ")
        if materia.lower() != 'x':
            lista.append(materia)
    return lista
print(facultad())