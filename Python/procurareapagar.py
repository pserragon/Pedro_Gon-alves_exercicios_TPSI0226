
nomes = ["da","fa","oi","da"]

def insert(nomesi):
    nomesi.append(input("insert um nome: "))

def listar(nomesl):
    print("\n--- LISTA ---")
    for i in range(len(nomesl)):
        print(i, "-", nomesl[i])

def delete(nomesd):
    pos = int(input("insert posição: "))
    if pos >= 0 and pos < len(nomesd):
        nomesd.pop(pos)
        print("Nome apagado")
    else:
        print("Posição inválida")

def procurar(nomesp):
    nome = input("insert nome: ")

    for i in range(len(nomesp)):
        if nomesp[i] == nome:
            print("Encontrado:", nome, "na posição", i)

            op = input("Apagar? (s/n): ")

            if op == "s":
                nomesp.pop(i)
                print("Apagado:", nome, "da posição", i)

            return

    print("Nome não encontrado")

while True:
    listar(nomes)   

    print("\n1 - inserir nome")
    print("2 - listar nomes")
    print("3 - delete nome")
    print("4 - procurar nome")
    print("5 - sair")

    opt = input("Escolha Opção: ")

    match opt:
        case "1":
            insert(nomes)
        case "2":
            listar(nomes)
        case "3":
            delete(nomes)
        case "4":
            procurar(nomes)
        case "5":
            print("fim do programa")
            break
        case _:
            print("Opção inválida")