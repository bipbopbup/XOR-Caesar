# XOR-Caesar

XOR-Caesar permite cifrar y descrifrar con Caesar y por fuerza bruta mediante comandos. El XOR no está implementado porque un compañero no hizo su parte, pero vamos entregando la nuestra.

Creado por:
Lucas Marco             - BiBimBap#9000
Luis Miguel Lombardo    - electricluis#7204
Juan Esteban Rincón     - Esquizo 2033#1500


# Typer

Typer es una librería de python para crear comandos.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install typer.

```bash
pip install typer
```

## Usage

```bash

# returns 'ayuda'
python app.py --help

# returns 'cifrado por Caesar'
python app.py caesarcipher text 42

# returns 'Descifrado por Caesar'
python app.py caesardecipher text 42

# returns 'romper Caesar por fuerza bruta'
python app.py caesarbrute text