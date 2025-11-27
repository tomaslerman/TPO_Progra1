from .funciones_generales import fechaYvalidacion, extraer_encabezado_submenu, mostrar_encabezado, validar_opcion, open_json_file, leer_productos 
import json
from functools import reduce

def submenu_reportes():
    opcion = 0
    encabezados_sub_menu_reportes = extraer_encabezado_submenu("reportes")
    while opcion != -1:
        print("---"* 10)
        print("Submenú Reportes")
        print("---"* 10)
        mostrar_encabezado(encabezados_sub_menu_reportes)
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue

        opcion = validar_opcion(opcion, 1, 5, encabezados_sub_menu_reportes)
        if opcion == 1:
            estadisticas_ventas() 
            input("Presione Enter para continuar...")
        elif opcion == 2:
            cant_cl_ac = total_clientes_activos()
            print(f"La cantidad de clientes activos actualmente es {cant_cl_ac}")
            input("Presione Enter para continuar...")
        elif opcion == 3:
            tot_gastado = total_gastado_por_cliente()
            input("Presione Enter para continuar...")
        elif opcion == 4:
            buscar_producto_minimo()
            input("Presione Enter para continuar...")
        elif opcion == 5:
            fecha_a_buscar = fechaYvalidacion()
            total_dia = total_ventas_por_fecha(fecha_a_buscar)
            input("Presione Enter para continuar...")
    input("Volviendo a menu...")

def estadisticas_ventas():
    try:
        with open("ventas.txt", "r", encoding="utf-8") as archivo:
            total_ventas = 0
            suma_total = 0.0

            for linea in archivo:
                partes = linea.strip().split(";")
                if len(partes) != 4:
                    continue
                try:
                    total = float(partes[3])
                except ValueError:
                    continue

                total_ventas += 1
                suma_total += total

    except FileNotFoundError:
        print("Error: no se encontró el archivo ventas.txt.")
        return
    except OSError:
        print("Error al abrir ventas.txt.")
        return

    promedio = suma_total / total_ventas if total_ventas > 0 else 0
    print(f"Cantidad de ventas: {total_ventas}")
    print(f"Total vendido: ${suma_total:.2f}")
    print(f"Promedio por venta: ${promedio:.2f}")

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


def sumar_totales_cliente(arch, id_cliente):
    total_cliente = 0.0
    for linea in arch:
        partes = linea.strip().split(";")
        if len(partes) != 4:
            continue

        try:
            id_cli = int(partes[2])
            total  = float(partes[3])
        except ValueError:
            continue

        if id_cli == id_cliente:
            total_cliente += total

    return total_cliente

def total_gastado_por_cliente():
    clientes = open_json_file("clientes.json")
    if not clientes:
        print("No hay clientes cargados.")
        return

    while True:
        id_ing = input("Ingrese el ID del cliente: ")
        if id_ing.isdigit():
            id_cliente = int(id_ing)
            break
        print("Error: debe ingresar un número entero.")

    cliente = clientes.get(str(id_cliente))
    if cliente is None:
        print("El cliente no existe.")
        return

    if str(cliente.get("estado", "")).lower() != "active":
        print(f"El cliente {cliente.get('nombre','')} está inactivo. No tiene ventas activas.")
        return

    try:
        with open("ventas.txt", "r", encoding="utf-8") as arch:
            total = sumar_totales_cliente(arch, id_cliente)
    except FileNotFoundError:
        print("Error: no se encontró el archivo ventas.txt.")
        return
    except OSError:
        print("Error al abrir ventas.txt.")
        return

    print(f"El cliente {cliente['nombre']} gastó un total de: ${total:.2f}")
    return total

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

def total_ventas_por_fecha(fecha_busqueda):
    """
    Devuelve el total de las ventas realizadas en una fecha determinada,
    usando reduce() para sumar los totales directamente desde el archivo.
    """
    try:
        with open("ventas.txt", "r", encoding="utf-8") as archivo:
            totales = []
            for linea in archivo:
                partes = linea.strip().split(";")
                if len(partes) == 4 and partes[1] == fecha_busqueda:
                    try:
                        total = float(partes[3])
                        totales.append(total)
                    except ValueError:
                        continue  

        if len(totales) == 0:
            print(f"No hay ventas registradas para la fecha {fecha_busqueda}.")
            return 0

        total_final = reduce(lambda x, y: x + y, totales)
        print(f"Total de ventas del día {fecha_busqueda}: ${total_final:.2f}")
        return total_final

    except FileNotFoundError:
        print("Error: no se encontró el archivo ventas.txt.")
        return 0
