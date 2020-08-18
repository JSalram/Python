lista=["Juan","Pepe","Carlos","María"]
listaNotas=[]  # len(lista) == len(listaNotas)

seguir=True  # Mostrar opción con break

while seguir:
    # Doble columna se ve mejor
    print("1. Imprimir lista")
    print("2. Añadir alumno")
    print("3. Eliminar alumno")
    print("4. Posición alumno")
    print("5. Ordenar lista")
    print("6. Invertir lista")
    print("7. Introducir nota")
    print("8. Media de notas")
    print("9. Salir")

    opcion = int(input("Elige una opción: "))
    n=0  # ¿n = 0?
    if opcion== 1:  # Imprime únicamente las listas
        print(lista)
        print(listaNotas)

    elif opcion==2:  # Añadir nota por cada alumno
        alumno = input("Alumno: ")
        lista.append(alumno)
        
    elif opcion==3:
        # Preguntar si por nombre o por posición
        # Eliminar nota a la par del alumno
        alumno = input("Alumno: ")
        lista.remove(alumno)
        
    elif opcion==4:  # Al imprimir las posiciones, esta opción sobra
        alumno = input("Alumno: ")
        print(lista.index(alumno))

    elif opcion==5:  # No funciona
        # Crear función 'ordenaBurbuja' para ordenar alumnos en orden alfabético o por nota
        (lista.sort)

    elif opcion==6:  # No funciona
        # Revertir lista de alumnos y listaNotas
        (lista.reverse)
    
    elif opcion==7:  # Eliminar o modificar esta opción
        nota=float(input("Introducir nota: "))
        listaNotas.append(nota)

    elif opcion==8:
        # Crear funcion media para reducir código
        # Redondear nota media a 2 decimales

        continuar=True
        
        if len(lista)!=len(listaNotas):  # Bien pensado
            continuar= False
            print ("Introduzca todas las notas")

        while continuar:  # ¿while continuar?
            n=0
            for i in listaNotas:
            n+=i  # No está marginado, no funciona
            media=n/len(listaNotas)
            print("la media es:",media)
            continuar=False
        
                
    elif opcion==9:
        seguir=False

    else:
        seguir= False  # ¿seguir = False?
        print("Opción incorrecta. Introduzca una opción válida")
    
# Añadir saltos de línea para mejorar la ejecución
# Espaciar código para facilitar su lectura
# Emplear métodos vistos en clase como el .format()
