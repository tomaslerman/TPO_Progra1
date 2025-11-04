from .funciones_generales import mostrar_encabezado, validar_opcion, leer_ventas, fechaYvalidacion, buscar_id, open_json_file, extraer_encabezado_submenu
from .datos_de_prueba import *
from .recetas import agregar_receta
import json

def submenu_ventas():
    encabezados = extraer_encabezado_submenu("ventas")
    opcion = 0
    while opcion != -1:
        print("---"* 10)
        print("Submenú Ventas")
        print("---"* 10)
        mostrar_encabezado(encabezados)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados)
        if opcion == 1:  # Agregar venta
            agregar_venta_y_detalle()
            enter = input("Volviendo a menu...")
        elif opcion == 2:  # Modificar detalle de venta
            modificar_venta()
            enter = input("Volviendo a menu...")
        elif opcion == 3:  # Dar baja venta
            dar_baja_ventas()
            enter = input("Volviendo a menu...")
        elif opcion == 4:  # Mostrar lista completa
            leer_ventas()
            enter = input("Presione Enter para continuar...")
           # mostrar_matriz(encabezados_ventas, matriz_ventas)
    enter = input("Volviendo al menú principal...")

def agregar_venta_y_detalle():
    matriz_clientes = open_json_file('clientes.json')

    try:
        with open('ventas.txt', 'r', encoding='utf-8') as archivo_ventas:
            lineas = archivo_ventas.readlines()
            if lineas:
                ultimo_id = int(lineas[-1].split(';')[0])
            else:
                ultimo_id = 0
    except(FileNotFoundError,OSError) as error:
        print(f"Error{error}")
        return
    id_venta = ultimo_id + 1
    fecha = fechaYvalidacion()
    id_cliente = int(input("Ingrese el ID del cliente: "))
    pos = -1
    while pos == -1:
        for key in matriz_clientes:
            if int(key) == id_cliente:
                pos = key
        if pos == -1:
            print("Error! El ID del cliente es inválido.")
            id_cliente = int(input("Ingrese el ID del cliente: "))
    print("")
    print("Ingresando a detalle de venta...")
    input("Presione Enter para continuar...")
    print("")
    total = agregar_detalle_de_venta(id_cliente, id_venta)
    total = float(total)
    print(f'Subtotal de la venta: ${total}')
    descuento = buscar_descuento_obra_social(id_cliente)
    print(f"Descuento aplicado: {descuento}%")
    total2 = aplicar_descuento(total, descuento)
    print(f"Total de la venta: ${total2}")
    venta = [id_venta, fecha, id_cliente, total2]
    try:
        with open('ventas.txt', 'a', encoding='utf-8') as archivo_ventas:
            archivo_ventas.write(f"{venta[0]};{venta[1]};{venta[2]};{venta[3]}\n")
    except(FileNotFoundError,OSError) as error:
        print(f"Error{error}")

