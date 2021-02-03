# Debe funcionar para cualquier cadena
def quitaAcentos(cad,vocal,vocalSinAcento):
    
    cadNew = ""
    
    for letra in cad:
        if letra == vocal:
            cadNew += vocalSinAcento
        else:
            cadNew += letra
    
    return cadNew

cad = "quería compré día"

a = (quitaAcentos(cad,"í","i"))
print(quitaAcentos(a,"é","e"))




def quitaAcentos2(cad):
    acentos = "ÁÉÍÓÚáéíóú"
    sinAcentos = "AEIOUaeiou"

    nuevaCad = ""

    for letra in cad:
        if letra in acentos:
            pos = acentos.index(letra)
            nuevaCad += sinAcentos[pos]
        else:
            nuevaCad += letra
        
    return nuevaCad


cadena = input("Cadena: ")
print(quitaAcentos2(cadena))
