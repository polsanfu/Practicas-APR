numero = int(input("Ingrese un numero natural: "))
numero_res=numero

if numero < 0:
    exit()
factorial = 1

if numero != 0:
    while numero > 0:
        factorial = factorial * numero
        numero = numero - 1

print(f"El factorial de {numero_res} es: {factorial}")

numero_e = int(input("Ingrese un numero natural: "))


if numero_e < 0:
    exit()
factorial_2 = 1
e_aprox = 1
if numero_e != 0:
    for i in range(1,numero_e):
        factorial_2 = factorial_2 * i
        e_aprox = e_aprox + 1/factorial_2

print(f"El valor aproximado de e usando {numero_e} términos es: {e_aprox}")
