import numpy as np
def PosMov (SA):
    height, width = SA.shape
    HP=0
    for col in range(height):
        for row in range(width):
            if EA[col][row] == 0:
                HP=HP+1
    return HP