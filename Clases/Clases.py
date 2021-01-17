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


# pancho = Perro("pancho", "blanco")
# pancho.ladra()


class Test:
    def testeo(self):
        print("Prueba")


# Test().testeo()


class Figuras:
    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura

    def __str__(self):
        return str(self.altura) + " x " + str(self.anchura)

    @classmethod
    def cuadrado(cls, lado):
        return cls(lado, lado)

    @staticmethod
    def hola():
        print("Hola")


f = Figuras.cuadrado(5)
print(f)

Figuras.hola()
