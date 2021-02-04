# Ejercicio 1
def encuentra(lista, n, pos=0):
    if pos == len(lista):
        return False
    elif lista[pos] == n:
        return True
    else:
        return encuentra(lista, n, pos+1)


nums = [1, 2, 3, 5, 6, 7, 8]
a = 7
print(f"Encuentra ({a}) = {encuentra(nums, a)}")


# Ejercicio 2
def producto(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + producto(a, b-1)


a, b = 4, 0
print(f"Producto ({a}x{b}) = {producto(a, b)}")


# Ejercicio 3
def division(a, b):
    if a < b:
        return 0
    else:
        return 1 + division(a-b, b)

        # division(10, 2) --> 5
        # division(8, 2) --> 4
        # division(6, 2) --> 3
        # division(4, 2) --> 2
        # division(2, 2) --> 1
        # division(0, 2) --> 0


a = 10
b = 2
print(f"División ({a}/{b}) = {division(a, b)}")


# Ejercicio 4
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


a = 5
print(f"Fibonacci ({a}) = {fibonacci(a)}")


# Ejercicio 5
def invierteCadena(cad, pos=0):
    if pos == len(cad)-1:
        return cad[pos]
    else:
        return invierteCadena(cad, pos+1) + cad[pos]

    # invierteCadena("Hola", 0) + "H" --> "aloH"
    # invierteCadena("Hola", 1) + "o" --> "alo"
    # invierteCadena("Hola", 2) + "l" --> "al"
    # "a"


cad = "Hola"
print(f"Invierte Cadena ({cad}): {invierteCadena(cad)}")


# Ejercicio 8
def sumaPares(n):
    if n < 2:
        return 0
    else:
        if n % 2 == 0:
            return n + sumaPares(n-2)
        else:
            return sumaPares(n-1)


a = 12
print(f"SumaPares ({a}) = {sumaPares(a)}")


# Ejercicio 10
def convierteBase(n, base):
    if n < base:
        res = str(n)
    else:
        res = convierteBase(n // base, base) + str(n % base)

    # 28 % 2 == 0
    # 14 % 2 == 0
    # 7 % 2 == 1
    # 3 % 2 == 1
    # 3 // 2 == 1

    # convierteBase(28 // 8, 8) == 3
    # 3 + (28 % 8) == 3 + 4 == 34

    return res
