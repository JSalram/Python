# Funciones de cadenas (replace, startswith, endswith, upper, lower, split, join)
## .replace(viejaCad, nuevaCad)

## .startswith(cadena)

## .endswith(cadena)

## .upper()

## .lower()

## .split(separador)

## separador.join(estructura)


# =============================================================================================


# Formateo de cadenas ({0}{1}{2})(.format)
nombre = input("Nombre: ")
edad = input("Edad: ")

## Usando variables
saludo = "Hola mi nombre es {nombre} y tengo {edad} años".format(nombre=nombre, edad=edad)
print(saludo)

## Usando una lista de elementos
notas = [6, 7, 3, 9]
print("Notas: {0}, {1}, {2}, {3}, {4}".format(6, 7, 3, 9, 5))
print("Notas: {0}, {1}, {2}, {3}, {4}".format(*notas))  # *lista ==> Representa los elementos de una lista

# format() sin elementos


# =============================================================================================


# Cortes de cadena [inicio:fin[:incremento]

# ToDo EJERCICIO: Invertir cadena
