# Método de la burbuja
## Ascendente
lista = [4, 6, 9, 8, 4, 2, 1]

for i in lista:
    for j in range(len(lista) - 1):
        k = j + 1

        if lista[j] > lista[k]:
            temp = lista[j]
            lista[j] = lista[k]
            lista[k] = temp

print(lista)


## Descendente
lista = [4, 6, 9, 8, 4, 2, 1]

for i in lista:
    # El error era que necesitaba llegar hasta 0,
    # ya que no se cuenta la posición 0 para j pero sí para k
    # y no terminaba de ordenarlo por completo por ello
    for j in range(len(lista) - 1, 0, -1):
        k = j - 1

        if lista[j] < lista[k]:
            temp = lista[j]
            lista[j] = lista[k]
            lista[k] = temp
    print(lista)

print(lista)


# =============================================================================================


# Método de selección
lista = [4, 6, 9, 8, 4, 2, 1]
print("INICIO: " + str(lista))

for i in range(len(lista)):
    menor = lista[i]
    pos = i

    for j in range(i + 1, len(lista)):
        if lista[j] < menor:
            menor = lista[j]
            pos = j

    lista.insert(i, menor)
    del lista[pos + 1]

print("FIN: " + str(lista))


# =============================================================================================


# Método de inserción
## Cadenas
def sustituyeCaracter(cadena, caracterASustituir, caracterSustituto):
    cadSust = ""
    for letra in cadena:
        if letra == caracterASustituir:
            cadSust += caracterSustituto
        else:
            cadSust += letra

        print(cadSust)

    return cadSust


cadena = "Hola Mundo"
print(sustituyeCaracter(cadena, "o", "a"))


## Listas
lista = [0, 3, 2, 1]
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


# =============================================================================================


# Busqueda binaria
def busquedaBinaria(lista, obj):
    encontrado = False
    ini = 0
    fin = len(lista) - 1
    pos = -1

    while ini <= fin and not encontrado:
        centro = (ini + fin) // 2
        if obj == lista[centro]:
            encontrado = True
            pos = centro
        elif obj < lista[centro]:
            fin = centro - 1
        else:
            ini = centro + 1

    return pos
