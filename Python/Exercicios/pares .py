# pares

pares = 0
impares = 0
numero = 1

while pares < 30 or impares < 30:

    if numero % 2 == 0 and pares < 30:
        print("Par:", numero)
        pares = pares + 1

    elif numero % 2 != 0 and impares < 30:
        print("Ímpar:", numero)
        impares = impares + 1

    numero = numero + 1