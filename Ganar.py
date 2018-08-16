def Ganar(SA):
    Empate=PosMov(SA)
    for i in range(3):
        if SA[i][0] == 1 and SA[i][1] == 1 and SA[i][2] == 1:
            print('You are the champion')
            n=1
            break
        elif SA[i][0] ==2 and SA[i][1] == 2 and SA[i][2] == 2:
            print('You are not the champion')
            n=-1
            break
        if SA[0][i] == 1 and SA[1][i] == 1 and SA[2][i] == 1:
            print('You are the champion')
            n=1
            break
        elif SA[0][i] ==2 and SA[1][i] ==2 and SA[2][i] ==2:
            print('You are not the champion')
            n=-1
            break
        if SA[0][0] == 1 and SA[1][1] == 1 and SA[2][2] == 1:
            print('You are the champion')
            n=1
            break
        elif SA[0][0] == 2 and SA[1][1] == 2 and SA[2][2] == 2:
            print('You are not the champion')
            n=-1
            break
        if SA[0][2] == 1 and SA[1][1] == 1 and SA[2][0] == 1:
            print('You are the champion')
            n=1
            break
        elif SA[0][2] == 2 and SA[1][1] == 2 and SA[2][0] == 2:
            print('You are not the champion')   
            n=-1
            break
        if Empate==0:
            print('There is not the champion') 
            n=0
        else:
            print('You can play')
            n=2
    return n
    return n