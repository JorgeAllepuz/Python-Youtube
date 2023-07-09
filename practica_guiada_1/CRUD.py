from tkinter import *
from tkinter import messagebox
import sqlite3

raiz=Tk()
raiz.title("Programa de datos")

miFrame=Frame(raiz,width=300, height=400)
miFrame.pack()

# funciones

def conexionBBDD():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR (50),
            PASSWORD VARCHAR (50),
            APELLIDO VARCHAR (50),
            DIRECCION VARCHAR (50),
            COMENTARIOS VARCHAR (100))
            ''')

        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya existe")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor=="yes":
        raiz.destroy()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    comCuadro.delete(1.0, END)

def crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    # a continuacion dos maneras de hacerlo, una comentada para evitar error
    """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '"+ miNombre.get() +
                     "','" + miPass.get() +
                     "','" + miApellido.get() +
                     "','" + miDireccion.get() +
                     "','" + comCuadro.get("1.0", END) + "')")"""
    
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),comCuadro.get("1.0", END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
    
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")
    limpiarCampos()

def leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miId.get())

    elUsuario=miCursor.fetchall()
    for usuario in elUsuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        comCuadro.insert(1.0, usuario[5])

    miConexion.commit()

def actualizar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    # a continuacion dos maneras de hacerlo, una comentada para evitar error
    
    """miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='" + miNombre.get() +
                    "', PASSWORD='" + miPass.get() + 
                    "', APELLIDO='" + miApellido.get() +
                    "', DIRECCION='" + miDireccion.get() +
                    "', COMENTARIOS='" + comCuadro.get("1.0", END) +
                    "' WHERE ID=" + miId.get())"""
    
    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),comCuadro.get("1.0", END)
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=?, APELLIDO=?, PASSWORD=?, DIRECCION=?, COMENTARIOS=?" +
                     "WHERE ID=" + miId.get(),(datos))
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado correctamente")
    limpiarCampos()

def borrar():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miId.get())
    
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado correctamente")
    limpiarCampos()



# menú de la interfaz grafica

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=limpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar", command=borrar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")


barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

# descripcion de los label de los cuadros de texto

idLabel=Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=5, pady=5)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=5, pady=5)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=5, pady=5)

apeLabel=Label(miFrame, text="Apellidos:")
apeLabel.grid(row=3, column=0, sticky="e", padx=5, pady=5)

dirLabel=Label(miFrame, text="Dirección:")
dirLabel.grid(row=4, column=0, sticky="e", padx=5, pady=5)

comLabel=Label(miFrame, text="Comentarios:")
comLabel.grid(row=5, column=0, sticky="ne", padx=5, pady=5)

# cuadros entry para introducir texto

miId=StringVar()
miNombre=StringVar()
miPass=StringVar()
miApellido=StringVar()
miDireccion=StringVar()

idCuadro=Entry(miFrame, textvariable=miId)
idCuadro.grid(row=0, column=1, padx=5, pady=5)
idCuadro.config(bg="black", fg="red", justify="left")

nombreCuadro=Entry(miFrame, textvariable=miNombre)
nombreCuadro.grid(row=1, column=1, padx=5, pady=5)

passCuadro=Entry(miFrame, textvariable=miPass)
passCuadro.grid(row=2, column=1, padx=5, pady=5)
passCuadro.config(show="*")

apeCuadro=Entry(miFrame, textvariable=miApellido)
apeCuadro.grid(row=3, column=1, padx=5, pady=5)

dirCuadro=Entry(miFrame, textvariable=miDireccion)
dirCuadro.grid(row=4, column=1, padx=5, pady=5)

comCuadro=Text(miFrame, width=20, height=8)
comCuadro.grid(row=5, column=1, padx=5, pady=5)

comScroll=Scrollbar(miFrame, command=comCuadro.yview)
comScroll.grid(row=5, column=1, padx=5, pady=5, sticky="nse")

comCuadro.config(yscrollcommand=comScroll.set) # hace que el ascensor del scroll funcione bien

# botones inferiores

miFrame2=Frame(raiz)
miFrame2.pack()

crearBoton=Button(miFrame2, text="Create", command=crear)
crearBoton.grid(row=0, column=0, sticky="e", padx=5, pady=5)

leerBoton=Button(miFrame2, text="Read", command=leer)
leerBoton.grid(row=0, column=1, sticky="e", padx=5, pady=5)

ActualBoton=Button(miFrame2, text="Update", command=actualizar)
ActualBoton.grid(row=0, column=2, sticky="e", padx=5, pady=5)

borrarBoton=Button(miFrame2, text="Delete", command=borrar)
borrarBoton.grid(row=0, column=3, sticky="e", padx=5, pady=5)

raiz.mainloop()


