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
    
 # abrindo as legendas dos códigos/símbolos funcionais 
#(para futura tradução)

    legenda=pd.read_excel('A09 legenda MTx_traduzida.xls', header = None)
    legenda.values
    
     # formando uma lista
    legenda=legenda.values.tolist()
    
    lex=[]
    for i in legenda:
        a=i[1]
        lex.append(a)

# abrindo matriz de transição do corpus
    MT=[]
    with open('Matriz de transição RBF - ' + corpus + '.txt', 'r') as file:
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
    semente=input('informe o acorde-semente: ')
    
    # encontrar a linha da MT referente à semente
    n=lex.index(semente)
    
    # atribuir as probabilidades a pesos de escolhas
    weights=MT1[n]
    
    # o usuário determina o número de iterações desejadas
    itera= input('informe o número de iterações desejadas: ')
    
    #.................
    
    # gerando uma progressão funcional com n elementos
    progr=[semente]
    for i in range(0,int(itera)-1):
        n=lex.index(semente)
        weights=MT1[n]
        chosen = random.choices(lex,weights, k=1)
        chosen=''.join(map(str,chosen))
        progr.append(chosen)
        semente=chosen
        weights=MT1[n]        
    
    
    # salvando a lista como arquivo de texto
    
    with open('Progressão harmônica baseada no corpus ' + corpus +'.txt', 'w') as filehandle:
        for listitem in progr:
            filehandle.write(listitem)
    
    #.............................
    # abrindo léxico F-TA

    lex1=pd.read_excel('lexico_cat_func_TA.xls', header = None)
    lex1.values
    
     # formando uma lista
    lex2=lex1.values.tolist()

    lex3=[]
    for i in lex2:
        a=i[1:3]
        lex3.append(a)
        
    #..................
    
    # resgatando as fundamentais
    fund=[]
    for i in lex2:
        a=i[1]
        b=i[3]
        fund.append([a,b])
    print(progr)
    #...................
# traduzir a progressão funcional em progressão de TAs

    progr1=[]
    for i in progr:
        a=i
        for j in lex3:
            b=j[0]
            c=j[1]
            if a==b:
                progr1.append(c)
                
#........................

    # Abrir lista de resultados referente à distribuição de TAs no corpus em questão
    
    TAs=[]
    with open('RESULTADOS HARMONIA - Distribuição dos TAs ' + corpus + '.txt', 'r') as file:
        for linha in file:
            TAs.append(linha.replace('\n',''))
            
#........................

    # normalizando lista

    x=TAs
    TAs1=[]
    
    # Remover as aspas externas de cada elemento
    x = [item.strip("'") for item in x]
    
    # Converter cada elemento em uma lista usando eval()
    x = [eval(item) for item in x]
    
    # Imprimir nova lista
    for item in x:
        TAs1.append(item)

# ........................

