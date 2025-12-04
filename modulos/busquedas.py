from .funciones_generales import buscar_id, mostrar_encabezado, extraer_encabezado_busquedas
from functools import reduce
import json
def submenu_busquedas():
   
    encabezados_submenu_busquedas = extraer_encabezado_busquedas("busquedas")
    opcion = 0
    while opcion != -1:
        print("---" * 10)
        print("Submenú Búsquedas")
        print("---" * 10)
        mostrar_encabezado(encabezados_submenu_busquedas)
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error! Opción inválida.")
            continue
        while opcion not in [1, 2, -1]:
            print("Error! Opción inválida.")
            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Error! Opción inválida.")
                opcion = 0 
                continue

        if opcion == 1:
            try:
                id_cliente = int(input("Ingrese el ID del cliente: "))
            except ValueError:
                print("Error! Debe ingresar un número entero.")
                continue
            ventas_de_x_cliente(id_cliente)
            input("Presione Enter para continuar...")
        elif opcion == 2:
            try:
                id_producto = int(input("Ingrese el ID del producto: "))
            except ValueError:
                print("Error! Debe ingresar un número entero.")
                continue
            ventas_de_x_producto(id_producto)
            input("Presione Enter para continuar...")
    input("Volviendo al menú principal...")

def ventas_de_x_producto(id_producto):

    try:
        with open("productos.json", "r", encoding="utf-8") as archivo:
            diccionario_productos = json.load(archivo)
    except FileNotFoundError:
        print("Error! El archivo de productos no existe.")
        diccionario_productos = {}
    key_producto = str(id_producto)
    if key_producto in diccionario_productos:
        info = diccionario_productos[key_producto]
        print(f"Ventas del producto {info['descripcion']} (ID {id_producto}):")
    else:
        print("Error! El ID del producto es inválido.")
        return 

    matriz_detalle_ventas = []
    try:
        with open("detalle_ventas.txt", "r", encoding="utf-8") as arch_detalle_ventas:
            matriz_detalle_ventas = [linea.strip().split(";") for linea in arch_detalle_ventas if linea.strip()]
    except FileNotFoundError:
        print("Error! El archivo de detalle de ventas no existe.")
        return

    ventas_producto = [detalle for detalle in matriz_detalle_ventas if detalle[1] == str(id_producto)]
    
    if not ventas_producto:
        print("No hay ventas registradas para este producto.")
        return

    print(f"{'ID Venta':<10}{'ID Receta':<10}{'Subtotal':<10}")
    
    for detalle in ventas_producto:
        try:
            print(f"{int(detalle[0]):<10}{detalle[1]:<10}${float(detalle[2]):<10.2f}")
        except (ValueError, IndexError):
            print("Error en el formato de una línea de detalle de ventas.")

def ventas_de_x_cliente(id_cliente):
    id_cliente_str = str(id_cliente)

    try:
        with open("ventas.txt", "r", encoding="utf-8") as f:
            ventas = [
                l.strip().split(";")
                for l in f
                if l.strip()
            ]
    except FileNotFoundError:
        print("Error! El archivo de ventas no existe.")
        return

    try:
        ventas_dict = list(
            map(
                lambda v: {
                    "id_venta": v[0],
                    "fecha": v[1],
                    "id_cliente": v[2],
                    "total": float(v[3])
                },
                ventas
            )
        )
    except (IndexError, ValueError):
        print("Error en el formato de alguna línea del archivo de ventas.")
        return

    ventas_cliente = list(filter(lambda v: v["id_cliente"] == id_cliente_str, ventas_dict))

    if not ventas_cliente:
        print(f"No hay ventas registradas para el cliente {id_cliente}.")
        return

    montos = list(map(lambda v: v["total"], ventas_cliente))
    total_gastado = reduce(lambda acc, x: acc + x, montos, 0)

    ultimas3 = ventas_cliente[-3:]

    print(f"Cliente {id_cliente} gastó un total de: ${total_gastado:.2f}")
    print("Últimas 3 ventas:")
    for v in ultimas3:
        print(f"ID: {v['id_venta']} | Fecha: {v['fecha']} | Total: ${v['total']:.2f}")
