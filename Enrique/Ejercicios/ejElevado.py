def elevado(a,b):
    print(pow(a,b))

a=int(input("Introduce un número: "))
b=int(input("Introduce un número: "))
elevado(a,b)


# Método elevado manual
def elevado2(a, b):
    n = a

    if b == 0:
        return 1
    else:
        while b > 1:
            n *= a
            b -= 1

    return n

a = int(input("Número 1: "))
b = int(input("Número 2: "))
print(elevado2(a, b))
