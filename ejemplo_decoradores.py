def funcion_decoradora(funcion_paramatro):
    def funcion_interior():
        # Acciones adicionales que decoran
        print("vamos a realizar un cálculo")
        funcion_paramatro()
        # Acciones adicionales que decoran
        print("Hemos terminado el cálculo")
    return funcion_interior









@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)


suma()

resta()