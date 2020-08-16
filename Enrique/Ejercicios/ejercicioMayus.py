########## 1er Método ##########
cad = "hola me llamo javi"
print(cad)

lista = cad.split(" ")
listaCap = []

for palabra in lista:
    cap = palabra[0].upper() + palabra[1:]

    listaCap.append(cap)

cad = " ".join(listaCap)
print(cad)



########## 2º Método ##########
cad = "hola me llamo javi"
cap = ""

for i in range(len(cad)):

    if i == 0:
        cap += cad[i].upper()
    elif cad[i-1] == " ":
        cap += cad[i].upper()
    else:
        cap += cad[i]

print(cap)
