from .funciones_generales import mostrar_matriz_cuadro, mostrar_encabezado,mostrar_datos, extraer_encabezado_submenu, buscar_id, extraer_encabezado, open_json_file
import re
import json

def submenu_inventario():
    opcion = 0
    encabezados_submenu_inventario = extraer_encabezado_submenu("inventario")
    archivo = "producto.json"
    while True:
        print("---" * 10)
        print("Submenú Inventario")
        print("---" * 10)
        mostrar_encabezado(encabezados_submenu_inventario)

        try:
            opcion = int(input("Seleccione una opción: "))
            while (opcion > 0 and opcion < 5) and opcion != -1:
                if opcion == 1:
                    try:
                        agregar_productos(archivo)
                        input("Producto agregado exitosamente, presione Enter para continuar ...")
                    except Exception as e:
                        print(f"Error al agregar producto: {e}")
                        input("Presione Enter para continuar...")
                        
                elif opcion == 2:
                    try:
                        modificar_productos(archivo)
                        input("Producto modificado exitosamente, presione Enter para continuar...")
                    except Exception as e:
                        print(f"Error al modificar producto: {e}")
                        input("Presione Enter para continuar...")
                elif opcion == 3:
                    try:
                        dar_baja_productos(archivo)
                        input("Producto eliminado exitosamente ...")
                    except Exception as e:
                        print(f"Error al dar de baja el producto: {e}")
                        input("Presione Enter para continuar...")    
                elif opcion == 4:
                    try:
                        mostrar_datos("producto.json","r")
                    except ValueError:
                        print("Error al mostrar datos")
                        input("Presione Enter para continuar")
                elif opcion == 5:
                    try: 
                        detalle_medicamento(archivo)
                    except ValueError:
                        print(" Error al mostrar detalles de medicamentos")
                print("---" * 10)
                print("Submenú Inventario")
                print("---" * 10)
                mostrar_encabezado(encabezados_submenu_inventario)   
                try:
                    opcion = int(input("Seleccione una opción: "))  
                except ValueError:
                    print("Error: Debe ingresar un número entero válido.")       
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
    enter = input("Presione Enter para volver al menu principal...")

def agregar_productos(archivo):
    productos = open_json_file(archivo)
    descripciones = [prod['nombre'] for prod in productos]
    id = len(productos) + 1
    try:
        nombre = input(str("Ingrese el nombre del producto: "))
    except ValueError:
        print(" Error: Ingrese un nombre válido.")
    if nombre in descripciones:
        existe_prod = True
        pos = descripciones.index(nombre) + 1
    while existe_prod:
        print(f'El producto ya existe en el inventario, id: {pos}')
        try:
            nombre = input(str("Ingrese el nombre del producto: "))
        except ValueError:
            print(" Error: Ingrese un nombre válido.")
        if nombre in descripciones:
            existe_prod = True
            pos = descripciones.index(nombre) + 1
    try:
        stock = int(input("Ingrese el stock del producto: "))
        if stock < 0:
            print(" Error: El stock no puede ser negativo.")
            return
    except ValueError:
        print(" Error: Ingrese un número válido para el stock.")
        return
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print(" Error: El precio no puede ser negativo.")
            return
    except ValueError:
        print(" Error: Ingrese un número válido para el precio.")
        return
    nuevo_producto = {
        "codigo": id,
        "nombre": nombre,
        "stock": stock,
        "precio": precio
    }
    productos.append(nuevo_producto)
    try:
        with open(archivo, "w", encoding="utf-8") as file:
            json.dump(productos, file, indent=4)
    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as mensaje:
        print(" Error al abrir o escribir en el archivo:", mensaje)

def modificar_productos(archivo):    
    productos = open_json_file(archivo)
    codigos = [prod['codigo'] for prod in productos]
    try:
        id_modificar = int(input("Ingrese el ID del producto a modificar: "))
    except ValueError:
        print(" Error: Ingrese un número válido para el ID.")
        return
    while id_modificar not in codigos:
        try:
            id_modificar = int(input("Error. Ingrese el ID del producto a modificar: "))
        except ValueError:
            print(" Error: Ingrese un número válido para el ID.")
            return
    pos_id = codigos.index(id_modificar)

    try:
        opcion_modificar = input("¿Qué desea modificar? (1. nombre/2. stock/3. precio): ")
    except ValueError:
        print(" Error: Ingrese una opción válida.")
        return
    if opcion_modificar == '1':
        try:
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            productos[pos_id]['nombre'] = nuevo_nombre
        except ValueError:
            print(" Error: Ingrese un nombre válido.")
    elif opcion_modificar == '2':
        try:
            nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
            productos[pos_id]['stock'] = nuevo_stock
        except ValueError:
            print(" Error: Ingrese un número válido para el stock.")
    elif opcion_modificar == '3':
        try:
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            productos[pos_id]['precio'] = nuevo_precio
        except ValueError:
            print(" Error: Ingrese un número válido para el precio.")
    try:
        with open(archivo, "w", encoding="utf-8") as file:
            json.dump(productos, file, indent=4)
    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as mensaje:
        print(" Error al abrir o escribir en el archivo:", mensaje)

