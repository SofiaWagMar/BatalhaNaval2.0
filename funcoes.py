tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]

def define_posicoes(linha, coluna, orientacao, tam):
    final = []
    i = 0
    while i < tam:
        grupo = [0] * 2
        if orientacao == 'vertical':
            grupo[0] = linha + i
            grupo[1] = coluna
            i += 1
        elif orientacao == 'horizontal':
            grupo[0] = linha
            grupo[1] = coluna + i
            i += 1
        final.append(grupo)
    
    return final

def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    if navio not in frota:
        frota[navio] = []
    posicion = define_posicoes(linha, coluna, orientacao, tamanho)
    frota[navio].append(posicion)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],]
    
    for tipo, boats in frota.items():
        for barco in boats:
            for lincol in barco:
                tabuleiro[lincol[0]][lincol[1]] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    contador = 0
    for tipo, boats in frota.items():
        for barco in boats:
            if all(tabuleiro[lincol[0]][lincol[1]] == 'X' for lincol in barco) == True:
                contador += 1
    return contador