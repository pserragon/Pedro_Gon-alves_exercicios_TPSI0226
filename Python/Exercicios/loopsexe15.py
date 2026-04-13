# Exercício 16


soma = 0


contador = 0

while contador < 30:
    
    numero = int(input("Digite um número par entre 1 e 50: "))
    
    if numero >= 1 and numero <= 50 and numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
    
    
    
    else:
        print("Número inválido!")

media = soma / 30

print("A média dos números é:", media)