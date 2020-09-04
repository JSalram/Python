longitudes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 10 long máx

cad = input("Escribe una palabra ('fin' para salir): ")
while cad != "fin":
    if len(cad) <= len(longitudes):
        pos = len(cad) - 1
        longitudes[pos] += 1

    cad = input("Escribe una palabra ('fin' para salir): ")


for i in range(len(longitudes)):
    print("Palabras de longitud {}: {}".format(i+1, longitudes[i]))


# =======================================================================


i = 0
while i < 10:
    # Código...
    # Código...

    i += 1