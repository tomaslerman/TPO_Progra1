
from .funciones_generales import buscar_id_json,mostrar_matriz_cuadro, mostrar_encabezado,mostrar_datos, extraer_encabezado_submenu, buscar_id, extraer_encabezado
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
            if opcion == 1:
                try:
                    agregar_productos(archivo)
                    input("Producto agregado exitosamente, presione Enter para continuar ...")
                except Exception as e:
                    print(f"Error al agregar producto: {e}")
                    input("Presione Enter para continuar...")
                    
            if opcion == 2:
                try:
                    modificar_productos(archivo)
                    input("Producto modificado exitosamente, presione Enter para continuar...")
                except Exception as e:
                    print(f"Error al modificar producto: {e}")
                    input("Presione Enter para continuar...")
            if opcion == 3:
                try:
                    dar_baja_productos(archivo)
                    input("Producto eliminado exitosamente ...")
                except Exception as e:
                    print(f"Error al dar de baja el producto: {e}")
                    input("Presione Enter para continuar...")    
            if opcion == 4:
                try:
                     mostrar_datos("producto.json","r")
                except ValueError:
                    print("Error al mostrar datos")
                    input("Presione Enter para continuar")
            if opcion == 5:
                try: 
                    detalle_medicamento(archivo)
                except ValueError:
                    print(" Error al mostrar detalles de medicamentos")        
            if opcion == -1:
                try:
                    from .menu_p import menu_principal
                    menu_principal()
                except ValueError:
                    print("Opcion fuera del rango")
                       
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
             

def agregar_productos(archivo):
    try:
        try:
            with open(archivo, "r", encoding="UTF-8") as arch:
                productos=json.load(arch)
                       
        except (FileNotFoundError, OSError):
            productos=[]  # si el archivo no existe, se creará más adelante
       
        print("\n--- Agregando producto ...")
        while True:
            try:
                cod=int(input("Ingrese el código del medicamento: "))
                pos,existe=buscar_id_json(archivo, cod)
                if existe :
                    print("Error! El código ya existe. Ingrese un código diferente.")
                else:
                    break
            except ValueError:
                print("Error! Debe ingresar un número entero para el código.")
        while True:
            try:
                producto = input("Ingrese el nombre del medicamento a agregar : ").strip().capitalize()
                pos,existe_prod=buscar_id_json(archivo, producto)
                if existe_prod :
                    print("Error! El nombre del medicamento ya existe. Ingrese un nombre diferente.")
                else:
                    break    
            except ValueError:
                print("Error! Debe ingresar un nombre válido para el medicamento.")    
                
        stock = input("Ingrese la cantidad en stock: ")
        precio = input("Ingrese el precio unitario: $")

        nuevo_producto={
            "codigo": cod,
            "nombre": producto,
            "stock": stock,
            "precio": precio
            }
        productos.append(nuevo_producto)

        print("Producto agregado .\n")

        # Ordenar por código antes de guardar
        productos.sort(key=lambda x: int(x["codigo"]))

        with open(archivo, "w", encoding="utf-8") as arch:
            json.dump(productos, arch, indent=4, ensure_ascii=False)   #ensure_ascii evita la codificacion de esos caracteres en formato unicode dentro del JSON 

        print("Archivo actualizado correctamente.\n")
    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as mensaje:
        print(" Error al abrir o escribir en el archivo:", mensaje)


