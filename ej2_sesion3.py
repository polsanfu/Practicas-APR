numero = int(input("Introduzca por teclado un numero natural >0: "))

if numero <= 0:
    exit()

for x in range(1, numero, 1):
    div = numero%x
    if div == 0:
        resultado = print(x,end=", ")

print(numero)
