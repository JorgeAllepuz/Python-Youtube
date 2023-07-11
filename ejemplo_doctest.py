

def areaTriangulo(base, altura):
    """
    Esta función calcula el área de un triángulo dado
    >>> areaTriangulo(3,6)
    'El área del triángulo es: 9.0'
    >>> areaTriangulo(4,5)
    'El área del triángulo es: 10.0'
    >>> areaTriangulo(9,3)
    'El área del triángulo es: 13.5'
    """
    return "El área del triángulo es: "+str((base*altura)/2)


def compruebaMail(mailUsuario):
    """
    La función compruebaMail evalúa un email recibido en busca de la @. Si tiene
    una @ es correcto, si tiene más de una @ es incorrecto y si la @ está al final
    del email del usuario es incorrecta

    >>> compruebaMail('jorge@hotmail.com')
    True

    >>> compruebaMail('jorgehotmail.com@')
    False

    >>> compruebaMail('jorgehotmail.com')
    False

    >>> compruebaMail('jorge@hotmail.@com')
    False
    """
    arroba=mailUsuario.count("@")
    if (arroba !=1 or mailUsuario.rfind("@")==(len(mailUsuario)-1) or mailUsuario.find("@")==0):
        return False
    else:
        return True


import doctest
doctest.testmod()