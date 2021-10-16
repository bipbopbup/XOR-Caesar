lista = ["a","B","c","D"]

longitud = len(lista)

print(longitud)

for i in range(len(lista)):
    c = lista[i]
    if c.isupper():
        print(c.swapcase())
    else:
        print(c)
