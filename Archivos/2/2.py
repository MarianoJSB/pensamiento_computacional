file = open("2/regalo.txt",'r+')
lista = file.readlines()
def regalo(listaFun):
    return len(listaFun) * 1000
monto_regalos = regalo(lista)
if 'Santi\n' in lista:
    file.write("\nTomi")
print("Monto del regalo", monto_regalos)
print(lista)
file.close()