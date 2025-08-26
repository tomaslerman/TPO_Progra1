    
def login(matriz_login):
    print("Bienvenido al sistema de gestión de farmacia.")
    usuario = pedir_usuario()

    contrasena = pedir_contrasena()

    lista_contra=[dato for dato in matriz_login if dato[0] == usuario and dato[1] == contrasena]
    while len(lista_contra)==0:
        print("Usuario o contraseña incorrecta. Ingrese nuevamente su usuario y contraseña: ")
        usuario = pedir_usuario()

        contrasena = pedir_contrasena()
  
        lista_contra=[dato for dato in matriz_login if dato[0] == usuario and dato[1] == contrasena]
    print("Login ingresado correctamente para el usuario:", usuario)
    menu_principal()

def pedir_usuario():
    usuario = input("Ingrese usuario: ").strip()
    while not usuario.isalpha():
        print("El usuario debe contener solo letras.")
        usuario = input("Ingrese usuario nuevamente: ").strip()
    return usuario

def pedir_contrasena():
    contrasena = input("Ingrese contraseña: ").strip()
    while not contrasena.isalnum():
        print("La contraseña debe contener solo caracteres alfanuméricos.")
        contrasena = input("Ingrese contraseña nuevamente: ").strip()
    return contrasena

def agregar_usuario(matriz_login):
    usuario = input("Ingrese nuevo usuario: ")
    while not usuario.isalpha():
        print("El usuario debe contener solo letras.")
        usuario = input("Ingrese nuevamente el usuario: ")
        print("El usuario :", usuario,"fue ingresado correctamente.")
    contrasena= input("Ingrese nueva contraseña: ")
    while not contrasena.isalnum():
        print("La contraseña debe contener solo caracteres alfanuméricos.")
        contrasena= input("Ingrese nuevamente contraseña: ")
    matriz_login.append([usuario, contrasena])
    print("Usuario agregado correctamente.")      
    opcion = int(input("Ingrese una opción 1. Agregar usuario, 2. Eliminar usuario, 3. Modificar usuario, -1. Volver a menu: "))
    opcion = validar_opcion(opcion, 1, 3, encabezados_login)
    while opcion==-1:
        print("Volviendo al menú principal...")
        menu_principal()

def eliminar_usuario(matriz_login):
    datos=input("Presione 1 si no recuerda el usuario a eliminar:")
    if datos=="1":
        mostrar_matriz(encabezado_contra, matriz_login)
    usuario = input("Ingrese el usuario a eliminar: ")
    pos = buscar_id(matriz_login, usuario)
    while pos == -1:
        print("El usuario no existe.")
        usuario = input("Vuelva a ingresar el usuario a eliminar: ")
        pos = buscar_id(matriz_login, usuario)
    matriz_login.pop(pos)
    print("Usuario eliminado correctamente.")
    opcion = int(input("Ingrese una opción 1. Agregar usuario, 2. Eliminar usuario, 3. Modificar usuario, -1. Volver a menu: "))
    opcion = validar_opcion(opcion, 1, 3, encabezados_login)
    while opcion==-1:
        print("Volviendo al menú principal...")
        menu_principal()   

def modificar_usuario(matriz_login):
    datos=input("Presione 1 si no recuerda el usuario a eliminar:")
    if datos=="1":
        mostrar_matriz(encabezado_contra, matriz_login)
    usuario = input("Ingrese el usuario a modificar: ")
    fila=[dato for dato in matriz_login if dato[0] == usuario]
    while len(fila)==0:
        print("El usuario no existe.")
        usuario = input("Vuelva a ingresar el usuario a modificar: ")
        fila=[dato for dato in matriz_login if dato[0] == usuario]
    pos=matriz_login.index(fila[0])
    nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ") 
    while not nuevo_usuario.isalpha():
        print("El usuario debe contener solo letras.")
        nuevo_usuario = input("Ingrese nuevamente el nuevo nombre de usuario: ")
    nueva_contrasena= input("Ingrese nueva contraseña: ") 
    while not nueva_contrasena.isalnum():
        print("La contraseña debe contener solo caracteres alfanuméricos.")
        nueva_contrasena= input("Ingrese nuevamente contraseña: ")
    matriz_login[pos][0] = nuevo_usuario
    matriz_login[pos][1] = nueva_contrasena
    print("Usuario modificado correctamente")
    opcion = int(input("Ingrese una opción 1. Agregar usuario, 2. Eliminar usuario, 3. Modificar usuario, -1. Volver a menu: "))
    opcion = validar_opcion(opcion, 1, 3, encabezados_login)
    while opcion==-1:
        print("Volviendo al menú principal...")
        menu_principal()
    
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

