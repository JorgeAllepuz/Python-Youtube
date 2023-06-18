from tkinter import *
root=Tk() # nombramos la raiz
root.title("Mi primera ventana")
miFrame=Frame(root,width=500,height=400)
miFrame.pack()
miImagen=PhotoImage(file="graficos/pingu.gif").subsample(4,4)
# Label para la imagen
miLabelImagen=Label(miFrame,image=miImagen)
miLabelImagen.place(x=0,y=0)

# Label para el texto
miLabelTexto=Label(miFrame,text="Hola alumnos de Python",fg="blue",font=("Comic Sans MS",18))
miLabelTexto.place(x=230,y=100)


root.mainloop()
