try:
    read = open("4/4.txt", "r")
    lines = read.readlines()
    print(lines)
    read.close()
except:
    print("El archivo no se pudo encontrar")