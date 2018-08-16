def posMov (SA):
    HP=0
    for col in range(3):
        for row in range(3):
            if SA[col][row] == 0:
                HP=HP+1
    return HP