def mostrar_datos(archivo, modo):
    try:
        with open(archivo, modo, encoding="UTF-8") as datos:
            productos = json.load(datos)
            print("\nLISTADO DE PRODUCTOS")
            print(f'{"ID":<10}{"Descripción":<30}{"Stock":<6}{"Precio":<10}')

            for prod in productos:
                print(f"{prod['codigo']:<10}{prod['nombre']:<30}{prod['stock']:<6}${prod['precio']:<10.2f}")

    except (FileNotFoundError, OSError) as error:
        print(f'Error! {error}')

def dar_baja_productos(archivo):
    productos = open_json_file(archivo)
    if not productos:
        print("No hay productos para dar de baja.")
        return
    print("\n Lista actual de productos:")
    print("-"*50)
    mostrar_datos(archivo, "r")
    print("-"*50)
    codigos = [prod['codigo'] for prod in productos]
    try:
        codigo = int(input("\nIngrese el código del producto a dar de baja (o 0 para cancelar): "))
        if codigo == 0:
                print("Operación cancelada.\n")
                return
    except ValueError:
        print("Código no válido. Intente nuevamente.\n")
    while codigo not in codigos:
        print("Código no encontrado. Intente nuevamente.\n")
        try:
            codigo = int(input("\nIngrese el código del producto a dar de baja (o 0 para cancelar): "))
            if codigo == 0:
                    print("Operación cancelada.\n")
                    return
        except ValueError:
            print("Código no válido. Intente nuevamente.\n")
    pos = codigos.index(codigo)
    try:
        confirmar=input(f"¿Está seguro que desea dar de baja el producto {productos[pos]['nombre']}? (s/n): ").lower()
    except ValueError:
        print(" Error: Ingresó una opción no válida. Volviendo al submenu.\n")
        return
    if confirmar == 's':
        productos.pop(pos)
        with open(archivo, "w", encoding="utf-8") as arch:
            json.dump(productos, arch, ensure_ascii=False, indent=4)
        print("Producto dado de baja correctamente.\n")
        print("Todos los cambios han sido guardados.")
    else:
        print("Operación cancelada.\n")

def buscar_producto(archivo):
    productos = open_json_file(archivo)
    try:
        id_buscar = int(input("Ingrese el ID del producto a buscar: "))
    except ValueError:
        print(" Error: Ingrese un número válido para el ID.")
        return
    codigos = [prod['codigo'] for prod in productos]
    pos_id = codigos.index(id_buscar) if id_buscar in codigos else -1
    while pos_id == -1:
        try:
            id_buscar = int(input("Error. Ingrese el ID del producto a buscar: "))
        except ValueError:
            print(" Error: Ingrese un número válido para el ID.")
            return
        pos_id = codigos.index(id_buscar) if id_buscar in codigos else -1
    print(f"Producto encontrado: ID: {productos[pos_id]['codigo']}, Nombre: {productos[pos_id]['nombre']}, Stock: {productos[pos_id]['stock']}, Precio: ${productos[pos_id]['precio']:.2f}")

def detalle_medicamento(archivo):
    try:
        arch_productos = open_json_file(archivo)
        matriz_productos = [linea.strip().split(";") for linea in arch_productos]
        codigos = [int(prod['codigo']) for prod in arch_productos]
    except FileNotFoundError:
        print("Error! El archivo de productos no existe.")
        return
    print("")
    print("Listado de medicamentos:")
    mostrar_datos(archivo, "r")
    print("")
    try:
        id_med = int(input("Ingrese ID del medicamento a saber su detalle: "))
    except ValueError:
        print("Error: Ingrese un número válido para el ID.")
        return
    pos_id = codigos.index(id_med) if id_med in codigos else -1

    while pos_id == -1:
        
        id_med = int(input("Error. Ingrese ID del medicamento a saber su detalle: "))
        pos_id = codigos.index(id_med) if id_med in codigos else -1
    print("Medicamento seleccionado :",arch_productos[pos_id][1])
    if re.findall("zina$", arch_productos[pos_id][1].lower()):
        print("Medicamento antihistamínico de segunda generacion,uso para sintomas de alergias.")
    elif re.findall("mol$", arch_productos[pos_id][1].lower()):
        print("Medicamento analgesico y antipiretico,uso para dolor leve a moderado y fiebre.")
    elif re.findall("eno$", arch_productos[pos_id][1].lower()):
        print("Medicamento reduce la inflamacion en tejidos. ")
    elif re.findall("zol$", arch_productos[pos_id][1].lower()):
        print("Medicamento para reducir la produccion de acido en el estomago.")
    elif re.findall("lina$", arch_productos[pos_id][1].lower()):
        print("Medicamento para tratar infecciones bacterianas.")
    else:
        print("No se puede saber especificamente su tipo")

def stock_por_agotar(matriz_productos):
    productos_agotarse=[fila for fila in matriz_productos if (fila[2])<=2]
    ordenar_stock=sorted(productos_agotarse,key=lambda fila: (fila[2]))
    print("Productos de stock proximos a agotarse :")
    print(f"{'ID':<5} {'Descripcion':<10}    {'Stock':<10}   {'Precio_Unitario':<10}")
    for p in ordenar_stock:
        print(f"{p[0]:<5} {p[1]:<10}      {p[2]:<10}       {p[3]:<10}  ")