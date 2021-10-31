# Criando peças de dominó
import random
def cria_pecas():
    pecas = [ ]
    for i in range(0, 7):
        for j in range (0, 7):
            if j >= i:
                peca = [i, j]
                pecas.append(peca)

    random.shuffle(pecas)

    return pecas