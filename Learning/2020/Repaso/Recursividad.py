## Ejercicio 1
def encuentraNum(lista, n, pos=0):
    encontrado = n == lista[pos]

    if pos+1 == len(lista) and not encontrado:
        encontrado = False
    elif not encontrado:
        encontrado = encuentraNum(lista, n, pos+1)

    return encontrado


lista = [2, 3, 4, 5]
if encuentraNum(lista, 3):
    print("El número se encuentra dentro de la lista")
else:
    print("El número NO se encuentra dentro de la lista")


# =============================================================================================


## Ejercicio 2
def producto(x, y):

    if y == 1:
        res = x
    else:
        res = x + producto(x, y-1)

    return res


print("Producto recursivo: " + str(producto(2, 3)))


# =============================================================================================


## Ejercicio 3
def div(x, y):

    if x > y:
        res = 1 + div(x - y, y)
    else:
        res = 1

    return res


print("División recursiva: " + str(div(6, 3)))


# =============================================================================================


## Ejercicio 4
def fibonacci(n):
    if n == 1 or n == 0:
        resultado = 1
    else:
        resultado = fibonacci(n - 2) + fibonacci(n - 1)

    return resultado


print("Fibonacci: " + str(fibonacci(5)))


# =============================================================================================


## Ejercicio 5
def inviertePalabra(palabra, fin):
    if fin < 0:
        inv = ""
    else:
        inv = palabra[fin] + inviertePalabra(palabra, fin-1)

    return inv


cad = "Hola"
print("Invierte palabra recursivo: " + str(inviertePalabra(cad, len(cad)-1)))


# =============================================================================================


## Ejercicio 6
def cuentaDigitos(n):
    if n >= 0:
        if n < 10:
            dig = 1
        else:
            dig = 1 + cuentaDigitos(n / 10)
    else:
        if n > -10:
            dig = 1
        else:
            dig = 1 + cuentaDigitos(n / 10)

    return dig


print("Cuenta dígitos recursivo: " + str(cuentaDigitos(100)))


# =============================================================================================


## Ejercicio 7
def binario(n):
    if n < 2:
        res = str(n)
    else:
        res = binario(n // 2) + str(n % 2)

    # 28 % 2 == 0
    # 14 % 2 == 0
    # 7 % 2 == 1
    # 3 % 2 == 1
    # 3 // 2 == 1

    return res


print("Binario recursivo: " + binario(28))
""" http://recursostic.educacion.es/secundaria/edad/4esotecnologia/quincena5/4q2_contenidos_2c.htm """


# =============================================================================================


## Ejercicio 8
def sumaPares(n):
    if n == 0:
        res = 0
    else:
        if n % 2 == 0:
            res = n + sumaPares(n-1)
        else:
            res = sumaPares(n-1)

    return res


print("Suma pares recursivo: " + str(sumaPares(6)))


# =============================================================================================


## Ejercicio 9
def sumaEdades(lista, pos=0):
    if pos == len(lista):
        res = 0
    else:
        res = lista[pos] + sumaEdades(lista, pos+1)

    return res


edades = [23, 17, 30]
print("Suma edades recursivo: " + str(sumaEdades(edades)))


# =============================================================================================


## Ejercicio 'elevado'
def elevado(x, y):
    if y < 0:
        rec = "Exponente inválido"
    elif y == 0:
        rec = 1
    elif y == 1:
        rec = x
    else:
        rec = x * elevado(x, y-1)

    return rec


print(elevado(2, 3))


## Ejercicio 'factorial'
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))


## Ejercicio 'invierteCadena'
def invierteCadena(cad, pos, fin):
    if pos == fin:
        return cad[pos]
    else:
        return invierteCadena(cad, pos + 1, fin) + cad[pos]


cad = "Hola"
print(invierteCadena(cad, 0, len(cad)-1))


## Ejercicio 'palindromo'
def palindromo(cad, inicio, fin):

    if inicio >= fin:
        pal = True
    else:
        pal = cad[inicio] == cad[fin] and palindromo(cad, inicio+1, fin-1)

    return pal


cad = "orro"
print(palindromo(cad, 0, len(cad)-1))
