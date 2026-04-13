palavras = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]

grupos = {}

# AGRUPAR
for palavra in palavras:
    inicial = palavra[0]

    if inicial not in grupos:
        grupos[inicial] = []

    grupos[inicial].append(palavra)

# ORDENAR CADA GRUPO
for chave in grupos:
    lista = grupos[chave]
    n = len(lista)

    for i in range(n):
        for j in range(i + 1, n):

            p1 = lista[i]
            p2 = lista[j]

            k = 0
            troca = False

            while k < len(p1) and k < len(p2):
                if ord(p1[k]) > ord(p2[k]):
                    troca = True
                    break
                elif ord(p1[k]) < ord(p2[k]):
                    break
                k += 1

            # prefixo
            if k == len(p1) or k == len(p2):
                if len(p1) > len(p2):
                    troca = True

            if troca:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp

print(grupos)