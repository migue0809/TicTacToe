# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:55:10 2018

@author: mateo
"""

import numpy as py
from actState import newState,finState
from Ganar import ganar
from perderhijos import perderhijos
from PosMov import posMov
from MinMax import minMax
from compRuta import compRuta
alpha = -10e4
beta = 10e4
actState = py.array([(1,2,1), (0,1,0), (0,2,2)])
route = py.ones((posMov(actState),1),dtype=int)
minMax = minMax(actState)
posMov1 = posMov(actState)
VM = py.zeros((posMov1, 3, 3))
print(VM[1])
VH = py.zeros((posMov1, 1))
"""Esta es una funcion compuesta que articula a la funcion perderHijo() y a 
la funcion compRuta haciendo uso de la funcion actState().
buscarHijos() pide como entrada el estado actual, el vector ruta, la 
profundidad maxima de el arbol (posMov1) y el estado minMax del estado actual.
Basado en esa informacion esta funcion avanza con ayuda de actState para
encontar un estado final de empate, derrota o victoria todo esto señido a el
vector ruta que es modificado por perderHijos() explorando asi todo el arbol
y encontarndo la mejor opcion de juego con alluda de la funcion compRuta """
inState = actState.copy()
while True:
    sw = 1
    actState = inState.copy()
    for i in range(posMov1-1):
        if route[i+1,0] != 0:
            a = route[i+1,0]
            if minMax == 0:
                actState = newState(minMax, actState, a)
                if i == 0:
                    headState = actState.copy()
            elif minMax == 1:
                actState = newState(minMax, actState, a)
                if i == 0:
                    headState = actState.copy()
        minMax = not(minMax)
        b = ganar(actState)
        if b != 2:
            [route, alpha, beta] = perderhijos(inState, b, i+1, actState, route, alpha, beta)
            [VM, VH] = compRuta(headState, b, route, VM, VH, False)
            sw = 0
            break
    if sw != 0:
        preState = actState.copy()
        a = route[-1, 0]
        actState = finState(minMax,actState)
        b = ganar(actState)
        [route, alpha, beta] = perderhijos(inState, b, posMov1-1, preState, route, alpha, beta)
        [VM, VH] = compRuta(headState, b, route, VM, VH, False)

    print('Vector localización = ', route.T, '\nEstado Actual =\n', actState, '\nHeuristica', b, '\nAlpha = ', alpha,
          '\nBeta =', beta)
    print(
        '----------------------------------------------------------------------------------------------------------------')
    if route[0,0] > 1:
        [M,H] = compRuta(headState, b, route, VM, VH, True)
        print('HEURISTICA = ', H, '\nLA JUGADA DEBE SER = \n', M)
        break

                
                
                
                
            
            
            
            
        
        
    
    
    