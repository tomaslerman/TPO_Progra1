import funciones_generales
import datos_de_prueba

def agregar_cliente(matriz):
    cliente = []
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese edad: "))
    obra_social = funciones_generales.ingresar_id_obra_social(datos_de_prueba.matriz_obras_sociales,datos_de_prueba.encabezados_obras_sociales)#funcion para pedir obra social
    telefono = int(input("Ingrese un número de teléfono:"))
    id_cliente = len(matriz) + 1  
    cliente.append(id_cliente, obra_social, nombre, edad, telefono)
    matriz.append(cliente)

def modificar_cliente(matriz_clientes, matriz_obras_sociales, encabezados_obras_sociales):
    id_cliente = int(input("Ingrese el ID del cliente a modificar: "))
    pos = funciones_generales.buscar_id(matriz_clientes, id_cliente)
    while pos == -1:
        print("El ID del cliente es inválido")
        id_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
        pos = funciones_generales.buscar_id(matriz_clientes, id_cliente)
    nombre = input("Ingrese el nuevo nombre del cliente: ")
    edad = int(input("Ingrese la nueva edad del cliente: "))
    obra_social = funciones_generales.ingresar_id_obra_social(matriz_obras_sociales,encabezados_obras_sociales)  # función para ingresar ID de obra social
    telefono = int(input("Ingrese el nuevo número de teléfono del cliente: "))  
    matriz_clientes[pos][2] = nombre
    matriz_clientes[pos][3] = edad
    matriz_clientes[pos][1] = obra_social
    matriz_clientes[pos][4] = telefono
    print("Cliente modificado correctamente.")

def submenu_clientes():
    opcion = 0
    while opcion != -1:
        print("Submenú Clientes")
        funciones_generales.mostrar_encabezado(datos_de_prueba.encabezados_submenu_clientes)
        opcion = int(input("Seleccione una opción: "))
        opcion = funciones_generales.validar_opcion(opcion, 1, 4, datos_de_prueba.encabezados_submenu_clientes)
        if opcion == 1:  # Agregar cliente
            agregar_cliente(datos_de_prueba.matriz_clientes)
        elif opcion == 2:  # Modificar cliente
            modificar_cliente(datos_de_prueba.matriz_clientes)
        elif opcion == 3:  # Dar baja cliente
            funciones_generales.dar_baja_elementos(datos_de_prueba.matriz_clientes)
        elif opcion == 4:  # Mostrar lista completa
            funciones_generales.mostrar_matriz(datos_de_prueba.matriz_clientes)
        elif opcion == -1:  # Volver al menú principal
            print("Volviendo al menú principal.")
        else:
            print("Opción no válida. Intente nuevamente.")