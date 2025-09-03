from .ventas import submenu_ventas
from .productos import agregar_producto, modificar_producto, dar_baja_producto
from .cliente import submenu_clientes
from .funciones_generales import mostrar_encabezado, validar_opcion, mostrar_matriz_cuadro
from .datos_de_prueba import encabezados_menu, encabezados_productos, encabezados_submenu_inventario
from .estadisticas import submenu_reportes

def menu_principal():
    opcion = 0
    while opcion != -1:
        print("Menu Principal")
        mostrar_encabezado(encabezados_menu)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:  # ventas
            submenu_ventas()
        elif opcion == 2:  # Inventario
            submenu_inventario()
        elif opcion == 3:  # clientes
            submenu_clientes()
        elif opcion == 4:  # Reportes
            submenu_reportes()
        elif opcion == -1:  # Terminar programa
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente nuevamente.")

def submenu_inventario(matriz_productos):
    opcion = 0
    while opcion != -1:
        print("Submenú Inventario")
        mostrar_encabezado(encabezados_submenu_inventario)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_submenu_inventario)
        if opcion == 1:  # Agregar producto
            agregar_producto(matriz_productos)
            enter = input("Producto agregado exitosamente. Volviendo a menu...")
        elif opcion == 2:  # Modificar Producto
            modificar_producto(matriz_productos)
            enter = input("Producto modificado exitosamente. Volviendo a menu...")
        elif opcion == 3:  # Dar baja producto
            dar_baja_producto(matriz_productos)
            enter = input("Producto eliminado exitosamente. Volviendo a menu...")
        else:  # Mostrar lista completa
            mostrar_matriz_cuadro(encabezados_productos,matriz_productos)
    enter = input("Volviendo a menu...")
