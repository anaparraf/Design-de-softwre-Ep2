# Verifica quem ganhou o dominó
def verifica_ganhador(pecas_dos_jogadores):
    ganhador = -1

    for jog, pecas in pecas_dos_jogadores.items():
        if len(pecas) == 0:
            ganhador = jog

    return ganhador

