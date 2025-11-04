from .funciones_generales import mostrar_encabezado, validar_opcion, leer_ventas, fechaYvalidacion, buscar_id, open_json_file, extraer_encabezado_submenu
from .datos_de_prueba import *
from .recetas import agregar_receta

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

def open_ventas_file():
    matriz_ventas = []
    try:
        with open('ventas.txt', "rt", encoding="UTF-8") as arch:
            for linea in arch:
                fila = linea.strip().split(";")
                if len(fila) == 4:
                    try:
                        fila[0] = int(fila[0])
                        fila[2] = int(fila[2])
                        fila[3] = float(fila[3])
                        matriz_ventas.append(fila)
                    except ValueError:
                        print(f"Advertencia: línea con datos inválidos → {linea.strip()}")
                else:
                    print(f"Advertencia: línea con formato incorrecto → {linea.strip()}")
    except FileNotFoundError:
        print("Advertencia: no se encontró el archivo ventas.txt.")
    return matriz_ventas

def open_detalle_ventas_file():
    matriz_detalle_ventas = []
    try:
        with open('detalle_ventas.txt', "rt", encoding="UTF-8") as arch:
            for linea in arch:
                fila = linea.strip().split(";")
                if len(fila) == 3:
                    try:
                        fila[0] = int(fila[0])
                        fila[1] = int(fila[1])
                        fila[2] = int(fila[2])
                        matriz_detalle_ventas.append(fila)
                    except ValueError:
                        print(f"Advertencia: línea con datos inválidos → {linea.strip()}")
    except FileNotFoundError:
        print("Advertencia: no se encontró el archivo detalle_ventas.txt.")
    except Exception as e:
        print(f"Error al leer detalle_ventas.txt: {e}")
    return matriz_detalle_ventas

def open_recetas_file():
    matriz_recetas = []
    try:
        with open('recetas.txt', "rt", encoding="UTF-8") as arch:
            for linea in arch:
                fila = linea.strip().split(";")
                if len(fila) == 5:
                    try:
                        fila[0] = int(fila[0])
                        fila[1] = int(fila[1])
                        fila[4] = int(fila[4])
                        matriz_recetas.append(fila)
                    except ValueError:
                        print(f"Advertencia: línea con datos inválidos → {linea.strip()}")
    except FileNotFoundError:
        print("Advertencia: no se encontró el archivo recetas.txt.")
    except Exception as e:
        print(f"Error al leer recetas.txt: {e}")
    return matriz_recetas

def agregar_venta_y_detalle():
    matriz = open_ventas_file()
    matriz_detalle_ventas = open_detalle_ventas_file()
    matriz_clientes = open_json_file('clientes.json')
    venta = []

    if not matriz:
        id_venta = 1
    else:
        id_venta = matriz[-1][0] + 1

    fecha = fechaYvalidacion()
    id_cliente = int(input("Ingrese el ID del cliente: "))
    pos_cliente = buscar_id(matriz_clientes, id_cliente)
    while pos_cliente == -1:
        print("Error! El ID del cliente es inválido")
        id_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
        pos_cliente = buscar_id(matriz_clientes, id_cliente)

    print("Ingresando a detalle de venta...")
    input("Presione Enter para continuar...")
    total = agregar_detalle_de_venta(id_cliente, id_venta, matriz_detalle_ventas)
    print(f"Subtotal de la venta: ${total}")
    descuento = buscar_descuento_obra_social(id_cliente)
    print(f"Descuento aplicado: {descuento}%")
    total2 = aplicar_descuento(total, descuento)
    print(f"Total de la venta: ${total2}")
    venta = [id_venta, fecha, id_cliente, total2]
    matriz.append(venta)

    try:
        with open('ventas.txt', 'a', encoding='utf-8') as archivo_ventas:
            archivo_ventas.write(f"\n{id_venta};{fecha};{id_cliente};{total2}")
        print("Venta guardada exitosamente.")
    except OSError:
        print("Error al abrir ventas.txt para escritura.")
    except FileNotFoundError:
        print("Error: no se encontró el archivo ventas.txt para escritura.")

