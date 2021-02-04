def compruebaCadenas(c1, c2):
    i = 0
    if len(c1) == len(c2):
        iguales = True
    else:
        iguales = False
    # Otra manera --> iguales = len(c1) == len(c2)

    while i < len(c1) and iguales:
        iguales = c1[i] == c2[i]
        i += 1

    return iguales


cad1 = "mama"
cad2 = "mamaa"

print(compruebaCadenas(cad1, cad2))
