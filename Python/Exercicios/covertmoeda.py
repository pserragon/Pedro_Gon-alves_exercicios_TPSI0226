# Exercício 5: Mensagem de status
status = input("Digite o status (ok, erro, pendente): ").strip().lower()

match status:
    case "ok":
        print("Tudo certo")
    case "erro":
        print("Ocorreu um erro")
    case "pendente":
        print("Aguardando ação")
    case _:
        print("Status inválido")