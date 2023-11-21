# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 11:27:31 2023

@author: carlo
"""

# corporaKov = programa de composição de progressões funcionais originais a partir de dados
# de matrizes de transição de corpora de análise

import random
import pandas as pd

def kov(corpus: str):
    

# abrindo matriz de transição do corpus
    MT=[]
    with open('Matriz de transição r-letras - ' + corpus + '.txt', 'r') as file:
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
    semente=input('informe a r-letra semente: ')
    
    # encontrar a linha da MT referente à semente
    n=ord(semente)-97
    
    # atribuir as probabilidades a pesos de escolhas
    weights=MT1[n]
    
    # o usuário determina o número de iterações desejadas
    itera= input('informe o número de iterações desejadas: ')
    
    #.................
    alfa=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    # gerando uma progressão funcional com n elementos
    palavra=semente
    for i in range(0,int(itera)-1):
        n=ord(semente)-97
        weights=MT1[n]
        chosen = random.choices(alfa,weights, k=1)
        chosen=''.join(map(str,chosen))
        palavra += chosen
        semente=chosen
        weights=MT1[n]        
    
    print(palavra)
    
    # avaliando a cardinalidade da r-palavra  
    
    card=0
    for i in palavra:
        a=ord(i)-97
        if a<=7:
            card+=1
        elif a>7 and a<=15:
            card+=2
        elif a>15 and a<=20:
            card+=3
        else:
            card+=4
            
        
    palavra=['r-palavra: ', palavra, ' - cardinalidade = ' + str(card)]
    
    # salvando a lista como arquivo de texto
    
    with open('r-palavra baseada no corpus ' + corpus +'.txt', 'w') as filehandle:
        for listitem in palavra:
            filehandle.write(listitem)
    
 
