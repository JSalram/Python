long = {}
pal = input("Palabra: ")

while pal != "fin":
    l = len(pal)
    if l not in long:
        long[l] = []

    long[l].append(pal)
    pal = input("Palabra: ")


for clave in long:
    cant = len(long[clave])
    print(f"Palabras de longitud {clave}: {cant}")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

long = {}
pal = input("Palabra: ")

while pal != "fin":
    l = len(pal)
    if l not in long:
        long[l] = 0

    long[l] += 1
    pal = input("Palabra: ")

print(long)

for clave in long:
    print(f"Palabras de longitud {clave}: {long[clave]}")
