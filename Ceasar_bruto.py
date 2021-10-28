print("Caesar Brute Force")
textoOriginal = input("Introduce el texto que deseas cifrar: ")
salida = ""
for i in range(26):

    for c in textoOriginal:

        if c.isalpha() :
            desplazamiento = i
            if c.isupper():
                inicioAux = ord("A")
            else :
                inicioAux = ord("a")
        
            c_index = ord(c) - inicioAux
            new_index = (c_index - desplazamiento) % 26
            new_unicode = new_index + inicioAux
            new_character = chr(new_unicode)
        
            salida += new_character

        else :
            salida += c

    print("Llave "+ str(i) + " : " + salida)
    salida = ""