def agregar_detalle_de_venta(id_cliente, id_venta, matriz):
    matriz_productos = open_json_file('producto.json')
    nuevos_detalles = []
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
            matriz.append(detalle_venta)
            nuevos_detalles.append(detalle_venta)
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
            matriz.append(detalle_venta)
            nuevos_detalles.append(detalle_venta)
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

    # Guardar solo los nuevos detalles
    if nuevos_detalles:
        try:
            with open('detalle_ventas.txt', 'a', encoding='utf-8') as archivo_detalle:
                for detalle in nuevos_detalles:
                    archivo_detalle.write(f"\n{detalle[0]};{detalle[1]};{detalle[2]}")
            print("Detalle de venta guardado exitosamente.")
        except OSError:
            print("Error al abrir detalle_ventas.txt para escritura.")
        except FileNotFoundError:
            print("Error: no se encontró el archivo detalle_ventas.txt para escritura.")
    else:
        print("No se agregaron nuevos detalles.")

    print("Detalles de la venta agregados correctamente.")

    return total

def buscar_descuento_obra_social(id_cliente):
    matriz_clientes = open_json_file('clientes.json')
    matriz_obras_sociales = open_json_file('obras_sociales.json')
    id_cliente_str = str(id_cliente)
    if id_cliente_str in matriz_clientes:
        nombre_obra_social = matriz_clientes[id_cliente_str]["obra_social"]
        if nombre_obra_social in matriz_obras_sociales:
            return matriz_obras_sociales[nombre_obra_social]
    return 0 


def aplicar_descuento(total, descuento):
    total2 = total - (total * (descuento / 100)) if descuento else total
    if descuento:
        print(f"Descuento del {descuento}%. Total con descuento: ${total2}")
    return total2

