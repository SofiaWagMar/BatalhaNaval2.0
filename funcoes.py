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

def posicao_valida(frota, linha, coluna, orientacao, tam):
    tudocerto = True
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
    coloca = define_posicoes(linha, coluna, orientacao, tam)
    for tipo, boats in frota.items():
        for barco in boats:
            for lincol in barco:
                if lincol in coloca:
                    return False
                
    for position in coloca:
        if position [0] >= 10 or position[1] >= 10:
            return False
        
    return tudocerto

import funcoes as func
frota = {}
contador =  0
navios = {
    "porta-aviões": [1,4],
    "navio-tanque": [2,3],
    "contratorpedeiro": [3,2],
    "submarino": [4,1]

}

for nome in navios:
    quantidade = navios.get(nome)[0]
    tamanho = navios.get(nome)[1]
    tentativa = False
    while tentativa == False:
        tentaiva = True
        for i in range(quantidade):
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha "))
            coluna = int(input("Coluna "))
            if nome != "submarino":
                orientacao = int(input("[1] Vertical [2] Horizontal "))
                if orientacao ==1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            else:
                orientacao = "horizontal"

            if func.posicao_valida(frota, linha, coluna, orientacao, tamanho) == False:
                tentativa = False
                print("Esta posição não está válida!") 
                quantidade -= contador
                break
            else:
                func.preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                contador+=1
        contador = 0



frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = func.posiciona_frota(frota_oponente)
tabuleiro_jogador = func.posiciona_frota(frota)

posicao_ataque = []
afundado = 0
jogar = True
while jogar == True:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '___________      ___________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    tentativa2 =False
    while tentativa2 == False:
        tentativa2 = True
        linha_ataque = int(input("Jogador, qual linha deseja atacar?"))
        while linha_ataque not in [0,1,2,3,4,5,6,7,8,9,]:
            print('Linha inválida!')
            linha_ataque = int(input("Jogador, qual linha deseja atacar?"))

        coluna_ataque = int(input("Jogador, qual coluna deseja atacar?"))
        while coluna_ataque not in [0,1,2,3,4,5,6,7,8,9]:
            print('Coluna inválida!')
            coluna_ataque = int(input("Jogador, qual coluna deseja atacar?"))

        posicao = [linha_ataque, coluna_ataque]
        if posicao not in posicao_ataque:
            posicao_ataque.append(posicao)
        else:
            print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')
            tentativa2 = False

        tabuleiro_oponente = func.faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

        afundado=func.afundados(frota_oponente, tabuleiro_oponente)

    if afundado ==10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!') 
        jogar = False