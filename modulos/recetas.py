from .funciones_generales import fechaYvalidacion

def agregar_receta(id_producto):
    ultimo_id = 0
    try:
        with open('recetas.txt', 'r', encoding='utf-8') as archivo_recetas:
            for linea in archivo_recetas:
                partes = linea.strip().split(';')
                if len(partes) > 0 and partes[0].isdigit():
                    ultimo_id = int(partes[0])
    except FileNotFoundError:
        ultimo_id = 0
    except OSError as error:
        print(f"Error al leer recetas.txt: {error}")
        return None, None

    codigo = ultimo_id + 1
    fecha = fechaYvalidacion()
    medico = input("Ingrese el nombre completo del médico: ")
    try:
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Error: la cantidad debe ser un número entero.")
        return None, None

    try:
        with open('recetas.txt', 'a', encoding='utf-8') as archivo_recetas:
            archivo_recetas.write(f"{codigo};{id_producto};{fecha};{medico};{cantidad}\n")
    except (FileNotFoundError, OSError) as error:
        print(f"Error al escribir en recetas.txt: {error}")
        return None, None

    return codigo, cantidad