from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1,padx=5,pady=5)
cuadroNombre.config(fg="red",justify="center")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=5,pady=5)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1,padx=5,pady=5)

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=5,pady=5)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=1,column=0,sticky="e",padx=5,pady=5)

direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=2,column=0,sticky="e",padx=5,pady=5)
raiz.mainloop()