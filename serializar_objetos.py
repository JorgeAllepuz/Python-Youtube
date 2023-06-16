import pickle

class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enMarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",self.enMarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)


coche1=Vehiculos("Mazda","MX5")
coche2=Vehiculos("Seat","Leon")
coche3=Vehiculos("Renault","Clio")

coches=[coche1,coche2,coche3]
fichero=open("losCoches","wb")
pickle.dump(coches,fichero)
fichero.close()
del (fichero)

fichero_apertura=open("losCoches","rb")
misCoches=pickle.load(fichero_apertura)
fichero_apertura.close
for c in misCoches:
    print(c.estado())