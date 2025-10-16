from .ventas import submenu_ventas
from .cliente import submenu_clientes
from .productos import submenu_inventario
from .funciones_generales import mostrar_encabezado, validar_opcion
from .estadisticas import submenu_reportes
from .datos_de_prueba import encabezados_menu
from .estadisticas import submenu_reportes
from .busquedas import submenu_busquedas

def menu_principal():
    opcion = 0
    while opcion != -1:
        print("---"* 10)
        print("Menu Principal")
        print("---"* 10)
        mostrar_encabezado(encabezados_menu)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_menu)
        if opcion == 1:  # Ventas
            submenu_ventas()
        elif opcion == 2:  # Inventario
            submenu_inventario()
        elif opcion == 3:  # Clientes
            submenu_clientes()
        elif opcion == 4: # Busquedas
            submenu_busquedas()
        elif opcion == 5:  # Reportes
            submenu_reportes()
    
    print("Programa finalizado")

