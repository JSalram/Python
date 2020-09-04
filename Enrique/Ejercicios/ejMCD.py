# No funciona
def mcd(n1,n2):

    while(n2 > 0) and (n1 > 0):
        resto = n1 % n2

    return resto


def mcd2(n1, n2):
    n = max(n1, n2)

    while True:
        if n1 % n == 0 and n2 % n == 0:
            return n

        n -= 1



n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

print(mcd2(n1, n2))