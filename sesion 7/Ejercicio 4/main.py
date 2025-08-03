from operacion import Suma, Resta, Multiplicacion, Division

print("Calculadora")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.Division")
print("5.Salir")
opcion = int(input("Introduce una opcion: "))


while opcion not in [1, 2, 3, 4, 5]:
    print("Opción inválida. Inténtalo de nuevo.")
    opcion = int(input("Introduce una opción válida: "))

if opcion == 1:
    num_1 = int(input("Introduce un numero: "))
    num_2 = int(input("Introduce un numero: "))
    suma = Suma(num_1, num_2)
    print(suma)
elif opcion == 2:
    num_1 = int(input("Introduce un numero: "))
    num_2 = int(input("Introduce un numero: "))
    resta = Resta(num_1, num_2)
    print(resta)
elif opcion == 3:
    num_1 = int(input("Introduce un numero: "))
    num_2 = int(input("Introduce un numero: "))
    multiplicacion = Multiplicacion(num_1, num_2)
    print(multiplicacion)
elif opcion == 4:
    num_1 = int(input("Introduce un numero: "))
    num_2 = int(input("Introduce un numero: "))
    if num_2 == 0:
        print("No se puede dividir entre 0")
    else:
        division = Division(num_1, num_2)
        print(division)

elif opcion == 5:
    exit()



