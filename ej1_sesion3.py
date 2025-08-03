numero = int(input("Introduce un numero natural (>=0): "))

x = 0

for x in range(0,numero-1,1):
    x = 1 + x
    print(x,end=", ")
print(numero)


