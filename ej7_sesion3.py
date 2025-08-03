import math
real = float(input("Introduzca un numero real: "))
natural = int(input("Introduzca un numero natural mayor que 0: "))

if natural <= 0:
    exit()


i = 0
coseno_save = 0
while i < natural:
    res = (real**(2*i) / (math.factorial(2*i)) * (-1)**i)
    coseno_save = res + coseno_save
    i = i + 1

print(round(coseno_save, 2))