
nota = int(input("Nota: "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70:
        print("Bom")
    case n if n >= 50:
        print("Suficiente")
    case n if n >= 0:
        print("Insuficiente")
    case _:
        print("Valor inválido")