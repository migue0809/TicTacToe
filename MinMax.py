def MinMax (SA):
    height, width = SA.shape
    X=0
    O=0
    for col in range(width):
        for row in range(height):
            if SA[col][row] == 1:
                X = X+1
            if SA[col][row] == 2:
                O = O+1
            if X>O:
                State=False
            if O>X:
                State=True
            if X == O:
                State=True
    return State