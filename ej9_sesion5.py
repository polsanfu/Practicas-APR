def fibonacci(n):
    if n<= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    num = int(input("Introduzca un número natural: "))
    while num < 0:
        print("Eso no es un numero natural, vuelvelo a intentar")
        num = int(input("Introduzca un número natural: "))

    serie = [fibonacci(x) for x in range(0,num+1,1)]
    print(f"Serie de fibonacci en {num}: {serie}")

main()




