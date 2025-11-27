from .funciones_generales import formatear_nombre_cliente, open_json_file, extraer_encabezado_submenu, mostrar_encabezado, validar_opcion, mostrar_matriz_clientes
import json

def obtener_ultimo_id(ruta_archivo):
    """Devuelve el siguiente ID disponible según los clientes en el JSON."""
    clientes = leer_json(ruta_archivo)
    if clientes:
        ids = [int(k) for k in clientes.keys()]
        return max(ids) + 1
    else:
        return 1

def validar_nombre():
    nombre = input("Ingrese el nombre: ")
    nombre = formatear_nombre_cliente(nombre)
    while not nombre.replace(" ", "").isalpha():
        print("Valor no válido. Solo letras y espacios.")
        nombre = input("Ingrese el nombre: ")
        nombre = formatear_nombre_cliente(nombre)
    return nombre

def ingresar_obra_social():
    obras_sociales = open_json_file("obras_sociales.json")

    if not obras_sociales:
        print("No se pudieron cargar las obras sociales.")
        return None

    while True:
        nombre = input("Ingrese el nombre de la obra social: ").strip()

        # Buscar la key correspondiente al nombre ingresado
        key_encontrada = None
        for key, datos in obras_sociales.items():
            if datos["nombre"].lower() == nombre.lower():
                key_encontrada = key
                break

        if key_encontrada is not None:
            print(f"Obra social encontrada: {obras_sociales[key_encontrada]['nombre']} (ID {key_encontrada})")
            return key_encontrada
        else:
            print("Obra social no encontrada.")
            respuesta = input("¿Desea volver a intentarlo? (s/n): ").lower()
            if respuesta != "s":
                print("Operación cancelada.")
                return None

def ingresar_telefono():
    telefono = input("Ingrese el número de teléfono: ")

    while not telefono.isdigit() or len(telefono) < 7 or len(telefono) > 15:
        print("Error: el teléfono debe contener solo números y tener entre 7 y 15 dígitos.")
        respuesta = input("¿Desea volver a intentarlo? (s/n): ").lower()
        if respuesta != "s":
            print("Ingreso cancelado por el usuario.")
            return None
        telefono = input("Ingrese el número de teléfono: ")

    return telefono

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Error: el número debe ser mayor que 0.")
        except ValueError:
            print("Error: dato no válido, solo se permiten números.")
        
        resp = input("¿Desea volver a intentar? (s/n): ")
        if resp.lower() != "s":
            print("Ingreso cancelado por el usuario.")
            return None

