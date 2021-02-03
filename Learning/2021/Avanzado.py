# String format (f"")
saludo = "Hola"
nombre = "Enrique"

print(f"{saludo} me llamo {nombre}")

print("=============================================")

# if (asignación)
n = 6
par = "Es par" if n % 2 == 0 else "No es par"

print(par)

print("=============================================")

# Listas de comprensión
numeros = [2, 3, 4, 5]
doble = [n * 2 for n in numeros if n % 2 == 0]

# doble = []
# for n in numeros:
#     if n % 2 == 0:
#       doble += [n*2]

print(numeros)
print(doble)

print("=============================================")

# Declarar varias variables
a, b, c = 1, 2, 3
x = y = z = 5
n1, n2, *ns = 10, 20, 30, 40, 50
print(n1, n2, ns)

print("=============================================")

# Intercambiar valores
n1 = 1
n2 = 4
print(n1, n2)
if n2 > n1:
    n1, n2 = n2, n1

print(n1, n2)

print("=============================================")

# enumerate()
nums = [61, 23, 65]
for i, n in enumerate(nums, 1):
    print(f"{i} --> {n}")

print("=============================================")

# Descomprimir lista
lista = [1, 2, 3, 4, 5]
uno, dos, *_, cinco = lista
print(uno, dos, cinco)
