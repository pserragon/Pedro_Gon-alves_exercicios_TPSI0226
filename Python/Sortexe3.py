
palavra = "algoritmo"

letras = list(palavra)
n = len(letras)

for i in range(n):
    for j in range(n - 1):
        if ord(letras[j]) > ord(letras[j + 1]):
            temp = letras[j]
            letras[j] = letras[j + 1]
            letras[j + 1] = temp

resultado = "".join(letras)

print(resultado)