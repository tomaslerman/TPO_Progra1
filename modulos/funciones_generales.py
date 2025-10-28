import json

def validar_opcion(opcion,inicio,fin,encabezado):   
    while opcion !=-1 and opcion < inicio or opcion > fin:
        print("Debe ingresar rangos de opcion del ",inicio,"al",fin)
        mostrar_encabezado(encabezado)
        opcion=int(input("Ingrese nuevamente una opcion: "))
    return opcion

def extraer_encabezado_submenu(key):
    try:
        with open("encabezados_submenus.json", "r") as archivo:
            datos = json.load(archivo)
            encabezado = datos[key]
            return encabezado
    except FileNotFoundError:
        print("Error: No se encontró el archivo de encabezados.")
        return []

def extraer_encabezado_busquedas(key):
    try:
        with open("encabezados_busquedas.json", "r") as archivo:
            datos = json.load(archivo)
            encabezado = datos[key]
            return encabezado
    except FileNotFoundError:
        print("Error: No se encontró el archivo de encabezados.")
        return []

def extraer_encabezado(key):
    try:
        with open("encabezados_modulos.json", "r") as archivo:
            datos = json.load(archivo)
            encabezado = datos[key]
            return encabezado
    except FileNotFoundError:
        print("Error: No se encontró el archivo de encabezados.")
        return []

def mostrar_encabezado(encabezado):
    for k in encabezado:
        print(f'{k}. {encabezado[k]}')

def mostrar_matriz(titulos, matriz):
    print(" | ".join(titulos))
    print("-" * 40)  
    
    for fila in matriz:
        fila_completa = fila + [""] * (len(titulos) - len(fila))
        print(" | ".join(str(valor) for valor in fila_completa))

def mostrar_matriz_clientes(ruta_archivo):
    try:
        with open(ruta_archivo, "r") as archivo:
            clientes = json.load(archivo)
        titulos = ["ID", "Nombre", "Edad", "Teléfono", "Estado"]
        matriz = []
        for cliente in clientes.values():
            fila = [cliente["id_obra"], cliente["nombre"], cliente["edad"], cliente["telefono"], cliente["estado"]]
            matriz.append(fila)
    except FileNotFoundError:
        print("Error: No se encontró el archivo de clientes.")
        return
    anchos = [max(len(str(item)) for item in col) for col in zip(*([titulos] + matriz))]
    for i, titulo in enumerate(titulos):
        print(f"{titulo:<{anchos[i]}}", end="  ")
    print()
    for fila in range (len(matriz)):
        if matriz[fila][5] == "Active":
            for columna in range (len(matriz[fila])):
                print(f"{matriz[fila][columna]:<{anchos[columna]}}", end="  ")
            print()

def mostrar_matriz_cuadro(encabezados, matriz):
    for i in range(len(encabezados)):
        print(f"{encabezados[i]:<20}", end="")
    print()
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:<20}", end="")
        print()

def ingresar_id_obra_social(matriz_obras_sociales,encabezados_obras_sociales):
    print("Obras sociales disponibles:")
    mostrar_matriz_cuadro(encabezados_obras_sociales, matriz_obras_sociales)
    id_obra_social = int(input("Ingrese el ID de la obra social: "))
    existe = id_obra_social in [fila[0] for fila in matriz_obras_sociales]
    while not existe:
        print("El ID de la obra social es inválido")
        id_obra_social = int(input("Vuelva a ingresar el ID de la obra social: "))
        existe = id_obra_social in [fila[0] for fila in matriz_obras_sociales]
    return id_obra_social

def validar_mayor_que(valor, minimo):
    while valor <= minimo:
        print(f"El valor debe ser mayor que {minimo}")
        valor = int(input(f"Ingrese un valor mayor que {minimo}: "))
    return valor