def modificar_venta():
    matriz = open_ventas_file()
    matriz_clientes = open_json_file('clientes.json')
    matriz_productos = open_json_file('producto.json')
    matriz_recetas = open_detalle_ventas_file()
    matriz_codigos_ventas = [fila[0] for fila in matriz]

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

    pos = buscar_id(matriz, id_venta)
    print("Venta encontrada:")
    print(matriz[pos])
    print("¿Qué desea modificar?")
    for k, v in opciones_modificacion_ventas.items():
        print(f"{k}. {v}")
    try:
        modificacion = int(input("Seleccione una opción (1, 2 o 3): "))
    except ValueError:
        print("Error! Debe ingresar un número válido.")
        return

    if modificacion == 1:
        matriz[pos][1] = fechaYvalidacion()
        print("Fecha actualizada correctamente.")

    elif modificacion == 2:
        try:
            nuevo_cliente = int(input("Ingrese el nuevo ID del cliente: "))
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            return

        pos_cliente = buscar_id(matriz_clientes, nuevo_cliente)
        while pos_cliente == -1:
            print("El ID del cliente es inválido")
            try:
                nuevo_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return
            pos_cliente = buscar_id(matriz_clientes, nuevo_cliente)

        matriz[pos][2] = nuevo_cliente
        descuento = buscar_descuento_obra_social(nuevo_cliente)
        total = float(matriz[pos][3])
        matriz[pos][3] = aplicar_descuento(total, descuento)
        print("Cliente y descuento actualizados correctamente.")

    elif modificacion == 3:
        id_cliente = matriz[pos][2]
        print("¿Desea modificar la receta o venta libre?")
        tipo = int(input("Ingrese 1 para receta o 2 para venta libre: "))

        if tipo == 1:
            try:
                id_producto = int(input("Ingrese el código del producto asociado a la receta: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return

            producto_encontrado = False
            for p in matriz_productos:
                if p["codigo"] == id_producto:
                    producto_encontrado = True
                    producto_actual = p
                    break
            if not producto_encontrado:
                print("Error! El código del producto no existe.")
                return

            id_receta, cantidad = agregar_receta(id_producto, matriz_recetas)

            try:
                with open('recetas.txt', 'a', encoding='utf-8') as archivo_recetas:
                    archivo_recetas.write(f"{id_receta};{id_producto};{fechaYvalidacion()};{input('Ingrese el nombre del médico: ')};{cantidad}\n")
                print("Receta guardada exitosamente.")
            except OSError:
                print("Error al abrir recetas.txt para escritura.")
            except FileNotFoundError:
                print("Error: no se encontró el archivo recetas.txt para escritura.")

            subtotal = producto_actual["precio"] * cantidad
            descuento = buscar_descuento_obra_social(id_cliente)
            total2 = aplicar_descuento(subtotal, descuento)
            matriz[pos][3] = total2
            print(f"Detalle actualizado con receta. Total nuevo: ${total2:.2f}")

        elif tipo == 2:
            try:
                id_receta_eliminar = int(input("Ingrese el ID de la receta a eliminar (si corresponde): "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                id_receta_eliminar = None

            if id_receta_eliminar:
                nuevas_recetas = []
                for linea in matriz_recetas:
                    if int(linea[0]) != id_receta_eliminar:
                        nuevas_recetas.append(linea)
                try:
                    with open('recetas.txt', 'w', encoding='utf-8') as archivo_recetas:
                        archivo_recetas.writelines(nuevas_recetas)
                    print(f"Receta ID {id_receta_eliminar} eliminada exitosamente.")
                except FileNotFoundError:
                    print("Error: no se encontró el archivo recetas.txt para eliminar.")
                except Exception as e:
                    print(f"Error al eliminar la receta: {e}")

            try:
                id_producto = int(input("Ingrese el código del nuevo producto: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return

            while id_producto < 1 or id_producto > len(matriz_productos):
                print("Error! El código del producto es inválido.")
                id_producto = int(input("Ingrese nuevamente el código del producto: "))

            stock_disp = matriz_productos[id_producto - 1]["stock"]
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return

            while cantidad > stock_disp:
                print(f"Error! Sólo hay {stock_disp} unidades disponibles.")
                cantidad = int(input("Vuelva a ingresar la cantidad del producto: "))

            precio = matriz_productos[id_producto - 1]["precio"]
            subtotal = precio * cantidad
            descuento = buscar_descuento_obra_social(id_cliente)
            total2 = aplicar_descuento(subtotal, descuento)
            matriz[pos][3] = total2
            print(f"Detalle actualizado como venta libre. Total nuevo: ${total2:.2f}")

        else:
            print("Opción inválida.")
            return

    else:
        print("Opción inválida.")
        return

    try:
        with open('ventas.txt', 'w', encoding='utf-8') as archivo_ventas:
            for venta in matriz:
                archivo_ventas.write(f"{venta[0]};{venta[1]};{venta[2]};{venta[3]}\n")
        print("Venta modificada exitosamente.")
    except OSError:
        print("Error al abrir ventas.txt para escritura.")
    except FileNotFoundError:
        print("Error: no se encontró el archivo ventas.txt para escritura.")

def dar_baja_ventas():
    matriz_ventas = open_ventas_file()
    matriz_detalle_ventas = open_detalle_ventas_file()
    matriz_recetas = open_recetas_file()
    id_elemento = int(input("Ingrese el ID: "))
    pos = buscar_id(matriz_ventas,id_elemento)
    while pos==-1:
        print("Error! El ID ingresado es inválido")
        id_elemento = int(input("Vuelva a ingresar el ID: "))
        pos = buscar_id(matriz_ventas,id_elemento)
    for i in range(len(matriz_ventas[0])):
        print(matriz_ventas[pos][i])
    confirmacion = int(input("Desea eliminar estos datos? (1 para SI o 2 para NO): "))
    if confirmacion == 1:
        matriz_ventas.pop(pos)
        try:
            with open('ventas.txt', 'w', encoding='utf-8') as archivo_ventas:
                for venta in matriz_ventas:
                    archivo_ventas.write(f"{venta[0]};{venta[1]};{venta[2]};{venta[3]}\n")
            print("Ventas actualizadas exitosamente después de la baja.")
        except OSError:
            print("Error al abrir ventas.txt para escritura.")
        except FileNotFoundError:
            print("Error: no se encontró el archivo ventas.txt para escritura.")
        if matriz_detalle_ventas[pos][1] == "VL":
            pass
        else:
            matriz_detalle_ventas.pop(pos)
            matriz_recetas.pop(matriz_detalle_ventas[pos][1])
        try:
            with open('detalle_ventas.txt', 'w', encoding='utf-8') as archivo_detalle:
                for detalle in matriz_detalle_ventas:
                    archivo_detalle.write(f"{detalle[0]};{detalle[1]};{detalle[2]}\n")
            print("Detalle de ventas actualizado exitosamente después de la baja.")
        except OSError:
            print("Error al abrir detalle_ventas.txt para escritura.")
        except FileNotFoundError:
            print("Error: no se encontró el archivo detalle_ventas.txt para escritura.")
    else:
        print("Cancelando operación")
        enter = input("Volviendo a menu...")
