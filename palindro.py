def remove_espacos_e_minusculas(string):
    stringSemEspacos = string.replace(' ', '')
    stringTodaMinuscula = stringSemEspacos.lower()
    return stringTodaMinuscula

def verifica_palindromo():
    string = input("Insira a palavra ou número a ser conferida: ")
    string_processada = remove_espacos_e_minusculas(string)
    string_invertida = string_processada[::-1]
    return string_processada == string_invertida

def palindromo ():
    if verifica_palindromo():
        print("SIM")
    else:
        print("NAO")
