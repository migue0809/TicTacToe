from math import factorial
def gameSpace (SA):
    k = PosMov(SA)
    Suma = 0 
    for i in range(k):
        Suma = Suma + factorial(k)/factorial(i)
    return Suma