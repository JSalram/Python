## Busqueda binaria
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


# lista = list(range(31))  ## [0, 1, 2, ..., 30]
# print(busquedaBinaria(lista, 20))


alumnos = ["Juan", "Pepe", "Mario", "Antonio", "Marta", "Laura", "Irene"]
alumnos.sort()
# print(alumnos)
# print(busquedaBinaria(alumnos, "Juan"))


# =============================================================================================


print("=============================================================================================")
## Ejercicio 1
"""
fechas = []

for i in range(9):
    fechas.append("1" + str(i + 1) + "/" + str(i + 1) + "/200" + str(i))

print(fechas)

dias = []
meses = []
annos = []

for f in fechas:
    fecha = f.split("/")
    dias.append(int(fecha[0]))
    meses.append(int(fecha[1]))
    annos.append(int(fecha[2]))


print("Elige una opción de búsqueda:")
print("1. Día               2. Mes")
print("3. Año")
opcion = int(input("Opción: "))

if opcion == 1:
    dia = int(input("Día a buscar: "))
    pos = busquedaBinaria(dias, dia)
    if pos == -1:
        print("No existe esa fecha")
    else:
        print(fechas[pos])
elif opcion == 2:
    mes = int(input("Mes a buscar: "))
    pos = busquedaBinaria(meses, mes)
    if pos == -1:
        print("No existe esa fecha")
    else:
        print(fechas[pos])
elif opcion == 3:
    anno = int(input("Año a buscar: "))
    pos = busquedaBinaria(annos, anno)
    if pos == -1:
        print("No existe esa fecha")
    else:
        print(fechas[pos])
else:
    print("Opción inválida")
"""


# =============================================================================================

"""
print("=============================================================================================")
## Ejercicio 2
def insercion(lista, listaOrd):

    while len(lista) > 0:
        mayor = lista[0]
        pos = 0

        for i in range(len(lista)):
            if len(lista[i]) > len(mayor):
                mayor = lista[i]
                pos = i

        del lista[pos]
        listaOrd.append(mayor)


frases = [
    "Más vale pájaro en mano que cientos volando",
    "Cuando el río suena, agua lleva",
    "Aunque la mona se vista de seda mona se queda",
    "No hay mal que por bien no venga",
    "De tal palo tal astilla"
]

listaOrd = []
insercion(frases, listaOrd)
for frase in listaOrd:
    print(frase)
"""


# =============================================================================================


print("=============================================================================================")
## Ejercicio 3
def seleccion(lista):
    for i in range(len(lista)):
        menor = lista[i]
        pos = i

        for j in range(i+1, len(lista)):
            if len(lista[j]) < len(menor):
                menor = lista[j]
                pos = j

        lista.insert(i, menor)
        del lista[pos + 1]


frases = [
    "Más vale pájaro en mano que cientos volando",
    "Cuando el río suena, agua lleva",
    "Aunque la mona se vista de seda mona se queda",
    "No hay mal que por bien no venga",
    "De tal palo tal astilla"
]


palabrasFrases = []
for frase in frases:
    palabrasFrases.append(frase.split(" "))

print("[")
for i in palabrasFrases:
    print("     " + str(i) + " ==> Palabras: " + str(len(i)))
print("]")


seleccion(palabrasFrases)

for frases in palabrasFrases:
    print(" ".join(frases))
