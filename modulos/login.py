from .menu_p import menu_principal
from .datos_de_prueba import matriz_login, matriz_clientes, matriz_productos, matriz_recetas, matriz_ventas, matriz_detalle_ventas

def login(matriz_login):
    print("Bienvenido al sistema de gestión de farmacia.")
    while True:  # loop hasta que logre loguearse
        try:
            usuario = pedir_usuario()
            contrasena = pedir_contrasena()
            validar_credenciales(usuario, contrasena, matriz_login)
            print("Login ingresado correctamente para el usuario:", usuario)
            menu_principal()
            break  # corta el loop si el login fue correcto
        except ValueError as e:
            print(e)  # mensaje de error si no valida
            print("Intente nuevamente.\n")

def pedir_usuario():
    while True:
        try:
            usuario = input("Ingrese usuario: ").strip()
            if not usuario.isalpha():
                raise ValueError("El usuario debe contener solo letras.")
            return usuario
        except ValueError as e:
            print(e)

def pedir_contrasena():
    while True:
        try:
            contrasena = input("Ingrese contraseña: ").strip()
            if not contrasena.isalnum():
                raise ValueError("La contraseña debe contener solo caracteres alfanuméricos.")
            return contrasena
        except ValueError as e:
            print(e)

def validar_credenciales(usuario, contrasena, matriz_login):
    """Valida usuario y contraseña contra la matriz de logins."""
    lista_contra = [dato for dato in matriz_login if dato[0] == usuario and dato[1] == contrasena]
    if len(lista_contra) == 0:
        raise ValueError("Error: Usuario o contraseña incorrectos.")
