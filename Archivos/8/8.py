read = open("8/gustos.csv", "r")
leer = read.readlines()

def transformar(pro):
    pro = pro.strip("\n")
    pro = pro.split(";")
    return pro

productos = list(map(transformar, leer))
for i in productos:
    [n,c,g] = i
    print(f"A {n} {g} le gusta el {c}")
read.close()