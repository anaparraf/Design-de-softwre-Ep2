from funçoes import cria_pecas,  inicia_jogo , verifica_ganhador , posicoes_possiveis , adiciona_na_mesa , soma_pecas 

# Início 
with open('arquivo_textoinicio.txt', 'r') as arquivo:
    conteudo_completo = arquivo.read()
print(conteudo_completo)

# Pergunta qtd de jogadores
numero_jogadores = int(input('Quantas pessoas jogarão? (2-4)'))


