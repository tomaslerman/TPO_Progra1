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
