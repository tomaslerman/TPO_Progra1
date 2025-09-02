import funciones_generales, datos_de_prueba
def submenu_ventas():
    opcion = 0
    while opcion != -1:
        print("Submenú Ventas")
        funciones_generales.mostrar_encabezado(funciones_generales.encabezados_submenu_ventas)
        opcion = int(input("Seleccione una opción: "))
        opcion = funciones_generales.validar_opcion(opcion, 1, 4, funciones_generales.encabezados_submenu_ventas)
        if opcion == 1:  # Agregar venta
            agregar_venta_y_detalle(datos_de_prueba.matriz_ventas)
        elif opcion == 2:  # Modificar detalle de venta
            modificar_venta(datos_de_prueba.matriz_detalle_ventas)
        elif opcion == 3:  # Dar baja venta
            funciones_generales.dar_baja_elementos(datos_de_prueba.matriz_ventas)
        elif opcion == 4:  # Mostrar lista completa
            funciones_generales.mostrar_matriz(datos_de_prueba.matriz_ventas)
        elif opcion == -1:  # Volver al menú principal
            print("Volviendo al menú principal.")
        else:
            print("Opción no válida. Intente nuevamente.")

def agregar_venta_y_detalle(matriz):
    venta = []
    id_venta = len(matriz) + 1
    fecha = funciones_generales.fechaYvalidacion()
    id_cliente = int(input("Ingrese el ID del cliente: "))
    pos_cliente = funciones_generales.buscar_id(datos_de_prueba.matriz_clientes, id_cliente)
    while pos_cliente == -1:
        print("Error! El ID del cliente es inválido")
        id_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
        pos_cliente = funciones_generales.buscar_id(datos_de_prueba.matriz_clientes, id_cliente)
    total = int(input("Ingrese el total de la venta: "))
    venta.append(id_venta, fecha, id_cliente, total)
    matriz.append(venta)
    
def modificar_venta(matriz):
    id_venta = int(input("Ingrese el ID de la venta a modificar: "))
    pos = funciones_generales.buscar_id(matriz, id_venta)
    while pos == -1:
        print("El ID de la venta es inválido")
        id_venta = int(input("Vuelva a ingresar el ID de la venta: "))
        pos = funciones_generales.buscar_id(matriz, id_venta)
    fecha = funciones_generales.fechaYvalidacion()
    total = int(input("Ingrese el nuevo total de la venta: "))
    matriz[pos][1] = fecha
    matriz[pos][3] = total
    print("Venta modificada correctamente.")
def estadisticas_ventas(matriz_ventas):
    total_ventas = len(matriz_ventas)
    suma_total = sum([venta[3] for venta in matriz_ventas])
    promedio = suma_total / total_ventas if total_ventas > 0 else 0
    print(f"Cantidad de ventas: {total_ventas}")
    print(f"Total vendido: ${suma_total}")
    print(f"Promedio por venta: ${promedio:.2f}")

