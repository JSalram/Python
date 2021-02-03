# Ejercicio 3

lista = ["manzanas", "naranjas", 3.12, 45, "mandarinas", 1200, "fresas", "sandías", 12.1, "ciruelas"]


def clasificaCadenas(lista, orden=0):
    listaCadenas = []

    for i in lista:
        if isinstance(i, str):
            listaCadenas.append(i)

    if orden == 1:
        listaCadenas.sort()
    elif orden == -1:
        listaCadenas.sort(reverse=True)
    elif orden != 0:
        print("Parámetro de ordenación incorrecto")
        exit()

    return listaCadenas


def clasificaNumeros(lista, orden=0):
    listaNumeros = []

    for i in lista:
        if not isinstance(i, str):
            listaNumeros.append(i)

    if orden == 1:
        listaNumeros.sort()
    elif orden == -1:
        listaNumeros.sort(reverse=True)
    elif orden != 0:
        print("Parámetro de ordenación incorrecto")
        exit()

    return listaNumeros


cadenas = []
numeros = []
ordenar = input("¿Deseas ordenar las listas? (y / n ): ")
while ordenar != "y" and ordenar != "n":
    ordenar = input("Opción incorrecta. Vuelve a intentarlo (y / n ): ")

if ordenar == "y":
    print("Selecciona el orden en que deseas que aparezcan las listas: ")
    print("(1): Ascendente")
    print("(-1): Descendente")
    orden = input("Orden: ")
    try:
        orden = int(orden)
    except:
        print("El orden debe ser un numero entero")
        exit()
    while orden != 1 and orden != -1:
        orden = input("Opción incorrecta. Vuelve a intentarlo: ")
        try:
            orden = int(orden)
        except:
            print("El orden debe ser un numero entero")
            exit()
    cadenas = clasificaCadenas(lista, orden)
    numeros = clasificaNumeros(lista, orden)
else:
    cadenas = clasificaCadenas(lista)
    numeros = clasificaNumeros(lista)

print()
print("Lista cadenas: " + str(cadenas))
print("Lista números: " + str(numeros))
