# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:55:10 2018

@author: mateo
"""

import numpy as py
from actState import newState,finState
from Ganar import ganar
from perderhijos import perderhijos
from compRuta import compRuta
"""Esta es una funcion compuesta que articula a la funcion perderHijo() y a 
la funcion compRuta haciendo uso de la funcion actState().
buscarHijos() pide como entrada el estado actual, el vector ruta, la 
profundidad maxima de el arbol (posMov) y el estado minMax del estado actual.
Basado en esa informacion esta funcion avanza con ayuda de actState para
encontar un estado final de empate, derrota o victoria todo esto señido a el
vector ruta que es modificado por perderHijos() explorando asi todo el arbol
y encontarndo la mejor opcion de juego con alluda de la funcion compRuta """
def buscarHijos(actState, route, posMov, minMax, alpha, beta):  # actState = inState first iteration
    sw = 1
    inState = actState.copy()
    for i in range(posMov-1):
        if route[i+1,0] != 0:
            a = route[i+1,0]
            if minMax == 0:
                actState = newState(minMax, actState, a)
            elif minMax == 1:
                actState = newState(minMax, actState, a)
        minMax = not(minMax)
        b = ganar(actState)
        if b != 2:
            print(inState,b,i,actState)
            [route, alpha, beta] = perderhijos(inState, b, i+1, actState, route, alpha, beta)
            #compRuta(b, actState)
            sw = 0
            break
    if sw != 0:
        preState = actState.copy()
        a = route[-1, 0]
        actState = finState(minMax,actState)
        b = ganar(actState)
        [route, alpha, beta] = perderhijos(inState, b, posMov-1, preState, route, alpha, beta)

        #compRuta(b, actState)
        
    return(route,actState,b,alpha,beta)




alpha = -10e4
beta = -1
a1 = py.array([(1,2,1), (0,1,0), (0,2,2)])
a2 = py.array([[1],[3],[1]])
a3 = 3
a4 = True
[route,actState,b,alpha,beta] = buscarHijos(a1,a2,a3,a4,alpha,beta)
print('Vector localización = ',route.T,'\nEstado Actual =\n', actState,'\nHeuristica',b,'\nAlpha = ', alpha,'\nBeta =', beta)

        
                
                
                
                
                
            
            
            
            
        
        
    
    
    