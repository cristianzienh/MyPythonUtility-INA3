import math
def pi():
    prc = int(input('Digite o número de casas decimais --> '))
    print('Pi =', calcCasas(prc))

def calcCasas(n):
    return f'{math.pi:.{n}f}'