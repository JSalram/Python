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
cadena = "Hola"

for letra in cadena:  # letra = cadena[i]
    print(letra)

for letra in "Hola":
    print(letra)

alumnos = ["Javier", "Adriana", "Manuel", "Patricia", "Jorge"]

for alumno in alumnos:  # alumno = alumnos[i]
    print(alumno)

for alumno in ["Javier", "Adriana", "Manuel", "Patricia", "Jorge"]:
    print(alumno)

for i in range(10):
    print(i)


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