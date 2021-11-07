import funçoes as fç 
import random

# Início 
with open('arquivo_textoinicio.txt', 'r') as arquivo:
    conteudo_completo = arquivo.read()
print(conteudo_completo)

# Pergunta qtd de jogadores
numero_jogadores = int(input('Quantas pessoas jogarão? (2-4)'))

# chama função de saida e printa a mesa
saida = fç.inicia_jogo(numero_jogadores,fç.cria_pecas())
print('MESA:') 
print(saida['mesa'])

# apresenta peças do primeiro jogador
j1 = random.randint(1, 4)
j = saida['jogadores']
print('Jogador {} com {} peças'.format( j1 , len( j[j1-1])))
