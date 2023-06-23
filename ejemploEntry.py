from tkinter import *

raiz=Tk()
raiz.title("Pantalla de login de usuario")
miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()
#cuadros para introducir texto
miNombre=StringVar()
cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=0,column=1,padx=5,pady=5)
cuadroNombre.config(fg="red",justify="left")

cuadroPasswd=Entry(miFrame)
cuadroPasswd.grid(row=1,column=1,padx=5,pady=5)
cuadroPasswd.config(show="*",justify="left")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=5,pady=5)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=5,pady=5)

cuadroTexto=Text(miFrame,width=20,height=5)
cuadroTexto.grid(row=4,column=1,padx=5,pady=5)

scrollVert=Scrollbar(miFrame,command=cuadroTexto.yview)
scrollVert.grid(row=4,column=1,padx=5,pady=5,sticky="nse")

cuadroTexto.config(yscrollcommand=scrollVert.set)


# descripcion de cuadros de texto
nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=5,pady=5)

passwdLabel=Label(miFrame,text="Password:")
passwdLabel.grid(row=1,column=0,sticky="e",padx=5,pady=5)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=2,column=0,sticky="e",padx=5,pady=5)

direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=3,column=0,sticky="e",padx=5,pady=5)

textoLabel=Label(miFrame,text="Texto:")
textoLabel.grid(row=4,column=0,sticky="ne",padx=5,pady=5)

# boton
def codigoBoton():
    miNombre.set("Jorge")
botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)

botonEnvio.pack()

raiz.mainloop()