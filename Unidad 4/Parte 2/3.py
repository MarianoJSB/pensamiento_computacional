def dosPalabras(str1, str2):
    full = str1 + str2
    print(f"String: {full}")
    print(f"Substring: {str2}")
    return full.replace(str2, '')
print(dosPalabras("Campeones  a","Hola"))