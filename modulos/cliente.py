from .funciones_generales import open_json_file,extraer_encabezado_submenu, mostrar_encabezado, validar_opcion, mostrar_matriz_clientes
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
    while not nombre.replace(" ", "").isalpha():
        print("Valor no válido. Solo letras y espacios.")
        nombre = input("Ingrese el nombre: ")
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
        "id_obra": id_obra,
        "nombre": nombre,
        "edad": edad,
        "telefono": telefono,
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
    print(f"\nCliente encontrado: {cliente['nombre']} (Edad: {cliente['edad']}, Tel: {cliente['tel']}, Obra social: {cliente['obra_social']})")

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

    # TELÉFONO (en tu JSON la clave es 'tel')
    resp = input("¿Desea modificar el teléfono? (s/n): ").lower()
    if resp == "s":
        nuevo_tel = ingresar_telefono()
        cambios["tel"] = nuevo_tel

    # OBRA SOCIAL (en tu JSON la clave es 'obra_social')
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
    """Controla el proceso de baja usando archivo auxiliar (según PPT)."""
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
    if cliente["estado"].lower() == "inactive":
        print("El cliente ya se encuentra dado de baja.")
        return

    cliente["estado"] = "Inactive"
    guardar_json(ruta_archivo, clientes)
    print("Cliente dado de baja correctamente.")

def submenu_clientes():
    opcion = 0
    encabezados_submenu_clientes = extraer_encabezado_submenu("clientes")
    while opcion != -1:
        print("---"* 10)
        print("Submenú Clientes")
        print("---"* 10)
        mostrar_encabezado(encabezados_submenu_clientes)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_submenu_clientes)
        if opcion == 1:  # Agregar cliente
            agregar_cliente()
            enter = input("Cliente agregado exitosamente. Volviendo a menu...")
        elif opcion == 2:  # Modificar cliente
            modificar_cliente()
            enter = input("Cliente modificado exitosamente. Volviendo a menu...")
        elif opcion == 3:  # Dar baja cliente
            baja_cliente()
            enter = input("Cliente eliminado exitosamente. Volviendo a menu...")
        elif opcion == 4:  # Mostrar lista completa
            mostrar_matriz_clientes("clientes.json")
    enter = input(" Volviendo a menu...")

def ordenar_clientes_por_nombre(matriz_clientes):
    clientes_ordenados = sorted(matriz_clientes, key=lambda fila: fila[2].lower())
    print("Clientes ordenados por nombre:")
    for cliente in clientes_ordenados:
         print(cliente[2])