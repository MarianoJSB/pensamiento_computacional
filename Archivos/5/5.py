read = open("5/productos.csv","r")
lista = read.readlines()
read.close()

def transformar(pro):
    pro = pro.strip("\n")
    pro = pro.split(";")
    return pro

productos = list(map(transformar, lista))

for i in productos:
    [n,c,p,s] = i
    print(f"Nombre: {n}\nCodigo: {c}\nPrecio: {p}\nStock: {s}\n")
    
def agregar(dic):
    nombre = dic["nombre"]
    codigo = dic["codigo"]
    precio = dic["precio"]
    stock = dic["stock"]
    guardar = f"\n{nombre};{codigo};{precio};{stock}" 
    
    return guardar

dic = { 
    "nombre": "hojas A4",
    "codigo": 35662, 
    "precio": 600,
    "stock": 45 
}

write = open("5/productos.csv","a")
write.write(agregar(dic))
write.close()