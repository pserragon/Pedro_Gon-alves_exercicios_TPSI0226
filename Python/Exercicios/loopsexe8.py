# 10, 20, 30, 40, ..... 980, 990, 1000.e outro a fazer 15, 25, 35, 985, 995.(dois ciclos)
numero = int(input("Digite um número entre 1 e 100: "))

while numero < 1 or numero > 100:
    print("Número inválido!")
    numero = int(input("Digite novamente um número entre 1 e 100: "))

print("Número válido:", numero)
