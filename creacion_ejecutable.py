"""
1- Instalamos pyinstaler:
    desde consola ejecutamos el comando 'pip install pyinstaller'
2- Desde consola nos desplazamos al directorio donde tenemos el archivo de la aplicación
    ejecutamos 'pyinstaller practicaCalculadora.py'
3- Si queremos que nos cree un exe sin mas archivos y sin la consola de fondo, borramos los 
archivo que se han creado y ejecutaremos:
    ejecutamos 'pyinstaller --windowed --onefile practicaCalculadora.py'
4- Si queremos añadir un icono deberemos tener un archivo de imagen .ico en la misma carpeta de la aplicacion y ejecutaremos:
    ejecutamos 'pyinstaller --windowed --onefile --icon=./logo.ico practicaCalculadora.py'
4- El archivo lo encontraremos en la carpeta dist que se crea al ejecutar el comando
"""