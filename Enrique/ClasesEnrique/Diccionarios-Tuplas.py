# Tuplas ==> Inmutables
## Definir
tupla = ()

## Definir e insertar objetos
semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print(semana[4])

## Recorrer tuplas
for dia in semana:
    print(dia)


# =============================================================================================


# Diccionarios ==> Clave y Definición
## Definir
dic = {}


## Definir e insertar objetos
notas = {"Pepe": 4.5, "Juan": 6.7, "Rocío": 8.2}
print(notas["Pepe"])


## Diccionario con claves numéricas
numDic = {2: "valor", 45: 342.2, 90: False}
print(numDic[90])


## Diccionario con claves mixtas
mixDic = {1: "Cadena", True: 4.5, 5: '@'}
print(mixDic[5])


## Diccionario con listas
listaDic = {"alumnos": ["Pepe", "Juan", "Rocío"],
            "notas": [2.3, 5.6, 3.9]}
print(listaDic)


# Añadir elementos en un diccionario vacío
fecha = {}
fecha["dia"] = 26
fecha["mes"] = "Agosto"
fecha["anno"] = 2020

print(dic)

# -------------------------------------------

dic = {"alumnos": ["Pepe", "Juan"],
       "notas": [2.5, 4]}

alumno = "Rocío"
nota = 7.8

dic["alumnos"].append(alumno)
dic["notas"].append(nota)

print(dic)

# -------------------------------------------

alumnos = ["Juan", "Pepe", "Carlos", "María"]
notas = {"Pepe": 4.5}

for alumno in alumnos:
    if alumno not in notas:
        notas[alumno] = float(input("Nota de {}: ".format(alumno)))

## Recorrer diccionarios
for clave in notas:
    print("Nota de {}: {}".format(clave, notas[clave]))


# =============================================================================================


# ToDo: Eliminar elementos
notas = {"Pepe": 4.5}
del notas["Pepe"]
