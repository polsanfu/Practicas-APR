"""Realizar un programa (en el fichero ej1_sesion5.py) que pida al usuario que introduzca una
secuencia de números naturales acabada en -1, determine los que son primos, y muestre por
pantalla la suma de todos los números primos de la secuencia."""

def numero_primo(n):
    if n == 1 or n == 2:
        return True
    for x in range(2,n,1):
        if n % x == 0:
            return False
    return True

print("Introduce una secuencia de números, -1 para finalizar.")
n = int(input("Introduce un numero: "))
res = 0
if n == -1:
    exit()
while n != -1:
    if numero_primo(n) == True:
        res = res + n
        n = int(input("Introduce un numero: "))
    else:
        res = res
        n = int(input("Introduce un numero: "))


print(f"La suma de numeros primos es: {res}")

