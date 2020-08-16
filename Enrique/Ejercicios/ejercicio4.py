seguir = True

while seguir:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))
    n1=float(input("Introduce un número: "))
    n2=float(input("Introduce otro número: "))

    if opcion == 1:
        print("La suma es: ", n1+n2)
    elif opcion == 2:
        print("La resta es: ", n1-n2)
    elif opcion == 3:
        print("La multiplicación es: ", n1*n2)
    elif opcion == 4:
        print("La división es: ", n1/n2)
    elif opcion == 5:
        seguir = False
    else:
        print("Opción incorrecta")

# print con espacio y coma == doble espacio
# Sugerencia: Menú separado (incluso a doble columna)
# SUGERENCIA COMÚN: Dar espacios entre operaciones para facilitar lectura
