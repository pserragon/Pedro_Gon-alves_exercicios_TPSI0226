# Exercício 3: Pedra, Papel ou Tesoura
jogada = input("Escolha: pedra, papel ou tesoura: ").strip().lower()

match jogada:
    case "pedra":
        print("Jogaste Pedra")
    case "papel":
        print("Jogaste Papel")
    case "tesoura":
        print("Jogaste Tesoura")
    case _:
        print("Escolha inválida")