from .datos_de_prueba import *
from modulos.funciones_generales import buscar_id_prod, open_json_file

def test_buscar_id_prod_existente():
    """Debe encontrar el producto cuando el código existe."""
    clave, producto = buscar_id_prod("productos.json", 1)

    assert clave != -1, "Error: buscar_id_prod devolvió -1 para un código existente"
    assert producto is not None, "Error: debería devolver el diccionario del producto"


def test_buscar_id_prod_inexistente():
    """Debe devolver -1 cuando el código no existe."""
    clave, producto = buscar_id_prod("productos.json", 999)

    assert clave == -1, "Error: para un código inexistente debería devolver -1"
    assert producto is None, "Error: para un código inexistente debería devolver None"

def stock_por_agotar():
    productos = open_json_file("productos.json")
    if not productos:
        print("No hay productos registrados.")
        return
    productos_agotarse = [
        (id_prod, datos['descripcion'], datos['stock'], datos['precio'])
        for id_prod, datos in productos.items()
        if datos['stock'] <= 2
    ]
    return productos_agotarse # Retorna la lista de productos con stock menor al umbral. Con los datos actuales, debería retornar Paracetamol y Amoxicilina.

def test_stock_por_agotar():
    resultado = stock_por_agotar()
    esperado = [
        ('3', 'Amoxicilina', 2, 2000)
    ]
    # Caso falso
    '''esperado = [
        (1, "Paracetamol", 1, 10)
    ]'''
    assert resultado == esperado, f"Se esperaba {esperado} pero se obtuvo {resultado}"

  


