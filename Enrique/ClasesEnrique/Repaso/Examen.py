## Ejercicio 1
def funcion(lista):  # Nombre de la función autodescriptivo
    n = 0  # Mejor abajo
    for trabajador in lista:
        if lista[trabajador] < 900:
            lista[trabajador] = 900
            print("Sueldo coregido de {} a {}".format(trabajador, lista[trabajador]))

    for trabajador in lista:
        n += lista[trabajador]
    media = n / len(lista)

    for trabajador in lista:

        if media > lista[trabajador]:
            lista[trabajador] = lista[trabajador] + (lista[trabajador] * 0.03)
            # Falta indicar a qué trabajador se le ha incrementado el 3%
            print("Sueldo incrementado a {} en un 3%: {}€".format(trabajador, lista[trabajador]))

    print("El resultado final:", lista)  # Mejorar impresión final


import random  # Los módulos se importan al principio, antes de las funciones

a = random.randint(0, 2000)
b = random.randint(0, 2000)
c = random.randint(0, 2000)

# Sustituir diccionario por lista mixta: ["Pepe", sueldoPepe]
lista = {"Pepe": a, "Juan": b, "Pedro": c}
print(lista)

funcion(lista)


######################################################################################################


## Ejercicio 2
class Empleado:  # Las clases empiezan con una mayúscula
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        if sueldo >= 0:
            self.sueldo = sueldo  # Controlar errores
        else:
            self.sueldo = "Sueldo sin especificar"

        self.puesto = self.asignaPuesto()

    def __str__(self):
        # Mejorar la impresión
        return "{self.nombre} - {self.puesto} - {self.sueldo}".format(self=self)

    # Automatizar
    def asignaPuesto(self):
        if isinstance(self.sueldo, str):
            return "Puesto sin especificar"
        else:
            if self.sueldo <= 900:
                return "Auxiliar"
            elif 900 < self.sueldo <= 1500:
                return "Técnico"
            elif 1500 < self.sueldo <= 1800:
                return "Especialista"
            elif self.sueldo > 1800:
                return "Mánager"


trabajador1 = Empleado("Juan", -1000)
print(trabajador1)


######################################################################################################


## Ejercicio 3
"""
def sumaLista(lista, pos=0):
    if pos == len(lista)-1:
        suma = lista[pos]
    else:
        suma = lista[pos] + sumaLista(lista, pos+1)

    return suma
"""


print("\n\n")
from random import randint
from math import floor

masas = []
combustibles = []

for i in range(4):
    masas += [randint(0, 1000)]
    combustibles += [floor(masas[i] / 3) - 2]

print(masas)
print(combustibles)

print("Combustible total: {}".format(combustibles[0] + combustibles[1] + combustibles[2] + combustibles[3]))
# print("Combustible total: {}".format(sumaLista(combustibles)))
print("\n\n")


######################################################################################################


## Ejercicio 4
def burbuja(lista):
    for i in lista:
        for j in range(len(lista)-1):
            k = j + 1
            if lista[k] > lista[j]:
                temp = lista[j]
                lista[j] = lista[k]
                lista[k] = temp
    return lista


lista = [3, 5, 1, 6]
print(burbuja(lista))
