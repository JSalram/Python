anno = int(input("introduce un año: "))

if anno % 4 == 0 and (anno % 400 == 0 or anno % 100 != 0):
    print ("es bisiesto")
else:
    print ("no es bisiesto")

# año % 4 ==> año % 4 == 0
# año & 400 ==> año % 400 == 0
# Cuidado con los caracteres
# Fuera paréntesis
# SUGERENCIA COMÚN: Dar espacios entre operaciones para facilitar lectura

# Fallo mío: (divisible entre 400 OR indivisible entre 100)
