def calculate():
    print("informe o cálculo a executar:")
    args = input().split()
    operacao = args[0]
    n1 = int(args[1])
    n2 = int(args[2])
    if (operacao == "+") :
        print("soma:", n1 + n2) 
    elif (operacao == "-") :
        print("subtracao:", n1 - n2)  
def palindromo():
    string = input("Insira a palavra ou número a ser conferida: ")
    stringSemEspacos = string.replace(' ', '')
    stringTodaMinuscula = stringSemEspacos.lower()
    stringInvertida = stringTodaMinuscula[::-1]
    if stringInvertida == stringTodaMinuscula:
        print ("SIM")
    else:
        print ("NAO")
def pi():
    import math
    prc = int(input('Digite o número de casas decimais --> '))
    print(f"Pi = {math.pi:.{prc}f}")

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
def ordenar_string():
    lista_caracteres = list(input("digite alguma palavra"))
    lista_caracteres.sort()
    nova_string = "".join(lista_caracteres)
    print(nova_string)
