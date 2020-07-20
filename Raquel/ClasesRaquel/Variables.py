# int = 23
# float = 2.5
# char = '@'
# string = "Javier"
# bool = True

nombre = "Javier"
edad = input("Edad: ")
apellido = "Salado"

try:
    edadStr = int(edad)
except:
    print("No se puede convertir")
    exit()

# ...
# ...
# ...

print("Hola me llamo " + nombre, apellido + " y tengo " + str(edad) + " años")
