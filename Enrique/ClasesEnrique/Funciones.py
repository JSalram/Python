# Funciones  ==>  Se deben definir antes para poder llamarlas
## Void / Vacío
def holaMundo():
    print("Hola Mundo")


holaMundo()


def saludo(nombre):
    print("Hola " + nombre)


nombre = input("Nombre: ")
saludo(nombre)
saludo("Manuel")
saludo("Marta")


def modificaLista(lista, elemento, posicion=0):
    lista[posicion] = elemento


lista = [1, 5, 3, 4, 5]
print("Antes:", str(lista))
modificaLista(lista, 1, 2)
print("Después:", str(lista))



def muestraLista(lista):
    for i in range(len(lista)):
        print(i+1, "-", lista[i])


alumnos = ["Juan", "María", "Pepe"]
muestraLista(alumnos)


# =============================================================================================


## Return / Devuelven valores
def mult(a, b = 0):
    return a * b


print((mult(5)))
doble = 2 * mult(2, 3)
print(doble)


def media(lista):
    n = 0
    for i in lista:
        n += i

    return n / len(lista)


print(media([10, 0, 5]))


# =============================================================================================


## Return+
def doble(a, b):
    dobleA = 2 * a
    dobleB = 2 * b

    return dobleA, dobleB


a, b = doble(2, 3)
print(a)
print(b)


# =============================================================================================


## Parámetros por defecto
def modificaLista(lista, elemento, posicion=0):
    lista[posicion] = elemento


lista = [1, 5, 3, 4, 5]
modificaLista(lista, 6)
print(lista)


def saludo(saludo = "Hola", nombre = "Mundo"):
    saludoNombre = saludo + " " + nombre
    return saludoNombre


print(saludo("Hey", "Javi"))
print(saludo())


# =============================================================================================


## func
def mult(a, b):
    return a * b


def suma(a, b):
    return a + b


def doble(func, a, b):
    return 2 * func(a, b)


print(doble(mult, 3, 2))
print(doble(suma, 3, 2))


# =============================================================================================


## Recursividad
def factorial(n):
    if n == 1:
        resultado = 1
    else:
        resultado = n * factorial(n - 1)
    return resultado


### Otro método ###
def factorial2(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


print(factorial(5))
print(factorial2(5))


##### Más funciones recursivas #####
def fibonacci(n):
    if n == 1 or n == 0:
        resultado = 1
    else:
        resultado = fibonacci(n - 2) + fibonacci(n - 1)

    return resultado


print(fibonacci(5))


def inviertePalabra(palabra):
    palabraInv = ""
    i = len(palabra)-1

    while i >= 0:
        palabraInv += palabra[i]
        i -= 1

    return palabraInv


def palindromo(func, palabra):
    if func(palabra) == palabra:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


palindromo(inviertePalabra, "oro")


# =============================================================================================


# Explicación Parámetros
def mult(n1, n2):
    return n1 * n2


a = int(input("Número 1: "))
b = int(input("Número 2: "))

print(mult(a, b))


def ordenaLista(lista1, lista2):
    return None


alumnos = ["Javi", ...]
notas = [2.4, ...]

ordenaLista(alumnos, notas)
