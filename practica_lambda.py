# funciones tradicionales
"""def area_triangulo(base, altura):
    return(base*altura)/2

print(area_triangulo(5,7))"""

# Las funciones lambda son funciones anónimas que nos ayudan a simplificar el codigo, estan diseñadas para calculos sencillos sin condicionales.
area_triangulo=lambda base,altura:(base*altura)/2

print(area_triangulo(2,4))

triangulo1=area_triangulo(2,4)
print(triangulo1)

# otras funciones lambda

#alCubo=lambda numero:pow(numero,3)
alCubo=lambda numero:numero**3

print(alCubo(13))

# otras funciones lambda
destacar_valor=lambda comision:"¡{}! €".format(comision)

comision_Ana=15585

print(destacar_valor(comision_Ana))