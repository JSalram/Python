# Funciones de cadenas (replace, startswith, endswith, upper, lower, split, join)
## .replace(viejaCad, nuevaCad)
cad = "Hola me llamo Javi"
print(cad.replace("Javi", "Enrique"))


## .startswith(cadena)
cad = "Hola me llamo Javi"
print(not cad.startswith("Hola"))  # not ==> Para negar métodos


## .endswith(cadena)
cad = "Hola me llamo Javi"
print(cad.endswith("Javi"))


## .upper()
cad = "hola me llamo javi"

i = cad.index("javi")
cad = cad[0].upper() + cad[1:i] + cad[i].upper() + cad[i+1:]
print(cad)


## .lower()
cad = "Hola me llamo Javi"
print(cad.lower())


## .split(separador)
cad = "Hola me llamo Javi"
lista = cad.split(" ")
print(lista)


## separador.join(estructura)
cad = "Hola me llamo Javi"
lista = cad.split(" ")

cad = " - ".join(lista)
print(cad)


# =============================================================================================


# Formateo de cadenas ({0}{1}{2})(.format)
nombre = input("Nombre: ")
edad = input("Edad: ")

## Usando variables
saludo = "Hola me llamo {nombre} y tengo {edad} años.".format(nombre=nombre, edad=edad)
print(saludo)

## Usando una lista de elementos
listaAlumnos = ["Rodolfo", "Javi", "Juan", "Pepe"]
print("Alumnos: {0}, {1}, {2}, {3}".format("Rodolfo", "Javi", "Juan", "Pepe"))
print("Alumnos: {0}, {1}, {2}, {3}".format(*listaAlumnos))  # *lista ==> Representa los elementos de una lista


# =============================================================================================


# Cortes de cadena [inicio:fin[:incremento]
cad = "Ayer compré palomitas"

print(cad[::-1])

inicio = cad.index("palomitas")
print(cad[inicio:])
