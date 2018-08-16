# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 10:46:01 2018

@author: mateo
"""

import numpy as py
"""Esta funcion pide como enrada 3 parametros el estado minMax, el estado
estado actual y una fila del vector ruta.Todo ello con el fin de optener el
el estado nuevo o siguiente"""
def newState(minMax, actState, iRoute):
    [a,b] = py.where(actState == 0)
    if minMax == True:
        actState[a[iRoute-1],b[iRoute-1]] = 1 
    elif minMax == False:
        actState[a[iRoute-1],b[iRoute-1]] = 2  
        
#    print(actState)
    return(actState)


def finState(minMax, actState):
    [a, b] = py.where(actState == 0)
    if minMax == True:
        actState[a, b] = 1
    elif minMax == False:
        actState[a, b] = 2

    #    print(actState)
    return (actState)
        
#newState(True,py.array([(2,0,0), (0,1,1), (2,2,0)]),4)

