# Ejercicio 1
def encuentra(lista, n, pos=0):
    if pos == len(lista):
        return False
    elif lista[pos] == n:
        return True
    else:
        return encuentra(lista, n, pos+1)


nums = [1, 2, 3, 5, 6, 7, 8]
print(encuentra(nums, 7))


# Ejercicio 2
def producto(a, b):
    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + producto(a, b-1)


print(producto(4, 0))


# Ejercicio 3 --> TODO: Corregir
def division(a, b):
    if b == 0:
        return a
    else:
        return division(a, b-1) - b


print(division(8, 2))


# Ejercicio 4
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(5))


# Ejercicio 8
def sumaPares(n):
    if n < 2:
        return 0
    else:
        if n % 2 == 0:
            return n + sumaPares(n-2)
        else:
            return sumaPares(n-1)


print(sumaPares(12))
