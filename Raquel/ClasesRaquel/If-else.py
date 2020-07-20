num = int(input("Número: "))

# Operadores lógicos: > , < , == , != , >= , <=

if num > 5:
    print("Es mayor que 5")
    if num < 10:
        print("Es menor que 10")
elif num >= 5:
    print("Es mayor o igual a 5")
else:
    print("No es mayor que 5")