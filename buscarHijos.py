# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 08:55:10 2018

@author: mateo
"""

import numpy as py
from actState import newState
"""Esta es una funcion compuesta que articula a la funcion perderHijo() y a 
la funcion compRuta haciendo uso de la funcion actState().
buscarHijos() pide como entrada el estado actual, el vector ruta, la 
profundidad maxima de el arbol (posMov) y el estado minMax del estado actual.
Basado en esa informacion esta funcion avanza con ayuda de actState para
encontar un estado final de empate, derrota o victoria todo esto señido a el
vector ruta que es modificado por perderHijos() explorando asi todo el arbol
y encontarndo la mejor opcion de juego con alluda de la funcion compRuta """
def buscarHijos(actState, route, posMov, minMax): # actState = inState first iteration 
    for i in range(posMov-1):
        if route[i,0] != 0:
            a = route[i,0]
            if minMax == 0:
                actState = newState(minMax,actState,a)
            elif minMax == 1:
                actState = newState(minMax,actState,a)
        minMax = not(minMax)
        b = ganar(actState)
        if b != 2:
            perderHijo(i,b,actState)
            compRuta(b,actState)
            break
    if i == (posMov-1):
        preState = actState
        a = route[posMov,0]
        actState = newState(minMax,actState,a)
        b = ganar(actSatate)
        perderHijo((posMov,b,preState)
        compRuta(b,actState)
        
    print(actState)
        
#a1 = py.array([(1,2,1), (0,1,0), (0,2,2)])
#a2 = py.array([[1],[1],[1]])
#a3 = 3
#a4 = True
#buscarHijos(a1,a2,a3,a4)
    
        
                
                
                
                
                
            
            
            
            
        
        
    
    
    