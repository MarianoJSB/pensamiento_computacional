curso = {
    "segundo": 'E'
}
lista = [
    {
    'nombre': 'mariano',
    'edad': 19,
    'dni': 46287442,
    'curso': curso
    },
    {
    'nombre': 'maria',
    'edad': 24,
    'dni': 46282442,
    'curso': curso
    },
    {
    'nombre': 'ana',
    'edad': 12,
    'dni': 45287442,
    'curso': curso
    },
]

mayorEdad = max(lista, key=lambda x: x["edad"])

print(f'La persona con mayor edad tiene {mayorEdad["edad"]} y es {mayorEdad["nombre"]}')