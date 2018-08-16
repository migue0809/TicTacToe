MovexVHeu=posMov(CR)+1
VH=np.zeros((1,MovexVHeu),dtype=int)
VM=np.zeros((MovexVHeu,3,3),dtype=int)

def compRuta(CR,Heuristica,VM,VH,T):
    a=Ruta[1,0]
    VM[a-1]=CR
    VH[a-1]=Heuristica+VH[a-1]
    
    return VM, VH
    
    if (T==True)
        MejorH=max(VH)
        MejorPos=np.where(MejorH,VH)
    
        return VM[MejorPos], MejorH