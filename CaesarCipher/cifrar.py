print("Caesar chipher")
textoOriginal = input("Introduce el texto que deseas cifrar: ")
desplazamiento = int(input("Introduce la clave para cifrar el texto: "))
salida = ""

for c in textoOriginal:

    if c.isalpha() :

        if c.isupper():
            inicioAux = ord("A")
        else :
            inicioAux = ord("a")
        
        c_index = ord(c) - inicioAux
        new_index = (c_index + desplazamiento) % 26
        new_unicode = new_index + inicioAux

        new_character = chr(new_unicode)
        
        salida += new_character

    else :
        salida += c

print("El texto cifrado es: " + salida)