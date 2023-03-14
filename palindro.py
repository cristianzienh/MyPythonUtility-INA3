def palindromo():
    string = input("Insira a palavra ou número a ser conferida: ")
    stringSemEspacos = string.replace(' ', '')
    stringTodaMinuscula = stringSemEspacos.lower()
    stringInvertida = stringTodaMinuscula[::-1]
    if stringInvertida == stringTodaMinuscula:
        print ("SIM")
    else:
        print ("NAO")