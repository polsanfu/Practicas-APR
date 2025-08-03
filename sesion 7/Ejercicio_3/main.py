from Usuario import Usuario
from Usuario import Contrasenya

nombre = input("Introduce el nombre de usuario: ")
while not nombre.isalnum():
    print("El nombre solo debe contener letras y números.")
    nombre = input("Introduce el nombre de usuario: ")

usuario = Usuario(nombre,"")  # Instanciamos el objeto Usuario después de obtener el nombre

# Validación del email
email = input("Introduce el email: ")
usuario.email = email  # Asignamos el email después de que el usuario lo ingrese
while usuario.validar_email() != 0:
    print("Error con el email. Asegúrate de que contenga '@' y '.' y solo caracteres alfanuméricos.")
    email = input("Introduce el email: ")
    usuario.email = email

contrasena = Contrasenya()
contrasena_input = input("Introduce la contraseña: ")
contrasena.valor = contrasena_input
while not contrasena.es_fuerte():
    print("La contraseña no es suficientemente segura.")
    contrasena.generar_pass()
    print(f"Contraseña generada: {contrasena.valor}")
    contrasena_input = input("Introduce una nueva contraseña segura: ")
    contrasena.valor = contrasena_input
print("Usuario creado con éxito!")