# Ejercicio 5
matriz = [[0, 8, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 5, 0, 0],
          [0, 0, 0, 0, 0]]


def coordenadas(matriz):
    diccionario = {}

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0:
                diccionario[i, j] = matriz[i][j]

    return diccionario


print(coordenadas(matriz))
