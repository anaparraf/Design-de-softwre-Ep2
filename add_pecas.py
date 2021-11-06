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
