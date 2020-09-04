"PRACTICA DEL CORREO DE BUCLES"

"PRACTICA 1"

tabla = int(input("Introduzca un numero del 0 al 12\n"))

# El controlador de excepciones SIEMPRE se pone justo después de pedir aquello que queremos controlar
while tabla <= 0 or tabla > 12:
    tabla = int(input("Error, Valor incorrecto. Introduzca un numero del 0 al 12\n"))

i = 1
while i <= 12:
    res = i * tabla

    print("{} x {} = {}".format(tabla, i, res))

    i += 1



"PRACTICA 4"

print("Instrucciones: El siguiente programa esta hecho para sacar")
print("la media de una serie de numeros, por favor introduzca")
print("todos los numeros de su serie, una vez haya terminado")
print("por favor introduzca un numero negativo para cerrar el")
print("programa y brindar su resultado.")

numero = int(input("Introduzca un numero\n"))
cantidad = 0
suma = 0

while numero >= 0:
    suma += numero
    cantidad = cantidad + 1

    # Aquello que modifique la condición del bucle SIEMPRE se pone al final del mismo
    numero = int(input("Introduzca un numero\n"))


print(suma)
print(cantidad)

if cantidad > 0:
    media = suma / cantidad
    print(media)



"PRACTICA 5"

cantidad = int(input("¿Que cantidad de estudiantes hay en clase?\n"))

i = 0
reprobados = 0
aprobados = 0
# minimo = 6.75 ==> Es innecesario

while i < cantidad:
    nota = float(input("Nota del alumno: "))

    if nota < 6.75:
        reprobados = reprobados + 1

    if nota > 6.75:
        aprobados = aprobados + 1

    i += 1

print("Los estudiantes aprobados son " + str(aprobados))
print("Los estudiantes reprobados son " + str(reprobados))