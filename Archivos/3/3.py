file = open("3/compras.txt", "w")
user = "!"
while user != "":
    user = input("¿Que agrego a la lista de compras? ")
    if user == "x":
        break
    file.write(f"\n{user}")
file.close()