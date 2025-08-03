import random


class Usuario:
    def __init__(self,nombre, email):
        self.nombre = nombre
        self.email = email

    def validar_nom(self):
        if self.nombre and self.nombre.isalnum():
            return True
        return False

    def validar_email(self):
        if "@" not in self.email:
            return -1
        partes = self.email.split('@')
        if len(partes) != 2:
            return -3
        if "." not in partes[1]:
            return -2

        for char in self.email:
            if not (char.isalnum() or char in {'@', '.'}):
                return -3
        return 0


class Contrasenya:
    def __init__(self, valor):
        self.valor = valor
        self.long = len(valor)

    def es_fuerte(self):
        mayusculas = 0
        minusculas = 0
        numeros = 0

        for c in self.valor:
            if c.isupper():
                mayusculas += 1
            elif c.islower():
                minusculas += 1
            elif c.isdigit():
                numeros += 1


        if mayusculas >= 2 and minusculas >= 1 and numeros >= 5:
            return True
        else:
            return False

def generar_pass(self):

    mayusculas = [chr(random.randint(65, 90)) for _ in range(2)]
    minuscula = [chr(random.randint(97, 122))]
    digitos = [chr(random.randint(48, 57)) for _ in range(5)]

    caracteres = mayusculas + minuscula + digitos
    random.shuffle(caracteres)

    self.valor = ''.join(caracteres)
    self.long = len(self.valor)