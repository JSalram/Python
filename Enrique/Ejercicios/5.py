lista=["Juan","Pepe","Carlos","María", "Fer", "Luisa", "David", "Nerea"]
seguir=True

while seguir:
    print("1. Imprimir Lista\n\
2. Añadir alumno\n\
3. Eliminar alumno\n\
4. Buscar alumno\n\
5. Ordenar lista\n\
6. Invertir lista\n\
7. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        i = 1
        for alumno in lista:
            print(str(i) + " - " + alumno)
            i += 1
    elif opcion == 2:
        alumno = input("Alumno: ")
        lista.append(alumno)
        print(lista)
    elif opcion == 3:
        pos = int(input("Posición: "))
        del lista[pos]
    elif opcion == 4:
        alumno = input("Alumno: ")
        print(lista.index(alumno))
    elif opcion == 5:
        print(lista.sort)
    elif opcion == 6:
        print(lista.reverse)
    else:
        seguir=False
        print("Opción incorrecta. Introduzca una opción válida")

    print()
    

# print(lista) debería estar únicamente en su opción
# Innecesario pedir alumno para ordenar, invertir o salir
# Falta la opción 7, y si escribes el 7 sale del programa e igual te dice que la opción es incorrecta
# Sugerencia: Lista vacía e ir rellenando / operando
# Sugerencia: Menú separado y a doble/triple columna
# SUGERENCIA COMÚN: Dar espacios entre operaciones para facilitar lectura
