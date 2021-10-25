import typer

app = typer.Typer()

@app.command()
def caesarCipher(text: str, key: int):
    """
    Ciphers a TEXT with an int KEY via caesarCipher. Execute as follows:
    
    python app.py TEXT KEY

    For example: python app.py caesarcipher hello 4
    """

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

    typer.echo("El texto cifrado es: " + salida)