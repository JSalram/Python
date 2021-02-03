# Try ... except ... finally (raise)
n = input("Número: ")

try:
    n = int(n)
except:
    raise Exception("Tiene que ser un número")
finally:
    print("La conversión ha sido controlada")


# Estructuras
### Cadenas
cad = ""
saludo = "Hola"
nombre = "Enrique"
saludoNombre = saludo + " " + nombre  # Hola Enrique
print(saludoNombre)
print(saludoNombre[2:4])
print(saludoNombre[:4])
print(saludoNombre[5:])
print(saludoNombre[1:5:2])
print(saludoNombre[::2])

print(saludoNombre[-1])
print(saludoNombre[:-2])
print(saludoNombre[::-1])
""" Hola EnriqueHola Enrique """

### Listas
lista = []
mix = [3, 5.4, "Adios"]
nums = [3, 5, 6, 1, 8, 0]
nums.append(2)
nums.sort()
nums.extend([2, 3, 5])
nums.extend(mix)

nums += [100, 200, 300]
print(nums)

while 3 in nums:
    nums.remove(3)

nums2 = [3, 2, 4, 3]
del nums2[3]
print(nums2)

for n in nums2:
    print(n)
for i in range(len(nums2)):
    print(f"{i} --> {nums2[i]}")
print("="*20)

### Diccionarios
diccionario = {}
empleado = {
    "nombre": "Juan",
    "edad": 26,
    "sueldo": 855.23
}

for c in empleado:
    print(f"{c} --> {empleado[c]}")

empresa = {
    "empleados":
    [
        empleado,
        {
            "nombre": "Pepe",
            "edad": 31,
            "sueldo": 921.3
        }
    ]
}
del empresa["empleados"]
print(empresa)

### Tuplas
tupla = (1, 2, 3, 4)

# Funciones
### return+
def posNeg(x):
    return x, -x


x = 4
a, b = posNeg(x)
print(a, b)

### scope
n = int(input("Número: "))

if n > 0:
    y = 3
else:
    y = -1

print(y)

a = 200


def suma10():
    global a
    a += 10


suma10()
print(a)
