from .ventas import submenu_ventas
from .cliente import submenu_clientes
from .productos import submenu_inventario
from .funciones_generales import mostrar_encabezado, validar_opcion, extraer_encabezado_submenu
from .estadisticas import submenu_reportes
from .estadisticas import submenu_reportes
from .busquedas import submenu_busquedas

def menu_principal():
    opcion = 0
    encabezados_menu = extraer_encabezado_submenu("menus")
    while opcion != -1:
        print("---" * 10)
        print("Menu Principal")
        print("---" * 10)
        mostrar_encabezado(encabezados_menu)

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: debe ingresar un número válido.")
            opcion = 0
            continue

        opcion = validar_opcion(opcion, 1, 5, encabezados_menu)

        if opcion == -1:
            # sale del while sin pedir otra vez
            break

        if opcion == 1:      # Ventas
            submenu_ventas()
        elif opcion == 2:    # Inventario
            submenu_inventario()
        elif opcion == 3:    # Clientes
            submenu_clientes()
        elif opcion == 4:    # Búsquedas
            submenu_busquedas()
        elif opcion == 5:    # Reportes
            submenu_reportes()

    print("Programa finalizado")