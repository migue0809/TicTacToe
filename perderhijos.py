def perderhijos(IS,heuristic, deep, AS, vecLocation,alpha,beta):
    import numpy as np
    from PosMov import posMov
    from MinMax import minMax
    vecChildren = (np.linspace(posMov(IS)+1,1,posMov(IS)+1)).reshape(posMov(IS)+1,1)
    if minMax(AS) == True:  #Detecta el turno jugador A o B. True Esta en un MAX
        if heuristic > alpha:
            beta = heuristic
        if alpha >= beta:
            if vecLocation[deep - 2, 0] < vecChildren[deep - 2, 0]:
                vecLocation[deep - 2, 0] = vecLocation[deep - 2, 0] + 1
                vecLocation[(deep-1):, 0] = np.ones(vecLocation[(deep-1):, 0].shape)  # Reemplazando el vector loc
            else:
                vecLocation[(deep - 2):, 0] =  np.zeros(vecLocation[(deep-2):, 0].shape)
        else:
            if vecLocation[deep,0] == vecChildren[deep,0]: # Si se chequearon todos los hermanos
                if vecLocation[deep-1,0] == vecChildren[deep-1,0]:
                    vecLocation[deep,0] = 0
                else:
                    vecLocation[deep-1,0] = vecLocation[deep-1,0]+1
                    vecLocation[deep:,0] = np.ones(vecLocation[deep:,0].shape)
            else:  # si faltan hermanos
                vecLocation[deep,0] = vecLocation[deep,0]+1
    else:
        if heuristic > beta:
            alpha = heuristic
        if alpha >= beta:
            if vecLocation[deep-2,0] < vecChildren[deep-2,0]:
                vecLocation[deep - 2, 0] = vecLocation[deep - 2, 0] + 1
                vecLocation[(deep-1):, 0] = np.ones(vecLocation[(deep-1):, 0].shape)  # Reemplazando el vector loc
            else:
                vecLocation[(deep - 2):, 0] = np.zeros(vecLocation[(deep - 2):, 0].shape)

        else:
            if vecLocation[deep, 0] == vecChildren[deep, 0]:  # Si se chequearon todos los hermanos
                if vecLocation[deep - 1, 0] == vecChildren[deep-1, 0]:
                    vecLocation[deep, 0] = 0
                else:
                    vecLocation[deep - 1, 0] = vecLocation[deep - 1, 0] + 1
                    vecLocation[deep:, 0] = np.ones(vecLocation[deep:, 0].shape)
            else:  # si faltan hermanos
                vecLocation[deep, 0] = vecLocation[deep, 0] + 1
    return vecLocation, alpha, beta



