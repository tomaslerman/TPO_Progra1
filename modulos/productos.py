
from .funciones_generales import validar_mayor_que,buscar_id,mostrar_matriz_cuadro, mostrar_encabezado, validar_opcion
from .datos_de_prueba import encabezados_productos, encabezados_submenu_inventario
import re


def submenu_inventario():
    archivo = "producto.txt"
    while True:
        print("---" * 10)
        print("Submenú Inventario")
        print("---" * 10)
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Dar baja producto")
        print("4. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                try:
                    agregar_productos(archivo)
                    input("Producto agregado exitosamente . ...")
                except Exception as e:
                    print(f"Error al agregar producto: {e}")
                    input("Presione Enter para continuar...")
                    
            elif opcion == 2:
                try:
                    modificar_productos(archivo)
                    input("Producto modificado exitosamente. ...")
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
                print("Volviendo al menú principal...\n")
                break 
            else:
                print("Opción fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
             

def agregar_productos(archivo):
    try:
        # Leer los datos existentes
        productos = []
        try:
            with open(archivo, "r", encoding="utf-8") as arch:
                for linea in arch:
                    codigo, nombre, stock, precio = linea.strip().split(";")
                    productos.append([codigo, nombre, stock, precio])
        except FileNotFoundError:
            pass  # si el archivo no existe, se creará más adelante
        print("\n--- Agregar productos ---")
        print("Debe ingresar al menos un producto antes de salir.\n")

        agrego = False  # Bandera para saber si se ingresó al menos un producto
        while True:
            codigo = input("Ingrese el código del producto (Enter para terminar): ")
            if codigo == "":
                if agrego:
                    break
                else:
                    print("Debe ingresar al menos un producto.\n")
                    continue

            existe = False #validar si el codigo existe
            for p in productos:
                if p[0] == codigo:
                    existe = True
                    break
            if existe:
                print("El código ya existe. Ingrese  otro codigo.\n")
                continue

            producto = input("Ingrese el nombre del medicamento: ")
            stock = input("Ingrese la cantidad en stock: ")
            precio = input("Ingrese el precio unitario: $")

            productos.append([codigo, producto, stock, precio])
            agrego=True
            print("Producto agregado .\n")

        # Ordenar por código antes de guardar
        productos.sort(key=lambda x: int(x[0]))

        with open(archivo, "w", encoding="utf-8") as arch:
            for p in productos:
                arch.write(";".join(p) + "\n")

        print("Archivo actualizado correctamente.\n")
    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as mensaje:
        print(" Error al abrir o escribir en el archivo:", mensaje)

def modificar_productos(archivo):
    try:
        # Leer los productos existentes
        with open(archivo, "r", encoding="utf-8") as arch:
            productos = [linea.strip().split(";") for linea in arch]

        if not productos:
            print(" No hay productos en el archivo.\n")
            return

        codigo_modificar = input("Ingrese el código del producto a modificar: ")

        # Buscar producto con filter + lambda
        encontrados = list(filter(lambda p: p[0] == codigo_modificar, productos))

        if not encontrados:
            print(" Producto no encontrado.\n")
            return

        producto_actual = encontrados[0]
        print(f"Producto actual: Nombre: {producto_actual[1]}, Stock: {producto_actual[2]}, Precio: {producto_actual[3]}")

        nuevo_nombre = input("Ingrese nombre del producto (Enter para dejar igual): ")
        nuevo_stock = input(" Ingrese nuevo stock (Enter para dejar igual): ")
        nuevo_precio = input(" Ingrese nuevo precio (Enter para dejar igual): $")

        # Reemplazar valores solo si se ingresó dato nuevo
        producto_actual[1] = nuevo_nombre if nuevo_nombre != "" else producto_actual[1]
        producto_actual[2] = nuevo_stock if nuevo_stock != "" else producto_actual[2]
        producto_actual[3] = nuevo_precio if nuevo_precio != "" else producto_actual[3]

        # Reemplazar el producto modificado en la lista completa usando map + lambda
        productos = list(map(lambda p: producto_actual if p[0] == codigo_modificar else p, productos))

        # Ordenar por código
        productos.sort(key=lambda x: int(x[0]))

        # Guardar nuevamente en el archivo
        with open(archivo, "w", encoding="utf-8") as arch:
            for p in productos:
                arch.write(";".join(p) + "\n")

        print("Producto modificado correctamente.\n")

    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as mensaje:
        print("Error al abrir o escribir en el archivo:", mensaje)

            
def dar_baja_productos(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as arch:
            lineas = arch.readlines()
        productos=[linea.strip().split(";") for linea in lineas]
        while True:
            print("\n Lista actual de productos:")
            print("-"*50)
            for prod in productos:
                print(f"Código: {prod[0]}, Medicamento: {prod[1]}, Stock: {prod[2]}, Precio Unitario: ${prod[3]}")
                print("-"*50)
            codigo=input("\nIngrese el código del producto a dar de baja (o enter para terminar): ")
            if codigo == " ":
                break
            encontrado=False
            for prod in productos:
                if prod[0]== codigo:
                    encontrado=True
                    confirmar=input(f"¿Está seguro que desea dar de baja el producto {prod[1]}? (s/n): ")
                    if confirmar.lower() == 's':
                        productos.remove(prod)
                        print("Producto dado de baja correctamente.\n")
                    else:
                        print("Operación cancelada.\n")
                    break
            if not encontrado:
                print("Código no encontrado. Intente nuevamente.\n")
        with open(archivo, "w", encoding="utf-8") as arch:
            for prod in productos:
                arch.write(",".join(prod) + "\n")
        print("Todos los cambios han sido guardados.")
    except OSError as mensaje:
        print(f"Error al abrir o escribir en el archivo: ", mensaje)


def buscar_producto(archivo):
    
    codigo_buscar = input("Ingrese el código del producto a buscar: ")
    try:
        with open(archivo, "r", encoding="utf-8") as arch:
            encontrado = False
            for linea in arch:
                codigo, nombre, stock, precio = linea.strip().split(";")
                if codigo == codigo_buscar:
                    print(f" Encontrado: {nombre} | Stock: {stock} | Precio: ${precio}\n")
                    encontrado = True
                    break
            if not encontrado:
                print(" Producto no encontrado.\n")
    except FileNotFoundError:
        print(" El archivo no existe.\n")







def detalle_medicamento(matriz):
    print("Listado de medicamentos:")
    print(mostrar_matriz_cuadro(encabezados_productos, matriz_productos))
    id_med = int(input("Ingrese ID del medicamento a saber su detalle: "))
    pos_id = buscar_id(matriz, id_med)

    while pos_id == -1:
        id_med = int(input("Error. Ingrese ID del medicamento a saber su detalle: "))
        pos_id = buscar_id(matriz, id_med)
    print("Medicamento seleccionado :",matriz[pos_id][1])
    if re.findall("zina$", matriz[pos_id][1].lower()):
        print("Medicamento antihistamínico de segunda generacion,uso para sintomas de alergias.") 
    elif re.findall("mol$", matriz[pos_id][1].lower()):
        print("Medicamento analgesico y antipiretico,uso para dolor leve a moderado y fiebre.")
    elif re.findall("eno$", matriz[pos_id][1].lower()):
        print("Medicamento reduce la inflamacion en tejidos. ")
    elif re.findall("zol$", matriz[pos_id][1].lower()):
        print("Medicamento para reducir la produccion de acido en el estomago.")
    elif re.findall("lina$", matriz[pos_id][1].lower()):
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