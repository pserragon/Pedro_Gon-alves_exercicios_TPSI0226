alunos = []

def inserir():
    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)

def listar():
    resultado = ""
    for aluno in alunos:
        resultado += f"nome: {aluno['nome']}\n"
        resultado += f"idade: {aluno['idade']}\n"
        resultado += f"curso: {aluno['curso']}\n\n"
    return resultado

while True:
    print("1 - Inserir")
    print("2 - Listar")
    print("0 - Sair")

    op = input("Opção: ")

    if op == "1":
        inserir()
    elif op == "2":
        print(listar())
    elif op == "0":
        break
    else:
        print("Opção inválida")