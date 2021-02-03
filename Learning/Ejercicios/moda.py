lista = [2, 5, 6, 8, 9, 0, 9]

n = 0
maxRep = 0

for i in lista:
    repeticiones = 0

    for k in lista:
        if k == i:
            repeticiones += 1

    if repeticiones > maxRep:
        maxRep = repeticiones
        n = i

print(str(n) + " - " + str(maxRep))