servidor = {"status": "ok", "tempo_resposta": 350}

status = servidor.get("status", "").lower()
tempo = servidor.get("tempo_resposta", 0)

match status:
    case "ok" if tempo > 200:
        print("Servidor lento")
    case "ok":
        print("Servidor ativo")
    case "erro":
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")