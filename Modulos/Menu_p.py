import ventas
import productos
import cliente
import funciones_generales
import datos_de_prueba

def menu_principal():
    opcion = 0
    while opcion != -1:
        print("Menu Principal")
        funciones_generales.mostrar_encabezado(datos_de_prueba.encabezados_menu)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:  # ventas
            ventas.submenu_ventas()
        elif opcion == 2:  # Inventario
            productos.submenu_inventario()
        elif opcion == 3:  # clientes
            cliente.submenu_clientes()
        elif opcion == 4:  # Reportes
            funciones_generales.submenu_reportes()
        elif opcion == -1:  # Terminar programa
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente nuevamente.")