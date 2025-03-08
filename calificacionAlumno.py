
calificacion = int(input("Ingrese la calificación numérica del estudiante (entre 0 y 100): "))

if 90 <= calificacion <= 100:
    print("A - Excelente")
elif 80 <= calificacion <= 89:
    print("B - Muy bien")
elif 70 <= calificacion <= 79:
    print("C - Aprobado")
elif 60 <= calificacion <= 69:
    print("D - Pasable")
elif 0 <= calificacion < 60:
    print("F - No aprobado")
else:
    print("La calificación ingresada no es válida, debe estar entre 0 y 100.")