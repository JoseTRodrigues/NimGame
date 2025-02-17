# -*- coding: utf-8 -*-
"""
JOGO DE NIM: ADVERSÁRIO AUTOMÁTICO RECORRENDO A MACHINE LEARNING

@author: José Rodrigues
"""

#%% IMPORTS
from random import randint
from copy import deepcopy

#%%############################ TORRE INICIAL #################################

number=16
l=int(number**0.5) #nº de linhas de peças
b=2*l-1 #nº de peças da base da pirâmide

def palitos(n):
    p=[]
    for i in range(1,n+1,2):
        p.append(i*[1])
    return p

p=palitos(b)

def torre(x):
    "Print da torre de palitos"
    print('\nTorre:\n\nlinha')
    l=[]
    for i in range(len(x)):
        l.append(i*3)
    l.reverse()
    for i in range(len(l)):
        print(f'  {i}   {(l[i])*" "}{x[i]}')
    return

#%%############################  ESTATÍSTICA  #################################

'COMBINAÇÕES DE PEÇAS POSSÍVEIS'
comb=[]
for i in range(len(p[0])+1):
    for j in range(len(p[1])+1):
        for k in range(len(p[2])+1):
            for w in range(len(p[3])+1):
                comb.append([i,j,k,w])
comb.pop(0)
comb.reverse()
        
'JOGADAS POSSÍVEIS (em cada combinação de peças): (l,n), com l = nº da linha (a contar a partir do 0) e \
n = nº de peças retiradas'
stat={}
for i in range(len(comb)):
    z=comb[i]
    dic={}
    for j in range(len(z)):
        d=z[j]
        for k in range(1,d+1):
            for w in range(1,min(k,d)+1):
                dic[(j,w)] = 0
            stat[tuple(comb[i])]=dic


#%%############################   SIMULAÇÃO   #################################

def nim(jogos):
    
    # print('\nLegenda:\nt-turno; j-jogador; l-nº da linha; n-nº de peças retiradas\n')
    
    for g in range(1,jogos+1):
        t=1 #turno
    
        moves={} #jogadas
        moves[1]={} #jogadas do jogador 1
        moves[2]={} #jogadas do jogador 2
        
        # print(f'--- {g}º jogo ---')
        # print('t','j','l','n')
        
        peças=[]
        
        z=[[]]
        p=palitos(b)
        while p!=z*l:
            '1 Jogo'
            peças.append((len(p[0]),len(p[1]),len(p[2]),len(p[3]))) #combinação de peças no momento da jogada
            
            jogador=1 if t%2!=0 else 2
            
            x=moves[jogador][t]=max(stat[peças[t-1]], key=stat[peças[t-1]].get)#jogada com mais pontos
            if stat[peças[t-1]][x]>0:
                for i in range(list(x)[1]):
                    p[list(x)[0]].remove(1)
            
            else: #jogada aleatória no caso de não haver melhor jogada
                escolha1=randint(0,len(p)-1) #escolha de linha
                while p[escolha1]==[]:
                    escolha1=randint(0,len(p)-1)
                    
                escolha2=randint(1,len(p[escolha1])) #nº de peças retiradas
                for i in range(escolha2):
                    p[escolha1].remove(1)
                
                moves[jogador][t]=(escolha1,escolha2)
                
            # print(t,jogador,escolha1,escolha2,p)
            
            t+=1
            
        # print(f'\nGanha jogador{jogador}\n')
        
        'Pontuação das jogadas'
        # last player wins, collect statistics:  
        for i in moves[jogador]:
          stat[peças[i-1]][moves[jogador][i]]+= 1
        
        # switch to other player that lost:
        jogador = 2 if jogador == 1 else 1
        for i in moves[jogador]:
          stat[peças[i-1]][moves[jogador][i]] -= 1

    # """
    # print das melhores jogadas
    # """
    # print('\n\nMelhores Jogadas para uma dada combinação de peças (l- nº da linha; n- nº de peças retiradas):')
    # print('\ncomb. de peças  jogada(l,n)  pontuação')
    # for i in range(len(comb)):
    #     best = max(stat[tuple(comb[i])], key=stat[tuple(comb[i])].get) 
    #     value = stat[tuple(comb[i])][best]
    #     # if value<0:
    #     #     best = '-'
    #     #     value = ''
    #     print (f"{tuple(comb[i])}:      {best}      {value:>5}")

    return

