import sqlite3

#miConexion=sqlite3.connect("GestionProductos")
miConexion=sqlite3.connect("ProductosAutomatica")

miCursor=miConexion.cursor()

# CREA LA BASE DE DATOS
"""miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')"""

# INSERTA VARIOS ARTICULOS A LA VEZ
"""productos=[
    ("AR01", "pelota", 20, "juguetería"),
    ("AR02", "pantalon", 15, "confección"),
    ("AR03", "destornillador", 25, "ferretería"),
    ("AR04", "jarron", 45, "cerámica")

]    

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)"""

# INSERTA ARTICULOS DE UNO EN UNO
"""miCursor.execute("INSERT INTO PRODUCTOS VALUES('AR06', 'tren', 15, 'juguetería')")"""

# CREA UNA BASE DE DATOS CON EL CAMPO CLAVE AUTOMÁTICO Y AÑADIMOS ARTICULOS
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')
                 
productos=[
    ("pelota", 20, "juguetería"),
    ("pantalon", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarron", 45, "cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miConexion.commit()

miConexion.close()