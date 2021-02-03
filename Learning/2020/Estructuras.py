# Recorrer estructuras
# While
lista = ["Rodolfo", "Javi", "Juan", "Pepe", "Juan", "Lola", "Juan"]

i = 0
while i < len(lista):
    if i == 3:
        i += 1

    print(str(i+1) + " - " + str(lista[i]))

    i += 1


# =============================================================================================


# For
listaAlumnos = ["Rodolfo", "Javi", "Juan", "Pepe", "Juan", "Lola", "Juan"]

for alumno in listaAlumnos:  # alumno ==> listaAlumnos[i]
    print(alumno)

lista = [3, 7, 1, 4, 2, 9, 0]

n = 0
for i in lista:
    print(i)
    n += i

print("Suma: " + str(n))


# =============================================================================================


# Range([inicio,] fin [,incremento])
## Break y Continue
lista = [3, 2, 7, 3, 1, 5]

for i in range(len(lista)):
    if i == 2:
        continue  # ==> Fuerza el avance al siguiente ciclo del bucle

    print(i, end=" - ")
    print(lista[i])


for i in range(len(lista)):
    if i == 2:
        break  # ==> Fuerza la salida del bucle

    print(i, end=" - ")
    print(lista[i])

