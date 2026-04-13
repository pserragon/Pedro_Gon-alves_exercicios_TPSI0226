# algoritmo que leia um número inteiro, e diga se ele é um número primo ou não.

numero = int(input("Digite um número inteiro: "))

contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        contador = contador + 1

if contador == 2:
    print("O número é primo")
else:
    print("O número não é primo")






