# Exercício 12

numero = int(input("Digite um número: "))

contador = 0

for i in range(1, numero):
    
    soma = numero + i
    sub = numero - i
    mult = numero * i
    div = numero / i

    print(numero, "+", i, "=", soma)
    print(numero, "-", i, "=", sub)
    print(numero, "*", i, "=", mult)
    print(numero, "/", i, "=", div)
    print()

    contador = contador + 4

print("Total de operações realizadas:", contador)