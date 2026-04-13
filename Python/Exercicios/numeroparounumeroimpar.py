# ler a nota de 10 alunos calcular a media 

soma = 0

for i in range(10):
 
 nota = float(input("Digite a nota do aluno: "))
 
 soma = soma + nota

 media = soma / 10

 print("A média é:", media)

