# Para aplicar en los ID
print("\nzfill:")
# cadena.zfill(ancho)
n = 25
cad = str(n).zfill(6)
print(cad) # 000025

# Para buscar un valor en una lista que no sea ID
vocales = ['a','e','i','o','u']
pos_i = vocales.index('i') # Busca la posición de la primera aparición del valor. Se le puede pasar un inicio y fin para buscar en un rango.
print("Posición de i:", pos_i) # Posición de i: 2

# Para estadísticas
nombres = ["Ana", "Luis", "Pedro", "Ana", "Carlos", "Ana", "Luis"]
cantidad_ana = nombres.count("Ana") # Cuenta cuántas veces aparece "Ana" en la lista
print("Apariciones de 'Ana':", cantidad_ana) # Apariciones de 'Ana': 3

# Para total de venta
suma_total = sum(numeros) # Suma de todos los elementos

# Podeos usar para busquedas alfabéticas
print("Recorrer parcialmente una lista utilizando rebanadas:")
lista = [19, 23, 48, 19, 38, 9]
for i in lista:
    print(i, end=" ") # 19 23 48 19 38 9 
print()
for i in lista[2:5]:
    print(i, end=" ") # 48 19 38
print()

# Para limpiar cadenas
# cadena.strip([caracteres]), cadena.lstrip([caracteres]), cadena.rstrip([caracteres])
print("\nstrip, lstrip y rstrip:")
cadena = "  Hola, mundo!  "
limpia = cadena.strip() # Elimina espacios en blanco al inicio y al final
print(limpia) # "Hola, mundo!"

cadena = "++Hola, mundo!--"
limpia = cadena.strip("+-!") # Elimina los caracteres '+' y '-' al inicio y al final
print(limpia)  # "Hola, mundo"

#Para alinear cadenas
# cadena.center(ancho, [relleno])
# cadena.ljust(ancho, [relleno])
# cadena.rjust(ancho, [relleno])
print("\ncenter, ljust y rjust:")
cadena = "Python"
print(cadena.center(20, '*')) # *******Python*******
print(cadena.ljust(20, '-')) # Python--------------
print(cadena.rjust(20, '+')) # ++++++++++++++Python

#Formato moneda
formatoMoneda = lambda valor: f'${valor:,.2f}'

#Formato porcentaje
formatoPorcentaje = lambda valor: f'{valor:.2f}%'