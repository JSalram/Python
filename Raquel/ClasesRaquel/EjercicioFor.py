alumnos = ["Javier", "Adriana", "Manuel", "Patricia", "Jorge", "Rocío"]
alumnos.sort()
print(alumnos)

for i in range(len(alumnos)):  # len(alumnos) ==> 5
    print(str(i+1) + " - " + alumnos[i])

"""
## Equivalente a:
i = 0
while i < len(alumnos):
    print(str(i+1) + " - " + alumnos[i])
    i += 1
"""
