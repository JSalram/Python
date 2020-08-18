def media(lista):
    n = 0
    for i in listaNotas:
        n += i
            
    media = round(n / len(listaNotas), 2)
    return media


lista = ["Juan","Pepe","Carlos","María"]
listaNotas = [2.0, 5.7, 3.4, 9.2]

seguir = True

while seguir:
    print("1. Imprimir lista                    2. Añadir alumno")
    print("3. Eliminar alumno                   4. Ordenar lista ")
    print("5. Invertir lista                    6. Media de notas ")
    print("7. Salir")

    opcion = int(input("Elige una opción: "))
    print()

    if opcion == 1:
        print("____Lista_de_alumnos____")
        for i in range(len(lista)):
            print("{i} - {alum}: {nota}".format(i = i+1, alum = lista[i], nota = listaNotas[i]))


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

        if elim == 1:
            i = int(input("Posición en la lista del alumno: "))
            i -= 1
            if 0 <= i < len(lista):
                print("\'{}\' eliminado con éxito".format(lista[i]))
                del lista[i]
                del listaNotas[i]
            else:
                print("No existe ningún alumno en esa posición.")

        elif elim == 2:
            alumno = input("Alumno: ")

            if alumno in lista:
                i = lista.index(alumno)
                del lista[i]
                del listaNotas[i]
            else:
                print("El alumno indicado no coincide")


    elif opcion == 4:
        # Crear función 'ordenaBurbuja' para ordenar alumnos en orden alfabético o por nota
        print("Falta método")


    elif opcion == 5:
        lista.reverse()
        listaNotas.reverse()


    elif opcion == 6:
        print("La media es:",  media(listaNotas))
    
    
    elif opcion == 7:
        seguir = False

    else:
        print("Opción incorrecta. Introduzca una opción válida")

    print("\n")
