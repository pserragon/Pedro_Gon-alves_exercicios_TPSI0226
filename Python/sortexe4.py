
palavras = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

def contar_minusculas(palavra):
    contador = 0
    for letra in palavra:
        if 'a' <= letra <= 'z':
            contador += 1
    return contador

n = len(palavras)

for i in range(n):
    for j in range(i + 1, n):

        p1 = palavras[i]
        p2 = palavras[j]

        if contar_minusculas(p1) > contar_minusculas(p2):
            temp = palavras[i]
            palavras[i] = palavras[j]
            palavras[j] = temp

print(palavras)