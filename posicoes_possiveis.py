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