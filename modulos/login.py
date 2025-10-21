from .menu_p import menu_principal

def login():
    print("Bienvenido al sistema de gestión de farmacia.")
    while True:  # loop hasta que logre loguearse
        try:
            usuario = pedir_usuario()
            contrasena = pedir_contrasena()
            validar_credenciales(usuario, contrasena, diccionario_login)
            print(f"Login ingresado correctamente para el usuario: {usuario}")
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

def validar_credenciales(usuario, contrasena, diccionario_login):
    """Valida usuario y contraseña usando un diccionario."""
    if usuario not in diccionario_login or diccionario_login[usuario] != contrasena:
        raise ValueError("Error: Usuario o contraseña incorrectos.")
