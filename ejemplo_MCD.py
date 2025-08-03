a=int(input("Introduzca a: "))
b=int(input("Introduzca b: "))
if a<b:
    aux=b
    b=a
    a=aux
res=a%b
while res!=0:
    aux=a
    a = b
    b=aux%b
    res=a%b

print(f"El MCD es {b}")