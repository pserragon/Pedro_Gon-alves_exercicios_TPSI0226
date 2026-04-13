# 1 a 100 com doWhile


numero = int(input("Digite um número entre 1 e 100: "))

while numero < 1 or numero > 100:
    numero = int(input("Número inválido. Digite um número entre 1 e 100: "))

print("Número válido:", numero)



