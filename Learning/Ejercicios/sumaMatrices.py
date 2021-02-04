def printMatriz(a):
    for array in a:
        for num in array:
            print(num, end=" ")
        print()


def sumaMatrices(a, b):
    suma = []
    for y in range(len(a)):
        suma.append([])
        for x in range(len(a[y])):
            s = a[y][x] + b[y][x]
            suma[y].append(s)

    return suma


def pideMatrices():
    matriz = []
    for y in range(4):
        matriz.append([])
        for x in range(3):
            num = int(input(f"Posición ({x}, {y}): "))
            matriz[y].append(num)

    return matriz


A = B = pideMatrices()
s = sumaMatrices(A, B)
printMatriz(s)
print()
printMatriz(A)