def agregar_cliente(matriz):
    cliente = []
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese edad: "))
    obra_social = ingresar_id_obra_social(matriz_obras_sociales,encabezados_obras_sociales)#funcion para pedir obra social
    telefono = int(input("Ingrese un número de teléfono:"))
    id_cliente = len(matriz) + 1  
    cliente.append(id_cliente, obra_social, nombre, edad, telefono)
    matriz.append(cliente)

def modificar_cliente(matriz_clientes, matriz_obras_sociales, encabezados_obras_sociales):
    id_cliente = int(input("Ingrese el ID del cliente a modificar: "))
    pos = buscar_id(matriz_clientes, id_cliente)
    while pos == -1:
        print("El ID del cliente es inválido")
        id_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
        pos = buscar_id(matriz_clientes, id_cliente)
    nombre = input("Ingrese el nuevo nombre del cliente: ")
    edad = int(input("Ingrese la nueva edad del cliente: "))
    obra_social = ingresar_id_obra_social(matriz_obras_sociales,encabezados_obras_sociales)  # función para ingresar ID de obra social
    telefono = int(input("Ingrese el nuevo número de teléfono del cliente: "))  
    matriz_clientes[pos][2] = nombre
    matriz_clientes[pos][3] = edad
    matriz_clientes[pos][1] = obra_social
    matriz_clientes[pos][4] = telefono
    print("Cliente modificado correctamente.")

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

def agregar_producto(matriz_productos):
    producto = []
    codigo = (len(matriz_productos) + 1)
    descripcion = input("Ingrese la descripción: ")
    cant_stock = int(input("Ingrese cantidad en stock: "))#funcion para validar mayores que que un numero(0)
    cant_stock=validar_mayor_que(cant_stock,0)
    precio_unit = int(input("Ingrese el precio unitario: $"))#funcion para validar mayores que un numero(1)
    precio_unit=validar_mayor_que(precio_unit,1)
    producto.append(codigo,descripcion,cant_stock,precio_unit)
    matriz_productos.append(producto)

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
    print("Producto modificado correctamente.")

def validar_mayor_que(valor, minimo):
    while valor <= minimo:
        print(f"El valor debe ser mayor que {minimo}")
        valor = int(input(f"Ingrese un valor mayor que {minimo}: "))
    return valor

def dar_baja_producto(matriz_productos):
    id_producto=int(input("Ingrese el ID del producto a dar de baja: "))
    pos=buscar_id(matriz_productos,id_producto)
    while pos==-1:
        print("Error el ID ingresado no es valido")
        id_producto = int(input("Vuelva a ingresar el ID del producto: "))
        pos = buscar_id(matriz_productos,id_producto)
    for i in range(len(matriz_productos[0])):
        print(matriz_productos[pos][i], end="\t")
    print()
    confirmacion = input("¿Está seguro que desea dar de baja este producto? 1 para si o 2 para no: ")
    if confirmacion==1:
        matriz_productos.pop(pos)
        enter=input("Presione Enter para continuar y volver al menu")
    else:
        print("Operación cancelada. El producto no fue dado de baja.")
        enter=input("Presione Enter para continuar y volver al menu")
    return matriz_productos    
        

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
                   
def buscar_id(matriz,dato):
    for i in range(len(matriz)):
        if matriz[i][0] == dato:
            return i
    return 

def agregar_obra_social(matriz_obras_sociales):
    obra_social = []
    id_o_s = len(matriz_obras_sociales) + 1
    nombre = input("Ingrese el nombre de la obra social: ")
    descuento = int(input("Ingrese el descuento que aplica la obra social: "))
    while descuento < 0 or descuento > 100:
        print("El descuento debe estar entre 0 y 100")
        descuento = int(input("Vuelva a ingresar el descuento: "))
    obra_social.append(id_o_s, nombre, descuento)
    matriz_obras_sociales.append(obra_social)

def modificar_obra_social(matriz_obras_sociales):
    id_obra_social = int(input("Ingrese el ID de la obra social a modificar: "))
    pos = buscar_id(matriz_obras_sociales, id_obra_social)
    while pos == -1:
        print("El ID de la obra social es inválido")
        id_obra_social = int(input("Vuelva a ingresar el ID de la obra social: "))
        pos = buscar_id(matriz_obras_sociales, id_obra_social)
    nombre = input("Ingrese el nuevo nombre de la obra social: ")
    descuento = int(input("Ingrese el nuevo descuento que aplica la obra social: "))
    while descuento < 0 or descuento > 100:
        print("El descuento debe estar entre 0 y 100")
        descuento = int(input("Vuelva a ingresar el descuento: "))
    matriz_obras_sociales[pos][1] = nombre
    matriz_obras_sociales[pos][2] = descuento
    print("Obra social modificada correctamente.")
    
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

