def mmc():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    if a > b:
        maior = a
    else:
        maior = b

    i = maior
    while True:
        if i % a == 0 and i % b == 0:
            mmc = i
            break
        i += 1

    print("O MMC de", a, "e", b, "é:", mmc)
    
mmc()