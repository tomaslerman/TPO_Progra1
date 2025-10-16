from .funciones_generales import buscar_id

def submenu_busquedas():
    opcion = 0
    while opcion != -1:
        print("---"* 10)
        print("Submenú Búsquedas")
        print("---"* 10)
        print("1. Ventas de un cliente específico")
        print("2. Ventas de un producto específico")
        print("-1. Volver al menú principal")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error! Opción inválida.")
            continue
        while opcion not in [1, 2, -1]:
            print("Error! Opción inválida.")
            opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            id_cliente = int(input("Ingrese el ID del cliente: "))
            ventas_de_x_cliente(id_cliente)
            enter = input("Presione Enter para continuar...")
        elif opcion == 2:
            id_producto = int(input("Ingrese el ID del producto: "))
            ventas_de_x_producto(id_producto)
            enter = input("Presione Enter para continuar...")
    enter = input("Volviendo al menú principal...")

def ventas_de_x_cliente(id_cliente):
    try:
        arch_clientes = open("clientes.txt", "r", encoding="utf-8")
        matriz_clientes = [linea.strip().split(";") for linea in arch_clientes]
    except FileNotFoundError:
        print("Error! El archivo de clientes no existe.")
    finally:
        try:
            arch_clientes.close()
        except:
            print("Error al cerrar el archivo de clientes.")
    pos_cliente = buscar_id(matriz_clientes, id_cliente)
    if pos_cliente == -1:
        print("Error! El ID del cliente es inválido.")
        return
    if matriz_clientes[pos_cliente][5] == "Inactive":
        print("El cliente está inactivo. No se pueden mostrar las ventas.")
        return
    print(f"Ventas del cliente {matriz_clientes[pos_cliente][2]} (ID {id_cliente}):")
    try:
        arch_ventas = open("ventas.txt", "r", encoding="utf-8")
        matriz_ventas = [linea.strip().split(";") for linea in arch_ventas]
    except FileNotFoundError:
        print("Error! El archivo de ventas no existe.")
        return
    finally:
        try:
            arch_ventas.close()
        except:
            print("Error al cerrar el archivo de ventas.")
    ventas_cliente = [venta for venta in matriz_ventas if int(venta[2]) == id_cliente]
    if not ventas_cliente:
        print("No hay ventas registradas para este cliente.")
        return
    print(f"{'ID Venta':<10}{'Fecha':<15}{'Total':<10}")
    for venta in ventas_cliente:
        print(f"{int(venta[0]):<10}{venta[1]:<15}${float(venta[3]):<10.2f}")

#Hasta acá funciona

def ventas_de_x_producto(id_producto):
    try:
        arch_productos = open("productos.txt", "r", encoding="utf-8")
        matriz_productos = [linea.strip().split(";") for linea in arch_productos]
    except FileNotFoundError:
        print("Error! El archivo de productos no existe.")
        return
    finally:
        try:
            arch_productos.close()
        except:
            print("Error al cerrar el archivo de productos.")
    pos_producto = buscar_id(matriz_productos, id_producto)
    if pos_producto == -1:
        print("Error! El ID del producto es inválido.")
        return
    print(f"Ventas del producto {matriz_productos[pos_producto][1]} (ID {id_producto}):")
    try:
        arch_detalle_ventas = open("detalle_ventas.txt", "r", encoding="utf-8")
        matriz_detalle_ventas = [linea.strip().split(";") for linea in arch_detalle_ventas]
    except FileNotFoundError:
        print("Error! El archivo de detalle de ventas no existe.")
        return
    finally:
        try:
            arch_detalle_ventas.close()
        except:
            print("Error al cerrar el archivo de detalle de ventas.")
    ventas_producto = [detalle for detalle in matriz_detalle_ventas if int(detalle[1]) == id_producto]
    if not ventas_producto:
        print("No hay ventas registradas para este producto.")
        return
    print(f"{'ID Venta':<10}{'ID Receta':<10}{'Subtotal':<10}")
    for detalle in ventas_producto:
        print(f"{int(detalle[0]):<10}{detalle[1]:<10}${float(detalle[2]):<10.2f}")