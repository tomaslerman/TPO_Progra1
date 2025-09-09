from .menu_p import menu_principal
from .datos_de_prueba import matriz_login, matriz_clientes, matriz_productos, matriz_recetas, matriz_ventas, matriz_detalle_ventas
    
def login(matriz_login):
    print("Bienvenido al sistema de gestión de farmacia.")
    usuario = pedir_usuario()

    contrasena = pedir_contrasena()

    lista_contra=[dato for dato in matriz_login if dato[0] == usuario and dato[1] == contrasena]
    while len(lista_contra)==0:
        print("Usuario o contraseña incorrecta. Ingrese nuevamente su usuario y contraseña: ")
        usuario = pedir_usuario()

        contrasena = pedir_contrasena()
  
        lista_contra=[dato for dato in matriz_login if dato[0] == usuario and dato[1] == contrasena]
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