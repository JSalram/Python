# Lambdas
print("Lambdas\n-------")


## Lambda en funciones
def test(f, arg):
    return f(arg)


print(test(lambda x: x * 2, 5))

## Lambda sin función
print((lambda x: x * x)(10))

## Lambda en variables
double = lambda x: x * 2
print(double(2))

add = lambda x, y: x + y
print(add(3, 4))


print("=============================================================================================")


# Map y filter
print("Map y filter\n------------")


## Map ==> Con operadores
def plus5(x):
    return x + 5


numeros = [5, 10, 15, 20]
res = list(map(plus5, numeros))
print(res)

print(list(map(lambda x: x + 5, numeros)))

## Filter ==> Con condiciones
numeros = [5, 10, 15, 20]
res2 = list(filter(lambda x: x > 10, numeros))
print(res2)


print("=============================================================================================")


# Generadores
print("Generadores\n-----------")


def cont(x):
    for i in range(x):
        yield i


print(list(cont(10)))


print("=============================================================================================")


# Decoradores
print("Decoradores\n-----------")


def decor(func):
    def wrap():
        print("**********")
        func()
        print("**********")

    return wrap


@decor
def printHola():
    print("Hola mundo")


printHola()


print("=============================================================================================")


# Recursividad
print("Recursividad\n------------")


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(4))


print("=============================================================================================")


# Conjuntos (como SQL)
print("Conjuntos\n---------")


nums1 = {1, 3, 5, 7, 9}
nums2 = {2, 3, 4, 5, 6}

print(nums1 | nums2)  # | == unión (ambos conjuntos)
print(nums1 & nums2)  # & == intersección (elementos contenidos en ambos)
print(nums1 - nums2)  # - == diferencia (elementos que contiene el primero que no el segundo)
print(nums2 - nums1)  # - == diferencia (elementos que contiene el primero que no el segundo)
print(nums1 ^ nums2)  # ^ == diferencia simétrica (elementos únicos de cada conjunto)


print("=============================================================================================")


# itertools
print("itertools\n---------")
import itertools

for i in itertools.count(3):
    if i > 10:
        break
    print(i, end="   ")

