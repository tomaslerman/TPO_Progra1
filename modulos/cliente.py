from .funciones_generales import mostrar_encabezado, validar_opcion, mostrar_matriz_clientes, buscar_id, ingresar_id_obra_social
import json
import os


DELIM = ";"
def obtener_ultimo_id(ruta_archivo):
    arch = None
    try:
        arch = open(ruta_archivo, "r")
        lineas = arch.readlines()
    except FileNotFoundError:
        lineas = []
    except OSError:
        print("No se pudo abrir el archivo para lectura.")
        lineas = []
    finally:
        try:
            if arch is not None:
                arch.close()
        except:
            print("No se pudo cerrar el archivo")

    # calcular el próximo id
    if len(lineas) > 0:
        ultima = lineas[-1].strip().split(";")
        try:
            return int(ultima[0]) + 1
        except:
            print("Error al convertir el ID a entero. Se asignará ID 1.")
            return 1
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


def guardar_cliente(ruta_archivo, id_cliente, id_obra, nombre, edad, telefono, estado):
    
    arch = None
    try:
        arch = open(ruta_archivo, "a")
        linea = f"{id_cliente};{id_obra};{nombre};{edad};{telefono};{estado}\n"
        arch.write(linea)
        print("Cliente agregado correctamente.")
    except OSError:
        print("Error al escribir en el archivo.")
    finally:
        try:
            if arch is not None:
                arch.close()
        except:
            print("No se pudo cerrar el archivo")
  
def agregar_cliente():
    """Controla el alta del cliente, usando las funciones auxiliares."""
    ruta_archivo = "clientes.txt"
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
    guardar_cliente(ruta_archivo, id_cliente, id_obra, nombre, edad, telefono, estado)



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




def cerrar_archivos(arch, aux):
    """Cierra ambos archivos, controlando errores."""
    try:
        if arch is not None:
            arch.close()
        if aux is not None:
            aux.close()
    except:
        print("Error al cerrar los archivos.")


def reemplazar_archivo(ruta_original, ruta_aux):
    """Elimina el archivo original y renombra el auxiliar."""
    try:
        os.remove(ruta_original)
        os.rename(ruta_aux, ruta_original)
    except OSError:
        print("Error al reemplazar el archivo.")


def procesar_modificacion(arch, aux, id_buscar):
    """Copia los registros al auxiliar, modificando solo el que coincide con el ID."""
    encontrado = False

    for linea in arch:
        partes = linea.strip().split(DELIM)

        # Si la línea está vacía o incompleta, se copia igual
        if len(partes) < 6:
            aux.write(linea)
            continue

        try:
            id_cliente = int(partes[0])
        except ValueError:
            aux.write(linea)
            continue

        if id_cliente == id_buscar:
            encontrado = True
            print(f"\nCliente encontrado: {partes[2]} (Edad: {partes[3]}, Tel: {partes[4]})")

            # Pedir nuevos datos
            nuevo_nombre = validar_nombre()
            nueva_edad = pedir_entero("Ingrese la nueva edad: ")
            if nueva_edad is None:
                aux.write(linea)
                continue
            nueva_obra = pedir_entero("Ingrese el nuevo ID de obra social: ")
            if nueva_obra is None:
                aux.write(linea)
                continue
            nuevo_tel = pedir_entero("Ingrese el nuevo número de teléfono: ")
            if nuevo_tel is None:
                aux.write(linea)
                continue

            estado = partes[5]  # se mantiene igual
            nueva_linea = f"{id_cliente};{nueva_obra};{nuevo_nombre};{nueva_edad};{nuevo_tel};{estado}\n"
            aux.write(nueva_linea)
            print("\nRegistro modificado correctamente.")
        else:
            aux.write(linea)

    return encontrado

def modificar_cliente():
    """Controla todo el proceso de modificación usando un archivo auxiliar."""
    ruta_original = "clientes.txt"
    ruta_aux = "clientes_aux.txt"

    arch, aux = abrir_archivos(ruta_original, ruta_aux)
    if arch is None or aux is None:
        return

    try:
        id_buscar = pedir_entero("Ingrese el ID del cliente a modificar: ")
        if id_buscar is None:
            return

        encontrado = procesar_modificacion(arch, aux, id_buscar)

        if not encontrado:
            print("\nNo se encontró ningún cliente con ese ID.")

    finally:
        cerrar_archivos(arch, aux)
        reemplazar_archivo(ruta_original, ruta_aux)





def procesar_baja(arch, aux, id_buscar):
    """Copia los registros al auxiliar, marcando como Inactive el ID indicado."""
    encontrado = False

    for linea in arch:
        partes = linea.strip().split(DELIM)

        if len(partes) < 6:
            aux.write(linea)
            continue

        try:
            id_cliente = int(partes[0])
        except ValueError:
            aux.write(linea)
            continue

        # Si el ID coincide, marcamos como Inactive
        if id_cliente == id_buscar:
            encontrado = True
            print(f"\nCliente encontrado: {partes[2]} (Estado actual: {partes[5]})")

            if partes[5].strip().lower() == "inactive":
                print("El cliente ya se encuentra dado de baja.")
                aux.write(linea)
                continue

            partes[5] = "Inactive"
            nueva_linea = f"{partes[0]};{partes[1]};{partes[2]};{partes[3]};{partes[4]};{partes[5]}\n"
            aux.write(nueva_linea)
            print("Cliente dado de baja correctamente.")
        else:
            aux.write(linea)

    return encontrado




def baja_cliente():
    """Controla el proceso de baja usando archivo auxiliar (según PPT)."""
    ruta_original = "clientes.txt"
    ruta_aux = "clientes_aux.txt"

    arch, aux = abrir_archivos(ruta_original, ruta_aux)
    if arch is None or aux is None:
        return

    try:
        id_buscar = pedir_entero("Ingrese el ID del cliente a dar de baja: ")
        if id_buscar is None:
            return

        encontrado = procesar_baja(arch, aux, id_buscar)
        if not encontrado:
            print("\nNo se encontró ningún cliente con ese ID.")

    finally:
        cerrar_archivos(arch, aux)
        reemplazar_archivo(ruta_original, ruta_aux)




def submenu_clientes():
    opcion = 0
    while opcion != -1:
        print("---"* 10)
        print("Submenú Clientes")
        print("---"* 10)
        mostrar_encabezado(encabezados_submenu_clientes)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_submenu_clientes)
        if opcion == 1:  # Agregar cliente
            agregar_cliente(matriz_clientes)
            enter = input("Cliente agregado exitosamente. Volviendo a menu...")
        elif opcion == 2:  # Modificar cliente
            modificar_cliente(matriz_clientes, matriz_obras_sociales, encabezados_obras_sociales)
            enter = input("Cliente modificado exitosamente. Volviendo a menu...")
        elif opcion == 3:  # Dar baja cliente
            baja_cliente(matriz_clientes)
            enter = input("Cliente eliminado exitosamente. Volviendo a menu...")
        elif opcion == 4:  # Mostrar lista completa
            mostrar_matriz_clientes(encabezados_clientes,matriz_clientes)
    enter = input(" Volviendo a menu...")

def ordenar_clientes_por_nombre(matriz_clientes):
    clientes_ordenados = sorted(matriz_clientes, key=lambda fila: fila[2].lower())
    print("Clientes ordenados por nombre:")
    for cliente in clientes_ordenados:
         print(cliente[2])