def fechaYvalidacion():
    while True:
        try:
            anio = int(input("Ingrese año: "))
            assert 0 < anio <= 2025, "El año ingresado no es válido"
            break
        except ValueError:
            print("Error! Debe ingresar un número entero para el año.")
        except AssertionError as error:
            print(error)

    while True:
        try:
            mes = int(input("Ingrese mes: "))
            assert 1 <= mes <= 12, " El mes ingresado no es válido"
            break
        except ValueError:
            print(" Error! Debe ingresar un número entero para el mes.")
        except AssertionError as error:
            print(error)

    while True:
        try:
            dia = int(input("Ingrese día: "))

            if mes == 2:
                assert 1 <= dia <= 29, " El día ingresado no es válido para febrero,febrero tiene 28 dias."
            elif mes in [1, 3, 5, 7, 8, 10, 12]:
                assert 1 <= dia <= 31, " El día ingresado no es válido para este mes"
            else:
                assert 1 <= dia <= 30, " El día ingresado no es válido para este mes"

            break
        except ValueError:
            print("Error! Debe ingresar un número entero para el día.")
        except AssertionError as error:
            print(error)

    fecha = f"{dia}/{mes}/{anio}"
    return fecha

def buscar_por_nombre(matriz, nombre, columna, encabezados):
    resultados = [fila for fila in matriz if nombre.lower() in fila[columna].lower()]
    if resultados:
        mostrar_matriz_cuadro(encabezados, resultados)
    else:
        print("No se encontraron coincidencias.")

def buscar_id(matriz,dato):
    i=0
    pos = -1
    encontro=False
    while i < len(matriz) and encontro==False:
        if str (matriz[i][0])== str(dato):
            encontro=True
            pos = i
        i+=1    
    return pos

def buscar_id_json(archivo, codigo):
    
    try:
        with open(archivo, "r", encoding="UTF-8") as arch:
            productos = json.load(arch)
        for i, producto in enumerate(productos):
            if "codigo" in producto and str(producto["codigo"]) == str (codigo):
                return i, producto
        return -1, None
    except (FileNotFoundError, json.JSONDecodeError):
        return -1,None

def mostrar_datos(archivo,modo):
    try:
        with open (archivo,modo,encoding="UTF-8")as datos:
            productos=json.load(datos)
            print("--------------------")
            print("Datos de Productos:")
            print("---------------------")
            print(f'{"|Codigo|":^8}  {"|Medicamento|":^20} {"|Stock|":^10} {"|Precio|":^10}')  
            for pro in productos:
                prec=f"${pro["precio"]}" 
                print(f"{pro["codigo"]:^8}{pro["nombre"]:^20} {pro["stock"]:^15} {prec:^3}")
    except(FileNotFoundError,OSError) as error:
        print(f"Error{error}")




def dar_baja_elementos(matriz):
    id_elemento = int(input("Ingrese el ID: "))
    pos = buscar_id(matriz,id_elemento)
    while pos==-1:
        print("Error! El ID ingresado es inválido")
        receta = int(input("Vuelva a ingresar el ID: "))
        pos = buscar_id(matriz,id_elemento)
    for i in range(len(matriz[0])):
        print(matriz[pos][i])
    confirmacion = int(input("Desea eliminar estos datos? (1 para SI o 2 para NO): "))
    if confirmacion == 1:
        matriz.pop(pos)
        enter = input("Dato eliminado exitosamente. Volviendo a menu...")
    else:
        print("Cancelando operación")
        enter = input("Volviendo a menu...")
    
def open_json_file(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f" El archivo {archivo} no existe.\n")
        return []
    except json.JSONDecodeError:
        print(f" El archivo {archivo} no tiene un formato válido.\n")
        return []


def leer_ventas():
    """Lee ventas.txt y devuelve una lista de listas con los datos."""
    ventas = []
    try:
        with open("ventas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(";")
                if len(partes) == 4:
                    try:
                        id_venta = int(partes[0])
                        fecha = partes[1]
                        id_cliente = int(partes[2])
                        total = float(partes[3])
                        ventas.append([id_venta, fecha, id_cliente, total])
                    except ValueError:
                        print("Línea con datos no válidos, se omitirá:", linea)
    except FileNotFoundError:
        print("Error: no se encontró el archivo ventas.txt.")
    except OSError:
        print("Error al abrir ventas.txt.")
    return ventas