import sqlite3

miConexion=sqlite3.connect("PrimeraBase")
miCursor=miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR (20))")
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")
#miConexion.commit()

# INSERTA VARIOS PRODUCTOS A LA VEZ EN LA TABLA
"""variosProductos=[
    ("CAMISETA", 10, "DEPORTES"),
    ("JARRON", 90, "CERÁMICA"),
    ("CAMIÓN", 20, "DEPORTES")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)"""

# MOSTRAR ELEMENTOS DE LA BASE DE DATOS
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()
print(variosProductos)

for producto in variosProductos:
    print("Nombre articulo: ",producto[0],"Sección: ", producto[2])

miConexion.commit()

miConexion.close()