def menu_principal():
    opcion = 0
    while opcion != -1:
        print("Menu Principal")
        mostrar_encabezado(encabezados_menu)
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:  # Ventas
            submenu_ventas()
        elif opcion == 2:  # Inventario
            submenu_inventario()
        elif opcion == 3:  # Clientes
            submenu_clientes()
        elif opcion == 4:  # Reportes
            submenu_reportes()
        elif opcion == -1:  # Terminar programa
            print("Programa finalizado.")
        else:
            print("Opción no válida. Intente nuevamente.")

def submenu_ventas():
    opcion = 0
    while opcion != -1:
        print("Submenú Ventas")
        mostrar_encabezado(encabezados_submenu_ventas)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_submenu_ventas)
        if opcion == 1:  # Agregar venta
            agregar_venta_y_detalle(matriz_ventas)
        elif opcion == 2:  # Modificar detalle de venta
            modificar_venta(matriz_detalle_ventas)
        elif opcion == 3:  # Dar baja venta
            dar_baja_elementos(matriz_ventas)
        elif opcion == 4:  # Mostrar lista completa
            mostrar_matriz(matriz_ventas)
        elif opcion == -1:  # Volver al menú principal
            print("Volviendo al menú principal.")
        else:
            print("Opción no válida. Intente nuevamente.")

def agregar_venta_y_detalle(matriz):
    venta = []
    id_venta = len(matriz) + 1
    fecha = fechaYvalidacion()
    id_cliente = int(input("Ingrese el ID del cliente: "))
    pos_cliente = buscar_id(matriz_clientes, id_cliente)
    while pos_cliente == -1:
        print("Error! El ID del cliente es inválido")
        id_cliente = int(input("Vuelva a ingresar el ID del cliente: "))
        pos_cliente = buscar_id(matriz_clientes, id_cliente)
    total = int(input("Ingrese el total de la venta: "))
    venta.append(id_venta, fecha, id_cliente, total)
    matriz.append(venta)

def modificar_venta(matriz):
    id_venta = int(input("Ingrese el ID de la venta a modificar: "))
    pos = buscar_id(matriz, id_venta)
    while pos == -1:
        print("El ID de la venta es inválido")
        id_venta = int(input("Vuelva a ingresar el ID de la venta: "))
        pos = buscar_id(matriz, id_venta)
    fecha = fechaYvalidacion()
    total = int(input("Ingrese el nuevo total de la venta: "))
    matriz[pos][1] = fecha
    matriz[pos][3] = total
    print("Venta modificada correctamente.")

def submenu_inventario():
    opcion = 0
    while opcion != -1:
        print("Submenú Inventario")
        mostrar_encabezado(encabezados_submenu_inventario)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_submenu_inventario)
        if opcion == 1:  # Agregar producto
            agregar_producto()
        elif opcion == 2:  # Modificar Producto
            modificar_producto()
        elif opcion == 3:  # Dar baja producto
            dar_baja_elementos(matriz_productos)
        elif opcion == 4:  # Mostrar lista completa
            mostrar_matriz(matriz_productos)
        elif opcion == -1:  # Volver al menú principal
            print("Volviendo al menú principal.")
        else:
            print("Opción no válida. Intente nuevamente.")

def submenu_clientes():
    opcion = 0
    while opcion != -1:
        print("Submenú Clientes")
        mostrar_encabezado(encabezados_submenu_clientes)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_submenu_clientes)
        if opcion == 1:  # Agregar cliente
            agregar_cliente(matriz_clientes)
        elif opcion == 2:  # Modificar cliente
            modificar_cliente(matriz_clientes)
        elif opcion == 3:  # Dar baja cliente
            dar_baja_elementos(matriz_clientes)
        elif opcion == 4:  # Mostrar lista completa
            mostrar_matriz(matriz_clientes)
        elif opcion == -1:  # Volver al menú principal
            print("Volviendo al menú principal.")
        else:
            print("Opción no válida. Intente nuevamente.")

