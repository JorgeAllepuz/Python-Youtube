def funcion_decoradora(funcion_paramatro):
    def funcion_interior(*args, **kwargs): # args le indica a la funcion que puede recibir un numero indeterminado de parametros
        # Acciones adicionales que decoran
        print("vamos a realizar un cálculo")
        funcion_paramatro(*args, **kwargs) # kwargs permite recibir argumentos del tipo clave=valor
        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo")
    return funcion_interior









@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
    print(base**exponente)


suma(7,5,3)

resta(12,10)

potencia(5,3)

potencia(base=5, exponente=3)