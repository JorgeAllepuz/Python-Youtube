"""nombreUsuario=input("Introduce tu nombre de usuario: ")
print("El nombre es: ",nombreUsuario.upper())
print("El nombre es: ",nombreUsuario.lower())
print("El nombre es: ",nombreUsuario.capitalize())"""

edad=input("Introduce la edad: ")
print(edad.isdigit())

while(edad.isdigit()==False):
    print("Por favor, introduce una edad valida")
    edad=input("Introduce la edad: ")

if (int(edad)<18):
    print("No puedes pasar")
else:
    print("Si puedes pasar")
