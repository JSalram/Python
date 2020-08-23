# Método de la burbuja
## Ascendente
## Descendente

"""
alumnos = ["Pepe", "Juan", "Lolo", "Maria", "María", "Rocío", "Lola"]
lista = [4, 6, 9, 8, 4, 2, 1]

for i in lista:
    for j in range(len(lista) - 1):
        k = j + 1

        if lista[j] > lista[k]:
            temp = lista[j]
            lista[j] = lista[k]
            lista[k] = temp

            temp2 = alumnos[j]
            alumnos[j] = alumnos[k]
            alumnos[k] = temp2

print(alumnos)
print(lista)
"""


# Método de selección

"""
lista = [3, 2, 1]

for i in range(len(lista)):
    menor = lista[i]
    pos = i

    for j in range(i, len(lista)):
        if lista[j] < menor:
            menor = lista[j]
            pos = j

    lista.insert(i, lista[pos])
    del lista[pos+1]
"""

# Método de inserción
## Cadenas
## Listas

"""
lista = [3, 2, 1]
listaOrd = []

while len(lista) > 0:
    menor = lista[0]
    pos = 0

    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            pos = i

    del lista[pos]
    listaOrd.append(menor)
"""