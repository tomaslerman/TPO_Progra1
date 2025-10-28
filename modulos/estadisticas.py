from .funciones_generales import extraer_encabezado, mostrar_encabezado, validar_opcion, open_json_file, leer_ventas, leer_productos 
import json

def submenu_reportes():
    opcion = 0
    encabezados_sub_menu_reportes = extraer_encabezado("reportes")
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

#recursividad: minimo precio de producto 


def contar_clientes_activos(clientes, claves=None, i=0):
    """
    Cuenta recursivamente la cantidad de clientes activos en el diccionario.
    """
    if claves is None:
        claves = list(clientes.keys())

    # Caso base: cuando llegamos al final de la lista de claves
    if i == len(claves):
        return 0
    else:
        clave_actual = claves[i]
        cliente = clientes[clave_actual]
        activo = 1 if cliente["estado"].lower() == "active" else 0
        return activo + contar_clientes_activos(clientes, claves, i + 1)

def total_clientes_activos():
    """
    Lee el archivo clientes.json y usa la función recursiva para contar los activos.
    """
    try:
        with open("clientes.json", "r", encoding="utf-8") as archivo:
            clientes = json.load(archivo)   
    except FileNotFoundError:
        print("Error: el archivo clientes.json no existe.")
        return 0
    except json.JSONDecodeError:
        print("Error: formato JSON inválido.")
        return 0
    except OSError:
        print("Error al abrir clientes.json.")
        return 0

    return contar_clientes_activos(clientes)


def sumar_totales_cliente(ventas, id_cliente, i=0):
    """Suma recursivamente los totales de ventas del cliente indicado."""
    if i == len(ventas):
        return 0
    else:
        venta = ventas[i]
        total_actual = venta[3] if venta[2] == id_cliente else 0
        return total_actual + sumar_totales_cliente(ventas, id_cliente, i + 1)
    

def total_gastado_por_cliente():
    """Pide un ID, valida que el cliente exista y esté activo, y muestra su total gastado."""
    clientes = open_json_file(clientes.json)
    if len(clientes) == 0:
        print("No hay clientes cargados.")
        return

    ventas = leer_ventas()
    if len(ventas) == 0:
        print("No hay ventas cargadas.")
        return

    # pedir ID y validar
    while True:
        try:
            id_cliente = int(input("Ingrese el ID del cliente: "))
            break
        except ValueError:
            print("Error: debe ingresar un número entero.")

    cliente = clientes.get(str(id_cliente))
    if cliente is None:
        print("El cliente no existe.")
        return

    if cliente["estado"].lower() != "active":
        print(f"El cliente {cliente['nombre']} está inactivo. No tiene ventas activas.")
        return

    total = sumar_totales_cliente(ventas, id_cliente)
    print(f"El cliente {cliente['nombre']} gastó un total de: ${total:.2f}")
    return total

#revisar:

def producto_minimo_precio(productos, i=0):
    """
    Devuelve el producto con el precio mínimo de forma recursiva.
    """
    if i == len(productos) - 1:
        return productos[i]  # caso base

    minimo_restante = producto_minimo_precio(productos, i + 1)

    if productos[i]["precio"] <= minimo_restante["precio"]:
        return productos[i]
    else:
        return minimo_restante

def buscar_producto_minimo():
    """Busca el producto con el precio más bajo e imprime los datos."""
    productos = leer_productos()
    if len(productos) == 0:
        print("No hay productos cargados.")
        return None

    producto_min = producto_minimo_precio(productos)
    print(f"Producto con menor precio: {producto_min['nombre']} (${producto_min['precio']})")
    return producto_min["codigo"]