def modificar_productos(archivo):
    try:
        with open(archivo, "r", encoding="UTF-8") as arch:
                productos=json.load(arch)
        print("\n--- Modificando producto ...")
        
        if not productos:
            print("No hay productos para modificar.")
            return
        
        while True:
            try:
                codigo_existe=int(input("Ingrese nuevo codigo del producto, si desea ver los datos presione 0: "))
                if codigo_existe==0:
                    mostrar_datos("producto.json","r")
                    continue
                break
            except ValueError:
                    print("Error! Debe ingresar numeros enteros")
        
        indice,producto_encontrado=buscar_id_json(archivo,codigo_existe)
        if indice == -1:
            print("El código no existe en el archivo.")
            return
             
        else:
             print(f"Producto encontrado puede continuar el proceso:")
        
        nuevo_codigo_ingresado=int(input(f"Ingrese el nuevo código del medicamento [{producto_encontrado['codigo']}]: "))
        nuevo_nombre = input(f"Ingrese el nuevo nombre del medicamento[{producto_encontrado['nombre']}]: ").strip().capitalize() 
        nuevo_stock = input(f"Ingrese el nuevo stock [{producto_encontrado['stock']}]: ")
        nuevo_precio = input(f"Ingrese el nuevo precio unitario [${producto_encontrado['precio']}]: $")
        
        if nuevo_codigo_ingresado:
            try:
                nuevo_cod_val=int(nuevo_codigo_ingresado)
                for p in productos:
                    if p!= producto_encontrado and int(p["codigo"]== nuevo_cod_val):
                        print("No puede repetir el codigo ingrese otro nuevamente:")
                        return
                producto_encontrado["codigo"] = nuevo_cod_val
            except ValueError:
                print("Codigo invalido se mantendra el anterior")
                
        if nuevo_nombre:
            try:
                producto_encontrado["nombre"] = nuevo_nombre
            except ValueError:
                print(" Nombre invalido se mantendra el nombre anterior")
        if nuevo_stock:
            try:
                producto_encontrado["stock"]=int(nuevo_stock)
            except ValueError:
                print("Stock invalido, se mantendra stock anterior.")
        if nuevo_precio:
            try:
                producto_encontrado["precio"]=int(nuevo_precio)
            except ValueError:
                print("Precio invalido se mantendra precio anterior.")   
        
        productos[indice] = producto_encontrado     
                   
        productos.sort(key=lambda x: int(x["codigo"]))
    
        # Guardar nuevamente en el archivo
        with open(archivo, "w", encoding="UTF-8") as arch:
            json.dump(productos, arch, indent=4, ensure_ascii=False)

        print("Producto modificado correctamente.\n")

    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as mensaje:
        print("Error al abrir o escribir en el archivo:", mensaje)
            
def dar_baja_productos(archivo): #### falta modificarrrr
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
            if codigo == "":
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
                arch.write(";".join(prod) + "\n")
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

def detalle_medicamento(archivo): ##### falta modificarrrrr
    encabezados_productos = extraer_encabezado("encabezados_productos")
    try:
        arch_productos = open("productos.txt", "r", encoding="utf-8")
        matriz_productos = [linea.strip().split(";") for linea in arch_productos]
    except FileNotFoundError:
        print("Error! El archivo de productos no existe.")
        return
    print("Listado de medicamentos:")
    print(mostrar_matriz_cuadro(encabezados_productos, matriz_productos))
    id_med = int(input("Ingrese ID del medicamento a saber su detalle: "))
    pos_id = buscar_id(archivo, id_med)

    while pos_id == -1:
        id_med = int(input("Error. Ingrese ID del medicamento a saber su detalle: "))
        pos_id = buscar_id(archivo, id_med)
    print("Medicamento seleccionado :",archivo[pos_id][1])
    if re.findall("zina$", archivo[pos_id][1].lower()):
        print("Medicamento antihistamínico de segunda generacion,uso para sintomas de alergias.") 
    elif re.findall("mol$", archivo[pos_id][1].lower()):
        print("Medicamento analgesico y antipiretico,uso para dolor leve a moderado y fiebre.")
    elif re.findall("eno$", archivo[pos_id][1].lower()):
        print("Medicamento reduce la inflamacion en tejidos. ")
    elif re.findall("zol$", archivo[pos_id][1].lower()):
        print("Medicamento para reducir la produccion de acido en el estomago.")
    elif re.findall("lina$", archivo[pos_id][1].lower()):
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