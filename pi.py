import math
def pi():
    prc = int(input('Digite o número de casas decimais --> '))
    print(calcCasas(prc))

def calcCasas(n):
    return f"Pi = {math.pi:.{n}f}"