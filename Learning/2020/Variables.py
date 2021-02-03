# print()
print("¡Hola Mundo!")

# Variables = int, float, bool, char, string
numero = 243        # Integer (int) ==> Números enteros
decimal = 2.6       # Float ==> Números decimales
booleano = True     # Booleano ==> Solo puede ser True / False (1/0)
character = '@'     # Character ==> Caracteres
nombre = "Javier"   # String ==> Cadenas de caracteres



## Operaciones con variables
### Suma / Concatenación (+)
n = 1
n2 = 2
suma = n + n2
print(suma)

saludo = "Hola"
mundo = "Mundo"
print(saludo, mundo)  # , ==> + " " +

### Resta (-)
n = 1
n2 = 2
resta = n - n2
print(resta)

### Multiplicación / Repetición (*)
n = 1
n2 = 2
mult = n * n2
print(mult)

cadena = "Hola" * 3
print(cadena)

### División (/)
n = 2
n2 = 2
div = n / n2
print(div)

### División exacta (//)
n = 1
n2 = 2
div = n // n2
print(div)

### Potencia (**)
n = 2
n2 = 2
print(n ** n2)

### Módulo (%)
n = 2
n2 = 3
print(n % n2)


# input()
var = input("Variable: ")
print(var)

# Convertir variables (try-except)

try:
    var = int(var)
except:
    print("La variable que le has pasado no es un número")
    exit()
print(var + 2)

nombre = "Javi"
edad = 22
print("Hola me llamo " + nombre + " y tengo " + str(edad) + " años")

strBool = "True"
booleano = bool(strBool)
print(booleano)

strFloat = "2.5"
decimal = float(strFloat)
print(decimal + 2.5)
