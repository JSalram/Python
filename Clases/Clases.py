# Clases

class Coche:
    def __init__(self, modelo, marca, matricula, potencia, color):
        self.modelo = str(modelo)
        self.marca = str(marca)
        self.matricula = str(matricula)
        self.potencia = int(potencia)
        self.color = str(color)

    def __str__(self):
        return '{self.matricula} - {self.modelo}, {self.marca}: Potencia: {self.potencia} Kw;' \
               ' Color: {self.color}'.format(self=self)


car = Coche("Mercedes Benz", "Clase E", "3425KMW", 130, "Negro")
print(car)
