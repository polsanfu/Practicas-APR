usuario = input("Introduce un nombre de usuario: ")


if usuario.isalnum():
    long = len(usuario)
    if long >= 6 and long <= 12:
        usuario_correcto = True
    else:
        usuario_correcto = False

else:
    usuario_correcto = False

contraseña = input("Introduce una contraeña: ")

if contraseña.isalnum():
    long = len(contraseña)
    if long == 8:
        espacio = contraseña.find(" ",)
        if espacio == -1:
            contra_correcta = True
        else:
            contra_correcta = False
    else:
        contra_correcta = False
else:
    contra_correcta = False

if usuario_correcto == True:
    if contra_correcta == True:
        print("Usuario y contraseña correctos")
    else:
        print("Contraseña incorrecta")
if usuario_correcto == False:
    if contra_correcta == True:
        print("usuario incorrecto")
    else:
        print("Usuario y contraseña incorrectos")






