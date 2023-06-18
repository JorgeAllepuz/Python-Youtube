from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas") # inserta el titulo en la ventana
raiz.resizable(True,True) # bloquea o permite modificar el tamaño de la ventana
#raiz.geometry("650x350") # asigna el tamaño de la ventana
raiz.config(bg="blue")
#raiz.iconbitmap("imagen.ico") # no funciona, he leido que en linux no funciona .ico
miFrame=Frame()
miFrame.pack(fill="both",expand="True")
miFrame.config(bg="red")
miFrame.config(width="650",height="350")
miFrame.config(bd=35)
miFrame.config(relief="groove")
miFrame.config(cursor="pirate")
raiz.mainloop()

