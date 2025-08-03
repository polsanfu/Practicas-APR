"""Realizar un programa (en el fichero ej4_sesion5.py) que muestre un histograma (representación
gráfica de una variable en forma de barras). Para ello el usuario introducirá los diferentes valores
que toma la variable, y el programa mostrará por pantalla las barras de longitud
correspondiente. Cada barra se corresponde con una línea de asteriscos, que contiene tantos
asteriscos como valor tenga la variable.
Realizar la función imp_hist que recibirá como parámetro un número e imprimirá por
pantalla tantos asteriscos como valor tenga dicho número."""

def imp_hist(numeros):
    print("*" * numeros)


numero = (input("Introduzca los valores del histograma separados por un espacio en blanco: "))
numeros = [int(x) for x in numero.split()]

for x in numeros:
    imp_hist(x)

