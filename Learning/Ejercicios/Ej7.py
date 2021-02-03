# Ejercicio 7
def cuentaCaracteres(cadena):
    diccionario = {"Dígitos": 0, "Minúsculas": 0, "Mayúsculas": 0, "Carácteres": 0}

    for i in cadena:
        if i.isdecimal():
            diccionario["Dígitos"] += 1
        elif i.islower():
            diccionario["Minúsculas"] += 1
        elif i.isupper():
            diccionario["Mayúsculas"] += 1
        else:
            diccionario["Carácteres"] += 1

    return diccionario


print(cuentaCaracteres(input("Cadena: ")))
