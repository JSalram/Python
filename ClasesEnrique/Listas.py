# Listas
## Definir lista vacía
lista = []

## Definir e insertar elementos
listaDefinida = [1, 2, 3, 4, 5]
cad = "Hola"
cadLista = ["H", "o", "l", "a"]


# =============================================================================================


# Acceder a los elementos
print(listaDefinida[3])
print(cad[0])

cad = input("Cadena: ")
i = 0
while i < len(cad):
    print(cad[i], end="")
    i += 1


# =============================================================================================


# Métodos de las listas
## .append(elemento) ==> Añade un elemento al final de la lista
lista = []
seguir = True
while seguir:
    alumno = input("Alumno: ")
    lista.append(alumno)
    print(lista)

    cad = input("¿Deseas salir? (y/n)\n")
    while cad != "y" and cad != "n":
        cad = input("Opción incorrecta. Vuelve a intentarlo (y/n)\n")
    if cad == "y":
        seguir = False

## .insert(índice, elemento) ==> Añade un elemento en la posición indicada
lista = [1, 2, 4, 5, 6, 7]
print(lista)
lista.insert(2, 3)
print(lista)

## .index(elemento) ==> Nos devuelve la posición de un elemento
lista = ["Rodolfo", "Javi", "Juan", "Pepe", "Juan", "Lola", "Juan"]
print(lista.index("Juan", 3, 5))

## .remove(elemento) ==> Le pasamos el elemento a borrar y elimina el primero que encuentra
lista = ["Rodolfo", "Javi", "Juan", "Pepe", "Juan", "Lola", "Juan"]
print(lista)
lista.remove("Juan")
print(lista)

## .reverse() ==> Le da la vuelta a la lista
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)

## .count(elemento) ==> Nos devuelve el número de veces que aparece un elemento
lista = ["Rodolfo", "Javi", "Juan", "Pepe", "Juan", "Lola", "Juan"]
print(lista.count("Juan"))

## .sort() ==> Ordena la lista
lista = [2, 6, 9, 3, 1, 7, 4]
lista.sort()
print(lista)
lista.sort(reverse=True)  # reverse ==> Parametro opcional para ordenarla de manera descendente
print(lista)


# =============================================================================================


# in / not in

# min() y max()

# len() y range([inicio,] fin [,incremento])

# Cortes de lista [inicio:fin[:incremento]