def agregar_detalle_de_venta(id_cliente, id_venta):
    matriz_productos = open_json_file('producto.json')
    total = 0

    try:
        producto = int(input("Ingrese el código del producto: "))
    except ValueError:
        print("Error! Debe ingresar un número válido.")
        producto = -1

    if [lambda p: p["codigo"] == producto for p in matriz_productos]:
        producto_encontrado = True
    else:
        producto_encontrado = False

    while (producto != -1) and not producto_encontrado:
        print("Error! El código del producto es inválido.")
        try:
            producto = int(input("Ingrese nuevamente el código del producto o -1 para dejar de agregar productos: "))
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            producto = -1
        if [lambda p: p["codigo"] == producto for p in matriz_productos]:
            producto_encontrado = True
        else:
            producto_encontrado = False

    while producto != -1:
        producto_actual = None
        for p in matriz_productos:
            if p["codigo"] == producto:
                producto_actual = p
                break

        if producto_actual is None:
            print("Error! El código del producto no existe.")
            break
        receta = input("¿El cliente tiene receta? (s/n): ").lower()
        while receta not in ['s', 'n']:
            print("Error! Opción inválida.")
            receta = input("¿El cliente tiene receta? (s/n): ").lower()

        if receta == 's':
            id_receta, cantidad = agregar_receta(id_cliente, matriz_productos)
            subtotal = producto_actual["precio"] * cantidad
            detalle_venta = [id_venta, id_receta, subtotal]
            try:
                with open('detalle_ventas.txt', 'a', encoding='utf-8') as archivo_detalle:
                    archivo_detalle.write(f"{detalle_venta[0]};{detalle_venta[1]};{detalle_venta[2]}\n")
            except(FileNotFoundError,OSError) as error:
                print(f"Error{error}")
            total += subtotal
        else:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                cantidad = 0

            while cantidad > producto_actual["stock"]:
                print(f"Error! Sólo hay {producto_actual['stock']} unidades disponibles.")
                try:
                    cantidad = int(input("Vuelva a ingresar la cantidad del producto: "))
                except ValueError:
                    print("Error! Debe ingresar un número válido.")
                    cantidad = 0
            subtotal = producto_actual["precio"] * cantidad
            detalle_venta = [id_venta, "VL", subtotal]
            try:
                with open('detalle_ventas.txt', 'a', encoding='utf-8') as archivo_detalle:
                    archivo_detalle.write(f"{detalle_venta[0]};{detalle_venta[1]};{detalle_venta[2]}\n")
            except(FileNotFoundError,OSError) as error:
                print(f"Error{error}")
            total += subtotal
        try:
            producto = int(input("Ingrese el código del producto o -1 para dejar de agregar productos: "))
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            producto = -1

        if [lambda p: p["codigo"] == producto for p in matriz_productos]:
            producto_encontrado = True
        else:
            producto_encontrado = False
            
        while (producto != -1) and not producto_encontrado:
            print("Error! El código del producto es inválido.")
            try:
                producto = int(input("Ingrese nuevamente el código del producto o -1 para dejar de agregar productos: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                producto = -1
            if [lambda p: p["codigo"] == producto for p in matriz_productos]:
                producto_encontrado = True
            else:
                producto_encontrado = False
    return total

def buscar_descuento_obra_social(id_cliente):
    matriz_clientes = open_json_file('clientes.json')
    matriz_obras_sociales = open_json_file('obras_sociales.json')
    id_cliente_str = str(id_cliente)

    if id_cliente_str in matriz_clientes:
        id_obra_social = str(matriz_clientes[id_cliente_str].get("obra_social"))
        if id_obra_social in matriz_obras_sociales:
            descuento = matriz_obras_sociales[id_obra_social].get("descuento", 0)
            return descuento
    return 0

def aplicar_descuento(total, descuento):
    total2 = total - (total * (descuento / 100)) if descuento else total
    if descuento:
        print(f"Descuento del {descuento}%. Total con descuento: ${total2}")
    return total2

def modificar_venta():
    matriz_clientes = open_json_file('clientes.json')
    matriz_productos = open_json_file('producto.json')
    matriz_codigos_ventas = []
    try:
        with open('ventas.txt', 'r', encoding='utf-8') as archivo_ventas:
            for linea in archivo_ventas:
                codigo_venta = int(linea.split(';')[0])
                matriz_codigos_ventas.append(codigo_venta)
    except (FileNotFoundError, OSError) as error:
        print(f"Error: {error}")

    try:
        id_venta = int(input("Ingrese el ID de la venta a modificar: "))
    except ValueError:
        print("Error! Debe ingresar un número válido.")
        return

    while id_venta not in matriz_codigos_ventas:
        print("El ID de la venta es inválido")
        try:
            id_venta = int(input("Vuelva a ingresar el ID de la venta: "))
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            return
    
    pos = matriz_codigos_ventas.index(id_venta)
    try:
        with open('ventas.txt', 'r', encoding='utf-8') as archivo_ventas:
            lineas = archivo_ventas.readlines()
            venta_linea = lineas[pos]
            venta_datos = venta_linea.strip().split(';')
            print("Datos actuales de la venta:")
            print(f"ID Venta: {venta_datos[0]}")
            print(f"Fecha: {venta_datos[1]}")
            print(f"ID Cliente: {venta_datos[2]}")
            print(f"Total: {venta_datos[3]}")
    except (FileNotFoundError, OSError) as error:
        print(f"Error: {error}")
        return
    try:
        with open('detalle_ventas.txt', 'r', encoding='utf-8') as archivo_detalle:
            lineas_detalle = archivo_detalle.readlines()
            for linea in lineas_detalle:
                detalle_datos = linea.strip().split(';')
                if int(detalle_datos[0]) == id_venta:
                    print("Detalle de la venta:")
                    print(f"ID Detalle: {detalle_datos[0]}")
                    print(f"ID Receta/Venta Libre: {detalle_datos[1]}")
                    print(f"Subtotal: {detalle_datos[2]}")
                else:
                    detalle_datos = None
    except (FileNotFoundError, OSError) as error:
        print(f"Error: {error}")
        return

    print("")
    print("¿Qué desea modificar?")
    for k, v in opciones_modificacion_ventas.items():
        print(f"{k}. {v}")
    try:
        modificacion = int(input("Seleccione una opción (1, 2 o 3): "))
    except ValueError:
        print("Error! Debe ingresar un número válido.")
        return

    if modificacion == 1:
        nueva_fecha = fechaYvalidacion()
        try:
            with open('ventas.txt', 'r', encoding='utf-8') as archivo_ventas:
                lineas = archivo_ventas.readlines()
            venta_datos[1] = nueva_fecha
            lineas[pos] = ';'.join(venta_datos) + '\n'
            with open('ventas.txt', 'w', encoding='utf-8') as archivo_ventas:
                archivo_ventas.writelines(lineas)
        except (FileNotFoundError, OSError) as error:
            print(f"Error: {error}")
            return
        print("Fecha actualizada correctamente.")

    elif modificacion == 2:
        try:
            nuevo_cliente = int(input("Ingrese el nuevo ID del cliente: "))
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            return
        while nuevo_cliente not in matriz_clientes:
            print("Error! El ID del cliente es inválido.")
            try:
                nuevo_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return
        try:
            with open('ventas.txt', 'r', encoding='utf-8') as archivo_ventas:
                lineas = archivo_ventas.readlines()
            venta_datos[2] = str(nuevo_cliente)
            lineas[pos] = ';'.join(venta_datos) + '\n'
            with open('ventas.txt', 'w', encoding='utf-8') as archivo_ventas:
                archivo_ventas.writelines(lineas)
        except (FileNotFoundError, OSError) as error:
            print(f"Error: {error}")
            return
        print("ID del cliente actualizado correctamente.")
    
    elif modificacion == 3:
        id_cliente = int(venta_datos[2])
        print("¿Desea modificar la receta o venta libre?")
        tipo = int(input("Ingrese 1 para receta o 2 para venta libre: "))

        if tipo == 1:
            try:
                id_producto = int(input("Ingrese el código del producto a modificar en la receta: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return
            
            producto_encontrado = False
            for producto in matriz_productos:
                if producto["codigo"] == id_producto:
                    producto_encontrado = True
                    producto_actual = producto
                    break
            while not producto_encontrado:
                print("Error! El código del producto es inválido.")
                try:
                    id_producto = int(input("Vuelva a ingresar el código del producto: "))
                except ValueError:
                    print("Error! Debe ingresar un número válido.")
                    return
                for producto in matriz_productos:
                    if producto["codigo"] == id_producto:
                        producto_encontrado = True
                        producto_actual = producto
                        break
            
            id_receta, cantidad = agregar_receta(id_cliente, matriz_productos)
            subtotal = producto_actual["precio"] * cantidad
            try:
                with open('detalle_ventas.txt', 'r', encoding='utf-8') as archivo_detalle:
                    lineas = archivo_detalle.readlines()
                for i in range(len(lineas)):
                    detalle_datos = lineas[i].strip().split(';')
                    if int(detalle_datos[0]) == id_venta:
                        detalle_datos[1] = str(id_receta)
                        detalle_datos[2] = str(subtotal)
                        lineas[i] = ';'.join(detalle_datos) + '\n'
                        break
                with open('detalle_ventas.txt', 'w', encoding='utf-8') as archivo_detalle:
                    archivo_detalle.writelines(lineas)
            except (FileNotFoundError, OSError) as error:
                print(f"Error: {error}")
                return
            
            descuento = buscar_descuento_obra_social(id_cliente)
            total2 = aplicar_descuento(subtotal, descuento)
            try:
                with open('ventas.txt', 'r', encoding='utf-8') as archivo_ventas:
                    lineas = archivo_ventas.readlines()
                venta_datos[3] = str(total2)
                lineas[pos] = ';'.join(venta_datos) + '\n'
                with open('ventas.txt', 'w', encoding='utf-8') as archivo_ventas:
                    archivo_ventas.writelines(lineas)
            except (FileNotFoundError, OSError) as error:
                print(f"Error: {error}")
                return
            print("Detalle de venta modificado correctamente.")
        
        elif tipo == 2:
            if detalle_datos is None:
                print("No se encontró el detalle de venta para modificar.")
                respuesta = input("Desea agregar un nuevo detalle de venta? (s/n)").lower()
                if respuesta == 's':
                    agregar_detalle_de_venta(id_cliente, id_venta)
                else:
                    print("Operación cancelada.")
                    return
            else:
                if detalle_datos[1] != "VL":
                    try:
                        with open('detalle_ventas.txt', 'w', encoding='utf-8') as archivo_detalle:
                            for linea in archivo_detalle:
                                detalle_datos = linea.strip().split(';')
                                if int(detalle_datos[0]) == id_venta:
                                    print("El detalle actual no es de venta libre.")
                                    respuesta = input("Desea cambiar a venta libre? (s/n)").lower()
                                    if respuesta == 's':
                                        detalle_datos[1] = "VL"
                                        try:
                                            cantidad = int(input("Ingrese la cantidad del producto: "))
                                        except ValueError:
                                            print("Error! Debe ingresar un número válido.")
                                            return
                                    else:
                                        print("Operación cancelada.")
                                        return
                    except (FileNotFoundError, OSError) as error:
                        print(f"Error: {error}")
                        return
                    try:
                        with open('recetas.json', 'w', encoding='utf-8') as archivo_recetas:
                            recetas = json.load(archivo_recetas)
                            recetas.pop(detalle_datos[1], None)
                            json.dump(recetas, archivo_recetas, ensure_ascii=False, indent=4)
                    except (FileNotFoundError, OSError) as error:
                        print(f"Error: {error}")
                        return
    else:
        print("Opción de modificación inválida.")

def dar_baja_ventas():
    id_venta = int(input("Ingrese el ID: "))
    pos = -1

    while pos==-1:
        try:
            with open('ventas.txt', 'r', encoding='utf-8') as archivo_ventas:
                for linea in archivo_ventas:
                    partes = linea.strip().split(';')
                    id_venta_linea = partes[0] 
                    if id_venta_linea == str(id_venta):
                        pos = 0
        except(FileNotFoundError,OSError) as error:
            print(f"Error{error}")
            return
        if pos == -1:
            print("Error! El ID ingresado es inválido")
            id_venta = int(input("Vuelva a ingresar el ID: "))
    
    print("Datos de la venta a eliminar:")
    try:
        with open('ventas.txt', 'r', encoding='utf-8') as archivo_ventas:
            for linea in archivo_ventas:
                partes = linea.strip().split(';')
                id_venta_linea = partes[0] 
                if id_venta_linea == str(id_venta):
                    print("ID Venta:", partes[0])
                    print("Fecha:", partes[1])
                    print("ID Cliente:", partes[2])
                    print("Total:", partes[3])
    except(FileNotFoundError,OSError) as error:
        print(f"Error{error}")
        return
    confirmacion = int(input("Confirma la eliminación? (1-Si / 2-No): "))
    if confirmacion == 1:
        try:
            with open('ventas.txt', 'r', encoding='utf-8') as archivo_ventas:
                lineas = archivo_ventas.readlines()
                nuevas_lineas = []
                for linea in lineas:
                    partes = linea.strip().split(';')
                    id_venta_linea = partes[0]
                    if id_venta_linea != str(id_venta):
                        nuevas_lineas.append(linea)
        except(FileNotFoundError,OSError) as error:
            print(f"Error{error}")
        try:
            with open('ventas.txt', 'w', encoding='utf-8') as archivo_ventas:
                archivo_ventas.writelines(nuevas_lineas)
        except(FileNotFoundError,OSError) as error:
            print(f"Error{error}")
    else:
        print("Cancelando operación")
          