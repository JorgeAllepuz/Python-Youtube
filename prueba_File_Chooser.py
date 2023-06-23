from tkinter import *
from tkinter import filedialog
import os

root=Tk()

def abreFichero():
    dir_inicio = os.path.expanduser("~")
    fichero=filedialog.askopenfilename(title="Abrir", initialdir=dir_inicio,filetypes=(("Todos los ficheros","*.*"), ("Ficheros de Excel", "*.xlsx"), ("Ficheros de texto","*.txt")))
    print(fichero)

Button (root, text="Abrir fichero", command=abreFichero).pack()


root.mainloop()