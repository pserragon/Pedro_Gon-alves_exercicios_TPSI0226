# Exercício 7: Reajuste com escala adicional
salario = float(input("Digite o salário: "))

if salario <= 1000:
    novo = salario * 1.20
elif salario <= 2000:
    novo = salario * 1.15
elif salario <= 5000:
    novo = salario * 1.10
else:
    novo = salario * 1.05

print(f"Novo salário: R$ {novo:.2f}")