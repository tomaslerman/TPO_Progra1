from .funciones_generales import mostrar_encabezado, validar_opcion, leer_ventas, fechaYvalidacion, open_json_file, extraer_encabezado_submenu
from .datos_de_prueba import *
from .recetas import agregar_receta
import os

OPCIONES_SUBMENU_VENTAS = (
    "1 - Agregar venta",
    "2 - Modificar detalle de venta",
    "3 - Dar baja venta",
    "4 - Mostrar lista completa",
    "-1 - Volver al menú principal",
)

def submenu_ventas():
    encabezados = extraer_encabezado_submenu("ventas")
    opcion = 0
    while opcion != -1:
        print("---" * 10)
        print("Submenú Ventas")
        print("---" * 10)

        # ----------------- USO DE SLICING DE CADENAS -------------------------
        # Tomo sólo las primeras 3 opciones de la tupla para mostrarlas
        for opcion_texto in OPCIONES_SUBMENU_VENTAS[:4]:
            print(opcion_texto)
        # ---------------------------------------------------------------------

        mostrar_encabezado(encabezados)
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            continue

        opcion = validar_opcion(opcion, 1, 4, encabezados)
        if opcion == 1:  # Agregar venta
            agregar_venta_y_detalle()
            input("Volviendo a menú...")
        elif opcion == 2:  # Modificar detalle de venta
            modificar_venta()
            input("Volviendo a menú...")
        elif opcion == 3:  # Dar baja venta
            dar_baja_ventas()
            input("Volviendo a menú...")
        elif opcion == 4:  # Mostrar lista completa
            leer_ventas()
            input("Presione Enter para continuar...")
    input("Volviendo al menú principal...")

