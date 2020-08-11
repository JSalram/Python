lista=["Juan","Pepe","Carlos","María", "Fer", "Luisa", "David", "Nerea"]
seguir=True
while seguir:
    print("1. Imprimir Lista\n2. Añadir alumno\n3. Eliminar alumno\n4. Buscar alumno\n5. Ordenar lista\n6. Invertir lista\n7. Salir")
    opcion = int(input("Elige una opción: "))
    alumno = input("Alumno: ")
    if opcion== 1:
        print(lista)
    elif opcion==2 4:  # Se coló un 4
        lista.append(alumno)
        print(lista)
    elif opcion==3:
        lista.remove(alumno)
        print(lista)
    elif opcion==4:
        print(lista.index(alumno))
    elif opcion==5:
        print(lista.sort)
    elif opcion==6:
        print(lista.reverse)
    else:
        seguir=False
        print("Opción incorrecta. Introduzca una opción válida")
    
# print(lista) debería estar únicamente en su opción
# Innecesario pedir alumno para ordenar, invertir o salir
# Falta la opción 7, y si escribes el 7 sale del programa e igual te dice que la opción es incorrecta
# Sugerencia: Lista vacía e ir rellenando / operando
# Sugerencia: Menú separado y a doble/triple columna
# SUGERENCIA COMÚN: Dar espacios entre operaciones para facilitar lectura
