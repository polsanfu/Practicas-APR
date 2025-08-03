from math import cos

def menu():
    print("Calculadora cientifica")
    print("************\n")
    print("Menu")
    print("1) Factorial")
    print("2) Exponencial")
    print("3) Coseno")
    print("4) Salir")

def opcion():
    opcionn = input("Ingrese una opcion: ")
    while not opcionn.isnumeric():
        print("Opcion invalida")
        opcionn = input("Ingrese una opcion: ")
    return int(opcionn)


def calculadora():
    while True:
        menu()
        opt = opcion()

        while opt not in [1, 2, 3, 4, 5]:
            print("Opcion invalida")
            opt = opcion()

        if opt == 4:
            print("Gracias por usar calculadora")
            break

        num1 = int(input("Ingrese un numero: "))

        if opt == 1:
            if num1 == 0 or num1 == 1:
                print(f"El factorial de {num1} es {num1}")
            else:
                factorial = 1
                for x in range(1, num1 + 1):
                    factorial *= x
                print(f"El factorial de {num1} es {factorial}")
        if opt == 2:
            e = 2.7182818284
            exp = e**num1
            print(f"El exponencial de {num1} es {exp}")
        if opt == 3:
            coseno = cos(num1)
            print(f"El coseno de {num1} es {coseno}")



calculadora()