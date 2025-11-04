opciones_modificacion_ventas = {
        1: "Fecha",
        2: "Cliente",
        3: "Producto/Receta"
    }

'''
DATOS BACKUP:

clientes.json
{
    "1": {
        "obra_social": 1,
        "nombre": "JuanPerez",
        "edad": 30,
        "tel": "123456789",
        "estado": "Active"
    },
    "2": {
        "obra_social": 2,
        "nombre": "MariaGomez",
        "edad": 45,
        "tel": "987654321",
        "estado": "Inactive"
    },
    "3": {
        "obra_social": 3,
        "nombre": "CarlosLopez",
        "edad": 40,
        "tel": "456789123",
        "estado": "Active"
    },
    "4": {
        "obra_social": 4,
        "nombre": "AnaMartinez",
        "edad": 35,
        "tel": "321654987",
        "estado": "Inactive"
    },
    "5": {
        "obra_social": 5,
        "nombre": "LuisFernandez",
        "edad": 28,
        "tel": "159753486",
        "estado": "Active"
    }
}

obras_sociales.json
{
    "1": {
        "nombre": "Osde",
        "descuento": 10
    },
    "2": {
        "nombre": "Hospitalitaliano",
        "descuento": 15
    },
    "3": {
        "nombre": "Medife",
        "descuento": 20
    },
    "4": {
        "nombre": "Omint",
        "descuento": 5
    },
    "5": {
        "nombre": "Osecac",
        "descuento": 12
    }
}

productos.json
{
    "1": {
        "descripcion": "Paracetamol",
        "stock": 100,
        "precio": 50
    },
    "2": {
        "descripcion": "Ibuprofeno",
        "stock": 3,
        "precio": 15
    },
    "3": {
        "descripcion": "Amoxicilina",
        "stock": 2,
        "precio": 20
    },
    "4": {
        "descripcion": "Omeprazol",
        "stock": 5,
        "precio": 25
    },
    "5": {
        "descripcion": "Cetirizina",
        "stock": 4,
        "precio": 30
    }

ventas.txt
1;2023-10-01;1;150
2;2023-10-02;2;200
3;2023-10-03;1;300
4;2023-10-04;3;250
5;2023-10-05;2;400

detalle_ventas.txt
1;1;100
1;2;150
3;3;200
4;4;250
5;5;300

encabezados_modulos.json
{
    "ventas" : {
        "1": "ID",
        "2": "Fecha",
        "3": "ID Cliente",
        "4": "Total"
    },

    "productos" : {
        "1": "ID Producto",
        "2": "Descripción",
        "3": "Stock",
        "4": "Precio Unitario"
    },

    "recetas" : {
        "1": "ID Receta",
        "2": "ID Producto",
        "3": "Fecha",
        "4": "Médico",
        "5": "Cantidad"
    },

    "clientes" : {
        "1": "ID Cliente",
        "2": "ID Obra Social",
        "3": "Nombre",
        "4": "Edad",
        "5": "Teléfono",
        "6": "Estado"
    },

    "detalle_ventas" : {
        "1": "ID Venta",
        "2": "ID Receta",
        "3": "Subtotal"
    },
    "obras_sociales" : {
        "1": "ID Obra Social",
        "2": "Nombre",
        "3": "Descuento"
    }
}

encabezados_submenus.json
{
   {
    "contra" : {
        "1" : "Usuario",
        "2": "Contraseña"
    },
    "menus": {
        "1": "Ventas",
        "2": "Inventario",
        "3": "Clientes",
        "4": "Busquedas",
        "5": "Reportes",
        "-1": "Terminar programa"
    },
    "encabezados_menu": {
        "1": "1. Ventas",
        "2": "2. Inventario",
        "3": "3. Clientes",
        "4": "4. Busquedas",
        "5": "5. Reportes",
        "-1": "-1. Terminar programa"
    },
    "encabezados_submenu_ventas": {
        "1": "1. Agregar venta",
        "2": "2. Modificar venta",
        "3": "3. Dar baja venta",
        "4": "4. Mostrar lista completa",
        "-1": "-1. Volver a menu"
    },
    "encabezados_submenu_inventario": {
        "1": "1. Agregar producto",
        "2": "2. Modificar Producto",
        "3": "3. Dar baja producto",
        "4": "4. Mostrar lista (sólo activos)",
        "5": "5. Detalle de medicamento",
        "-1": "-1. Volver a menu"
    },
    "encabezados_submenu_clientes": {
        "1": "1. Agregar cliente",
        "2": "2. Modificar Cliente",
        "3": "3. Dar baja cliente",
        "4": "4. Mostrar lista completa",
        "-1": "-1. Volver a menu"
    },
    "encabezados_sub_menu_reportes": {
        "1": "Estadística de ventas",
        "-1": "-1. Volver a menu"
    }
}

login.json
{
    "stephy": "uade1010",
    "tomas": "uade2020",
    "matias": "uade3030",
    "lourdes": "uade4040"
}
'''