def submenu_reportes():
    opcion = 0
    while opcion != -1:
        print("Submenú Reportes")
        mostrar_encabezado(encabezados_sub_menu_reportes)
        opcion = int(input("Seleccione una opción: "))
        opcion = validar_opcion(opcion, 1, 4, encabezados_sub_menu_reportes)
        if opcion == 1:  # Estadística de ventas
            estadisticas_ventas()
        elif opcion == -1:  # Volver al menú principal
            print("Volviendo al menú principal.")
        else:
            print("Opción no válida. Intente nuevamente.")

def buscar_por_nombre(matriz, nombre, columna, encabezados):
    resultados = [fila for fila in matriz if nombre.lower() in fila[columna].lower()]
    if resultados:
        mostrar_matriz_cuadro(encabezados, resultados)
    else:
        print("No se encontraron coincidencias.")

def estadisticas_ventas(matriz_ventas):
    total_ventas = len(matriz_ventas)
    suma_total = sum([venta[3] for venta in matriz_ventas])
    promedio = suma_total / total_ventas if total_ventas > 0 else 0
    print(f"Cantidad de ventas: {total_ventas}")
    print(f"Total vendido: ${suma_total}")
    print(f"Promedio por venta: ${promedio:.2f}")


#programa principal
encabezado_contra=["Usuario","Contraseña"]
encabezados_menu = ["1. Ventas","2. Inventario","3. Clientes","4. Reportes","-1. Terminar programa"]
encabezados_submenu_ventas = ["1. Agregar venta","2. Modificar venta","3. Dar baja venta","4. Mostrar lista completa", "-1. Volver a menu"]
encabezados_submenu_inventario = ["1. Agregar producto","2. Modificar Producto","3. Dar baja producto","4. Mostrar lista completa", "-1. Volver a menu"]
encabezados_submenu_clientes = ["1. Agregar cliente","2. Modificar Cliente","3. Dar baja cliente","4. Mostrar lista completa", "-1. Volver a menu"]
encabezados_sub_menu_reportes = ["Estadística de ventas", "-1. Volver a menu"]
encabezados_ventas = ["id_venta","fecha","id_cliente","total"]

matriz_login=[["stephy","uade1010"],
              ["tomas","uade2020"],
              ["matias","uade3030"],
              ["lourdes","uade4040"]]
encabezados_ventas = ["id_venta","fecha","id_cliente","total"]
matriz_ventas = [[1, "2023-10-01", 1, 150],
                 [2, "2023-10-02", 2, 200],
                 [3, "2023-10-03", 1, 300],
                 [4, "2023-10-04", 3, 250],
                 [5, "2023-10-05", 2, 400]]
encabezados_productos = ["id_producto", "descripcion", "stock", "precio_unitario"]
matriz_productos = [[1, "Paracetamol", 1, 10],
                    [2, "Ibuprofeno", 3, 15],
                    [3, "Amoxicilina", 2, 20],
                    [4, "Omeprazol", 5, 25],
                    [5, "Cetirizina", 4, 30]]
encabezados_recetas = ["id_receta", "id_producto", "fecha", "medico","cantidad"]
matriz_recetas = [
    [1, 1, "2023-10-01", "Dr. Perez", 2],
    [2, 2, "2023-10-02", "Dr. Gomez", 1],
    [3, 3, "2023-10-03", "Dr. Lopez", 3],
    [4, 4, "2023-10-04", "Dr. Martinez", 1],
    [5, 5, "2023-10-05", "Dr. Fernandez", 4]
]
encabezados_clientes = ["id_cliente","id_obra_social", "nombre","edad", "telefono"]
matriz_clientes = [
    [1, 1, "Juan Perez", 30, "123456789"],
    [2, 2, "Maria Gomez", 25, "987654321"],
    [3, 3, "Carlos Lopez", 40, "456789123"],
    [4, 4, "Ana Martinez", 35, "321654987"],
    [5, 5, "Luis Fernandez", 28, "159753486"]
]
encabezados_detalle_ventas = ["id_venta", "id_receta",  "subtotal"]
matriz_detalle_ventas = [
    [1, 1, 100],
    [1, 2, 150],
    [3, 3, 200],
    [4, 4, 250],
    [5, 5, 300]
    ]
encabezados_obras_sociales = ["id_obra_social", "nombre", "descuento"]
matriz_obras_sociales = [
    [1, "Osde", 10],
    [2, "Hospital italiano", 15],
    [3, "Medife", 20],
    [4, "Omint", 5],
    [5, "Osecac", 12]
]

login(matriz_login)  # Llamada a la función de login
menu_principal()  # Llamada al menú principal para iniciar el programa


    
