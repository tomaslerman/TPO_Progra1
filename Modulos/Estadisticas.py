from .funciones_generales import mostrar_encabezado, validar_opcion
from .datos_de_prueba import encabezados_sub_menu_reportes
from .ventas import estadisticas_ventas

def submenu_reportes():
    opcion = 0
    while opcion != -1:
        print("Submenú Reportes")
        mostrar_encabezado(encabezados_sub_menu_reportes)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_sub_menu_reportes)
        if opcion == 1:  # Estadística de ventas
            estadisticas_ventas()
        elif opcion == -1:  # Volver al menú principal
            print("Volviendo al menú principal.")
        else:
            print("Opción no válida. Intente nuevamente.")