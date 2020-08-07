# Bucle While --> Bucle indefinido
## Bucle numérico
i = 0
while i <= 10:
    print(i)
    i += 1  # i = i + 1


# =============================================================================================


## Bucle booleano
seguir = True

i = 0
while seguir:
    print(i)
    i += 1
    if i == 5:
        seguir = False


# =============================================================================================


## Bucle con input
seguir = True

while seguir:
    print("1. Sumar\n2. Restar\n3. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Suma")
    elif opcion == 2:
        print("Resta")
    elif opcion == 3:
        seguir = False
    else:
        print("Opción incorrecta")


# =============================================================================================


## Bucle con cadenas
cad = input("¿Deseas continuar? (y/n)\n")

while cad != "y" and cad != "n":
    cad = input("Opción incorrecta. Vuelve a intentarlo (y/n)\n")


# =============================================================================================


## Bucle float (no preciso)
inicial = 10.5
objetivo = 5.2
distancia = 0

while inicial > objetivo:
    inicial -= 0.1
    distancia += 0.1
    print(distancia)

### Bucle float (usando el método round())
inicial = 10.5
objetivo = 5.2
distancia = 0

while inicial > objetivo:
    inicial = round(inicial - 0.1, 1)
    distancia = round(distancia + 0.1, 1)
    print(distancia)

### round(numero [,decimales])
n = round(17.5674, 2)
print(n)
