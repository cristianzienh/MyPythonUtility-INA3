def pi():
    import math
    prc = int(input('Digite o número de casas decimais --> '))
    print(f"Pi = {math.pi:.{prc}f}")