
palavras = ["banana", "uva", "abacaxi", "laranja"]

n = len(palavras)

for i in range(n):
    for j in range(i + 1, n):

        p1 = palavras[i]
        p2 = palavras[j]

        k = 0
        troca = False

        while k < len(p1) and k < len(p2):
            if ord(p1[k]) > ord(p2[k]):
                troca = True
                break
            elif ord(p1[k]) < ord(p2[k]):
                break
            k += 1

        # caso uma seja prefixo da outra
        if k == len(p1) or k == len(p2):
            if len(p1) > len(p2):
                troca = True

        if troca:
            temp = palavras[i]
            palavras[i] = palavras[j]
            palavras[j] = temp

print(palavras)