import Ventas
import Productos
import Cliente
import Funciones_generales
import Datos_de_prueba

def menu_principal():
    opcion = 0
    while opcion != -1:
        print("Menu Principal")
        Funciones_generales.mostrar_encabezado(Datos_de_prueba.encabezados_menu)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:  # Ventas
            Ventas.submenu_ventas()
        elif opcion == 2:  # Inventario
            Productos.submenu_inventario()
        elif opcion == 3:  # Clientes
            Cliente.submenu_clientes()
        elif opcion == 4:  # Reportes
            Funciones_generales.submenu_reportes()
        elif opcion == -1:  # Terminar programa
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente nuevamente.")