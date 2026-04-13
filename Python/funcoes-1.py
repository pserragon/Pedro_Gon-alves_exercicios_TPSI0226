# e um bloco isolado de codigo q pode ser chamado repetidamente evitando a repeticao de codigo 
# dado pertencer a um bloco de condigo pequeno tornando mais facil a sua manutençao 

# em seguranca no scope quando bem aplicada uma funcao pode criar uma abstracao dos outros blocos ou do cod principal 
# scopes e manipulação sao feitos atravez da passagem de valores/parametros e passagem das referencias das variaveis 

num1=12
num2=13

# valordereturn nomedafunçao (parametros de entrada)


def troca(nu1,nu2):
    nu1,nu2 = nu2,nu1
    return nu1,nu2


troca (num1, num2)
print ("num 1:" , num1,"num 2: ", num2)


# passagem por referencia 

lista1=[12,14,15]

print("lista antes da funçao", lista1)

def insertvalue(lista):
    lista.append(19)

insertvalue(lista1)

print("lista antes da funçao", lista1)



# algoritmos funcoes

nomes=[]
listanomeadora=[]

def insert (nomesi):
    nomesi.append(input("insert um nome"))


def listar(nomesl):
    for nome in nomes1 :
        print("nome : ", nome)



def delete (nomesd):
    nomes.pop( int(input("insert posicçao ")))

def procurar(nomesp:list):
    nome=input("insert nome de procura")
    for i in range(len(nomesp)):
        if nomesp[i] == nome:
            print("nome: ",nomesp[i] ," na posiçao ", i)
           



nomes=["da","fa","oi","da"]
#index   0    1    2   3
 
 
def insert(nomesi:list):
    nomesi.append(input("insert um nome"))
 
def listar(nomesl:list):
    for nome in nomesl:
        print("nome : " , nome)
 
def delete(nomesd:list):
    nomesd.pop( int(input(" insert posiçao ")))
 
def procurar(nomesp:list):
    nome=input("insert nome de procura")
    for i in range(len(nomesp)):
        if nomesp[i] == nome:
            print("nome: ",nomesp[i] ," na posiçao ", i)
   
 
while True:
    print ("1 - inserir nome")
    print ("2 - listar nomes")
    print ("3 - delete nome")
    print ("4 - procurar nome")
    print ("5 - sair")
    opt=input("Escolha Opção")
    match opt :
        case "1":
            insert(nomes)
        case "2":
            listar(nomes)
        case "3":
            delete(nomes)
        case "4":
            procurar(nomes)
            #print aqui os valores e posiçoes
        case "5":
            print("fim do programa")
            break
        case _:
            print("nao escolheu a opçao certa")
 