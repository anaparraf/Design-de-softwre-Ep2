# Exercício Programa 2
## Jogo de Dominó
### Design de Software 
+ Ana Beatriz Parra Ferreira
+ Felipe Tetsu No
## Regras do Jogo
O jogo pode ser jogado por 2, 3 ou 4 participantes. No início do jogo, cada participante recebe 7 peças de dominó para iniciar o jogo, se houver menos de 4 jogadores, então, as peças remanecentes devem ir para o monte;

1. Na vez de um jogador, esse deve observar as peças posicionadas nas pontas da montagem sobre a mesa e seus valores;
2. O jogador deve escolher uma peça de sua posse que tenha um dos números de alguma das pontas das peças da mesa;
3. Se tiver uma peça possível, então, o jogador deve colocar a peça na mesa e está encerrada sua jogada nessa rodada;
4. Caso o jogador não tenha peças possíveis para a mesa, então, se houver monte, deve pegar uma do monte.

Repete-se cada passo

Caso o jogador não tenha peça possível e também esgotado o monte, então, esse deve passar sua vez para o próximo jogador.

## vitória:
O jogador vitorioso é aquele que conseguir colocar todas suas peças na mesa, respeitando as regras dos valores das pontas, antes dos demais jogadores;
Quanto algum jogador ganhar, o jogo deve parar e o vencedor deve ser anunciado.
## Empate:
Existe a possibilidade de nenhum jogador colocar peças em toda uma rodada, isso porque o jogo pode estar fechado e sem monte. Nesse caso, o jogo está encerrado;
Para efeito de vitória, os participantes devem contar os valores das faces das peças em sua posse;
Ganha o jogador que tiver a menor contagem de pontos, sendo possível empate.