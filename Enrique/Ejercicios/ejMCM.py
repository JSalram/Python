def mcm(n1, n2):

    a = max(n1,n2)
    b = min(n1,n2)

    while b!=0:
        mcd = b
        b = a%b
        a = mcd

    mcm = (n1*n2)/mcd

    return mcm

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

print("El mcm de {} y {} es = {}".format(n1, n2, mcm(n1, n2)))

#  Evitar imprimir y pedir variables dentro de las funciones que operan
