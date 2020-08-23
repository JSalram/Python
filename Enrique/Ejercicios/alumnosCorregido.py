def eliminaAlumno(lista, lista2, opcion):
    if opcion == 1:
        i = int(input("Posición en la lista del alumno: "))
        i -= 1
        if 0 <= i < len(lista):
            print("\'{}\' eliminado con éxito".format(lista[i]))
            del lista[i]
            del lista2[i]
        else:
            print("No existe ningún alumno en esa posición.")

    elif opcion == 2:
        alumno = input("Alumno: ")

        if alumno in lista:
            i = lista.index(alumno)
            print("\'{}\' eliminado con éxito".format(lista[i]))
            del lista[i]
            del lista2[i]
        else:
            print("El alumno indicado no coincide.")


def media(lista):
    n = 0
    for i in listaNotas:
        n += i
            
    media = round(n / len(listaNotas), 2)
    return media


lista = ["Juan", "Pepe", "Carlos",  "María"]
listaNotas = [2.0, 5.7, 3.4, 9.2]

print()

while True:
    print("1. Imprimir lista                    2. Añadir alumno")
    print("3. Eliminar alumno                   4. Ordenar lista ")
    print("5. Invertir lista                    6. Media de notas ")
    print("7. Salir")

    opcion = int(input("Elige una opción: "))
    print()

    if opcion == 1:
        print("____Lista_de_alumnos____")
        for i in range(len(lista)):
            print("{} - {}: {}".format(i+1, lista[i], listaNotas[i]))


    elif opcion == 2:
        alumno = input("Alumno: ")
        nota = float(input("Nota: "))
        lista.append(alumno)
        listaNotas.append(nota)
       
        
    elif opcion == 3:
        print("Indica la forma de eliminar:")
        print("1. Por posición                  2. Por nombre")
        elim = int(input("Opción: "))

        while elim != 1 and elim != 2:
            elim = int(input("Opción incorrecta. Vuelve a intentarlo: "))

        eliminaAlumno(lista, listaNotas, elim)


    elif opcion == 4:
        print("Falta método ordenaBurbuja")
        lista.sort()
        listaNotas.sort()


    elif opcion == 5:
        lista.reverse()
        listaNotas.reverse()


    elif opcion == 6:
        print("La media es:",  media(listaNotas))
    
    
    elif opcion == 7:
        break

    else:
        print("Opción incorrecta. Introduzca una opción válida")

    print("------------------------------------------------------")
