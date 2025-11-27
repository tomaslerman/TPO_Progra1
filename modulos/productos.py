from .funciones_generales import mostrar_encabezado, mostrar_datos, extraer_encabezado_submenu, open_json_file, validar_opcion
import re
import json

def submenu_inventario():
    encabezados = extraer_encabezado_submenu("inventario")
    opcion = 0
    while opcion != -1:
        print("---" * 10)
        print("Submenú Inventario")
        print("---" * 10)
        mostrar_encabezado(encabezados)
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue

        opcion = validar_opcion(opcion, 1, 5, encabezados)
        if opcion == 1:  # Agregar producto
            agregar_productos('productos.json')
            input("Volviendo a menu...")
        elif opcion == 2:  # Modificar producto
            modificar_productos('productos.json')
            input("Volviendo a menu...")
        elif opcion == 3:  # Dar baja producto
            dar_baja_productos('productos.json')
            input("Volviendo a menu...")
        elif opcion == 4:  # Mostrar lista completa
            mostrar_datos('productos.json')
            input("Volviendo a menu...")
        elif opcion == 5:
            detalle_medicamento('productos.json')
            input("Volviendo a menu...")
    input("Volviendo al menú principal...")


def agregar_productos(archivo):
    productos = open_json_file(archivo)

    print("\nProductos actuales:")
    for id_prod, datos in productos.items():
        print(f"{id_prod}. {datos['descripcion']} (Stock: {datos['stock']}, Precio: ${datos['precio']})")

    if productos:
        id_nuevo = int(max(productos.keys(), key=int)) + 1
    else:
        id_nuevo = 1

    descripciones_existentes = [datos["descripcion"].strip().lower() for datos in productos.values()]
    while True:
        nombre = input("\nIngrese el nombre del producto: ").strip()
        if not nombre:
            print("Error: el nombre no puede estar vacío.")
            continue

        if nombre.lower() in descripciones_existentes:
            for id_prod, datos in productos.items():
                if datos["descripcion"].strip().lower() == nombre.lower():
                    print(f"El producto '{nombre}' ya existe (ID {id_prod}).")
                    break
        else:
            break

    while True:
        try:
            stock = int(input("Ingrese el stock del producto: "))
            if stock < 0:
                print("Error: el stock no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Error: debe ingresar un número entero válido.")

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("Error: el precio no puede ser negativo.")
            else:
                break
        except ValueError:
            print("Error: debe ingresar un número válido para el precio.")

    productos[str(id_nuevo)] = {
        "descripcion": nombre,
        "stock": stock,
        "precio": precio
    }

    try:
        with open(archivo, "w", encoding="utf-8") as file:
            json.dump(productos, file, indent=4, ensure_ascii=False)
        print(f"\nProducto '{nombre}' agregado correctamente (ID {id_nuevo}).")
    except OSError as e:
        print("Error al escribir en el archivo:", e)

def modificar_productos(archivo):
    productos = open_json_file(archivo)

    if not productos:
        print("No hay productos cargados.")
        return

    print("\nLISTADO DE PRODUCTOS:")
    print(f'{"ID":<6}{"Descripción":<25}{"Stock":<8}{"Precio":<10}')
    for id_prod, datos in productos.items():
        print(f'{id_prod:<6}{datos["descripcion"]:<25}{datos["stock"]:<8}{datos["precio"]:<10.2f}')

    id_modificar = input("\nIngrese el ID del producto a modificar: ").strip()
    if id_modificar not in productos:
        print("Error: El ID ingresado no existe.")
        return

    print("\n¿Qué desea modificar?")
    print("1. Descripción")
    print("2. Stock")
    print("3. Precio")
    opcion = input("Seleccione una opción (1/2/3): ").strip()

    if opcion == "1":
        nuevo_nombre = input("Ingrese la nueva descripción: ").strip()
        if nuevo_nombre:
            productos[id_modificar]["descripcion"] = nuevo_nombre
            print("Descripción actualizada.")
        else:
            print("Error: descripción no válida.")
            return

    elif opcion == "2":
        try:
            nuevo_stock = int(input("Ingrese el nuevo stock: "))
            if nuevo_stock >= 0:
                productos[id_modificar]["stock"] = nuevo_stock
                print("Stock actualizado.")
            else:
                print("Error: el stock no puede ser negativo.")
        except ValueError:
            print("Error: debe ingresar un número entero.")
            return

    elif opcion == "3":
        try:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            if nuevo_precio >= 0:
                productos[id_modificar]["precio"] = nuevo_precio
                print("Precio actualizado.")
            else:
                print("Error: el precio no puede ser negativo.")
        except ValueError:
            print("Error: debe ingresar un número válido.")
            return

    else:
        print("Opción no válida.")
        return

    try:
        with open(archivo, "w", encoding="utf-8") as file:
            json.dump(productos, file, indent=4, ensure_ascii=False)
            print("Cambios guardados correctamente.")
    except OSError as e:
        print(f"Error al escribir en el archivo: {e}")


