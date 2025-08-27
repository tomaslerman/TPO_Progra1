import Modulos
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
Modulos.Login.login(matriz_login)
Modulos.Funciones_generales.menu_principal()