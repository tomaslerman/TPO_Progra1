from .funciones_generales import buscar_id

def ventas_de_x_cliente(id_cliente):
    try:
        arch_clientes = open("clientes.txt", "r", encoding="utf-8")
        matriz_clientes = [linea.strip().split(";") for linea in arch_clientes]
    except FileNotFoundError:
        print("Error! El archivo de clientes no existe.")
    finally:
        try:
            arch_clientes.close()
        except:
            print("Error al cerrar el archivo de clientes.")
    pos_cliente = buscar_id(matriz_clientes, id_cliente)
    if pos_cliente == -1:
        print("Error! El ID del cliente es inválido.")
        return
    print(f"Ventas del cliente {matriz_clientes[pos_cliente][2]} (ID {id_cliente}):")
    try:
        arch_ventas = open("ventas.txt", "r", encoding="utf-8")
        matriz_ventas = [linea.strip().split(";") for linea in arch_ventas]
    except FileNotFoundError:
        print("Error! El archivo de ventas no existe.")
        return
    finally:
        try:
            arch_ventas.close()
        except:
            print("Error al cerrar el archivo de ventas.")
    ventas_cliente = [venta for venta in matriz_ventas if venta[2] == id_cliente]
    if not ventas_cliente:
        print("No hay ventas registradas para este cliente.")
        return
    print(f"{'ID Venta':<10}{'Fecha':<15}{'Total':<10}")
    for venta in ventas_cliente:
        print(f"{venta[0]:<10}{venta[1]:<15}${venta[3]:<10.2f}")

#Programa principal para probar la función
ventas_de_x_cliente(1)