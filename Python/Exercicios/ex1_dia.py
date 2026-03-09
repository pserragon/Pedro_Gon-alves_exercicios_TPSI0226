# Exercício 2: Classificação de número
num = input("Digite um número de 1 a 3: ").strip()

match num:
    case "1":
        print("Número um")
    case "2":
        print("Número dois")
    case "3":
        print("Número três")
    case _:
        print("Número inválido")