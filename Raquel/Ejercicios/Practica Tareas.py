#Ejercicio 1 whatsapp
#
#n= str(input("¿Desea ver numeros pares o impares (par/impar)\n"))
#
#i=0
#if n == str("par"):
#    while i <= 10:
#        if i % 2 == 0:
#            print(i)
#    i+=1
#
#if n == str("impar"):
#    while i <= 10:
#        if i % 2 != 0:
#            print(i)
#    i+=1

#Ejercicios Tabla de multiplicar

# tabla= int(input("Ingrese el numero del cual desea ver la tabla de multiplicar\n"))
#
# multiplicador=0
# i=0
#
# while multiplicador <= 12:
#     print(str(tabla) + "x" + str(multiplicador) + "=" + str(tabla*multiplicador))
#     multiplicador += 1



#Escriba un programa que pida dos números enteros.
# El programa pedirá de nuevo el segundo número mientras
# no sea mayor que el primero. El programa terminará escribiendo los dos números.

"""
print("Escribe dos números, siendo el primero menor que el segundo")
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

while n1 > n2:
    print("ERROR - Recuerda que el primer número debe ser menor que el segundo")
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))

print("{a} y {b}".format(a=n1, b=n2))
"""



# Ejercicio alumnos
"""
cantidad = int(input("¿Que cantidad de estudiantes hay en clase?\n"))

i = 0
while i < cantidad:
    nota = float(input("Nota del alumno: "))
    
    if i == 0:
        menor = nota
        mayor = nota

    if nota < menor:
        menor = nota

    if nota > mayor:
        mayor = nota

    i += 1

print(menor)
"""