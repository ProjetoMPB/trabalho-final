# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import mido
from itertools import groupby
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 01 Analisa Ritmo:

# a partir de um vetor R, segmentado, em formato xls (ou csv), associado a uma música,
#identifica perfil métrico, r-letras e r-palavras, atualizando as listas referentes a
# essas estruturas em listas acumuladas

# corpus=input('informe o corpus :')
# titulo = input('informe o título da música (com sua numeração) :')

def ritmo(corpus: str, titulo: str):
    
    w = pd.read_csv(titulo + '.csv', header = None, sep = ';') #abrir vetor de r-sentença da música
    sentence=w.values.tolist()[0]
    
    # separando as palavras para inserir em matriz acumulada
    prv = ''
    palavras = []
    for letra in sentence:
        if letra != '\\':
            prv += letra
        else:
            palavras.append(prv)
            prv = ''   
        
    
    # desempacotando as r-palavras
#    palavras_d = []
#    for sublist in palavras:
#        for item in sublist:
#            palavras_d.append(item)
    
  
    # abrir lista acumulada de r-palavras 
    with open('r_palavras_acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in palavras:
            file.write(palavra + '\n')


#*************************************
# Preservar lista acumulada de palavras com o título da obra

   # tit_palavras=[titulo, palavras_d]
    
    # abrir lista acumulada de títulos+ r-palavras 
    with open('LISTAGEM DE R-PALAVRAS TOTAIS ' + corpus + '.txt', 'a') as file:
        for i in range(0,len(palavras)):
            if i==0:
                file.write(titulo + '\n')
            else:
                file.write(palavras[i] + '\n')
            
#*************************************            
    
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # Computação das r-letras
    r_letras=[]
    
    # preeenchimento do vetor com as r-letras dentro da música analisada
    for i in palavras:
        a = i
        for j in a:
            r_letras.append(j)
    
    #preservar a sentença como lista 
    with open(' .txt', 'w') as filehandle:
        for listitem in r_letras:
            filehandle.write('%s\n' % listitem)
    
    # acondição de segurança
#    if input("are you sure?(y/n)")=="y":
    # abrir vetor acumulado  de r-letras
    with open('r_letras_acumuladas ' + corpus + '.txt', 'a') as file:
        for letra in r_letras:
            a=str(letra)
            file.write(a + '\n')
 #   else:
  #      print('Operação cancelada!')
    
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # Computação do perfil métrico
    # formando o perfil métrico da música analisada
    atual=12*[0]
    
    for i in r_letras:
        if i == 'b':
            atual[0]=atual[0]+1
        elif i == 'c':
            atual[3]=atual[3]+1      
        elif i == 'd':
            atual[4]=atual[4]+1    
        elif i == 'e':
            atual[6]=atual[6]+1      
        elif i == 'f':
            atual[8]=atual[8]+1    
        elif i == 'g':
            atual[9]=atual[9]+1      
        elif i == 'h':
            atual[0]=atual[0]+1    
            atual[3]=atual[3]+1      
        elif i == 'i':
            atual[0]=atual[0]+1    
            atual[4]=atual[4]+1      
        elif i == 'j':
            atual[0]=atual[0]+1    
            atual[6]=atual[6]+1      
        elif i == 'k':
            atual[0]=atual[0]+1    
            atual[8]=atual[8]+1      
        elif i == 'l':
            atual[0]=atual[0]+1    
            atual[9]=atual[9]+1      
        elif i == 'm':
            atual[3]=atual[3]+1    
            atual[6]=atual[6]+1      
        elif i == 'n':
            atual[3]=atual[3]+1    
            atual[9]=atual[9]+1      
        elif i == 'o':
            atual[4]=atual[4]+1    
            atual[8]=atual[8]+1      
        elif i == 'p':
            atual[6]=atual[6]+1    
            atual[9]=atual[9]+1      
        elif i == 'q':
            atual[0]=atual[0]+1  
            atual[3]=atual[3]+1    
            atual[6]=atual[6]+1   
        elif i == 'r':
            atual[0]=atual[0]+1  
            atual[3]=atual[3]+1    
            atual[9]=atual[9]+1 
        elif i == 's':
            atual[0]=atual[0]+1  
            atual[4]=atual[4]+1    
            atual[8]=atual[8]+1 
        elif i == 't':
            atual[0]=atual[0]+1  
            atual[6]=atual[6]+1    
            atual[9]=atual[9]+1 
        elif i == 'u':
            atual[3]=atual[3]+1  
            atual[6]=atual[6]+1    
            atual[9]=atual[9]+1 
        elif i == 'v':
            atual[0]=atual[0]+1  
            atual[3]=atual[3]+1    
            atual[6]=atual[6]+1 
            atual[9]=atual[9]+1         
        elif i == 'w':
            atual[0]=atual[0]+1  
            atual[6]=atual[6]+1    
            atual[8]=atual[8]+1 
            atual[10]=atual[10]+1          
        elif i == 'x':
            atual[0]=atual[0]+1  
            atual[3]=atual[3]+1          
            atual[6]=atual[6]+1    
            atual[8]=atual[8]+1 
            atual[10]=atual[10]+1    
        elif i == 'y':
            atual[2]=atual[2]+1  
            atual[4]=atual[4]+1          
            atual[6]=atual[6]+1    
            atual[8]=atual[8]+1 
            atual[10]=atual[10]+1          
        elif i == 'z':
            atual[0]=atual[0]+1          
            atual[2]=atual[2]+1  
            atual[4]=atual[4]+1          
            atual[6]=atual[6]+1    
            atual[8]=atual[8]+1 
            atual[10]=atual[10]+1          
    
    #preservar a sentença como lista 
#    with open(' .txt', 'w') as filehandle:
#       for listitem in atual:
#            filehandle.write('%s\n' % listitem)
    
    # acondição de segurança
    #if input("are you sure?(y/n)")=="y":
    # abrir vetor acumulado  de r-letras
    with open('Perfil métrico acumulado ' + corpus + '.txt', 'a') as file:
        for letra in atual:
            a=str(letra)
            file.write(a + '\n')
  #  else:
   #     print('Operação cancelada!')

##############################################
##############################################
##############################################
##############################################

def contornoMelodico(corpus: str, titulo: str):
    def midiParaLista(mid):
        # Essa função pega um arquivo midi, lido através do mido, e o converte em uma lista contendo somente as notas e o canal.
        # Inspirada no código em https://stackoverflow.com/questions/63105201/python-mido-how-to-get-note-starttime-stoptime-track-in-a-list
        midi_lista = []
    
        for event in mid:
            if event.type == 'note_on':
                midi_lista.append([event.note, event.channel])
        
        midi_lista.append([88, 1]) # Adicionei um Mi5 artificial no segundo canal para ter um final de frase ao final do midi.
        return midi_lista
    
    def listaParaFrasesNum(midi_lista):
        # Pega a lista gerada acima e transforma nas frases (ainda em números midi)
        buffer = []
        frases = []
        for event in midi_lista:
            if event[0] != 88 and event[1] == 0:
                buffer.append(event[0])
            elif event[0] == 88 and event[1] == 1:
                frases.append(buffer)
                buffer = []
        
        return frases
    
    def frasesNumParaDiffs(frases_num):
        # Pega as frases geradas acima e toma as diferenças entre números midi consecutivos
        diffs = []
        for frase in frases_num:
            diffs.append([frase[i + 1] - frase[i] for i in range(len(frase) - 1)])
        
        return diffs
    
    def diffCódigoLetra(diff):
        #  Recebe como entrada um valor de diferença e o converte na letra correspondente.
        if diff == 0:
            letra = 'u'
        elif diff > 0 and diff < 3:
            letra = 'P'
        elif diff >= 3 and diff <= 5:
            letra = 'A'
        elif diff > 5:
            letra = 'S'
        elif diff < 0 and diff > -3:
            letra = 'p'
        elif diff <= -3 and diff >= -5:
            letra = 'a'
        elif diff < -5:
            letra = 's'
        
        return letra
    
    def diffsParaLetras(diffs):
        # Pega as diferenças geradas como saída da função "frasesNumParaDiffs" e as converte em letras.
        letras = []
        for diff in diffs:
            letras.append([diffCódigoLetra(i) for i in diff])
        
        return letras
    
    # junta as c-letras em uma c-palavra e retorna uma lista
    
    def juntaPalavras(letras):
        palavras=[]
        for i in letras:
            prv=''
            for j in i:
                prv=prv+j
            palavras.append(prv)
        return palavras
    
    mid = mido.MidiFile(titulo + '.mid')
    midi_lista = midiParaLista(mid)
    frases_num = listaParaFrasesNum(midi_lista)
    diffs = frasesNumParaDiffs(frases_num)
    c_palavras = diffsParaLetras(diffs)
    c_ps=juntaPalavras(c_palavras)
    
    # encontrando clímax e nadir
    M=midi_lista
    # prv=[]
    x=0
    climax=[]
    for i in M:
        a=i[0]
        b=i[1]
        if b==0:
            if a>= x:
                climax=a
                x=climax
    
    # prv=[]
    x=climax
    nadir=[]
    for i in M:
        a=i[0]
        b=i[1]
        if b==0:
            if a<= x:
                nadir=a
                x=nadir
    
    # combinar os dois em uma variável
    ambito=[climax, nadir]
    
    #preservar o âmbito como lista 
#    with open(' .txt', 'w') as filehandle:
 #       for listitem in ambito:
  #          filehandle.write('%s\n' % listitem)
    
    # condição de segurança

    # abrir lista acumulada de âmbitos
    with open('ambito acumulado ' + corpus + '.txt', 'a') as file:
        for palavra in ambito:
            file.write(str(palavra) + '\n')

    
    #$$$$$$$$$$$$$ PROCESSAMENTO DE C-PALAVRAS
    
    #preservar a sentença como lista 
#    with open(' .txt', 'w') as filehandle:
 #       for listitem in c_ps:
  #          filehandle.write('%s\n' % listitem)
    
    # condição de segurança
    # abrir lista acumulada de c-palavras 
    with open('c_palavras_acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in c_ps:
            file.write(palavra + '\n')

    
    #$$$$$$$$$$$$$ PROCESSAMENTO DE C-LETRAS
    # fazer uma lista com c-letras separadas
    c_letras=[]
    for i in c_ps:
        for j in i:
            c_letras.append(j)
    
    #preservar a lista 
#    with open(' .txt', 'w') as filehandle:
#        for listitem in c_letras:
#            filehandle.write('%s\n' % listitem)
    
    # condição de segurança
    # abrir lista acumulada de c-palavras 
    with open('c_letras_acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in c_letras:
            file.write(palavra + '\n')


##############################################
##############################################
##############################################
##############################################

def harmonia(corpus: str, titulo: str):
    # 01 Analisa Harmonia:
    
    # a partir de uma matriz H (8 x n) em formato xls (ou csv), associada a uma música,
    #identifica acordes específicos, tonalidades e funções, atualizando as listas referentes a
    # essas estruturas em listas acumuladas
    
    # Adicionalmente, preserva as progressões funcionais das músicas (identificadas), atualizando uma listagem de corpus,
    #para processamento futuro (ENCONTRA FUNÇÃO)
    
    w = pd.read_excel(titulo + '.xls', header = None, nrows = 7) #abrir vetor de r-sentença da música
    H=w.values.tolist()
    
    #*************************
    # 1 - ACORDES ESPECÍFICOS
    # (a) Separar as linhas dos acordes específicos
    
    AC=[]
    for i in range(0,len(H)):
        if i==0 or i==2 or i==3:
            AC.append(H[i])
    
    # (b) formatar cada acorde como uma lista [fund, genus, var]
    
    for i in AC:
        a=i
        ac_esp=[]
        for j in range(0,len(i)):
            b=AC[0][j]
            c=AC[1][j]
            d=AC[2][j]
            ac_esp.append([b,c,d])
    len(ac_esp)   
    
    #preservar a progressão como lista 
    with open(' .txt', 'w') as filehandle:
        for listitem in ac_esp:
            filehandle.write('%s\n' % listitem)
    
    # condição de segurança
#    if input("are you sure?(y/n)")=="y":
    # abrir lista acumulada de acordes específicos 
    with open('acordes específicos acumulados ' + corpus + '.txt', 'a') as file:
        for palavra in ac_esp:
            file.write(str(palavra) + '\n')
#    else:
#        print('Operação cancelada!')
    
    #*************************
    # 1.1 - RBAs
    # (a) eliminando as variantes => relações abstratas (a-RBAs)
    
    A=[]
    
    for i in ac_esp:
        prv=[]
        for j in range(0,len(i)):
    
            if j == 0 or j==1:
                prv.append(i[j])
        A.append(prv)
    
    # (b) combinando as RBAs como duplas [G1|iG2]...
    
    rba=[]

    for i in range(0,len(A)-1):
        a=A[i]
        a1=a[0]
        b=A[i+1]
        b1=b[0]
        dif=b1-a1 % 12
        if dif <0:
            dif=dif+12
        g1=chr(a[1])
        g2=chr(b[1])
        R=g1 + '|' + str(dif) + g2
        rba.append(R)
    
    #preservar RBAs como lista 
    with open(' .txt', 'w') as filehandle:
        for listitem in rba:
            filehandle.write('%s\n' % listitem)
    
    # condição de segurança
#    if input("are you sure?(y/n)")=="y":
    # abrir lista acumulada de RBAs
    with open('RBAs acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in rba:
            file.write(str(palavra) + '\n')
#    else:
#        print('Operação cancelada!')
    
    #*************************
    # 2 - TONALIDADES E TÔNICAS
    # (a) Separar as linhas das tonalidades
    T=[]
    for i in range(0,len(H)):
        if i==5 or i==6:
            T.append(H[i])
    
    # (b) formatar cada seq. de tonalidades numa música como uma lista [ton.1, ton.2, ...]
    for i in T:
        a=i
        ton=[]
        for j in range(0,len(i)):
            b=T[0][j]
            c=T[1][j]
            ton.append([b,c])
    
    # (c) Retornar uma lista sucinta, apenas com as modulações 
    ton1 = [i[0] for i in groupby(ton)]
    
    # (d) Inserir sinal para separação de peças
    ton1=['|',ton1]
    
    # (e) Destacar a tônica da peça analisada
    tonica=ton[0]
    
    #preservar a seq de tonalidades como lista 
    with open(' .txt', 'w') as filehandle:
        for listitem in ton1:
            filehandle.write('%s\n' % listitem)
    
    # condição de segurança
#    if input("are you sure?(y/n)")=="y":
    # abrir lista acumulada de tonalidades internas
    with open('tonalidades acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in ton1:
            file.write(str(palavra) + '\n')
#    else:
 #       print('Operação cancelada!')
    
    #preservar a tônica da peça como lista 
    with open(' .txt', 'w') as filehandle:
        for listitem in tonica:
            filehandle.write('%s\n' % listitem)
    
    # condição de segurança
#    if input("are you sure?(y/n)")=="y":
    # abrir lista acumulada de tônicas proncipais
    with open('tônicas principais acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in tonica:
            file.write(str(palavra) + '\n')
#    else:
#        print('Operação cancelada!')
    
    #*************************
    # 3 - ESTADO ACORDAL
    # (a) Separar as linhas das fundamentais e baixos
    F_bx=[]
    for i in range(0,len(H)):
        if i==0 or i==1:
            F_bx.append(H[i])
    
    # (b) formatar cada seq. como uma lista [fund, bx] ...
    for i in F_bx:
        a=i
        estado=[]
        for j in range(0,len(i)):
            b=F_bx[0][j]
            c=F_bx[1][j]
            estado.append([b,c])
    
    #preservar duplas fund/bx da peça como lista 
    with open(' .txt', 'w') as filehandle:
        for listitem in estado:
            filehandle.write('%s\n' % listitem)
    
    
    # abrir lista acumulada de duplas fund/bx 
    with open('duplas fund-bx acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in estado:
            file.write(str(palavra) + '\n')
#    else:
 #       print('Operação cancelada!')
    
    #*************************
    # 4 - FUNÇÕES 
    # (a) Separar a linha das funções 
    cat=[]
    for i in range(0,len(H)):
        if i==4:
            cat.append(H[i])
    
    # (b) desmpacotando a lista cat
    cat_func = []
    for i in cat:
        for j in i:
            cat_func.append(j)
    
    #preservar categorias funcionais da peça como lista 

    # abrir lista acumulada de duplas fund/bx 
    with open('categorias funcionais acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in cat_func:
            file.write(str(palavra) + '\n')

    
    # 4.1 RBFs
    # (a) Retornar uma lista sucinta (eliminando repetições de cat. contíguas)
    cat_func1 = [i[0] for i in groupby(cat_func)]
    
    # (b) agrupar duas a duas, formando RBFs
    rbf=[]
    for i in range(0,len(cat_func1)-1):
        a=cat_func1[i]
        b=cat_func1[i+1]
        rbf.append([a,b])
    
    # preservar RBFs da peça como lista 

    # abrir lista acumulada de RBFs
    with open('RBFs acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in rbf:
            file.write(str(palavra) + '\n')
    
    #*************************
    # 5 - PROGRESSÕES FUNCIONAIS E COMPASSOS 
    
    # reabrindo a matriz H, agora incluindo a linha dos compassos

    w = pd.read_excel(titulo + '.xls', header = None) 
    w1=w.values.tolist()

    # formar lista com os compassos
    compassos=w1[-1]    
       
    # combinando categorias funcionais e compassos em uma lista [cat, comp] ...
    duplas=[]
    for i in range(0,len(cat_func)):
        a=cat_func[i]
        b=compassos[i]
        duplas.append([a,b])
    
    # inserindo título
    progress=[duplas]
    
    #preservar progressões e título da peça como lista 

    # abrir lista acumulada de progressões acumuladas
    with open('Progressões funcionais acumuladas ' + corpus + '.txt', 'a') as file:
        for palavra in progress:
            file.write(str(palavra) + '\n')


#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

def NF(corpus: str, nome: str):
    
# Dada matriz NF, plota TEIA  e converte matriz NF como lista

# FUNÇÕES

    def lerMatrizNotasFuncoes(arquivo: str):
        mapa_NF = pd.read_excel(arquivo, header = None)
        mapa_NF.index = ['E', 'D', 'C', 'B', 'A']
    
        return mapa_NF
    
    def criaDFAuxiliares():
        mapa_NF_proc1 = pd.DataFrame(columns = ['x', '1', '3', '5', '6', '7', '9', '11', '13', '14', 'b9/#9', '#11', 'b13'],
                                    index = ['1', '#1/b2', '2', '#2/b3', '3', '4', '#4/b5', '5', '#5/b6', '6', '#6/b7', '7']).fillna(0)
        
        mapa_NF_proc2 = pd.DataFrame(columns = ['infl', 'triade', 'tetrade', 't. simples', 't. alteradas'],
                                    index = ['1', '#1/b2', '2', '#2/b3', '3', '4', '#4/b5', '5', '#5/b6', '6', '#6/b7', '7']).fillna(0)
        
        return mapa_NF_proc1, mapa_NF_proc2
    
    def geraMapaNFProc1(mapa_NF, mapa_NF_proc1, modo):
        # escalaMaiorParaLinha = {1: 0, 1.5: 1, 2: 2, 2.5: 3, 3: 4, 4: 5, 4.5: 6, 5: 7, 5.5: 8, 6: 9, 6.5: 10, 7: 11}
        # notasFuncoesParaColuna = {0: 0, 1: 1, 3: 2, 4: 2, 5: 3, 6: 4, 7: 5, 9: 6, 11: 7, 13: 8, 14: 9, -9: 10, 811: 11, -13: 12}
        escalaMaiorParaGrau = {1: '1', 1.5: '#1/b2', 2: '2', 2.5: '#2/b3', 3: '3', 4: '4', 4.5: '#4/b5', 5: '5', 5.5: '#5/b6', 6: '6', 6.5: '#6/b7', 7: '7'}
        escalaMenorParaGrau = {1: '1', 1.5: '#1/b2', 2: '2', 3: '#2/b3', 3.5: '3', 4: '4', 4.5: '#4/b5', 5: '5', 6: '#5/b6', 6.5: '6', -7: '#6/b7', 7: '7'}
        
        notasFuncoesMaiorParaFuncao = {0: 'x', 1: '1', 3: '3', 4: '3', 5: '5', 6: '6', 7: '7', 9: '9', 11: '11', 13: '13', 14: '14', -9: 'b9/#9', 811: '#11', -13: 'b13'}
        notasFuncoesMenorParaFuncao = {0: 'x', 1: '1', 3: '3', 5: '5', 6: '6', 7: '7', 9: '9', 11: '11', 13: '13', 14: '14', -9: 'b9/#9', 811: '#11', -13: 'b13'}
    
        notas = mapa_NF.shape[1] # quantidade de notas na musica
    
        if modo == 'maior': # escolhe o dicionário de tradução de acordo com o modo
            escalaParaGrau = escalaMaiorParaGrau
            notasFuncoesParaFuncao = notasFuncoesMaiorParaFuncao
        elif modo == 'menor':
            escalaParaGrau = escalaMenorParaGrau
            notasFuncoesParaFuncao = notasFuncoesMenorParaFuncao
    
        for nota in range(notas): # itera sobre as notas na musica
            # NÍVEL GLOBAL [linha]
            grau = escalaParaGrau[mapa_NF[nota]['A']] # olha a linha 'A' dessa nota e a transforma de acordo com o dicionario escalaMaiorParaGrau, ou seja, converte o número na matriz NF no grau correspondente
            
            # NÍVEL LOCAL (NOTAS-ESTRUTURAIS) [coluna]
            if (mapa_NF[nota][['E', 'D', 'C', 'B']] == 0).all(): # se as linhas 'E', 'D', 'C', e 'B' dessa nota forem nulas, transforma de acordo com o dicionario notasFuncoesParaFuncao, ou seja, converte o número na matriz NF para a função correspondente e o coloca na coluna adequada (primeira)
                funcao = notasFuncoesParaFuncao[0]
            else:
                idxAux = (mapa_NF[nota][['E', 'D', 'C', 'B']] != 0).idxmax() # se uma das linhas 'E', 'D', 'C', e 'B' dessa nota nao for nula, pega o valor correspondente e transofrma de acordo com o dicionario notasFuncoesParaFuncao, ou seja, converte o número na matriz NF para a função correspondente e o coloca na coluna adequada
                funcao = notasFuncoesParaFuncao[mapa_NF[nota][idxAux]]
      
            mapa_NF_proc1[funcao][grau] += 1
        
        return mapa_NF_proc1
    
    def calculaInidiceAncoragem(mapa_NF_proc1):
        dict_pesos = {'1': 1, '3': 3, '5': 2, '6/7': 5, '9/11/13/14': 7, 'b9/#9/#11/b13': 9}
        dict_contagem_notas = {'1': mapa_NF_proc1['1'].sum(),
                               '3': mapa_NF_proc1['3'].sum(),
                               '5': mapa_NF_proc1['5'].sum(),
                               '6/7': mapa_NF_proc1[['6', '7']].sum().sum(),
                               '9/11/13/14': mapa_NF_proc1[['9', '11', '13', '14']].sum().sum(),
                               'b9/#9/#11/b13': mapa_NF_proc1[['b9/#9', '#11', 'b13']].sum().sum()}
    
        vetor_pesos = np.array(list(dict_pesos.values()))
        vetor_contagem_notas = np.array(list(dict_contagem_notas.values()))
    
        K = vetor_contagem_notas.dot(vetor_pesos)/vetor_contagem_notas.sum()
        Kmin = 1
        Kmax = 9
    
        indice_ancoragem = 1 - (K - Kmin)/(Kmax - Kmin)
    
        return indice_ancoragem
    
    def geraMapaNFProc2(mapa_NF_proc1, mapa_NF_proc2):
        mapa_NF_proc2['infl'] = mapa_NF_proc1['x']
        mapa_NF_proc2['triade'] = mapa_NF_proc1[['1', '3', '5']].sum(axis = 1)
        mapa_NF_proc2['tetrade'] = mapa_NF_proc1[['6', '7']].sum(axis = 1)
        mapa_NF_proc2['t. simples'] = mapa_NF_proc1[['9', '11', '13', '14']].sum(axis = 1)
        mapa_NF_proc2['t. alteradas'] = mapa_NF_proc1[['b9/#9', '#11', 'b13']].sum(axis = 1)
    
        return mapa_NF_proc2
    
    def converteDFParaProp(df, prop = True):
        if prop:
             return df * 1/df.sum().sum()
        else:
            return df * 100/df.sum().sum()
    
    def mapaNFProc2ParaRTheta(mapa_NF_proc2):
        grausParaTheta = {'1': 0, '#1/b2': 1, '2': 2, '#2/b3': 3, '3': 4, '4': 5, '#4/b5': 6, '5': 7, '#5/b6': 8, '6': 9, '#6/b7': 10, '7': 11}
        for grau in grausParaTheta:
            grausParaTheta[grau] *= np.pi/6
    
        funcaoParaR = {'infl': 1, 'triade': 2, 'tetrade': 3, 't. simples': 4, 't. alteradas': 5}
    
        pontos = []
        valores = []
        for funcao in mapa_NF_proc2.columns:
            for grau in mapa_NF_proc2.index:
                if mapa_NF_proc2[funcao][grau] != 0:
                    pontos.append([funcaoParaR[funcao], grausParaTheta[grau]])
                    valores.append(mapa_NF_proc2[funcao][grau])
        
        return pontos, valores
    
# ------------------------------------

    def processaParaTeia(arquivo: str, modo = None):
        mapa_NF = lerMatrizNotasFuncoes(arquivo)
        mapa_NF_proc1, mapa_NF_proc2 = criaDFAuxiliares()
        mapa_NF_proc1 = geraMapaNFProc1(mapa_NF, mapa_NF_proc1, modo = modo)
        mapa_NF_proc2 = geraMapaNFProc2(mapa_NF_proc1, mapa_NF_proc2)
        mapa_NF_proc2_pct = converteDFParaProp(mapa_NF_proc2, prop = False)
        pts, vls = mapaNFProc2ParaRTheta(mapa_NF_proc2_pct)
        indice_ancoragem = calculaInidiceAncoragem(mapa_NF_proc1)
    
        return pts, vls, indice_ancoragem

# ------------------------------------

# GRÁFICO TEIA

    def plotaTeia(pts, vls, modo):
        # PREPARA O FUNDO DA PLOTAGEM
        r = np.arange(1, 6)
        theta = np.pi * np.arange(0, 12)/6
    
        pts_fundo = []
        cor_fundo = []
        for rad in r:
            for ang in theta:
                pts_fundo.append([rad, ang])
                if int(6*ang/np.pi) == 0: # tonica
                    cor_fundo.append('red')
                if modo == 'maior':
                    if int(6*ang/np.pi) in {2, 4, 5, 7, 9, 11}: # diatonicas (modo maior)
                        cor_fundo.append('blue')
                    elif int(6*ang/np.pi) in {1, 3, 6, 8, 10}: # cromaticas (modo maior)
                        cor_fundo.append('gray')
                elif modo == 'menor':
                    if int(6*ang/np.pi) in {2, 3, 5, 7, 8, 11}: # diatonicas (modo menor)
                        cor_fundo.append('blue')
                    elif int(6*ang/np.pi) in {1, 4, 6, 9, 10}: # cromaticas (modo menor)
                        cor_fundo.append('gray')
    
        theta_ang = theta/np.pi * 180
    
        # PLOTA O FUNDO
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize = (8, 8))
        ax.scatter(np.array(pts_fundo)[:,1], np.array(pts_fundo)[:,0], marker = '.', s = 20, c = cor_fundo, alpha = 0.3)
        
        # CRIA COLORMAP ABSOLUTO E DISCRETO
        plasma_5_plus = mpl.colormaps['plasma'].resampled(5 + 1) # 5 cores (2 em 2) + 1 para acima de 10%
        # plasma_10_plus = mpl.colormaps['plasma'].resampled(10 + 1) # 10 cores (1 em 1) + 1 para acima de 10%
    
        def _forward(x):
            return np.clip(x, a_min = 0, a_max = 10)
        
        def _inverse(x):
            return x
        
        norm = mpl.colors.FuncNorm((_forward, _inverse), vmin = 0, vmax = 10)
    
        # PLOTA A TEIA
        teia = ax.scatter(np.array(pts)[:,1], np.array(pts)[:,0], marker = 'o', c = vls, cmap = plasma_5_plus, norm = norm, s = 80)
    
        # AJUSTES VISUAIS
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['font.size'] = 14
    
        ax.set_thetagrids(theta_ang)
        ax.set_thetalim(0, 2*np.pi)
        if modo == 'maior':
            ax.set_xticklabels([1, ' ', 2, ' ', 3, 4, ' ', 5, ' ', 6, ' ', 7])
        elif modo == 'menor':
            ax.set_xticklabels([1, ' ', 2, 3, ' ', 4, ' ', 5, 6, ' ', ' ', 7])
    
        ax.set_rmax(5.15)
        ax.set_rticks(range(1, 6))
        ax.set_yticklabels([' ', ' ', ' ', ' ', ' '])
    
        ax.grid(True)
        ax.spines['polar'].set_visible(False)
        ax.set_axisbelow(True)
        
    
        cbar = fig.colorbar(teia, label = 'Porcentagem de ocorrência', orientation = 'vertical')
        
        # 10 cores (1 em 1) + 1 para acima de 10%
        # cbar.set_ticks([0.5 + t*0.9 for t in range(10 + 1)])
        # cbar.set_ticklabels(['0% ~ 1%', '1% ~ 2%', '2% ~ 3%', '3% ~ 4%', '4% ~ 5%', '5% ~ 6%', '6% ~ 7%', '7% ~ 8%', '8% ~ 9%', '9% ~ 10%', '> 10%'] )
    
        # 5 cores (2 em 2) + 1 para acima de 10%
        cbar.set_ticks([0.75 + t*1.7 for t in range(5 + 1)])
        cbar.set_ticklabels(['0% ~ 2%', '2% ~ 4%', '4% ~ 6%', '6% ~ 8%', '8% ~ 10%', '> 10%'] )
    
        ax.set_title(nome + ' |  ia = ' + str(indice_ancoragem_M), va = 'bottom')
        #plt.text(1,7, 'ia = ' + str(indice_ancoragem_M),size= 9)
        #plt.show()
        plt.savefig(str(indice_ancoragem_M) + ' - Teia NF - ' + nome + '.svg', format = 'svg', bbox_inches = 'tight')
        
        #---------------------------------------
        
        # IDENTIFICAR O MODO
        
    M=lerMatrizNotasFuncoes(nome + '.xls')
    M1=M.values.tolist()
    
    graus=M1[4]
#    print(graus)
    
    #buscar por -7 
    k=0
    for i in graus:
        if i==-7 or i== 3.5:
            k+=1
        elif i== 2.5 or i== 5.5:
            k+=0
        else:
            k+=0
    
    if k >= 1:
        modo = 'menor'
    else:
        modo = 'maior'
    print(modo)
    
    #----------------------------------------
    
    # PLOTAGEM
    
    pts_M, vls_M, indice_ancoragem_M = processaParaTeia(nome + '.xls', modo)
    indice_ancoragem_M=round(indice_ancoragem_M,3)
    print(indice_ancoragem_M)
    plotaTeia(pts_M, vls_M, modo)
    
    #preservar a matriz como lista 

    with open(' .txt', 'w') as filehandle:
        for listitem in M1:
            filehandle.write('%s\n' % listitem)
    

    
# salvando as listas como arquivo de texto

    with open('Lista NF - ' + nome +'.txt', 'w') as filehandle:
        for listitem in M1:
            filehandle.write('%s\n' % listitem)    
            
            
    
    ia=[str(indice_ancoragem_M)]
    
    #preservar ia em lista 
    with open(' .txt', 'w') as filehandle:
        for listitem in ia:
            filehandle.write('%s\n' % listitem)
    

    # abrir lista acumulada de ias 
    with open('ia acumulados ' + corpus + '.txt', 'a') as file:
        for palavra in ia:
            file.write(str(indice_ancoragem_M) + '\n')
            
       
                              

            
# *********************************************

# Aqui deveria entrar então a atualização da lista acumulada (maior ou menor, dependendo do modo
# da música analisada). Na primeira análise o ideal seria, para cada modo, ter uma lista vazia com 12 listas internas
# com 13 zeros. À medida que as análises vão sendo feitas, os dados de cada música iriam se somando
# e sendo salvos nas listas acumuladas.

# isolando a lista de NFs da peça analisada
    NF_aux = lerMatrizNotasFuncoes(nome + '.xls')
    NF_proc_vazio_aux, _ = criaDFAuxiliares()
    NF_proc_aux = geraMapaNFProc1(NF_aux, NF_proc_vazio_aux, modo = modo)
    
    NF_proc_aux.to_numpy()
    x0=NF_proc_aux.values.tolist()
    
# abrir a lista acumulada de NF do modo em questão (eu criei aqui uma lista zerada para ir atualizando)
    mat=[]
    
    with open('Matriz NF acumulada - modo ' + modo + ' - corpus ' + corpus + '.txt', 'r') as file:
        for linha in file:
            mat.append(linha.replace('\n',''))

# normalização
    x=mat
    mat1=[]
    
    # Remover as aspas externas de cada elemento
    x = [item.strip("'") for item in x]
    
    # Converter cada elemento em uma lista usando eval()
    x = [eval(item) for item in x]
    
    # Imprimir nova lista
    for item in x:
        mat1.append(item)
       
    # condição necessária caso a lista acumulada esteja vazia (1a análise)
    if len(mat1)==1:
    # desempacotando
        mat2=[]
        for i in mat1:
            for j in i:
                mat2.append(j)
    else:
        mat2=mat1
        
# atualizando lista acumulada de NF do modo em questão 
    mat3=[]
    for i in range(0, len(mat2)):
        a=mat2[i]
        b=x0[i] 
        prv=[]
        for j in range(0,len(a)):
            c=a[j]
            d=b[j] 
            e=c+d 
            prv.append(e)
        mat3.append(prv)

# salvando a lista atualizada, pra seguir em frente com outra música
    with open('Matriz NF acumulada - modo ' + modo + ' - corpus ' + corpus + '.txt', 'w') as filehandle:
        for listitem in mat3:
            filehandle.write('%s\n' % listitem)