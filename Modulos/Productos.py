from .datos_de_prueba import encabezados_submenu_inventario,matriz_productos,encabezados_productos
from .funciones_generales import validar_mayor_que,buscar_id,stock_por_agotar,mostrar_matriz_cuadro
import re

def agregar_producto(matriz_productos):

    codigo = (len(matriz_productos) + 1)
    descripcion = input("Ingrese el nombre del medicamento: ")
    cant_stock = int(input("Ingrese cantidad en stock: "))#funcion para validar mayores que que un numero(0)
    cant_stock=validar_mayor_que(cant_stock,0)
    precio_unit = int(input("Ingrese el precio unitario: $"))#funcion para validar mayores que un numero(1)
    precio_unit=validar_mayor_que(precio_unit,1)
    producto=[codigo,descripcion,cant_stock,precio_unit]
    matriz_productos.append(producto)
    print("Producto agregado correctamente.")
    return matriz_productos

def modificar_producto(matriz_productos):
    id=int(input("Ingrese el código del producto a modificar: "))
    pos = buscar_id(matriz_productos,id)
    while pos==-1:
        print(" El código del producto es inválido")
        id = int(input("Vuelva a ingresar el código del producto: "))
        pos = buscar_id(matriz_productos,id)
    descripcion = input("Ingrese la nueva descripción del producto: ")
    cant_stock = int(input("Ingrese la nueva cantidad en stock: "))
    cant_stock=validar_mayor_que(cant_stock,0)#funcion para validar mayores que que un numero(0)
    precio_unit = int(input("Ingrese el nuevo precio unitario: $"))
    precio_unit=validar_mayor_que(precio_unit,1)#funcion para validar mayores que un numero(1)
    matriz_productos[pos][1] = descripcion
    matriz_productos[pos][2] = cant_stock
    matriz_productos[pos][3] = precio_unit

def dar_baja_producto(matriz_productos):
    
    print("Producto a eliminar:")
    print(mostrar_matriz_cuadro(encabezados_productos, matriz_productos))
    id_producto=int(input("Ingrese el ID del producto a dar de baja : "))
    pos=buscar_id(matriz_productos,id_producto)
    while pos==-1:
        print("Error el ID ingresado no es valido")
        id_producto = int(input("Vuelva a ingresar el ID del producto: "))
        pos = buscar_id(matriz_productos,id_producto)
    for i in range(len(matriz_productos[0])):
        print(matriz_productos[pos][i], end="\t")
    print()
    confirmacion = int(input("¿Está seguro que desea dar de baja este producto? 1 para si o 2 para no: "))
    if confirmacion==1:
        matriz_productos.pop(pos)
        enter=input("Presione Enter para continuar y volver al menu")
    elif confirmacion==2:
        print("Operación cancelada. El producto no fue dado de baja.")
        enter=input("Presione Enter para continuar y volver al menu")
    return matriz_productos

def detalle_medicamento(matriz):
    print("Listado de medicamentos:")
    print(mostrar_matriz_cuadro(encabezados_productos, matriz_productos))
    id_med = int(input("Ingrese ID del medicamento a saber su detalle: "))
    pos_id = buscar_id(matriz, id_med)
    #print(pos_id)
    while pos_id == -1:
        id_med = int(input("Error. Ingrese ID del medicamento a saber su detalle: "))
        pos_id = buscar_id(matriz, id_med)
    print("Medicamento seleccionado :",matriz[pos_id][1])
    if re.findall("zina$", matriz[pos_id][1].lower()):
        print("Medicamento antihistamínico de segunda generacion,uso para sintomas de alergias.") 
    elif re.findall("mol$", matriz[pos_id][1].lower()):
        print("Medicamento analgesico y antipiretico,uso para dolor leve a moderado y fiebre.")
    elif re.findall("eno$", matriz[pos_id][1].lower()):
        print("Medicamento reduce la inflamacion en tejidos. ")
    elif re.findall("zol$", matriz[pos_id][1].lower()):
        print("Medicamento para reducir la produccion de acido en el estomago.")
    elif re.findall("lina$", matriz[pos_id][1].lower()):
        print("Medicamento para tratar infecciones bacterianas.")
    else:
        print("No se puede saber especificamente su tipo")
