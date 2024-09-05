print("Empresa de salas de juegos")
Edad = int(input("Ingrese su edad: "))
if Edad < 4:
    print("Puede ingresar gratis.")
elif Edad < 18:
    print("Usted debe pagar 5.000")
elif  Edad > 18:
    print("Usted debe pagar 10.000")