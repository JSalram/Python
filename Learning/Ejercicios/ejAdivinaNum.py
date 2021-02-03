import random
# Bien pensado el random

def AdivinaNum():

    a = random.randrange(1,100)
    seguir = True
    repeticiones = 0

    while seguir:
        n = int(input("¿Qué número crees que es? "))
        if a == n:
            repeticiones +=1 
            if repeticiones == 1:
                print("Increíble, lo has acertado a la primera")
            elif 2 <= repeticiones <= 5:
                print ("{} intentos, está genial".format(repeticiones))
            elif repeticiones > 5:
                print("Has necesitado {} intentos...".format(repeticiones))
            seguir = False  
        
        elif a < n:
            print("El número a adivinar es menor que",n)
            repeticiones += 1
        
        elif a > n:
            print("El número a adivinar es mayor que",n)
            repeticiones += 1



print(AdivinaNum())  #print() no es necesario

