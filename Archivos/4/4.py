reemplazar = input("¿Que palabra desea reemplazar? ")
nueva = input("¿Que palabra nueva desea ingresar? ")

file_read = open("4/reemplazo.txt","r")
lista = file_read.readlines()
file_read.close()

file_write = open("4/reemplazo.txt","w")
for linea in lista:
    linea.lower()
    file_write.write(linea.replace(reemplazar,nueva))
file_write.close()
