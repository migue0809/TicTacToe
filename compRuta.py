

def compRuta(CR,Heuristica,Ruta,VM,VH,T):

    import numpy as np
    if (T==True):
        MejorH=np.max(VH)
        [X,Y]=np.where(VH == MejorH)
        return VM[X][Y], MejorH
    else:
        a = Ruta[1, 0]
        VM[a - 1] = CR
        VH[a - 1] = Heuristica + VH[a - 1]
        return VM, VH