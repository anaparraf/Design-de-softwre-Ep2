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



# Verifica quem ganhou o dominó
def verifica_ganhador(pecas_dos_jogadores):
    ganhador = -1

    for jog, pecas in pecas_dos_jogadores.items():
        if len(pecas) == 0:
            ganhador = jog

    return ganhador



#Soma peças do dominó
def soma_pecas(pecas_jogador):
    valor_de_cada = []
    for peca in pecas_jogador:
        valor_de_cada.append(peca[0]+peca[1])

    return sum(valor_de_cada)   



# Possições possíveis da mão
def posicoes_possiveis (mesa, pecas):
    
    ponta_mesa = []
    pecas_possiveis = []
    
    if mesa == []:
        posicoes_possiveis = [0, 1, 2, 3, 4, 5, 6]
    if mesa != []:
        i = len (mesa) - 1  
        for p in mesa:
            if p == mesa[0]:
                ponta_mesa.append(p[0])
            if p == mesa[i]:
                ponta_mesa.append(p[1])
        for m in pecas:
            if m[0] == ponta_mesa[0] or m[0] == ponta_mesa[1] or m[1] == ponta_mesa[0] or m[1] == ponta_mesa[1]:
                pecas_possiveis.append(m)
        a = 0
        b = 0
        posicoes_possiveis = []
        while a < len (pecas):
            j = pecas[a]
            for k in pecas_possiveis:
                if j == k:
                    posicoes_possiveis.append(a)
            a = a + 1


    return posicoes_possiveis



# Adicionando peças a mesa num jogo de dominó
def adiciona_na_mesa(peca, mesa):
    ponta_mesa = []
    nova_mesa = []
    i = len (mesa) - 1 
    for p in mesa:
            if p == mesa[0]:
                ponta_mesa.append(p[0])
            if p == mesa[i]:
                ponta_mesa.append(p[1])
    if mesa == []:
        nova_mesa.append (peca)
    elif peca[0] == ponta_mesa[0]:
        esquerda = peca[0]
        direita = peca[1]
        inverter = [direita, esquerda]
        nova_mesa.append (inverter)
        nova_mesa.extend (mesa)
    elif peca[0] == ponta_mesa[1]:
        nova_mesa.extend (mesa)
        nova_mesa.append (peca)
    elif peca[1] == ponta_mesa[0]:
        nova_mesa.append (peca)
        nova_mesa.extend (mesa)
    elif peca[1] == ponta_mesa[1]:
        esquerda = peca[0]
        direita = peca[1]
        inverter = [direita, esquerda]
        nova_mesa.extend (mesa)
        nova_mesa.append (inverter)
        
    return nova_mesa