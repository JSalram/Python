# Recorrer estructuras
# While

s = "Hola"

i = 0
while i < len(s):
    letra = s[i]
    print(letra)
    i += 1

alumnos = ["Javier", "Adriana", "Manuel", "Patricia", "Jorge"]

i = 0
while i < len(alumnos):
    print(alumnos[i])
    i += 1

i = 0
while i <= 10:

    if i != 5:
        print(i)
    i += 1


# ==========================================================================


# For
### Recorriendo cadenas
for letra in "Hola":
    print(letra)

cadena = "Hola"
for letra in cadena:  # letra = cadena[i]
    print(letra)

"""
## Equivalente a:
i = 0
while i < len(cadena):
    cadena[i]
    i += 1
"""


### Recorriendo listas
for alumno in ["Javier", "Adriana", "Manuel", "Patricia", "Jorge"]:
    print(alumno)

alumnos = ["Javier", "Adriana", "Manuel", "Patricia", "Jorge"]
for alum in alumnos:  # alum = alumnos[i]
    print(alum)

"""
Equivalente a:
i = 0
while i < len(alumnos):
    print(alumnos[i])
    i += 1
"""


### Recorriendo range()
for i in range(10):
    print(i)

"""
## Equivalente a:
i = 0
while i < 10:
    print(i)
    i += 1
"""


### Recorriendo estructuras por posición con range()
alumnos = ["Javier", "Adriana", "Manuel", "Patricia", "Jorge"]
for i in range(len(alumnos)):  # ==> for i in range(5)
    print(alumnos[i])

"""
## Equivalente a:
i = 0
while i < len(alumnos):
    print(alumnos[i])
    i += 1
"""


# ==========================================================================


# Break y Continue

for i in range(11):
    if i % 2 != 0:
        continue    # Finaliza el ciclo y continúa dentro del bucle
    print(i)

while True:
    salir = input("¿Deseas salir? (s/n)\n")
    if salir == "s":
        break       # Fuerza la salida del bucle


# ==========================================================================


# Range([inicio,] fin [,incremento])

for i in range(0, 11, 2):
    print(i)

for i in range(1, 11, 2):
    print(i)
