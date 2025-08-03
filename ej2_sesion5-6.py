"""Realizar un programa (en el fichero ej2_sesion5.py) que sume los dígitos pares de un número
entero, que introducirá el usuario por teclado. Para ello implementar la función es_par que
determinará si el digito que recibe como parámetro es par o no. Dicha función devolverá el
booleano True si el número es par y False en caso contrario."""


def es_par(dig):
    if dig % 2 == 0:
        return True
    else:
        return False

numero = int(input("Introduce un numero: "))
suma = 0
numeros = str(numero)
for dig in numeros:
    if es_par(int(dig)) == True:
        suma += int(dig)
    else:
        suma = suma
print(f"La suma de numeros pares es: {suma}")
