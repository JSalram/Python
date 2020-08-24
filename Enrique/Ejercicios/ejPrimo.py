# Hay números que se le escapan (p.e.: 97)
def primo(a):
    if a==0:
        print("No es válido")
    elif a==1 or a==2 or a==3 or a==5 or a==7:
        return True
    elif a%1==0 and a%a==0 and (a&2==0 or a%3==0 or a%4==0 or a&5==0 or a&6==0 or a&7==0):
        return False
    else:
        return True
a=int(input("Introduce número a comprobar: "))
print(primo(a))


def primo2(n):
    esPrimo = True
    divisores = 0

    if n <= 0 or n == 1:
        return None
    else:
        for i in range(1, n+1):
            if n % i == 0:
                divisores += 1

            if divisores > 2:
                esPrimo = False
                break

    return esPrimo


print("Primo2 = " + str(primo2(a)))
