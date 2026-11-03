from funcoes import preenche_frota as fullF
from funcoes import faz_jogada as fazJ
from funcoes import posiciona_frota as posF
from funcoes import afundados as afun
from funcoes import posicao_valida as posV
import random


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join(
            [str(item) for item in tabuleiro_jogador[linha]]
        )
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0'
             for info in tabuleiro_oponente[linha]]
        )
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'

    return texto


frota = {}

i = 0
while i < 10:
    if i < 1:
        navio = 'porta-aviões'
        tam = 4
    elif i < 3:
        navio = 'navio-tanque'
        tam = 3
    elif i < 6:
        navio = 'contratorpedeiro'
        tam = 2
    else:
        navio = 'submarino'
        tam = 1

    print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tam}')

    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))

    if navio != 'submarino':
        pergunta = int(input('Orientação: [1] Vertical [2] Horizontal '))

        while pergunta not in [1, 2]:
            print('Orientação inválida!')
            pergunta = int(input('Orientação: [1] Vertical [2] Horizontal '))

        if pergunta == 1:
            orientacao = 'vertical'
        else:
            orientacao = 'horizontal'
    else:
        orientacao = 'vertical'

    if posV(frota, linha, coluna, orientacao, tam):
        frota = fullF(frota, navio, linha, coluna, orientacao, tam)
        i += 1
    else:
        print('Esta posição não está válida!')


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


tabuleiro_oponente = posF(frota_oponente)
tabuleiro_jogador = posF(frota)

posicao_ataque = []
posicoes_ataque_oponente = []
afundado = 0
jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    teste2 = False

    while teste2 == False:
        linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

        while linha_ataque < 0 or linha_ataque > 9:
            print('Linha inválida!')
            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

        coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

        while coluna_ataque < 0 or coluna_ataque > 9:
            print('Coluna inválida!')
            coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

        posicao = [linha_ataque, coluna_ataque]

        if posicao not in posicao_ataque:
            posicao_ataque.append(posicao)
            teste2 = True
        else:
            print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')

    tabuleiro_oponente = fazJ(
        tabuleiro_oponente, linha_ataque, coluna_ataque
    )

    afundado = afun(frota_oponente, tabuleiro_oponente)

    if afundado == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    else: 
        jogada_oponente_valida = False
        while jogada_oponente_valida == False:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)
            
            if [linha_oponente, coluna_oponente] not in posicoes_ataque_oponente:
                posicoes_ataque_oponente.append([linha_oponente, coluna_oponente])
                jogada_oponente_valida = True
                
        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')
        
        tabuleiro_jogador = fazJ(tabuleiro_jogador, linha_oponente, coluna_oponente)
        
        afundados_jogador = afun(frota, tabuleiro_jogador)
        if afundados_jogador == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False