import typer

app = typer.Typer()

@app.command()
def caesarBrute(text: str):
    """
    Given a TEXT ciphered via caesarCipher, returns every text deciphered with every key from 0 to 25. Execute as follows:
    
    python app.py TEXT

    For example: python app.py caesarbrute hello
    """
    print("Caesar Brute Force")

    salida = ""
    for i in range(26):

        for c in text:

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