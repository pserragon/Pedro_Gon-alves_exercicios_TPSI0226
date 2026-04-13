frase = input("Introduz uma frase: ").lower()

palavras = frase.split()

contador = {}
total = 0

for palavra in palavras:
    total += 1
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print(contador)
print("Total de palavras:", total)