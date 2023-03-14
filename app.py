import sys
from calculadora import *
from parouimpar import *
from dia_semana import *
from palindro import *
from verifica_se_ha import *

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
print("informe a funcão:\n1 - Calculadora\n9 - Pi com x casas decimais" +
"\n6 par ou impar\n" +
      "\nEnter - Sair")
funcao = input()
if (funcao == "1"):
    calculate()
elif (funcao == '9'):
    pi()
elif (funcao =='6'):
    par_ou_impar()
elif (funcao == "5"):
    calculate(palindromo)
elif (funcao == "2"):
    string = input("Digite a string a ser invertida: ")
    print(string[::-1])
elif (funcao == "3"):
    ordenar_string()
elif (funcao == "4"):
    dia_semana()
elif (funcao == '9'):
    pi()
elif (funcao == "10"):
    verifica_se_ha()
else:
    print("Função não implementada!") 
print("Bye!")

