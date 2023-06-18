from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas") # inserta el titulo en la ventana
raiz.resizable(True,True) # bloquea o permite modificar el tamaño de la ventana
raiz.geometry("650x350") # asigna el tamaño de la ventana
raiz.config(bg="blue")
#raiz.iconbitmap("imagen.ico") # no funciona, he leido que en linux no funciona .ico
raiz.mainloop()

