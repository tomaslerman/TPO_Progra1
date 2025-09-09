from .funciones_generales import fechaYvalidacion, buscar_id
from .datos_de_prueba import matriz_productos, matriz_recetas

def agregar_receta(id_producto,matriz_recetas):
    receta = []
    codigo = len(matriz_recetas) + 1
    fecha = fechaYvalidacion()
    medico = input("Ingrese el nombre completo del médico: ")
    cantidad = int(input("Ingrese la cantidad de medicamento: "))
    receta = [codigo, id_producto, fecha, medico, cantidad]
    matriz_recetas.append(receta)
    return codigo, cantidad