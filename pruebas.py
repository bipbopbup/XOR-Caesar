
a = "SSSSS"

if a.isupper():
    print("true")
else:
    print("false")

lista = ["a","B","c","D"]

longitud = len(lista)

print(longitud)

for i in range(longitud):
    c = lista[i]
    if c.isupper():
        print(c.swapcase())
    else:
        print(c)