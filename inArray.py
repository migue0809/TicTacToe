import numpy as np
def inArray():
    array = list()
    i = 3
    j = 3


    for x in range(i):
        if i <= 0 or i>10:
             print("Failure!")
             break
        elif j <= 0 or j>10:
             print("Failure!")
             break
        else:
            for y in range(j):
                 num = int(input("Value: "))
                 array.append(int(num))


    a = np.reshape(array,(i,j))
    print('La matriz de juego ingresada es: \n',a)
    return(a)
