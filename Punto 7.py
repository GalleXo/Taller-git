print("Tramos Impositivos")
print("¿De cuánto es su renta? ")
renta = input()
renta = int(renta)
if renta <= 1000000:
    print("Su tipo impositivo es del 5%.")
elif renta <= 2000000:
    print("Su tipo impositivo es del 15%.")
elif renta <= 3500000:
    print("Su tipo impositivo es del 20%.")
elif renta <= 6000000:
    print("Su tipo impositivo es del 30%.")
elif renta > 6000000:
    print("Su tipo impositivo es del 45%.")