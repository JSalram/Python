# Ejercicio 1

def diagonales(matriz):
    lista = []
    diagonal1 = 0
    diagonal2 = 0

    i = 0
    j = len(matriz) - 1
    while i < len(matriz):
        diagonal1 += matriz[i][i]
        diagonal2 += matriz[i][j]
        j -= 1
        i += 1

    lista.append(diagonal1)
    lista.append(diagonal2)

    return lista


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

print("Sumas diagonales: " + str(diagonales(matriz)))
