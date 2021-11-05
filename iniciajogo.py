#Iniciando jogo de dominó
#Separa as peças pra cada jogador 
def inicia_jogo(numero_jogadores,pecas):
    saida = { }

    jogadores = { }
    monte = [ ]
    mesa = [ ]

    # Preenchendo jogadores
    for i in range(numero_jogadores):
        jogadores[i] = [ ]
        for j in range(7 * i, 7 * (i + 1)):
            peca = pecas[j]
            jogadores[i].append(peca)

    # Preenchendo o dicionario
    saida["jogadores"] = jogadores

    # Calculando o monte
    if numero_jogadores < 4:
        fim = len(pecas)
        for i in range(numero_jogadores * 7, fim):
            peca = pecas[i]
            monte.append(peca)
    else:
        monte = [ ]

    saida["monte"] = monte

    #Mesa retorna vazia
    saida["mesa"] = mesa
    
    return saida
