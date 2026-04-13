dia = input("Dia da semana: ").lower()

match dia:
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sábado" | "domingo":
        print("Fim de semana")
    case _:
        print("Dia inválido")