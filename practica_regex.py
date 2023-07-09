import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
textoBuscar=("aprender")

print(re.search("aprender", cadena))

textoEncontrado=re.search(textoBuscar, cadena)
print(textoEncontrado)

print(textoEncontrado.start())

print(textoEncontrado.end())

print(textoEncontrado.span())

textoBuscarOtro="Python"

print(re.findall(textoBuscarOtro, cadena))
print(len(re.findall(textoBuscarOtro, cadena)))

