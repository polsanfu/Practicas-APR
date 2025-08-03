def imprime_triangulo(ancho, car):
    for x in range(1,int(ancho/2 + 1.0) ,1):
        print(car * x)
    for x in range(int(ancho/2 + 1),0,-1):
        print(car * x)

ancho = float(input("Introduce el ancho para el triangulo: "))
car = input("Introduce el caracter con el que quieres dibujar el triangulo: ")

imprime_triangulo(ancho, car)

