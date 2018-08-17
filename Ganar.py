def ganar(EA):
    from PosMov import posMov
    Empate=posMov(EA)
    for i in range(3):
        if EA[i][0] == 1 and EA[i][1] == 1 and EA[i][2] == 1:
            #print('You are the champion')
            n=1
            break
        elif EA[i][0] ==2 and EA[i][1] == 2 and EA[i][2] == 2:
            #print('You are not the champion')
            n=-1
            break
        if EA[0][i] ==1 and EA[1][i] ==1 and EA[2][i] ==1:
            #print('You are the champion')
            n=1
            break
        elif EA[0][i] ==2 and EA[1][i] ==2 and EA[2][i] ==2:
            #print('You are not the champion')
            n=-1
            break
        if EA[0][0] == 1 and EA[1][1] == 1 and EA[2][2] == 1:
            #print('You are the champion')
            n=1
            break
        elif EA[0][0] == 2 and EA[1][1] == 2 and EA[2][2] == 2:
            #print('You are not the champion')
            n=-1
            break
        if EA[0][2] == 1 and EA[1][1] == 1 and EA[2][0] == 1:
            #print('You are the champion')
            n=1
            break
        elif EA[0][2] == 2 and EA[1][1] == 2 and EA[2][0] == 2:
            #print('You are not the champion')
            n=-1
            break
        if Empate==0:
            #print('There is no champion')
            n=0
        else:
            #print('You can play')
            n=-1000
    
    return n