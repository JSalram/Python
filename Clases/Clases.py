# Clases
class Animal:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color


class Gato(Animal):
    def maulla(self):
        print(self.nombre + ": \'Miau\'")


class Perro(Animal):
    def ladra(self):
        print(self.nombre + ": \'Guau\'")


pancho = Perro("pancho", "blanco")
pancho.ladra()


class Test:
    def testeo(self):
        print("Prueba")


Test().testeo()
