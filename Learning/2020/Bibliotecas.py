# Módulos / Biblioteca
## (math, random, os, ...)
from random import randint as r
from math import log10, exp, pi

print(r(1, 10))
print(log10(20))
print(exp(2))
print(pi)

"""
from turtle import *
color('red', 'yellow')
begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()
done()
"""


# =============================================================================================


# ToDo: type() y isinstance()
var = "Hola"
print(type(var))

if isinstance(var, str):
    print("Es del tipo que preguntamos")