def agregar_venta_y_detalle():
    matriz_clientes = open_json_file("clientes.json")

    ultimo_id = 0
    try:
        with open("ventas.txt", "r", encoding="utf-8") as archivo_ventas:
            for linea in archivo_ventas:
                if linea.strip():  # Evita líneas vacías
                    ultimo_id = int(linea.split(";")[0])
    except (FileNotFoundError, OSError):
        # Si no existe, es la primera venta; ultimo_id queda en 0
        pass

    id_venta = ultimo_id + 1
    fecha = fechaYvalidacion()

    try:
        id_cliente = int(input("Ingrese el ID del cliente: "))
    except ValueError:
        print("Error! Debe ingresar un número válido.")
        return

    pos = -1
    while pos == -1:
        for key in matriz_clientes:
            if int(key) == id_cliente:
                pos = key
                break
        if pos == -1:
            print("Error! El ID del cliente es inválido.")
            try:
                id_cliente = int(input("Ingrese el ID del cliente: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return

    print("")
    print("Ingresando a detalle de venta...")
    input("Presione Enter para continuar...")
    print("")
    total = agregar_detalle_de_venta(id_cliente, id_venta)
    total = float(total)
    print(f"Subtotal de la venta: ${total}")
    descuento = buscar_descuento_obra_social(id_cliente)
    print(f"Descuento aplicado: {descuento}%")
    total2 = aplicar_descuento(total, descuento)
    print(f"Total de la venta: ${total2}")
    venta = [id_venta, fecha, id_cliente, total2]
    try:
        with open("ventas.txt", "a", encoding="utf-8") as archivo_ventas:
            archivo_ventas.write(
                f"{venta[0]};{venta[1]};{venta[2]};{venta[3]}\n"
            )
    except (FileNotFoundError, OSError) as error:
        print(f"Error {error}")


def agregar_detalle_de_venta(id_cliente, id_venta):
    matriz_productos = open_json_file("producto.json")
    total = 0

    try:
        producto = int(input("Ingrese el código del producto: "))
    except ValueError:
        print("Error! Debe ingresar un número válido.")
        producto = -1

    producto_encontrado = any(p["codigo"] == producto for p in matriz_productos)

    while (producto != -1) and not producto_encontrado:
        print("Error! El código del producto es inválido.")
        try:
            producto = int(
                input(
                    "Ingrese nuevamente el código del producto o -1 para dejar de agregar productos: "
                )
            )
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            producto = -1
        producto_encontrado = any(p["codigo"] == producto for p in matriz_productos)

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
        while receta not in ["s", "n"]:
            print("Error! Opción inválida.")
            receta = input("¿El cliente tiene receta? (s/n): ").lower()

        if receta == "s":
            id_producto = producto
            id_receta, cantidad = agregar_receta(id_cliente, id_producto)
            if id_receta is None or cantidad is None:
                return 0

            subtotal = producto_actual["precio"] * cantidad
            detalle_venta = [id_venta, id_receta, subtotal]
            try:
                with open(
                    "detalle_ventas.txt", "a", encoding="utf-8"
                ) as archivo_detalle:
                    archivo_detalle.write(
                        f"{detalle_venta[0]};{detalle_venta[1]};{detalle_venta[2]}\n"
                    )
            except (FileNotFoundError, OSError) as error:
                print(f"Error {error}")
            total += subtotal
        else:
            try:
                cantidad = int(input("Ingrese la cantidad del producto: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                cantidad = 0

            while cantidad > producto_actual["stock"]:
                print(
                    f"Error! Sólo hay {producto_actual['stock']} unidades disponibles."
                )
                try:
                    cantidad = int(
                        input("Vuelva a ingresar la cantidad del producto: ")
                    )
                except ValueError:
                    print("Error! Debe ingresar un número válido.")
                    cantidad = 0

            subtotal = producto_actual["precio"] * cantidad
            detalle_venta = [id_venta, "VL", subtotal]
            try:
                with open(
                    "detalle_ventas.txt", "a", encoding="utf-8"
                ) as archivo_detalle:
                    archivo_detalle.write(
                        f"{detalle_venta[0]};{detalle_venta[1]};{detalle_venta[2]}\n"
                    )
            except (FileNotFoundError, OSError) as error:
                print(f"Error {error}")
            total += subtotal

        try:
            producto = int(
                input(
                    "Ingrese el código del producto o -1 para dejar de agregar productos: "
                )
            )
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            producto = -1

        producto_encontrado = any(p["codigo"] == producto for p in matriz_productos)

        while (producto != -1) and not producto_encontrado:
            print("Error! El código del producto es inválido.")
            try:
                producto = int(
                    input(
                        "Ingrese nuevamente el código del producto o -1 para dejar de agregar productos: "
                    )
                )
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                producto = -1
            producto_encontrado = any(
                p["codigo"] == producto for p in matriz_productos
            )

    return total


def buscar_descuento_obra_social(id_cliente):
    matriz_clientes = open_json_file("clientes.json")
    matriz_obras_sociales = open_json_file("obras_sociales.json")
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
        # ----------------- USO DE SLICING PARA FORMATO --------------------------
        total_str = f"{total2:.2f}"
        # Por ejemplo, me quedo sólo con la parte entera y los dos decimales
        total_str_formateado = total_str[:total_str.find('.') + 3]
        print(f"Descuento del {descuento}%. Total con descuento: ${total_str_formateado}")
        # ------------------------------------------------------------------------
    return total2

def modificar_venta():
    matriz_clientes = open_json_file("clientes.json")
    matriz_productos = open_json_file("producto.json")
    matriz_codigos_ventas = []

    try:
        with open("ventas.txt", "r", encoding="utf-8") as archivo_ventas:
            for linea in archivo_ventas:
                if linea.strip():
                    codigo_venta = int(linea.split(";")[0])
                    matriz_codigos_ventas.append(codigo_venta)
    except (FileNotFoundError, OSError) as error:
        print(f"Error: {error}")
        return

    try:
        id_venta = int(input("Ingrese el ID de la venta a modificar: "))
    except ValueError:
        print("Error! Debe ingresar un número válido.")
        return

    while id_venta not in matriz_codigos_ventas:
        print("El ID de la venta es inválido.")
        try:
            id_venta = int(input("Vuelva a ingresar el ID de la venta: "))
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            return

    venta_datos = None
    try:
        with open("ventas.txt", "r", encoding="utf-8") as archivo_ventas:
            for linea in archivo_ventas:
                datos = linea.strip().split(";")
                if int(datos[0]) == id_venta:
                    venta_datos = datos
                    break
        if not venta_datos:
            print("No se encontró la venta.")
            return
        print("Datos actuales de la venta:")
        print(f"ID Venta: {venta_datos[0]}")
        print(f"Fecha: {venta_datos[1]}")
        print(f"ID Cliente: {venta_datos[2]}")
        print(f"Total: {venta_datos[3]}")
    except (FileNotFoundError, OSError) as error:
        print(f"Error: {error}")
        return

    print("")
    detalle_datos = None
    try:
        with open("detalle_ventas.txt", "r", encoding="utf-8") as archivo_detalle:
            for linea in archivo_detalle:
                datos = linea.strip().split(";")
                if int(datos[0]) == id_venta:
                    detalle_datos = datos
                    print("Detalle de la venta:")
                    print(f"ID Detalle: {datos[0]}")
                    print(f"ID Receta/Venta Libre: {datos[1]}")
                    print(f"Subtotal: {datos[2]}")
                    break
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

    # --- Modificar fecha
    if modificacion == 1:
        nueva_fecha = fechaYvalidacion()
        try:
            with open("ventas.txt", "r", encoding="utf-8") as archivo_ventas, open(
                "temp_ventas.txt", "w", encoding="utf-8"
            ) as temp:
                for linea in archivo_ventas:
                    datos = linea.strip().split(";")
                    if int(datos[0]) == id_venta:
                        datos[1] = nueva_fecha
                        linea = ";".join(datos) + "\n"
                    temp.write(linea)
            os.replace("temp_ventas.txt", "ventas.txt")
        except (FileNotFoundError, OSError) as error:
            print(f"Error: {error}")
            return
        print("Fecha actualizada correctamente.")

    # --- Modificar cliente
    elif modificacion == 2:
        try:
            nuevo_cliente = int(input("Ingrese el nuevo ID del cliente: "))
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            return
        nuevo_cliente = str(nuevo_cliente)

        while nuevo_cliente not in matriz_clientes:
            print("Error! El ID del cliente es inválido.")
            try:
                nuevo_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return
            nuevo_cliente = str(nuevo_cliente)

        try:
            with open("ventas.txt", "r", encoding="utf-8") as archivo_ventas, open(
                "temp_ventas.txt", "w", encoding="utf-8"
            ) as temp:
                for linea in archivo_ventas:
                    datos = linea.strip().split(";")
                    if int(datos[0]) == id_venta:
                        datos[2] = nuevo_cliente
                        linea = ";".join(datos) + "\n"
                    temp.write(linea)
            os.replace("temp_ventas.txt", "ventas.txt")
        except (FileNotFoundError, OSError) as error:
            print(f"Error: {error}")
            return
        print("ID del cliente actualizado correctamente.")

    # --- Modificar detalle (receta o venta libre)
    elif modificacion == 3:
        id_cliente = int(venta_datos[2])
        print("¿Desea modificar la receta o venta libre?")
        try:
            tipo = int(input("Ingrese 1 para receta o 2 para venta libre: "))
        except ValueError:
            print("Error! Debe ingresar un número válido.")
            return

        # Receta
        if tipo == 1:
            try:
                id_producto = int(
                    input("Ingrese el código del producto a modificar en la receta: ")
                )
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return

            producto_actual = next(
                (p for p in matriz_productos if p["codigo"] == id_producto), None
            )
            while not producto_actual:
                print("Error! Código inválido.")
                try:
                    id_producto = int(
                        input("Vuelva a ingresar el código del producto: ")
                    )
                except ValueError:
                    print("Error! Debe ingresar un número válido.")
                    return
                producto_actual = next(
                    (p for p in matriz_productos if p["codigo"] == id_producto), None
                )

            id_receta, cantidad = agregar_receta(id_cliente, id_producto)
            if id_receta is None or cantidad is None:
                print("No se modificó la receta.")
                return

            subtotal = producto_actual["precio"] * cantidad

            try:
                with open(
                    "detalle_ventas.txt", "r", encoding="utf-8"
                ) as archivo_detalle, open(
                    "temp_detalle.txt", "w", encoding="utf-8"
                ) as temp:
                    for linea in archivo_detalle:
                        datos = linea.strip().split(";")
                        if int(datos[0]) == id_venta:
                            datos[1] = str(id_receta)
                            datos[2] = str(subtotal)
                            linea = ";".join(datos) + "\n"
                        temp.write(linea)
                os.replace("temp_detalle.txt", "detalle_ventas.txt")
            except (FileNotFoundError, OSError) as error:
                print(f"Error: {error}")
                return

            descuento = buscar_descuento_obra_social(id_cliente)
            total2 = aplicar_descuento(subtotal, descuento)
            try:
                with open("ventas.txt", "r", encoding="utf-8") as archivo_ventas, open(
                    "temp_ventas.txt", "w", encoding="utf-8"
                ) as temp:
                    for linea in archivo_ventas:
                        datos = linea.strip().split(";")
                        if int(datos[0]) == id_venta:
                            datos[3] = str(total2)
                            linea = ";".join(datos) + "\n"
                        temp.write(linea)
                os.replace("temp_ventas.txt", "ventas.txt")
            except (FileNotFoundError, OSError) as error:
                print(f"Error: {error}")
                return
            print("Detalle de venta modificado correctamente.")

        # Venta libre
        elif tipo == 2:
            if not detalle_datos:
                print("No se encontró el detalle de venta para modificar.")
                respuesta = input(
                    "Desea agregar un nuevo detalle de venta? (s/n): "
                ).lower()
                if respuesta == "s":
                    agregar_detalle_de_venta(id_cliente, id_venta)
                else:
                    print("Operación cancelada.")
            else:
                print("El detalle actual no es de venta libre.")
                respuesta = input(
                    "¿Desea cambiar a venta libre? (s/n): "
                ).lower()
                if respuesta == "s":
                    try:
                        with open(
                            "detalle_ventas.txt", "r", encoding="utf-8"
                        ) as archivo_detalle, open(
                            "temp_detalle.txt", "w", encoding="utf-8"
                        ) as temp:
                            for linea in archivo_detalle:
                                datos = linea.strip().split(";")
                                if int(datos[0]) == id_venta:
                                    datos[1] = "VL"
                                    linea = ";".join(datos) + "\n"
                                temp.write(linea)
                        os.replace("temp_detalle.txt", "detalle_ventas.txt")
                    except (FileNotFoundError, OSError) as error:
                        print(f"Error: {error}")
                        return
                    print("Venta cambiada a tipo libre.")
                else:
                    print("Operación cancelada.")
        else:
            print("Opción inválida.")
    else:
        print("Opción inválida.")


def dar_baja_ventas():
    try:
        id_venta = int(input("Ingrese el ID: "))
    except ValueError:
        print("Error! Debe ingresar un número válido.")
        return

    pos = -1

    while pos == -1:
        try:
            with open("ventas.txt", "r", encoding="utf-8") as archivo_ventas:
                for linea in archivo_ventas:
                    partes = linea.strip().split(";")
                    if partes and partes[0] == str(id_venta):
                        pos = 0
                        break
        except (FileNotFoundError, OSError) as error:
            print(f"Error {error}")
            return

        if pos == -1:
            print("Error! El ID ingresado es inválido")
            try:
                id_venta = int(input("Vuelva a ingresar el ID: "))
            except ValueError:
                print("Error! Debe ingresar un número válido.")
                return

    print("Datos de la venta a eliminar:")
    try:
        with open("ventas.txt", "r", encoding="utf-8") as archivo_ventas:
            for linea in archivo_ventas:
                partes = linea.strip().split(";")
                if partes and partes[0] == str(id_venta):
                    print("ID Venta:", partes[0])
                    print("Fecha:", partes[1])
                    print("ID Cliente:", partes[2])
                    print("Total:", partes[3])
                    break
    except (FileNotFoundError, OSError) as error:
        print(f"Error {error}")
        return

    try:
        confirmacion = int(
            input("Confirma la eliminación? (1-Si / 2-No): ")
        )
    except ValueError:
        print("Opción inválida. Cancelando operación.")
        return

    if confirmacion == 1:

        try:
            with open("ventas.txt", "r", encoding="utf-8") as archivo_ventas, open(
                "temp_ventas.txt", "w", encoding="utf-8"
            ) as temp:
                for linea in archivo_ventas:
                    partes = linea.strip().split(";")
                    if partes and partes[0] == str(id_venta):
                        continue
                    temp.write(linea)
            os.replace("temp_ventas.txt", "ventas.txt")
        except (FileNotFoundError, OSError) as error:
            print(f"Error {error}")


        try:
            with open(
                "detalle_ventas.txt", "r", encoding="utf-8"
            ) as archivo_detalle, open(
                "temp_detalle.txt", "w", encoding="utf-8"
            ) as temp:
                for linea in archivo_detalle:
                    if not linea.startswith(f"{id_venta};"):
                        temp.write(linea)
            os.replace("temp_detalle.txt", "detalle_ventas.txt")
            print("Detalles de venta eliminados.")
        except (FileNotFoundError, OSError):
            print("No se encontró detalle_ventas.txt, se omitió.")

        try:
            with open(
                "recetas.txt", "r", encoding="utf-8"
            ) as archivo_recetas, open(
                "temp_recetas.txt", "w", encoding="utf-8"
            ) as temp:
                for linea in archivo_recetas:
                    if not linea.startswith(f"{id_venta};"):
                        temp.write(linea)
            os.replace("temp_recetas.txt", "recetas.txt")
            print("Recetas asociadas eliminadas.")
        except (FileNotFoundError, OSError):
            print("No se encontró recetas.txt, se omitió.")
    else:
        print("Cancelando operación")