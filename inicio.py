# Início 
with open('arquivo_textoinicio.txt', 'r') as arquivo:
    conteudo_completo = arquivo.read()
print(conteudo_completo)

# Pergunta qtd de jogadores
numero_jogadores = input('Quantas pessoas jogarão? (2-4)')
