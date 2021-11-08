from funcoes import *  
import random

# Início 
with open('arquivo_textoinicio.txt', 'r') as arquivo:
    conteudo_completo = arquivo.read()
print(conteudo_completo)

# Pergunta qtd de jogadores
numero_jogadores = int(input('Quantas pessoas jogarão? (2-4)'))

# chama função de saida e printa a mesa
saida = inicia_jogo(numero_jogadores,cria_pecas())
print('MESA:') 
print(saida['mesa'])


#  cria ordem dos jogadores
l = [0,1,2,3]
ordem = random.shuffle(l)

jogadordavez = ordem
pecacada = saida['jogadores']

print('Jogador {} com {} peças'.format(  jogadordavez , len( pecacada[jogadordavez])))