def leer_json(ruta_archivo):
    """Lee un archivo JSON y devuelve un diccionario."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: el archivo JSON está dañado. Se usará un diccionario vacío.")
        return {}

def guardar_json(ruta_archivo, data):
    """Guarda un diccionario en formato JSON."""
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except OSError:
        print("Error al escribir en el archivo JSON.")

def agregar_cliente():
    """Controla el alta del cliente, usando las funciones auxiliares."""
    ruta_archivo = "clientes.json"
    clientes = leer_json(ruta_archivo)

    id_cliente = obtener_ultimo_id(ruta_archivo)
    nombre = validar_nombre()
    edad = pedir_entero("Ingrese edad: ")
    if edad is None:
        return
    id_obra = ingresar_obra_social()
    if id_obra is None:
        return
    telefono = ingresar_telefono()
    if telefono is None:
        return

    estado = "Active"

    clientes[str(id_cliente)] = {
        "obra_social": str(id_obra),
        "nombre": nombre,
        "edad": edad,
        "tel": telefono,
        "estado": estado
    }

    guardar_json(ruta_archivo, clientes)
    print("Cliente agregado correctamente.")

def abrir_archivos(ruta_original, ruta_aux):
    """Abre el archivo original en lectura y el auxiliar en escritura."""
    arch = None
    aux = None
    try:
        arch = open(ruta_original, "r", encoding="utf-8")
        aux = open(ruta_aux, "w", encoding="utf-8")
        return arch, aux
    except FileNotFoundError:
        print("El archivo de clientes no existe.")
        return None, None
    except OSError:
        print("Error al abrir los archivos.")
        return None, None

def modificar_cliente():
    ruta_archivo = "clientes.json"
    clientes = leer_json(ruta_archivo)

    id_buscar = pedir_entero("Ingrese el ID del cliente a modificar: ")
    if id_buscar is None:
        return

    id_str = str(id_buscar)
    if id_str not in clientes:
        print("No se encontró ningún cliente con ese ID.")
        return

    cliente = clientes[id_str]

    # --- Verificar si el cliente está activo antes de modificar ---
    estado_actual = cliente.get("estado", "Active")
    if estado_actual.lower() != "active":
        print("\nEl cliente seleccionado está INACTIVO.")
        resp_reactivar = input("¿Desea reactivar al cliente para poder modificarlo? (s/n): ").lower()
        if resp_reactivar != "s":
            print("Operación cancelada. No se realizaron modificaciones.")
            return
        # Reactivar cliente
        cliente["estado"] = "Active"
        clientes[id_str] = cliente
        guardar_json(ruta_archivo, clientes)
        print("Cliente reactivado correctamente.\n")

    # Lectura de datos actuales
    nombre_cliente = cliente.get("nombre", "Sin nombre")
    edad_cliente = cliente.get("edad", "Sin edad")
    telefono_cliente = cliente.get("tel", "Sin teléfono")
    obra_cliente = cliente.get("obra_social", "Sin obra social")

    print(f"\nCliente encontrado: {nombre_cliente} (Edad: {edad_cliente}, Tel: {telefono_cliente}, Obra social: {obra_cliente})")

    cambios = {}

    # NOMBRE
    resp = input("¿Desea modificar el nombre? (s/n): ").lower()
    if resp == "s":
        cambios["nombre"] = validar_nombre()

    # EDAD
    resp = input("¿Desea modificar la edad? (s/n): ").lower()
    if resp == "s":
        nueva_edad = pedir_entero("Ingrese la nueva edad: ")
        if nueva_edad is not None:
            cambios["edad"] = nueva_edad

    # TELÉFONO 
    resp = input("¿Desea modificar el teléfono? (s/n): ").lower()
    if resp == "s":
        nuevo_tel = ingresar_telefono()
        if nuevo_tel is not None:
            cambios["tel"] = nuevo_tel

    # OBRA SOCIAL
    resp = input("¿Desea modificar la obra social? (s/n): ").lower()
    if resp == "s":
        nueva_obra = ingresar_obra_social()
        if nueva_obra is not None:
            cambios["obra_social"] = str(nueva_obra)

    # aplicar los cambios de verdad
    if cambios:
        cliente.update(cambios)
        clientes[id_str] = cliente
        guardar_json(ruta_archivo, clientes)
        print("\nRegistro modificado correctamente.")
    else:
        print("\nNo se realizaron cambios.")

def baja_cliente():
    """Controla el proceso de baja lógica del cliente."""
    ruta_archivo = "clientes.json"
    clientes = leer_json(ruta_archivo)

    id_buscar = pedir_entero("Ingrese el ID del cliente a dar de baja: ")
    if id_buscar is None:
        return

    id_str = str(id_buscar)
    if id_str not in clientes:
        print("No se encontró ningún cliente con ese ID.")
        return

    cliente = clientes[id_str]
    if cliente.get("estado", "").lower() == "inactive":
        print("El cliente ya se encuentra dado de baja.")
        return

    cliente["estado"] = "Inactive"
    clientes[id_str] = cliente
    guardar_json(ruta_archivo, clientes)
    print("Cliente dado de baja correctamente.")

def submenu_clientes():
    opcion = 0
    encabezados_submenu_clientes = extraer_encabezado_submenu("clientes")
    while opcion != -1:
        print("---" * 10)
        print("Submenú Clientes")
        print("---" * 10)
        mostrar_encabezado(encabezados_submenu_clientes)
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: debe ingresar un número.")
            continue

        opcion = validar_opcion(opcion, 1, 5, encabezados_submenu_clientes)
        if opcion == 1:  # Agregar cliente
            agregar_cliente()
            input("Cliente agregado exitosamente. Volviendo a menú...")
        elif opcion == 2:  # Modificar cliente
            modificar_cliente()
            input("Cliente modificado exitosamente. Volviendo a menú...")
        elif opcion == 3:  # Dar baja cliente
            baja_cliente()
            input("Cliente dado de baja exitosamente. Volviendo a menú...")
        elif opcion == 4:  # Mostrar lista activos
            mostrar_matriz_clientes("clientes.json", False)
        elif opcion == 5:  # Mostrar lista completa
            mostrar_matriz_clientes("clientes.json", True)
    input(" Volviendo a menú...")

def ordenar_clientes_por_nombre(matriz_clientes):
    clientes_ordenados = sorted(matriz_clientes, key=lambda fila: fila[2].lower())
    print("Clientes ordenados por nombre:")
    for cliente in clientes_ordenados:
        print(cliente[2])
