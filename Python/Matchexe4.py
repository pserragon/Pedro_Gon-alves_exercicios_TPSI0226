valor = input("Valor: ")

# tentar converter para número se possível
try:
    if "." in valor:
        valor = float(valor)
    else:
        valor = int(valor)
except:
    pass

match valor:
    case int():
        print("Número inteiro")
    case float():
        print("Número decimal")
    case list():
        print("Lista")
    case str():
        if valor.isdigit():
            print("String numérica")
        else:
            print("String textual")
    case _:
        print("Tipo desconhecido")