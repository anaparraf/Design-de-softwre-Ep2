#Formata peças de [a,b] para [a|b]

def formata_peca(lista_pecas):
    pecas_formatadas = []
    for peca in lista_pecas:
        p = str(lista_pecas)
        nova_peca = p.replace(',',' |')
        pecas_formatadas.append(nova_peca)
        
        return pecas_formatadas

