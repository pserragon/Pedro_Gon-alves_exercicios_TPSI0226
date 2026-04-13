# Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.


numero = 1

print("Números Ímpares:")
while numero <= 60:
    if numero % 2 != 0:
        print(numero)
    numero = numero + 1

numero = 1

print("\nNúmeros Pares:")
while numero <= 60:
    if numero % 2 == 0:
        print(numero)
    numero = numero + 1




