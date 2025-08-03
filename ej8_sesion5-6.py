def Celsius():
    celsius = input("Introduce grados celsius: ")
    while not celsius.isnumeric():
        print("Tipo de grado invalido")
        celsius = input("Introduce grados celsius: ")
    return float(celsius)


def conversor_grados():
    Celsius_value = Celsius()
    F = (Celsius_value * 9/5) + 32
    K = Celsius_value + 273.15
    print(f"El equivalente son {F} grados Fahrenheit y {K} grados Kelvin ")


conversor_grados()