import sys
from calculadora import *

#Seleciona função
#1 - Calculadora
#2 - Inverte string
#3 - Ordena caracters da string
#4 - Retorna dia da semana para data
#5 - Detecta palíndromos
#6 - Retorna se é número é par ou impar
#7 - Sorteia um número aleatório para um dado intervalo numérico
#8 - Verifica se palavra/caracter existe na string
#9 - Imprime o número Pi com x casas decimais 
#Enter - Sair
print("informe a funcão:\n1 - Calculadora" +
      "\nEnter - Sair")
funcao = input()
if (funcao == "5"):
    calculate()
else:
    print("Função não implementada!") 
print("Bye!")

def palindromo():
    string = input("Insira a palavra ou número a ser conferida: ")
    stringSemEspacos = string.replace(' ', '')
    stringTodaMinuscula = stringSemEspacos.lower()
    stringInvertida = stringTodaMinuscula[::-1]
    if stringInvertida == stringTodaMinuscula:
        print ("SIM")
    else:
        print ("NAO")
