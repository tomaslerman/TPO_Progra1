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
