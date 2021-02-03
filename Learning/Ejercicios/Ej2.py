# Ejercicio 2
def sumatorio(matriz):
    filas = []
    columnas = []
    columna = 0

    for tam in matriz:
        sumaFilas = 0
        sumaColumnas = 0
        for i in tam:
            sumaFilas += i
        for j in matriz:
            sumaColumnas += j[columna]
        columna += 1
        columnas.append(sumaColumnas)
        filas.append(sumaFilas)

    return filas, columnas


tamanno = input("Tamaño de la matriz: ")
try:
    tamanno = int(tamanno)
except ValueError:
    print("Tamaño inválido")
    exit()

matriz = []
submatriz = []

i = 0
j = 0
indice = 1
while j < tamanno:
    num = input("Número " + str(indice) + ": ")
    try:
        num = int(num)
    except:
        print("Número inválido")
        exit()

    submatriz.append(num)
    i += 1
    indice += 1

    if i == tamanno:
        matriz.append(submatriz)
        submatriz = []
        i = 0
        j += 1

filas, columnas = sumatorio(matriz)

print("Suma filas: ", end="")
print(filas)
print("Suma columnas: ", end="")
print(columnas)