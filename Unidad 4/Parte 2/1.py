def vocales(string):
    vocal = ['a','e','i','o','u']
    for i in string:
        if i in vocal:
            print(i)
vocales("Hola")