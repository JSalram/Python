def media(listaNotas):
    n = 0
    for i in listaNotas:
        n+=i

    media=round(n/len(listaNotas),2)
    print("la media es:",media)


def elimnarAlumno(lista,listaNotas,forma):  # Errata en el nombre
    if forma == 1:
        i = int(input("Introduzca la posición: "))
        i-=1
        if 0 <= i < len(lista):
            del lista[i]
            del listaNotas[i]
        else:
            print("Posición incorrecta")

    if forma == 2:
        alumno = input("Alumno: ")

        if alumno in lista:
            i = lista.index(alumno)
            del lista[i]
            del listaNotas[i]


def ordenaBurbuja(lista,listaNotas):
    for i in range(len(lista)):
        for j in range(len(lista)-1):  # range(lista) != range(len(lista)) (también falta el -1)
            k=j+1
            if listaNotas[j]>listaNotas[k]:
                
                temp = listaNotas[j]
                listaNotas[j] = listaNotas[k]
                listaNotas[k] = temp

                temp2 = lista[j]
                lista[j] = lista[k]
                lista[k] = temp2
    """print(lista,"-",listaNotas)"""  # No es necesario
    # Si quieres, puedes imprimir "Lista ordenada" a modo de información
    print("Lista ordenada por nota")


# ==================================================================


lista=["Juan","Pepe","Carlos","María"]
listaNotas=[3.0,9.5,8.9,4.5]

seguir=True

while seguir:
    print("1. Imprimir lista                2. Añadir alumno")
    print("3. Eliminar alumno               4. Ordenar lista")
    print("5. Invertir lista                6. Media notas")
    print("7. Salir")
    
    print()
    opcion = int(input("Elige una opción: "))
    print()

    if opcion == 1:
        for i in range(len(lista)):
            print("{} - {}:{}".format(i+1,lista[i],listaNotas[i]))  # Faltaba paréntesis

    elif opcion == 2:
        # Controlar el rango de las notas
        alumno = input("Alumno: ")
        nota = float(input("Nota: "))
        lista.append(alumno)
        listaNotas.append(nota)

    elif opcion == 3:
        # Si indicas algo distinto de 1 o 2, igualmente ejecuta la función eliminaAlumno
        # De todas formas, lo que quieres hacer se puede escribir directamente en la función
        print("1.Eliminar por posicion              2.Eliminar por nombre")
        forma = int(input("Elige forma de eliminar alumno: "))

        if forma != 1 or forma != 2:  # La negación siempre por delante (!=)
            # 'OR' no sería correcto en este caso
            print("Introduzca una opción válida")

        elimnarAlumno(lista,listaNotas,forma)

    elif opcion == 4:
        ordenaBurbuja(lista,listaNotas)
        
    elif opcion == 5:
        lista.reverse()
        listaNotas.reverse()

    elif opcion == 6:
        media(listaNotas)
               
    elif opcion == 7:
        seguir = False

    else:
        print("Opción incorrecta. Introduzca una opción válida")

# La línea separatoria está fuera del bucle, por lo que sólo se ejecuta al salir
    print("-------------------------------------------------")


# Las funciones se definen primero y luego se llaman

def media(listaNotas):
    
    n = 0
    for i in listaNotas:
        n+=i

    media=round(n/len(listaNotas),2)
    print("la media es:",media)

def elimnarAlumno(lista,listaNotas,forma):
    if forma == 1:
        i = int(input("Introduzca la posición: "))
        i-=1
        if 0 <= i < len(lista):
            del lista[i]
            del listaNotas[i]
        else:
            print("Posición incorrecta")

    if forma == 2:
        alumno = input("Alumno: ")

        if alumno in lista:
            i = lista.index(alumno)
            del lista[i]
            del listaNotas[i]


def ordenaBurbuja(lista,listaNotas):
    for i in range(len(lista)):
        for j in range(lista):
            k=j+1
            if listaNotas[j]>listaNotas[k]:
                
                temp = listaNotas[j]
                listaNotas[j] = listaNotas[k]
                listaNotas[k] = temp

                temp2 = lista[j]
                lista[j] = lista[k]
                lista[k] = temp2
    print(lista,"-",listaNotas)

    
    
# Espaciar código para facilitar su lectura
