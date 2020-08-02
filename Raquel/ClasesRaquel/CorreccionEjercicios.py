# Ejercicio de alumnos

alumnos = ["Javier", "Adriana", "Manuel", "Patricia", "Jorge"]
alumnos.sort()
print(alumnos)


# ==========================================================================


# Ejercicio de pares/impares

numeros = input("¿Desea números pares o impares?\n")

i = 0
while i <= 10:
    if numeros == "pares":
        if i % 2 == 0:
            print(i)
    elif numeros == "impares":
        if i % 2 != 0:
            print(i)
    i += 1

if numeros == "pares":
    i = 0
    while i <= 10:
        print(i)
        i += 2
elif numeros == "impares":
    i = 1
    while i <= 10:
        print(i)
        i += 2
