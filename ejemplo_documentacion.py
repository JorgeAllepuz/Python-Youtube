from modulos import funciones_matematicas
class Areas:
    """Esta clase calcula las áreas de diferentes áreas geométricas"""

    def areaCuadrado(lado):
        """Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro"""
        return "El area del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):
        """Calcula el área de un triángulo utilizando los parámetros base y altura"""
        return "El área del triángulo es: "+ str((base*altura)/2)

#print(Areas.areaTriangulo(2,7))

#print(Areas.areaCuadrado.__doc__) # imprime la documentación asociada a esa función

#help(Areas.areaTriangulo) # imprime la documentación asociada a esa función y ayuda extra

#help(Areas) # imprime la documentación asociada a esa función y ayuda extra

help(funciones_matematicas)

