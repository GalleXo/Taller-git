print("¿Cuál es su edad?")
Edad = input()
Edad = int(Edad)
print("¿Cuál es su ingreso mensual?")
IngresoM = input()
IngresoM = int(IngresoM)
if Edad >= 18 and IngresoM >= 3000000:
    print("Tiene que tributar.")
else:
    print("No tiene que tributar.")