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

def iE(corpus: str):
    
    
    # abrir a Matriz de c-palavras

    A1=[]
    with open ('c_palavras_acumuladas ' + corpus + '.txt', 'r') as file:
        for linha in file:
            A1.append(linha.replace('\n',''))
#..........................
    
    # índice de economia intervalar (iE)
    
    pen=[]
    conta=0
    for i in A1:
        conta = conta +1
        prv=0
        t=len(i)
        for j in i:
            if j=='u':
                x=0
            elif j=='p' or j=='P':
                x=1
            elif j=='a' or j=='A':
                x=3
            elif j=='s' or j=='S':
                 x=5   
            prv=prv+x
        media=prv/t
        pen.append(media)

    iP0=sum(pen)/conta
    
    #normalizado   
    iP=1-iP0/5
    print(iP)
    
    lista=['iE',iP]
    
   
   # salvando a lista

    with open('RESULTADOS ALTURA - índice de economia intervalar ' + corpus + ' .txt', 'w') as filehandle:
       for listitem in lista:
           filehandle.write('%s\n' % listitem + '\n')            

    
#..........................

    
    # índice de economia intervalar compensada (iEc)
    
    pen=[]
    conta=0
    for i in A1:
        conta = conta +1
        prv=0
        t=len(i)
        for j in i:
            if j=='u':
                x=0
            elif j=='p':
                x=-1
            elif j=='P':
                x=1                
            elif j=='a':
                x=-3                
            elif j=='A':
                x=3             
            elif j=='s':
                x=-5               
            elif j=='S':
                x=5
            prv=prv+x
        media=abs(prv/t)
        pen.append(media)

    iP0=sum(pen)/conta
    
    #normalizado   
    iP=1-iP0/5
    print(iP)
    
    lista=['iEc',iP]
    
   
   # salvando a lista

    with open('RESULTADOS ALTURA - índice de economia intervalar compensada' + corpus + ' .txt', 'w') as filehandle:
       for listitem in lista:
           filehandle.write('%s\n' % listitem + '\n')  
