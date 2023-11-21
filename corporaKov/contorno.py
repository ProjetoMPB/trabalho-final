# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 11:27:31 2023

@author: carlo
"""

# corporaKov = programa de composição de progressões funcionais originais a partir de dados
# de matrizes de transição de corpora de análise

import random
import pandas as pd

def gerar(corpus: str):
    

# abrindo matriz de transição do corpus
    MT=[]
    with open('Matriz de transição c-letras - ' + corpus + '.txt', 'r') as file:
        for linha in file:
            MT.append(linha.replace('\n',''))

    # normalizando lista
    x=MT
    MT1=[]
    
    # Remover as aspas externas de cada elemento
    x = [item.strip("'") for item in x]
    
    # Converter cada elemento em uma lista usando eval()
    x = [eval(item) for item in x]
    
    # Imprimir nova lista
    for item in x:
        MT1.append(item)
        
    # o usuário fornece a semente da progressão    
    semente=input('informe a c-letra semente: ')
    
    # encontrar a linha da MT referente à semente
    if semente =='u':
        n=0
    elif semente=='P':
        n=1
    elif semente=='p':
        n=2
    elif semente=='A':
        n=3
    elif semente=='a':
        n=4
    elif semente=='S':
        n=5
    elif semente=='s':
        n=6


    # atribuir as probabilidades a pesos de escolhas
    weights=MT1[n]
    
    # o usuário determina o número de iterações desejadas
    itera= input('informe a cardinalidade desejada para a c-palavra: ')
    itera=int(itera)-1
    
    #.................
    alfa=['u','P','p','A','a','S','s']
    
    # gerando uma progressão funcional com n elementos
    palavra=semente
    for i in range(0,int(itera)-1):
        if semente =='u':
            n=0
        elif semente=='P':
            n=1
        elif semente=='p':
            n=2
        elif semente=='A':
            n=3
        elif semente=='a':
            n=4
        elif semente=='S':
            n=5
        elif semente=='s':
            n=6
        weights=MT1[n]
        chosen = random.choices(alfa,weights, k=1)
        chosen=''.join(map(str,chosen))
        palavra += chosen
        semente=chosen
        weights=MT1[n]        
    
    print(palavra)
    
    # salvando a lista como arquivo de texto
    
    with open('c-palavra baseada no corpus ' + corpus +'.txt', 'w') as filehandle:
        for listitem in palavra:
            filehandle.write(listitem)
    
 
    