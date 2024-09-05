print("Pizzería Bella Napoli")
print (" 1. Si  2. No")
Pizza =input("Quiere una pizza vegetariana?.  (1 o 2):")
if Pizza == "1":
    print(" P. Pimiento  T. Tofu")
    Vegetariana = input(" Elija un ingrediente (P o T):")
    if Vegetariana == "P":
        print("La pizza es vegetariana y viene con mozzarella, tomate y pimiento.")
    else:
        print("La pizza es vegetariana y viene con mozzarella, tomate y tofu.")
else:
    print("p. Peperoni  j. Jamón  s. Salmón")
    NoVegetariana = input("Elija un ingrediente (p, j o s): ")
    if NoVegetariana == "p":
        print("La pizza no es vegetariana y viene con mozzarella, tomate y peperoni.")
    elif NoVegetariana == "j":
        print("La pizza no es vegetariana y viene con mozzarella, tomate y jamón.")
    else:
        print("La pizza no es vegetariana y viene con mozzarella, tomate y salmón.") 