def dar_baja_productos(archivo):
    productos = open_json_file(archivo)
    if not productos:
        print("No hay productos para dar de baja.")
        return

    print("\nLista actual de productos:")
    print("-" * 50)
    mostrar_datos(archivo)
    print("-" * 50)

    codigo = input("\nIngrese el ID del producto a dar de baja (o 0 para cancelar): ").strip()
    if codigo == "0":
        print("Operación cancelada.\n")
        return
    if codigo not in productos:
        print("Código no encontrado. Intente nuevamente.\n")
        return

    confirmar = input(
        f"¿Está seguro que desea dar de baja el producto '{productos[codigo]['descripcion']}'? (s/n): "
    ).lower()
    if confirmar == 's':
        productos.pop(codigo)
        try:
            with open(archivo, "w", encoding="utf-8") as arch:
                json.dump(productos, arch, ensure_ascii=False, indent=4)
            print("Producto dado de baja correctamente.\nTodos los cambios han sido guardados.")
        except OSError as e:
            print("Error al escribir en el archivo:", e)
    else:
        print("Operación cancelada.\n")


def buscar_producto(archivo):
    productos = open_json_file(archivo)
    if not productos:
        print("No hay productos registrados.")
        return

    id_buscar = input("Ingrese el ID del producto a buscar: ").strip()

    if id_buscar not in productos:
        print("Error: El ID ingresado no existe.")
        return

    prod = productos[id_buscar]
    print(
        f"Producto encontrado: ID: {id_buscar}, "
        f"Descripción: {prod['descripcion']}, "
        f"Stock: {prod['stock']}, "
        f"Precio: ${prod['precio']:.2f}"
    )


def detalle_medicamento(archivo):
    productos = open_json_file(archivo)
    if not productos:
        print("No hay productos cargados.")
        return

    print("\nListado de medicamentos:")
    mostrar_datos(archivo)
    print("")

    id_med = input("Ingrese ID del medicamento para ver su detalle: ").strip()

    if id_med not in productos:
        print("Error: ID no encontrado.")
        return

    descripcion = productos[id_med]["descripcion"]
    print(f"Medicamento seleccionado: {descripcion}")

    desc_lower = descripcion.lower()
    if re.findall("zina$", desc_lower):
        print("Medicamento antihistamínico de segunda generación, usado para síntomas de alergia.")
    elif re.findall("mol$", desc_lower):
        print("Medicamento analgésico y antipirético, usado para dolor leve a moderado y fiebre.")
    elif re.findall("eno$", desc_lower):
        print("Medicamento que reduce la inflamación en tejidos.")
    elif re.findall("zol$", desc_lower):
        print("Medicamento que reduce la producción de ácido en el estómago.")
    elif re.findall("lina$", desc_lower):
        print("Medicamento utilizado para tratar infecciones bacterianas.")
    else:
        print("No se puede determinar específicamente su tipo.")


def stock_por_agotar(archivo):
    productos = open_json_file(archivo)
    if not productos:
        print("No hay productos registrados.")
        return

    productos_agotarse = [
        (id_prod, datos['descripcion'], datos['stock'], datos['precio'])
        for id_prod, datos in productos.items()
        if datos['stock'] <= 2
    ]

    if not productos_agotarse:
        print("No hay productos con stock bajo.")
        return

    ordenar_stock = sorted(productos_agotarse, key=lambda p: p[2])

    print("\nProductos próximos a agotarse:")
    print(f"{'ID':<5} {'Descripción':<20} {'Stock':<10} {'Precio Unitario':<15}")
    for p in ordenar_stock:
        print(f"{p[0]:<5} {p[1]:<20} {p[2]:<10} ${p[3]:<15.2f}")
