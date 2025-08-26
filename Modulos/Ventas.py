def submenu_ventas():
    opcion = 0
    while opcion != -1:
        print("Submenú Ventas")
        mostrar_encabezado(encabezados_submenu_ventas)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_submenu_ventas)
        if opcion == 1:  # Agregar venta
            agregar_venta_y_detalle(matriz_ventas)
        elif opcion == 2:  # Modificar detalle de venta
            modificar_venta(matriz_detalle_ventas)
        elif opcion == 3:  # Dar baja venta
            dar_baja_elementos(matriz_ventas)
        elif opcion == 4:  # Mostrar lista completa
            mostrar_matriz(matriz_ventas)
        elif opcion == -1:  # Volver al menú principal
            print("Volviendo al menú principal.")
        else:
            print("Opción no válida. Intente nuevamente.")
