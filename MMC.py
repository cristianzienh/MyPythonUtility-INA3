<<<<<<< HEAD
def mmc():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

=======
def mmc(a, b):
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    print("O MMC de", a, "e", b, "é:", mmc(a, b))
>>>>>>> 582defea8e54667cc83fccb0a2689b472b6aa867
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

<<<<<<< HEAD
    print("O MMC de", a, "e", b, "é:", mmc)

=======
    return mmc
>>>>>>> 582defea8e54667cc83fccb0a2689b472b6aa867
