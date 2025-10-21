from .funciones_generales import mostrar_encabezado, validar_opcion, mostrar_matriz_clientes, extraer_encabezado_submenu_clientes
import json
import os

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
    id_obra = pedir_entero("Ingrese ID de obra social (número): ")
    if id_obra is None:
        return
    telefono = pedir_entero("Ingrese número de teléfono: ")
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
    """Controla todo el proceso de modificación usando un archivo auxiliar."""
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
    print(f"\nCliente encontrado: {cliente['nombre']} (Edad: {cliente['edad']}, Tel: {cliente['telefono']})")

    nuevo_nombre = validar_nombre()
    nueva_edad = pedir_entero("Ingrese la nueva edad: ")
    if nueva_edad is None:
        return
    nueva_obra = pedir_entero("Ingrese el nuevo ID de obra social: ")
    if nueva_obra is None:
        return
    nuevo_tel = pedir_entero("Ingrese el nuevo número de teléfono: ")
    if nuevo_tel is None:
        return

    cliente.update({
        "nombre": nuevo_nombre,
        "edad": nueva_edad,
        "id_obra": nueva_obra,
        "telefono": nuevo_tel
    })

    guardar_json(ruta_archivo, clientes)
    print("\nRegistro modificado correctamente.")


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
    encabezados_submenu_clientes = extraer_encabezado_submenu_clientes()
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