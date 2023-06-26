import sqlite3

miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

# DE ESTA MANERA VEMOS LOS ARTICULOS DE LA SECCION DE CONFECCIÓN
"""miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='juguetería'")
productos=miCursor.fetchall()
print(productos)"""

# CREAMOS UNA ACTUALIZACION DE ARTICULO, EN ESTE CASO MODIFICAMOS EL PRECIO DEL ARTICULO "PELOTA"
"""miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")"""

# BORRADO DE ARTICULO O ARTICULOS
miCursor.execute("DELETE FROM PRODUCTOS WHERE CODIGO_ARTICULO='AR06'")

miConexion.commit()

miConexion.close()