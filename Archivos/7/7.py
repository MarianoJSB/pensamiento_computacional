def leer_info(archivo):
    file = open(archivo, "r")
    info = file.readlines()
    for i in range(len(info)):
        info[i] = info[i].strip("\n")
    file.close()
    return info

peliculas = leer_info("7/peliculas.txt")
salas = leer_info("7/salas.txt")

funciones = open("7/funciones.csv", "w")
for j in range(len(peliculas)):
    funciones.write(salas[j] + ";" + peliculas[j] + "\n")
funciones.close()