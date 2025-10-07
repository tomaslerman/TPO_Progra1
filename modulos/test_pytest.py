from .datos_de_prueba import *
from .funciones_generales import buscar_id
def test_buscar_id():
    # Caso válido
    assert buscar_id(matriz_productos, 2) == 1, "Debería devolver índice 1 para ID 2"
    # Caso inexistente
    assert buscar_id(matriz_productos, 99) == -1, "Debería devolver -1 para un ID inexistente"
    # Caso string
    assert buscar_id(matriz_productos, "3") == 2, "Debería funcionar también con ID como string"