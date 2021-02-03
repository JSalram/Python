############### SOLUCIÓN ###############
a = [4, 7 , 2, 9, 7, 3, 4, 6, 8, 2]
print("Desordenada:", str(a))

for i in a:
    for j in range(len(a)-1):
        k = j + 1

        if a[j] > a[k]:
            temp = a[j]
            a[j] = a[k]
            a[k] = temp



print("Ordenada:", str(a))
