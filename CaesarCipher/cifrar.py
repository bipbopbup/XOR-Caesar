import typer

app = typer.Typer()

@app.command()
def caesarCipher(text: str, key: int):

    salida = ""

    for c in text:

        if c.isalpha() :

            if c.isupper():
                inicioAux = ord("A")
            else :
                inicioAux = ord("a")
            
            c_index = ord(c) - inicioAux
            new_index = (c_index + key) % 26
            new_unicode = new_index + inicioAux

            new_character = chr(new_unicode)
            
            salida += new_character

        else :
            salida += c

    print("El texto cifrado es: " + salida)