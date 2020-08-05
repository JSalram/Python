# If - elif - else
## Operadores lógicos: > , < , == , != , >= , <=

n = int(input("Número: "))

if n > 0:
    # Si se cumple la condición, ejecuta este código:
    print("Es mayor que 0")
elif n == 0:
    # Si no se cumple la anterior, prueba con ésta:
    print("Es igual que 0")
else:      # n < 0
    # Si no se cumple ninguna de las anteriores, ejecuta esto:
    print("No es mayor que 0")
print("Esta fuera de la condición")  # Imprime esto siempre, ya que está fuera

if n > 0:
    # Si es mayor que 0, ejecuta:
    print("Mayor que 0")
if n > 5:
    # Si es mayor que 5, ejecuta:
    print("Mayor que 5")


var = 2
var2 = 3
print(var != var2) # Las condiciones devuelven un booleano (True / False)



## and / or
n = int(input("Número: "))

if n > 0 and n < 10:    # 0 < n < 10
    print("Mayor que 0 y menor que 10")
else:
    print("Lo contrario")

if n > 0 and n < 10 or n > 10:  # Se encapsulan automáticamente las condiciones separadas por 'and'
    print("Mayor que 0 o mayor que 10")
else:
    print("Lo contrario")



# Otras condicionales
## Condicionales de cadenas
cad = "Hala"

if cad == "Hola":
    print("Es correcto")

alumno = "Antonio"
alumno2 = "Javier"

## Condicionales de booleanos
booleano = alumno < alumno2

if booleano:
    print(alumno + " va por delante de " + alumno2)
else:
    print(alumno2 + " va por delante de " + alumno)
