from .datos_de_prueba import *
def stock_por_agotar(matriz_productos):
    productos_agotarse=[fila for fila in matriz_productos if (fila[2])<=2]
    return productos_agotarse # Retorna la lista de productos con stock menor al umbral. Con los datos actuales, debería retornar Paracetamol y Amoxicilina.

def test_stock_por_agotar():
    resultado = stock_por_agotar(matriz_productos)
    esperado = [
        [1, "Paracetamol", 1, 10],
        [3, "Amoxicilina", 2, 20]
    ]
    assert resultado == esperado, f"Se esperaba {esperado} pero se obtuvo {resultado}"