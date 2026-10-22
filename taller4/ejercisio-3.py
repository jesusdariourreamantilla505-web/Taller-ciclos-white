suma = 0.0
cantidad = 0

print("Ingrese las notas(digite -99 para terminar )")
nota = float(input("Nota: "))

while nota != -99:
    suma = suma + nota 
    cantidad = cantidad + 1
    nota = float(input("Nota: "))

if cantidad > 0:
    promedio = suma / cantidad 
    print("Cantidad:", cantidad, "; promedio", promedio)
else:
    print("Cantidad: 0; Sin notas")