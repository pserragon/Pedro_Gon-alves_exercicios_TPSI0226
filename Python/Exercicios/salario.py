# Exercício 3: Maior de três números
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print(f"O maior número é: {maior}")