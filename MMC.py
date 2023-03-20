def mmc(a, b):
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

    return mmc

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print("O MMC de", a, "e", b, "é:", mmc(a, b))