limite = int(input("Hasta que numero: "))

def n_primos(lim):
    for i in range(2, lim + 1):
        primo = True
        for j in range(2,i):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(f"{i} es primo")
        else:
            print(f"{i} no es primo")
print(n_primos(limite))