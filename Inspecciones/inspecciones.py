from Avion import Avion

# Modo Consola
while True:
    print("1. Diamonds          2. Pipers          3. Acrobáticas")

    tipo = int(input("Modelo de Avión: ")) - 1
    while tipo < 0 or tipo >= 3:
        tipo = int(input("Respuesta inválida.\n  Modelo de Avión: ")) - 1

    anno = int(input("Año (2021-2030): "))
    while anno < 2021 or anno > 2030:
        anno = int(input("Respuesta inválida.\n  Año (2021-2030): "))

    a = Avion(tipo)
    a.printAnno(anno)

    seguir = input("¿Continuar? (y/n)\n")
    while seguir != "y" and seguir != "n":
        seguir = input("Respuesta inválida.\n  ¿Continuar? (y/n)\n")

    if seguir == "n":
        break
    print("\n\n==========================================================\n\n")
