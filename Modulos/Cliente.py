from .funciones_generales import mostrar_encabezado, validar_opcion, mostrar_matriz_clientes, buscar_id, ingresar_id_obra_social
from .datos_de_prueba import matriz_clientes, encabezados_submenu_clientes, matriz_obras_sociales, encabezados_obras_sociales

def agregar_cliente(matriz):
    cliente = []
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese edad: "))
    obra_social = ingresar_id_obra_social(matriz_obras_sociales,encabezados_obras_sociales)#funcion para pedir obra social
    telefono = int(input("Ingrese un número de teléfono:"))
    id_cliente = len(matriz) + 1  
    cliente.append(id_cliente, obra_social, nombre, edad, telefono)
    matriz.append(cliente)

def modificar_cliente(matriz_clientes, matriz_obras_sociales, encabezados_obras_sociales):
    id_cliente = int(input("Ingrese el ID del cliente a modificar: "))
    pos = buscar_id(matriz_clientes, id_cliente)
    while pos == -1:
        print("El ID del cliente es inválido")
        id_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
        pos = buscar_id(matriz_clientes, id_cliente)
    nombre = input("Ingrese el nuevo nombre del cliente: ")
    edad = int(input("Ingrese la nueva edad del cliente: "))
    obra_social = ingresar_id_obra_social(matriz_obras_sociales,encabezados_obras_sociales)  # función para ingresar ID de obra social
    telefono = int(input("Ingrese el nuevo número de teléfono del cliente: "))  
    matriz_clientes[pos][2] = nombre
    matriz_clientes[pos][3] = edad
    matriz_clientes[pos][1] = obra_social
    matriz_clientes[pos][4] = telefono
    print("Cliente modificado correctamente.")

def baja_cliente(matriz_clientes):
    id_cliente = int(input("Ingrese el ID del cliente a dar de baja: "))
    pos = buscar_id(matriz_clientes, id_cliente)
    while pos == -1:
        print("El ID del cliente es inválido")
        id_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
        pos = buscar_id(matriz_clientes, id_cliente)
    matriz_clientes[pos][5] = "Inactive"


def submenu_clientes():
    opcion = 0
    while opcion != -1:
        print("Submenú Clientes")
        mostrar_encabezado(encabezados_submenu_clientes)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_submenu_clientes)
        if opcion == 1:  # Agregar cliente
            agregar_cliente(matriz_clientes)
            enter = input("Cliente agregado exitosamente. Volviendo a menu...")
        elif opcion == 2:  # Modificar cliente
            modificar_cliente(matriz_clientes)
            enter = input("Cliente modificado exitosamente. Volviendo a menu...")
        elif opcion == 3:  # Dar baja cliente
            baja_cliente(matriz_clientes)
            enter = input("Cliente eliminado exitosamente. Volviendo a menu...")
        else:  # Mostrar lista completa
            mostrar_matriz_clientes(matriz_clientes)
    enter = input(" Volviendo a menu...")