# separando os TAs em genera
    Z=[]
    Y=[]
    X=[]
    W=[]
    V=[]
    z=[]
    y=[]
    x=[]
    w=[]
    v=[]
    for i in TAs1:
        a=i[0]
        b=i[1]
        if a[0]=='Z':
            Z.append([a,b])
        elif a[0]=='Y':
            Y.append([a,b])        
        elif a[0]=='X':
            X.append([a,b])           
        elif a[0]=='W':
            W.append([a,b])   
        elif a[0]=='V':
            V.append([a,b])           
        elif a[0]=='z':
            z.append([a,b])           
        elif a[0]=='y':
            y.append([a,b])           
        elif a[0]=='x':
            x.append([a,b])           
        elif a[0]=='w':
            w.append([a,b])           
        elif a[0]=='v':
            v.append([a,b])  
    
    # ........................
    
    # separando em cada genus variantes e probabilidades
    
    Z1=[]
    Z2=[]
    for i in Z:
        a=i[0]
        b=i[1]
        Z1.append(a)
        Z2.append(b)
    tot=sum(Z2)
    tx=1/tot
    
    Z2p=[]
    for i in Z2:
        a = i*tx
        Z2p.append(a)

    Y1=[]
    Y2=[]
    for i in Y:
        a=i[0]
        b=i[1]
        Y1.append(a)
        Y2.append(b)
    
    tot=sum(Y2)
    tx=1/tot
    
    Y2p=[]
    for i in Y2:
        a = i*tx
        Y2p.append(a)
        
    X1=[]
    X2=[]
    for i in X:
        a=i[0]
        b=i[1]
        X1.append(a)
        X2.append(b)
    
    tot=sum(X2)
    tx=1/tot
    
    X2p=[]
    for i in X2:
        a = i*tx
        X2p.append(a)
    
    W1=[]
    W2=[]
    for i in W:
        a=i[0]
        b=i[1]
        W1.append(a)
        W2.append(b)
    
    tot=sum(W2)
    tx=1/tot
    
    W2p=[]
    for i in W2:
        a = i*tx
        W2p.append(a)      
        
    V1=[]
    V2=[]
    for i in V:
        a=i[0]
        b=i[1]
        V1.append(a)
        V2.append(b)
    
    tot=sum(V2)
    tx=1/tot
    
    V2p=[]
    for i in V2:
        a = i*tx
        V2p.append(a)
        
    z1=[]
    z2=[]
    for i in z:
        a=i[0]
        b=i[1]
        z1.append(a)
        z2.append(b)
    
    tot=sum(z2)
    tx=1/tot
    
    z2p=[]
    for i in z2:
        a = i*tx
        z2p.append(a)
        
    y1=[]
    y2=[]
    for i in y:
        a=i[0]
        b=i[1]
        y1.append(a)
        y2.append(b)
    
    tot=sum(y2)
    tx=1/tot
    
    y2p=[]
    for i in y2:
        a = i*tx
        y2p.append(a)
        
    x1=[]
    x2=[]
    for i in x:
        a=i[0]
        b=i[1]
        x1.append(a)
        x2.append(b)
    
    tot=sum(x2)
    tx=1/tot
    
    x2p=[]
    for i in x2:
        a = i*tx
        x2p.append(a)
        
    w1=[]
    w2=[]
    for i in w:
        a=i[0]
        b=i[1]
        w1.append(a)
        w2.append(b)
    
    tot=sum(w2)
    tx=1/tot
    
    w2p=[]
    for i in w2:
        a = i*tx
        w2p.append(a)
            
    v1=[]
    v2=[]
    for i in v:
        a=i[0]
        b=i[1]
        v1.append(a)
        v2.append(b)
    
    tot=sum(v2)
    tx=1/tot
    
    v2p=[]
    for i in v2:
        a = i*tx
        v2p.append(a)
        
    #==============================
    #ESCOLHA DOS TAs POR SORTEIO PONDERADO
    
    progr2=[]
    for i in progr1:
        a=i
        if a=='Z':       
            chosen = random.choices(Z1,Z2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)
        elif a=='Y':       
            chosen = random.choices(Y1,Y2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)
        elif a=='X':       
            chosen = random.choices(X1,X2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)        
        elif a=='W':       
            chosen = random.choices(W1,W2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)             
        elif a=='V':       
            chosen = random.choices(V1,V2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)
        elif a=='z':       
            chosen = random.choices(z1,z2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)        
        elif a=='y':       
            chosen = random.choices(y1,y2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)           
        elif a=='x':       
            chosen = random.choices(x1,x2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)
        elif a=='w':       
            chosen = random.choices(w1,w2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)        
        elif a=='v':       
            chosen = random.choices(v1,v2p, k=1)
            chosen=''.join(map(str,chosen))
            progr2.append(chosen)            
                         
 
    # ........................
    
    # abrindo léxico F-TA para traduzir os acordes escolhidos em cifras

    lex4=pd.read_excel('LEXICO TAs - Python.xls', header = None)
    lex4.values
    
     # formando uma lista
    lex5=lex4.values.tolist()
    
    # eliminando a linha de numeração (supérfllua)
    lex6=lex5[1:3]
    
    #..........................
    
    #tradução dos códigos TAs em qualidades sufixais

    progr3=[]
    for i in progr2:
        a=i
        b=lex6[0]
        c=lex6[1]
        d=b.index(a)
        e=c[d]
        progr3.append(e)
        
    
    #.......................
    
    # obtendo as fundamentais da progressão 
    F=[]
    for i in progr:
        a=i
        for j in fund:
            b=j[0]
            c=j[1]
            if a==b:
                F.append(c)
    
    # ****************************
    # MACETE
   # caso fundamental H (II relativo) aconteça no sorteio


    x=0
    F1=[]
    for i in range(0,len(F)-1):
        a=F[i]
        b=F[i+1]
        if b=='C':
            a1='G'
        elif b=='C#' or b=='Db':
            a1='Ab'
        elif b=='D':
            a1='A'       
        elif b=='D#' or b=='Eb':
            a1='Bb'
        elif b=='E':
            a1='B'         
        elif b=='F':
            a1='C'
        elif b=='F#' or b=='Gb':
            a1='C#'       
        elif b=='G':
            a1='D'
        elif b=='G#' or b=='Ab':
            a1='Eb'
        elif b=='A':
            a1='E'
        elif b=='A#' or b=='Bb':
            a1='F'       
        elif b=='B':
            a1='F#'
        if a=='H':
            F1.append(a1)
            x=1
        else:
            F1.append(a)
    F1.append(F[-1])
            
    if x==1:
        F=F1  
         
   # ........................

    # formando as cifras completas
    cifras=[]
    for i in range(0,len(F)):
        a=F[i]
        b=progr3[i]
        cifras.extend([a+b])         
        
    # ===============
    
    #RESUMO
    
    print(cifras)   
    #print(progr3)
    print(progr2)
    print(progr1)
    print(progr)
    
    #.....................
    
    # salvando a lista como arquivo de texto
    
    progressao=[['Cifras em Dó maior', cifras],['Tipos acordais', progr2], ['Genera',progr1],['Análise funcional',progr]]
    
    with open('Progressão harmônica original baseada no corpus ' + corpus +'.txt', 'w') as filehandle:
        for listitem in progressao:
            filehandle.write(str(listitem))
    