#%%############################     JOGO      #################################



# 'DIFICULDADE'
# sdif=['facil','medio','dificil']
# dif=str(input(f'\nDificuldade? {sdif} '))
# while dif not in sdif:
#     print('\nEscreva uma das seguintes opcoes: facil, medio, dificil...')
#     dif=str(input())
# if dif =='facil':
#     nim(10)
# elif dif =='medio':
#     nim(1000)
# elif dif=='dificil':
#     print('loading')
#     nim(1000000)
#     print('done')

nim(1000000)
'INICIO'
sstart=['eu','computador']
start=str(input(f'\nQuem começa? {sstart} '))
while start not in sstart:
    print('\nEscreva uma das seguintes opcoes: eu, computador...')
    start=str(input())

'JOGO'
p1=deepcopy(p)
j=0

if start=='eu':
    torre(p1)
    while p1!=[[],[],[],[]]:
        j+=1
        print(f'\n------- JOGADA Nº {j} -------')
        
        'JOGADOR'
        n1=int(input('\nNº da linha (0,1,2,3)? '))
        n2=int(input(f'Nº de peças {tuple(range(1,len(p1[n1])+1))}? '))
        
        for i in range(n2):
            p1[n1].remove(1)
            
        torre(p1)    
        
        if p1==[[],[],[],[]]:
            print('\nVENCEU!!!')
            break
        # print(f'\nEu: \n{p1}')
        
        j+=1
        print(f'\n------- JOGADA Nº {j} (Computador) -------')
        'COMPUTADOR'
        peças=(len(p1[0]),len(p1[1]),len(p1[2]),len(p1[3]))
        x=max(stat[peças], key=stat[peças].get)#jogada com mais pontos
        if stat[peças][x]>0:
            for i in range(list(x)[1]):
                p1[list(x)[0]].remove(1)
        
        else: #jogada aleatória no caso de não haver melhor jogada
            escolha1=randint(0,len(p1)-1) #escolha de linha
            while p1[escolha1]==[]:
                escolha1=randint(0,len(p1)-1)
                
            escolha2=randint(1,len(p1[escolha1])) #nº de peças retiradas
            for i in range(escolha2):
                p1[escolha1].remove(1)
                
        torre(p1)      
        
        if p1==[[],[],[],[]]:
            print('\nPERDEU...')
            break
        # print(f'\nComputador: {p1}')

elif start=='computador':
    torre(p1)
    while p1!=[[],[],[],[]]:
        j+=1
        print(f'\n------- JOGADA Nº {j} (Computador) -------')
        print('\n')
        'COMPUTADOR'
        peças=(len(p1[0]),len(p1[1]),len(p1[2]),len(p1[3]))
        x=max(stat[peças], key=stat[peças].get)#jogada com mais pontos
        if stat[peças][x]>0:
            for i in range(list(x)[1]):
                p1[list(x)[0]].remove(1)
        
        else: #jogada aleatória no caso de não haver melhor jogada
            escolha1=randint(0,len(p1)-1) #escolha de linha
            while p1[escolha1]==[]:
                escolha1=randint(0,len(p1)-1)
                
            escolha2=randint(1,len(p1[escolha1])) #nº de peças retiradas
            for i in range(escolha2):
                p1[escolha1].remove(1)
        
        torre(p1)
                
        if p1==[[],[],[],[]]:
            print('\nPERDEU...')
            break

        j+=1
        print(f'\n------- JOGADA Nº {j} -------')        
        'JOGADOR'
        n1=int(input('\nNº da linha (0,1,2,3)? '))
        n2=int(input(f'Nº de peças {tuple(range(1,len(p1[n1])+1))}? '))
        print('\n')
        for i in range(n2):
            p1[n1].remove(1)
            
        torre(p1)
        
        if p1==[[],[],[],[]]:
            print('\nVENCEU!!!')
            break 
            
        # print(f'\nEu: {p1}')
    
    