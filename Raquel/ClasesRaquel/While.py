# Ejemplo de bucle
i = 0
while i <= 10:
    print(i)
    i = i + 1


# and / or
num = 10
if (num == 5 and num < 10) or num > 20:
    print("Es 5 y menor de 10")


# Bucle numérico
i = 0
while i <= 10:
    print(i, end=" - ")
    if i % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
    i += 1


# Bucle booleano
sigue = True
while sigue:
    print(i)
    if i >= 10:
        sigue = False
    i += 1


# Bucle con input
salir = "no"
while salir != "si":
    print("Sigues dentro")
    salir = input("¿Deseas salir? (si/no)\n")
    while salir != "si" and salir != "no":
        salir = input("Opción errónea. Vuelve a intentarlo (si/no): ")


# Bucle con cadenas
cadena = "Javi"
i = 0
while i < len(cadena):
    print(cadena[i], end=" ")
    i += 1


# Bucle float (no preciso)
objetivo = 25.5
inicial = 100
resto = 0

while inicial > objetivo:
    inicial = inicial - 0.1
    resto = resto + 0.1

print("Llegó")
print("La diferencia es de " + str(resto))

# Bucle float (usando el método round())
objetivo = 25.5
inicial = 100
resto = 0

while inicial > objetivo:
    inicial = round(inicial - 0.1, 1)
    resto = round(resto + 0.1, 1)

print("Llegó")
print("La diferencia es de " + str(resto))

# round(numero [,decimales])
decimal = 2.5
print(round(decimal))

# ToDo: error round
n = round(17.5)
print(n)
