"""i=1
while i<=10:
    print("Ejecución " + str(i))
    i+=1

print("Terminó la ejecución")"""
##########################################################
edad=int(input("Introduce tu edad: "))
contador=1
while edad<5 or edad>100:
    print("Has introducido una edad incorrecta, vuelve a intentarlo")
    
    if contador==3:
        print("Has consumido demasiados intentos")
        break
    edad=int(input("Introduce tu edad: "))
    if edad<5 or edad>100:
        contador+=1
if contador<3:
    print("Gracias por colaborar, puedes pasar")
    print("Edad del aspirante: " + str(edad))

print("Fin del programa")