from .menu_p import menu_principal
from .datos_de_prueba import diccionario_login, matriz_clientes, matriz_productos, matriz_recetas, matriz_ventas, matriz_detalle_ventas
    
def login(diccionario_login):
    print("Bienvenido al sistema de gestión de farmacia.")
    usuario = pedir_usuario()
    contrasena = pedir_contrasena()

    # Verificamos directamente en el diccionario
    while usuario not in diccionario_login or diccionario_login[usuario] != contrasena:
        print("Usuario o contraseña incorrecta. Ingrese nuevamente su usuario y contraseña: ")
        usuario = pedir_usuario()
        contrasena = pedir_contrasena()

    print("Login ingresado correctamente para el usuario:", usuario)
    menu_principal()

def pedir_usuario():
    usuario = input("Ingrese usuario: ").strip()
    while not usuario.isalpha():
        print("El usuario debe contener solo letras.")
        usuario = input("Ingrese usuario nuevamente: ").strip()
    return usuario


def pedir_contrasena():
    contrasena = input("Ingrese contraseña: ").strip()
    while not contrasena.isalnum():
        print("La contraseña debe contener solo caracteres alfanuméricos.")
        contrasena = input("Ingrese contraseña nuevamente: ").strip()
    return contrasena