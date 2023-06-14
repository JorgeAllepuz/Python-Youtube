class Coche():
    def __init__(self): # constructor
        self.__largoChasis=250 # encapsulación
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False

    def arrancar(self,arrancamos):
        self.__enMarcha=arrancamos
        if(self.__enMarcha):
            chequeo=self.__chequeoInterno()
        if(self.__enMarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enMarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas", "un ancho de ", self.__anchoChasis, "y un largo de ", self.__largoChasis)

    def __chequeoInterno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
        

miCoche=Coche() # instancia de clase
print(miCoche.arrancar(True))
print(miCoche.estado())

print("-----------A continuacion mostramos el segundo objeto---------------")

miCoche2=Coche() # instancia de clase
print(miCoche2.arrancar(False))
print(miCoche2.estado())
