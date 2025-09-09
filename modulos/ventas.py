from .funciones_generales import mostrar_encabezado, validar_opcion, dar_baja_elementos, mostrar_matriz, fechaYvalidacion, buscar_id
from .datos_de_prueba import encabezados_submenu_ventas, matriz_ventas, matriz_detalle_ventas, matriz_clientes, matriz_productos
from .recetas import agregar_receta

def submenu_ventas():
    opcion = 0
    while opcion != -1:
        print("Submenú Ventas")
        mostrar_encabezado(encabezados_submenu_ventas)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_submenu_ventas)
        if opcion == 1:  # Agregar venta
            agregar_venta_y_detalle(matriz_ventas)
            enter = input("Venta agregada exitosamente. Volviendo a menu...")
        elif opcion == 2:  # Modificar detalle de venta
            modificar_venta(matriz_detalle_ventas)
            enter = input("Venta modificada exitosamente. Volviendo a menu...")
        elif opcion == 3:  # Dar baja venta
            dar_baja_elementos(matriz_ventas)
            enter = input("Venta dada de baja exitosamente. Volviendo a menu...")
        elif opcion == 4:  # Mostrar lista completa
            mostrar_matriz(encabezados_submenu_ventas, matriz_ventas)
    enter = input("Volviendo al menú principal...")

def agregar_venta_y_detalle(matriz):
    venta = []
    id_venta = len(matriz) + 1
    fecha = fechaYvalidacion()
    id_cliente = int(input("Ingrese el ID del cliente: "))
    pos_cliente = buscar_id(matriz_clientes, id_cliente)
    while pos_cliente == -1:
        print("Error! El ID del cliente es inválido")
        id_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
        pos_cliente = buscar_id(matriz_clientes, id_cliente)
    print ("Ingresando a detalle de venta...")
    enter = input("Presione Enter para continuar...")
    total = agregar_detalle_de_venta(id_cliente, id_venta, matriz)
    venta = [id_venta, fecha, id_cliente, total]
    matriz.append(venta)

def agregar_detalle_de_venta(id_cliente, id_venta, matriz):
    detalle_venta = []
    total = 0
    producto = int(input("Ingrese el código del producto: "))
    while (producto <1 or producto > len(matriz_productos)) and producto != -1:
        print("Error! El código del producto es inválido.")
        producto = int(input("Ingrese nuevamente el código del producto o -1 para dejar de agregar productos: "))
    while producto != -1:
        receta = input("¿El cliente tiene receta? (s/n): ").lower()
        while receta not in ['s', 'n']:
            print("Error! Opción inválida.")
            receta = input("¿El cliente tiene receta? (s/n): ").lower()
        if receta == 's':
            id_receta, cantidad = agregar_receta(id_cliente,matriz_productos)
            subtotal = matriz_productos[producto][3] * cantidad
            detalle_venta = [id_venta, id_receta, subtotal]
            matriz.append(detalle_venta)
            total += subtotal
            producto = int(input("Ingrese el código del producto o -1 para dejar de agregar productos: "))
            while producto <1 or producto > len(matriz_productos) and producto != -1:
                print("Error! El código del producto es inválido.")
                producto = int(input("Ingrese nuevamente el código del producto o -1 para dejar de agregar productos: "))
        else:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            while cantidad > matriz_productos[producto][2]:
                print(f"Error! Sólo hay {matriz_productos[producto][2]} unidades disponibles.")
                cantidad = int(input("Vuelva a ingresar la cantidad del producto: "))
            subtotal = matriz_productos[producto][3] * cantidad
            detalle_venta = [id_venta, "VL", subtotal]
            matriz.append(detalle_venta)
            total += subtotal
            producto = int(input("Ingrese el código del producto o -1 para dejar de agregar productos: "))
            while (producto <1 or producto > len(matriz_productos)) and producto != -1:
                print("Error! El código del producto es inválido.")
                producto = int(input("Ingrese nuevamente el código del producto o -1 para dejar de agregar productos: "))
    print("Detalles de la venta agregados correctamente.")
    print(f"Total de la venta: ${total}")
    return total

def modificar_venta(matriz):
    id_venta = int(input("Ingrese el ID de la venta a modificar: "))
    pos = buscar_id(matriz, id_venta)
    while pos == -1:
        print("El ID de la venta es inválido")
        id_venta = int(input("Vuelva a ingresar el ID de la venta: "))
        pos = buscar_id(matriz, id_venta)
    fecha = fechaYvalidacion()
    total = int(input("Ingrese el nuevo total de la venta: "))
    matriz[pos][1] = fecha
    matriz[pos][3] = total