from .funciones_generales import fechaYvalidacion

def agregar_receta(id_producto):
    try:
        with open('recetas.txt', 'r', encoding='utf-8') as archivo_recetas:
            lineas = archivo_recetas.readlines()
            if lineas:
                ultimo_id = int(lineas[-1].split(';')[0])
            else:
                ultimo_id = 0
    except(FileNotFoundError,OSError) as error:
        print(f"Error{error}")
        return None
    codigo = ultimo_id
    fecha = fechaYvalidacion
    medico = str(input("Ingrese el nombre completo del médico: "))
    cantidad = int(input("Ingrese la cantidad: "))
    try:
        with open('recetas.txt', 'a', encoding='utf-8') as archivo_recetas:
            archivo_recetas.write(f"{codigo};{id_producto};{fecha};{medico};{cantidad}\n")
    except(FileNotFoundError,OSError) as error:
        print(f"Error{error}")
        return None
    return codigo, cantidad