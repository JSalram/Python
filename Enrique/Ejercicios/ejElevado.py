def elevado(a,b):
    print(pow(a,b))

a=int(input("Introduce un número: "))
b=int(input("Introduce un número: "))
elevado(a,b)
    

def elevado2(a, b):
    n = a

    while b > 1:
        n *= a
        b -= 1

    return n

a = int(input("Introduce un número: "))
b = int(input("Introduce un número: "))
print(elevado2(a, b))
