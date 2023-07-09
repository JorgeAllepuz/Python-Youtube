import re

nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María López"
nombre4="sandra García"
nombre5="Jara"
nombre6="Lara"

cadena1="Jorge Allepuz"
cadena2="465432165"
cadena3="a46516516"

# la función match busca coincidencias siempre al comienzo de la cadena de texto

#if re.match("Sandra", nombre2): 
#if re.match("Sandra", nombre4, re.IGNORECASE): # admite un tercer parametro re.IGNORECASE para hacer una busqueda no keysensitive
#if re.match(".ara", nombre5): # . actua como comodín
if re.match("\d", cadena2): # \d de digit busca digito al comienzo
    print("Hemos encontrado el nombre o numero")
else:
    print("No hemos encontrado el nombre o numero")


# la funcion search busca coincidencias en toda la cadena de texto

if re.search("ó", nombre1): 
    print("Hemos encontrado el nombre o numero")
else:
    print("No hemos encontrado el nombre o numero")


