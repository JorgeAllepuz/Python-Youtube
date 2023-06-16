email=input("Introduce tu dirección de Email: ")

#while (email.count("@")!=1 or email.rfind("@")==(len(email)-1) or email.find("@")==0):
while email.count("@") != 1 or "@" in email[:1] or "@" in email[-1:]:
    print("Email incorrecto")
    email=input("Introduce tu dirección de Email: ")
else:
    print("Email correcto")