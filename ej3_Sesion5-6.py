"""Realizar un programa (en el fichero ej3_sesion5.py) que determine el número de vocales de una
palabra. Para ello implementar la función es_vocal, que determina si el carácter que se le
pasa como parámetro es vocal o no. Dicha como función recibe como parámetro un carácter y
retorna un booleano. """

def es_vocales(palabra):
    suma = 0
    vocales = ["a","e","i","o","u"]
    for x in palabra:
        if x in vocales:
            suma = suma + 1
    return suma


palabra = input("Ingrese una palabra: ")
suma = es_vocales(palabra)
print(f"La suma de vocales de la palabra es de {suma}")

