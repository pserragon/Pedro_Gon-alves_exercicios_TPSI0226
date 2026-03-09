# Exercício 6: Escala de notas com teste oral
nota = float(input("Digite a nota: "))

match nota:
    case n if n >= 90:
        print("Excelente")
    case n if n >= 75:
        print("Bom")
    case n if n >= 50:
        print("Regular")
    case _:
        print("Insuficiente")