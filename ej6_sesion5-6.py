def menu():
    print("Calculadora")
    print("************\n")
    print("Menu")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Salir")


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

        if opt == 5:
            print("Gracias por usar calculadora")
            break

        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))

        if opt == 1:
            res = num1 + num2
            print(f"La suma es {res}")
        elif opt == 2:
            res = num1 - num2
            print(f"La resta es {res}")
        elif opt == 3:
            res = num1 * num2
            print(f"La multiplicacion es {res}")
        elif opt == 4:
            if num2 == 0:
                print("ERROR: Division entre 0")
            else:
                res = num1 / num2
                print(f"La Division es {res}")


calculadora()