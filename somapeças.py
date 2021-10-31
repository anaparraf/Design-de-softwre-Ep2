#Soma peças do dominó
def soma_pecas(pecas_jogador):
    valor_de_cada = []
    for peca in pecas_jogador:
        valor_de_cada.append(peca[0]+peca[1])

    return sum(valor_de_cada)   

