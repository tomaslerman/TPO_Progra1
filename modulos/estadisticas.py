from .funciones_generales import extraer_encabezado, mostrar_encabezado, validar_opcion

def submenu_reportes():
    opcion = 0
    encabezados_sub_menu_reportes = extraer_encabezado("encabezados_submenu_reportes")
    while opcion != -1:
        print("---"* 10)
        print("Submenú Reportes")
        print("---"* 10)
        mostrar_encabezado(encabezados_sub_menu_reportes)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_sub_menu_reportes)
        if opcion == 1:  # Estadística de ventas
            estadisticas_ventas()
            enter = input("Presione Enter para continuar...")
    enter = input("Volviendo a menu...")

def estadisticas_ventas(matriz):
    total_ventas = len(matriz)
    suma_total = sum([venta[3] for venta in matriz])
    promedio = suma_total / total_ventas if total_ventas > 0 else 0
    print(f"Cantidad de ventas: {total_ventas}")
    print(f"Total vendido: ${suma_total}")
    print(f"Promedio por venta: ${promedio:.2f}")

