# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 13:03:20 2023

@author: carlo
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib as mpl

# ECONOMIA - código para cálculo dos índices de economia dos contornos melódicos de um corpus

def iCtm(corpus: str):
    
    
    # abrir a Matriz de c-palavras

    A1=[]
    with open ('r_palavras_acumuladas ' + corpus + '.txt', 'r') as file:
        for linha in file:
            A1.append(linha.replace('\n',''))
#..........................
    
    # índice de contrametricidade (ic)
    
    ict=[]
    prv=[]
    for i in A1:
        q=len(i)
        y=i[-1]
        z=i[0]
        pen=0
        if y=='b':
            pen=pen+(3*q+1)/q
        if z=='b' or  z=='h' or  z=='i' or z=='j' or z=='k' or z=='l' or z=='q' or z=='r' or z=='s' or z=='t' or z=='v' or z=='w' or z=='x' or z=='z':
            pen=pen+(q+1)/q
        # letras intermediárias
        for j in range(1,len(i)):
            k=i[j]
            if k=='b' or  k=='h' or  k=='i' or k=='j' or k=='k' or k=='l' or k=='q' or k=='r' or k=='s' or k=='t' or k=='v' or k=='w' or k=='x' or k=='z':
               pen=pen+(q+.5)/q
        iD=1-pen/q
        # normalização
        iDn=(iD-(-1.5))/(1-(-1.5))
        prv.append([i,iDn])
        ict.append(iDn)
    
    # cálculo do ic médio
    icm=['ic médio', sum(ict)/len(ict)]

#---------------------

    # formando lista
    lista=[icm, 'ic individuais', prv]

   # salvando a lista

    with open('RESULTADOS RITMO - índice de contrametricidade ' + corpus + ' .txt', 'w') as filehandle:
       for listitem in lista:
           filehandle.write('%s\n' % listitem + '\n')  
 
    
 
    
 
