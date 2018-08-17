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
from inArray import inArray
alpha = -10e4
beta = 10e4
actState = inArray()
route = py.ones((posMov(actState),1),dtype=int)
minMax1 = minMax(actState)
posMov1 = posMov(actState)
VM = py.zeros((posMov1, 3, 3))
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
        if route[i,0] != 0:
            a = route[i,0]
            minMax1 = minMax(actState)  
            actState = newState(minMax1, actState, a)
            if i == 0:
                headState = actState.copy()  
        else:
            [route, alpha, beta] = perderhijos(inState, b, i, actState, route, alpha, beta)
            break
        b = ganar(actState)
        if b != 2 and route[0,0]==1:
            [VM, VH] = compRuta(headState, b, route, VM, VH, False)
            print(i+1)
            [route, alpha, beta] = perderhijos(inState, b, i+1, actState, route, alpha, beta)
            sw = 0
            break
    if sw != 0 and route[0,0]==1:
        preState = actState.copy()
        a = route[-1, 0]
        actState = finState(minMax1,actState)
        b = ganar(actState)
        [VM, VH] = compRuta(headState, b, route, VM, VH, False)
        [route, alpha, beta] = perderhijos(inState, b, posMov1-1, preState, route, alpha, beta)


    print('Vector localización = ', route.T, '\nEstado Actual =\n', actState, '\nHeuristica', b, '\nAlpha = ', alpha,
           '\nBeta =', beta)
    print(
         '----------------------------------------------------------------------------------------------------------------')
    if route[0,0] > 1:
        [M,H] = compRuta(headState, b, route, VM, VH, True)
        print('HEURISTICA = ', H, '\nLA JUGADA DEBE SER = \n', M)
        break

                
                
                
                
            
            
            
            
        
        
    
    
    