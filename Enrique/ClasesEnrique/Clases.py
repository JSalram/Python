# Clases / Registros
## Atributos (__init__)
class Coche:
    def __init__(self, marca, modelo, matricula):
        self.marca = marca
        self.modelo = modelo
        if self.compruebaMatricula(matricula):
            self.matricula = matricula
        else:
            self.matricula = "Sin matrícula"

    @staticmethod
    def compruebaMatricula(matricula):
        matriculaCorrecta = True

        if len(matricula) == 7:
            for i in range(len(matricula)):
                if i < 4:
                    if not matricula[i].isdecimal():
                        matriculaCorrecta = False
                else:
                    if matricula[i].isdecimal():
                        matriculaCorrecta = False
        else:
            matriculaCorrecta = False

        return matriculaCorrecta

    def __str__(self):
        # return "{} {} - {}".format(self.marca, self.modelo, self.matricula)
        return "{self.marca} {self.modelo} - {self.matricula}".format(self=self)

## Objetos
miCoche = Coche("Renault", "Megane", "1234BCD")
miCoche.matricula = "4721KLG"
print(miCoche.marca + " " + miCoche.modelo + " - " + miCoche.matricula)

## Métodos mágicos (__str__)
coche2 = Coche("Seat", "León", "3632FGK")
print(coche2)

## Métodos (def)
coche3 = Coche("Audi", "A4", "42234TFR")
print(coche3)


class Math:
    def pi():
        return 3.14

    def mult(x, y):
        return x * y


math = Math
print(math.mult(2, 3))
print(math.pi())


## Métodos estáticos (@staticmethod)
class Math:
    @staticmethod
    def pi():
        return 3.14

    @staticmethod
    def mult(x, y):
        return x * y

    @staticmethod
    def restar(x, y):
        return x - y


print(Math.restar(3, 2))


# =============================================================================================


# ToDo EJERCICIO: Alumnos
class Alumno:
    def __init__(self, numero, nombre, apellidos, nota):
        self.numero = numero
        self.nombre = nombre
        self.apellidos = apellidos
        self.nota = nota

    @staticmethod
    def media(listaClase):
        n = 0
        for alumno in listaClase:
            n += alumno.nota

        return round(n / len(listaClase), 2)

alumno1 = Alumno(1, "Juan", "Martinez Pérez", 4.6)
alumno2 = Alumno(2, "Rocío", "Martinez Pérez", 7)
alumno3 = Alumno(3, "Pepe", "Martinez Pérez", 8)

alumnos = [alumno1, alumno2, alumno3]
print(Alumno.media(alumnos))


# Otra forma de hacerlo
class Alumnos:
    def __init__(self, alumno, notas):
        self.alumno = alumno
        self.notas = notas

    def annadeAlumno(self, alumno, nota):
        self.alumno.append(alumno)
        self.notas.append(nota)

    def media(self):
        n = 0
        for nota in self.notas:
            n += nota

        return round(n / len(self.notas), 2)

    def __str__(self):
        cad = "___LISTA_ALUMNOS___\n"
        for i in range(len(self.alumno)):
            cad = cad + str(i+1) + " - " + self.alumno[i] + ": " + str(self.notas[i])
            cad += "\n"

        return cad


alumnos = ["Juan", "Pepe", "Rocío"]
notas = [3, 5, 7]

# aula = Alumnos([], [])
aula = Alumnos(alumnos, notas)
print(aula.media())

alumno = input("Alumno: ")
nota = input("Nota: ")

aula.annadeAlumno(alumno, nota)
print(aula)
