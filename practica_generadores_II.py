def devuelveCiudades(*ciudades): # El asterisco indica que la función va a recibir un numero indeterminado de ciudades y ademas en forma de tupla.
    for elemento in ciudades:
            yield from elemento

ciudadesDevueltas=devuelveCiudades("Madrid","Barcelona","Castellon","Zaragoza")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))