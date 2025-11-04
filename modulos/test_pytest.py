from .datos_de_prueba import *
from .funciones_generales import buscar_id

def test_buscar_id():
    try:
        arch_productos = open("productos.txt", "r", encoding="utf-8")
        matriz_productos = [linea.strip().split(";") for linea in arch_productos]
    except FileNotFoundError:
        print("Error! El archivo de productos no existe.")
        return
    # Caso válido
    assert buscar_id(matriz_productos, 2) == 1, "Debería devolver índice 1 para ID 2"
    # Caso inexistente
    assert buscar_id(matriz_productos, 99) == -1, "Debería devolver -1 para un ID inexistente"
    # Caso string
    assert buscar_id(matriz_productos, "3") == 2, "Debería funcionar también con ID como string"

def stock_por_agotar(matriz_productos):
    productos_agotarse=[fila for fila in matriz_productos if (fila[2])<=2]
    return productos_agotarse # Retorna la lista de productos con stock menor al umbral. Con los datos actuales, debería retornar Paracetamol y Amoxicilina.

def test_stock_por_agotar():
    try:
        arch_productos = open("productos.txt", "r", encoding="utf-8")
        matriz_productos = [linea.strip().split(";") for linea in arch_productos]
    except FileNotFoundError:
        print("Error! El archivo de productos no existe.")
        return
    resultado = stock_por_agotar(matriz_productos)
    esperado = [
        [1, "Paracetamol", 1, 10],
        [3, "Amoxicilina", 2, 20]
    ]
    assert resultado == esperado, f"Se esperaba {esperado} pero se obtuvo {resultado}"


