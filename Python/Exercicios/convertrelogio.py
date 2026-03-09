# Exercício 2: Reajuste salarial
salario = float(input("Digite o salário atual: "))

if salario <= 1000:
    percentual = 0.20
elif salario <= 3000:
    percentual = 0.15
elif salario <= 5000:
    percentual = 0.10
else:
    percentual = 0.05

novo_salario = salario * (1 + percentual)
print(f"Novo salário: R$ {novo_salario:.2f}")