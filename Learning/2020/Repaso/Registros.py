## EJERCICIO: Hora
class Hora:
    def __init__(self, h, m, s):
        seg = h * 3600 + m * 60 + s
        self.seg = seg

    def sumaHora(self, h):
        self.seg += h * 3600

    def getHoras(self):
        return self.seg // 3600

    def __str__(self):
        hora = self.seg // 3600
        min = self.seg % 3600 // 60
        seg = self.seg % 3600 % 60

        if min < 10:
            min = "0" + str(min)

        return "{}:{}:{}".format(hora, min, seg)


objHora = Hora(11, 9, 30)
print(objHora.seg)
objHora.sumaHora(1)
print(objHora.seg)
print(objHora)


hora = Hora(3, 4, 5)
h = hora.getHoras()

# hora = objHora.seg // 3600
# print(hora)
# min = objHora.seg % 3600 // 60
# print(min)
# seg = objHora.seg % 3600 % 60
# print(seg)


"""
Clase Hora:
- Atributos:
    - segundos

- Constructor:
    - horas
    - minutos
    - segundos

- Métodos:
    - sumaHoras(horas)
    - sumaMinutos(minutos)
    - sumaSegundos(segundos)
    - add(h)
    - substract(h)

- String:
    - Nos imprimirá la hora en formato HH:MM:SS
"""


# =============================================================================================


## EJERCICIO 15: 3 / 4 en Raya
class TresEnRaya:
    def __init__(self):
        self.tablero = [False, False, False, False, False, False, False, False, False]

    def __str__(self):
        cad = ""
        for i in range(len(juego.tablero)):
            if juego.tablero[i]:  ## Para representar X o vacío
                ficha = "X"
            else:
                ficha = " "

            cad += "[" + ficha + "]"
            if i == 2 or i == 5:
                cad += "\n"
        return cad


juego = TresEnRaya()
print(juego)


# =============================================================================================


## REPASO REGISTROS
class Alumnos:
    def __init__(self, nombre, apellidos, nota):
        self.nombreCompleto = apellidos + ", " + nombre
        self.nota = nota

    def __str__(self):
        return "{self.nombreCompleto}\nNota: {self.nota}".format(self=self)


alumno1 = Alumnos("Javier", "Salado Ramos", 5)
print(alumno1.nombreCompleto)
print(alumno1.nota)
print(alumno1)
