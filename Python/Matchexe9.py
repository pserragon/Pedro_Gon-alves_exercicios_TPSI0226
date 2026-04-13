requisicao = {"metodo": "POST", "conteudo": ""}

metodo = requisicao.get("metodo", "").upper()
conteudo = requisicao.get("conteudo", "")

match metodo:
    case "POST" if conteudo:
        print("Requisição POST com dados válidos")
    case "POST":
        print("Requisição POST sem dados")
    case "GET":
        print("Requisição GET recebida")
    case _:
        print("Método não suportado")