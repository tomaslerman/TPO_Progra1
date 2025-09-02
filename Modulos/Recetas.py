from .funciones_generales import fechaYvalidacion, buscar_id
from .datos_de_prueba import matriz_productos, matriz_recetas

def agregar_receta(matriz_recetas):
    receta = []
    codigo = len(matriz_recetas) + 1
    producto = int(input("Ingrese el código del producto: "))#funcion para buscar el producto y validar input mayor a (1)
    encontrado = buscar_id(matriz_productos,producto)
    while encontrado==-1:
        print("Error! Código de producto inválido")
        producto = int(input("Vuelva a ingresar el código del producto: "))
    fecha = fechaYvalidacion()
    medico = input("Ingrese el nombre completo del médico: ")
    cantidad = int(input("Ingrese la cantidad de medicamento: "))
    receta.append(codigo,producto,fecha,medico,cantidad)
    matriz_recetas.append(receta)