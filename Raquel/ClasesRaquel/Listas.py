# Listas
## Definir lista vacía
lista = []

## Definir e insertar elementos
listaInt = [1, 2, 3, 4, 5]
listaFloat = [1.2, 3.5, 6.2]
listaString = ["Hola", "Adiós"]
listaBoolean = [True, False, True, True]

# Acceder a los elementos
listaElementos = ["Hola", "me", "llamo", "Javi"]
print(listaElementos[3])

cadenaCaracteres = "Hola me llamo Javi"
print(cadenaCaracteres[3])


# ==========================================================================


# Métodos de las listas
## .append(elemento)
listaAppend = [1, 2, 3, 4, 5]
listaAppend.append(6)
print(listaAppend)

## .insert(índice, elemento)
listaInsert = [1, 2, 3, 4, 5]
listaInsert.insert(0, 0)
listaInsert.insert(2, 24)
print(listaInsert)

## .index(elemento)
listaIndex = [1, 2, 6, 5, 6, 7, 8]
print("Posición del número 6: " + str(listaIndex.index(6)))

## .remove(elemento)
listaRemove = ["Javi", "Raquel", "Juan", "Patricia", "Juan"]
print(listaRemove)
listaRemove.remove("Juan")
print(listaRemove)

## .reverse()
listaReverse = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listaReverse.reverse()
print(listaReverse)

## .count(elemento)
listaCount = ["Javi", "Raquel", "Juan", "Patricia", "Juan", "Juan"]
print(listaCount.count("Juan"))

## .sort()
listaSort = [1, 6, 2, 7, 3, 5, 4]
listaSort.sort(reverse=True)
print(listaSort)


# ==========================================================================


# in / not in
cadena = "Hola me llamo Javi"
if "Javi" in cadena:
    print("Existe")
else:
    print("No existe")

listaIn = [2.5, 3.5, 4.6, 6.2]
if 2.5 in listaIn:
    print("Está dentro")
if 2.6 not in listaIn:
    print("No lo contiene")


# ==========================================================================


# min() y max()
listaMinMax = [1, 2, 3, 4, 5, 6]
print("Mínimo:", str(min(listaMinMax)))
print("Máximo:", str(max(listaMinMax)))

cadenaMinMax = "abcdefghijk"
print("Mínimo:", min(cadenaMinMax))
print("Máximo:", max(cadenaMinMax))


# ==========================================================================


# len() y range([inicio,] fin [,incremento])
cadenaLen = "AEIOU"
print(len(cadenaLen))

listaLen = [1, 2, 3, 4, 5, 6]
print(len(listaLen))

rango = list(range(5, 10, 2))
print(rango)


# ==========================================================================


# Cortes de lista [inicio:fin[:incremento]
cadenaCortes = "Hola me llamo Javi"
subCadena = cadenaCortes[14:]
print(subCadena)

listaCortes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
subLista = listaCortes[1:6]
print(subLista)


# ==========================================================================


# Incremento y más
listaCortes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(listaCortes[::-1])

print(listaCortes[:-2])

frase = "Ayer fui a comprar el pan"
print(frase[::2])
