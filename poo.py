class Coche(): # clase
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False

    def arrancar(self,arrancamos):
        self.enMarcha=arrancamos
        if(self.enMarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ",self.ruedas,"ruedas. Un largo de chasis de",self.largoChasis,"Un ancho de chasis de", self.anchoChasis,"")
        

print("----Primer coche------")

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("----Segundo coche-----")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()


