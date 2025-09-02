def validar_opcion(opcion,inicio,fin,encabezado):   
    while opcion !=-1 and opcion < inicio or opcion > fin:
        print("Debe ingresar rangos de opcion del ",inicio,"al",fin)
        mostrar_encabezado(encabezado)
        opcion=int(input("Ingrese nuevamente una opcion: "))
    return opcion

def mostrar_encabezado(encabezado):
    for i in range(len(encabezado)):
        print(encabezado[i])

def mostrar_matriz(titulos,matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for titulo in titulos:
        print(titulo,end="\t")
    print()
    for fila in range (filas):
        for columna in range (columnas):
            print(matriz[fila][columna],end="\t")
        print()

def mostrar_matriz_cuadro(encabezados, matriz):
    for i in range(len(encabezados)):
        print(f"{encabezados[i]:<20}", end="")
    print()
    for fila in matriz:
        for elemento in fila:
            print(f"{elemento:<20}", end="")
        print()

def ingresar_id_obra_social(matriz_obras_sociales,encabezados_obras_sociales):
    print("Obras sociales disponibles:")
    mostrar_matriz_cuadro(encabezados_obras_sociales, matriz_obras_sociales)
    id_obra_social = int(input("Ingrese el ID de la obra social: "))
    pos = buscar_id(matriz_obras_sociales, id_obra_social)
    while pos == -1:
        print("El ID de la obra social es inválido")
        id_obra_social = int(input("Vuelva a ingresar el ID de la obra social: "))
        pos = buscar_id(matriz_obras_sociales, id_obra_social)
    return id_obra_social

def validar_mayor_que(valor, minimo):
    while valor <= minimo:
        print(f"El valor debe ser mayor que {minimo}")
        valor = int(input(f"Ingrese un valor mayor que {minimo}: "))
    return valor

def fechaYvalidacion():
    anio = int(input("Ingrese año: "))
    while anio<=0 or anio>2025:
        print("Error! El año ingresado no es válido")
        anio = int(input("Vuelva a ingrese año: "))
    mes = int(input("Ingrese mes: "))
    while mes<1 or mes>12:
        print("Error! El mes ingresado no es válido")
        mes = int(input("Vuelva a ingresar el mes:"))
    dia = int(input("Ingrese día: "))
    if mes==2:
        while dia<1 or dia>29:
            print("Error! El día ingresado no es válido")
            dia = int(input("Vuelva a ingresar el día:"))
    elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        while dia<1 or dia>31:
            print("Error! El día ingresado no es válido")
            dia = int(input("Vuelva a ingresar el día:"))
    else:
        while dia<1 or dia>30:
            print("Error! El día ingresado no es válido")
            dia = int(input("Vuelva a ingresar el día:"))
    fecha = (dia,"/",mes,"/",anio)
    return fecha

def buscar_por_nombre(matriz, nombre, columna, encabezados):
    resultados = [fila for fila in matriz if nombre.lower() in fila[columna].lower()]
    if resultados:
        mostrar_matriz_cuadro(encabezados, resultados)
    else:
        print("No se encontraron coincidencias.")

def buscar_id(matriz,dato):
    i=0
    pos = -1
    encontro=False
    while i < len(matriz) and encontro==False:
        if matriz[i][0]==dato:
            encontro=True
            pos = i
        i+=1    
    return pos

def dar_baja_elementos(matriz):
    id_elemento = int(input("Ingrese el ID: "))
    pos = buscar_id(matriz,id_elemento)
    while pos==-1:
        print("Error! El ID ingresado es inválido")
        receta = int(input("Vuelva a ingresar el ID: "))
        pos = buscar_id(matriz,id_elemento)
    for i in range(len(matriz[0])):
        print(matriz[pos][i])
    confirmacion = int(input("Desea eliminar estos datos? (1 para SI o 2 para NO): "))
    if confirmacion == 1:
        matriz.pop(pos)
        enter = input("Dato eliminado exitosamente. Volviendo a menu...")
    else:
        print("Cancelando operación")
        enter = input("Volviendo a menu...")
    
def stock_por_agotar(matriz_productos):
    productos_agotarse=[fila for fila in matriz_productos if (fila[2])<=2]
    ordenar_stock=sorted(productos_agotarse,key=lambda fila: (fila[2]))
    print("Productos de stock proximos a agotarse :")
    print(f"{'ID':<5} {'Descripcion':<10}    {'Stock':<10}   {'Precio_Unitario':<10}")
    for p in ordenar_stock:
        print(f"{p[0]:<5} {p[1]:<10}      {p[2]:<10}       {p[3]:<10}  ")
