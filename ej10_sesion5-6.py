def es_palindromo ():
    palabra = input("Introduce una palabra: ")
    palabra_1 = list(palabra)
    palabra_2 = palabra_1[::-1]

    if palabra_1 != palabra_2:
        print("No es palindromo")
    else:
        print("Es palindromo")

es_palindromo()
