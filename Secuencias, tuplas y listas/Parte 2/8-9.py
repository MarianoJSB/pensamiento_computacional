invitados = ('mariano', 'alan', 'jose', 'ariel')
invitados2 = ('alonso', 'ana', 'josefa', 'hector')

def fiesta(tupla, nombre):
    lista = list(tupla)
    index = lista.index(nombre)
    eliminar = lista.pop(index)
    return lista
print(fiesta(invitados, 'alan'))

def juntar(t1, t2):
    return t1 + t2
print(juntar(invitados, invitados2))