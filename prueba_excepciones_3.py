import math
def calculaRaiz(num1):
    if num1<0:
        raise ValueError ("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=int(input("Introduce un número: "))
try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print("Programa terminado")

###############################################################
"""def evaluaEdad(edad):
    if edad<0:
        raise TypeError("Edad introducida no valida")
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Eres mayor"
    
print(evaluaEdad(15))"""