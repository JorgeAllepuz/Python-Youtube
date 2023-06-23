from tkinter import *
raiz=Tk()
raiz.title("Calculadora de Jorge")
miFrame=Frame(raiz)
miFrame.pack()

operacion=""
reset_pantalla=False
resultado=0

# pantalla de la calculadora
numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=0,  column=0,  padx=5,  pady=0,  columnspan=4)
pantalla.config(bg="black",  width=28,  fg="green",  justify="right")

# pulsaciones teclado

def numeroPulsado(num):
    global operacion
    global reset_pantalla
    if reset_pantalla!=False:
        numeroPantalla.set(num)
        reset_pantalla=False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)


# función suma
def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado+=int(num) # resultado=resultado + int(num)
    operacion="suma"
    reset_pantalla=True
    numeroPantalla.set(resultado)

# función resta
num1=0
contador_resta=0
def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_resta==1:
            resultado=num1-int(num)
        else:
            resultado=int(resultado)-int(num)
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    contador_resta=contador_resta + 1
    operacion="resta"
    reset_pantalla=True

# función multiplicación
contador_multi=0
def multiplica(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global contador_resta
    global reset_pantalla
    if contador_multi==0:
        num1=int(num)
        resultado=num1
    else:
        if contador_multi==1:
            resultado=num1*int(num)
        else:
            resultado=int(resultado)*int(num)
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    
    contador_multi=contador_multi + 1
    operacion="multiplicacion"
    reset_pantalla=True

# función division
contador_divi=0
def divide(num):
    global operacion
    global resultado
    global num1
    global contador_divi
    global reset_pantalla
    if contador_divi==0:
        num1=float(num)
        resultado=num1
    else:
        if contador_divi==1:
            resultado=num1/float(num)
        else:
            resultado=float(resultado)/float(num)
        numeroPantalla.set(resultado)
        resultado=numeroPantalla.get()
    contador_divi=contador_divi + 1
    operacion="division"
    reset_pantalla=True

# función igual_resultado
def igual_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi
    
    if operacion=="suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
        resultado=0
    elif operacion=="resta":
        numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))
        resultado=0
        contador_resta=0
    elif operacion=="multiplicacion":
        numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))
        resultado=0
        contador_multi=0
    elif operacion=="division":
        numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))
        resultado=0
        contador_divi=0


# primera fila de la calculadora
botonSiete=Button(miFrame,  text="7", width=3, command=lambda:numeroPulsado("7"))
botonSiete.grid(row=1, column=0)
botonOcho=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
botonOcho.grid(row=1, column=1)
botonNueve=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
botonNueve.grid(row=1, column=2)
botonDiv=Button(miFrame, text="/", width=3, command=lambda:divide(numeroPantalla.get()))
botonDiv.grid(row=1, column=3)

# segunda fila de la calculadora
botonCuatro=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
botonCuatro.grid(row=2, column=0)
botonCinco=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
botonCinco.grid(row=2, column=1)
botonSeis=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
botonSeis.grid(row=2, column=2)
botonMult=Button(miFrame, text="X", width=3, command=lambda:multiplica(numeroPantalla.get()))
botonMult.grid(row=2, column=3)


# tercera fila de la calculadora
botonUno=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
botonUno.grid(row=3, column=0)
botonDos=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
botonDos.grid(row=3, column=1)
botonTres=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
botonTres.grid(row=3, column=2)
botonRest=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=3, column=3)

# cuarta fila de la calculadora
botonCero=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
botonCero.grid(row=4, column=0)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=4, column=1)
botonIgual=Button(miFrame,text="=", width=3, command=lambda:igual_resultado())
botonIgual.grid(row=4, column=2)
botonSum=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=4, column=3)

raiz.mainloop()