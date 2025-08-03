"""a) Escribir un programa (en el fichero ej4_sesion3.py) que pida al usuario que introduzca
una frase por teclado y cuente el número de palabras que hay en la frase. Recordar que
el método strip elimina los espacios en blanco del principio y final de la frase. Tener
en cuenta que las palabras de la frase estarán separadas únicamente por espacios en
blanco"""

frase = input("Introduce una frase: ")
frase.strip()
palabras = frase.split()
long=len(palabras)
print(f"La frase tiene {long} palabras")

"""A continuación extender el programa para que pida al usuario que introduzca una
palabra y determine si dicha palabra está en la frase."""

palabra = input("Introduce una palabra para ver si esta en la frase: ")

if palabra in frase:
    print("La palabra esta en la frase")
else:
    print("La palabra no esta en la frase")


