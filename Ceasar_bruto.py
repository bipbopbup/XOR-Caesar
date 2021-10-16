

print("Ceasar Brute Force")


entrada = open ('textito.txt', 'r')
salida = open ('salidita.txt','w')
mensaje = entrada.read()

#abc = [a,]
mensaje_b = mensaje.swapcase

print(mensaje_b)


#longitud = len(mensaje)
#print(longitud)

for i in mensaje:
    print(i)
    salida.write(i)
