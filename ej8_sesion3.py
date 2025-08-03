frase = input("Introduce una frase: ")

palabras = frase.split()

acronimo = ""

for palabra in palabras:
    acronimo = acronimo + palabra[0].upper()

print(acronimo)
