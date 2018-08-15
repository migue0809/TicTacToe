def compRuta(VR,Heuristica,SA):
    TamañoH=len(Heuristica)
    Move=PosMov(SA)
    Heuristica1=-1000
    for i in range(TamañoH):
        if Heuristica[i]>Heuristica1:
            Heuristica1=Heuristica[i]+Heuristica1
    CR=VR
            
    
    return Heuristica1,CR