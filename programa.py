from funcoes import define_posicoes as defp
from funcoes import preenche_frota as fullF
from funcoes import faz_jogada as fazJ
from funcoes import posiciona_frota as posF
from funcoes import afundados as afun
from funcoes import posicao_valida as posV

frota = {}

i = 0
while i < 10:
    if i < 1:
        navio = 'porta-aviões'
        tam = 4
    elif 1 <= i < 3:
        navio = 'navio-tanque'
        tam = 3
    elif 3 <= i < 6:
        navio = 'contratorpedeiro'
        tam = 2
    elif 6 <= i < 10:
        navio = 'submarino'
        tam = 1

    print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tam}')
    linha = int(input("linha: "))
    coluna = int(input("coluna: ")) 
    if navio != 'submarino':
        pergunta = int(input("orientação: vertical = [1] horizontal = [2] > "))
        if pergunta == 1:
            orientacao = 'vertical'
        elif pergunta == 2:
            orientacao = 'horizontal'   
    else:
        orientacao = 'vertical'
    
    if posV(frota, linha, coluna, orientacao, tam) == True:
        defp(linha, coluna, orientacao, tam)
        finalF = fullF(frota, navio, linha, coluna, orientacao, tam)
        finalT = posF(frota)
        i += 1
    elif posV (frota, linha, coluna, orientacao, tam) == False:
        print("Esta posição não está válida!")

print(finalF)