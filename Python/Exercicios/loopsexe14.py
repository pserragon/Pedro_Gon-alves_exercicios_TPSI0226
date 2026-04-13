# Exercício 15


contador = 0

for codigo in range(256):

    print(codigo, "=", chr(codigo))
    contador = contador + 1

    if contador == 20:
        resposta = input("Deseja continuar? (s/n): ")

        if resposta == "n":
            break

        contador = 0