from random import randint
nombre = input("Como te llamas? ")
saludo = input(f"Bueno, {nombre}, estoy pensando en un numero del 1 al 20.\nTienes hasta 6 intentos para adivinarlo.\n(Pulse intro para continuar)")
print(saludo)
numero = randint(1,20)
intentos = 0

while intentos < 6:
    random = int(input("Escribe un numero del 1 al 20: "))
    intentos = intentos + 1

    if random < numero:
        print("Tu estimacion es muy baja")
    elif random > numero:
        print("Tu estimacion es muy alta")
    else:
        print(f"El numero {numero} es el correcto, felicidades {nombre}.\nLo has conseguido en {intentos} intentos.")
        exit()
if random != numero:
    print(f"No has conseguido encontrar el numero en 6 intentos, pruebalo de nuevo. El numero era {numero}.")
    exit()

