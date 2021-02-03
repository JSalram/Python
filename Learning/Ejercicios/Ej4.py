# Ejercicio 4

listaNumeros = [10, 14, 11, 10, 12, 8, 7, 8, 10, 12, 14, 15]


def recortaLista(lista, tamanno):
    if tamanno >= 0:
        lista.sort(reverse=True)
        subLista = []

        i = 0
        while i < tamanno and i < len(lista) - 1:
            if lista[i] not in subLista:
                subLista.append(lista[i])
                i += 1
            else:
                tamanno += 1
                i += 1

        subLista.sort()
        return subLista
    else:
        print("El tamaño debe ser mayor que 0")
        exit()


tamanno = input("Indica el tamaño que deseas que tenga la lista: ")
try:
    tamanno = int(tamanno)
except ValueError:
    print("El tamaño debe ser un número entero")
    exit()
print(recortaLista(listaNumeros, tamanno))
