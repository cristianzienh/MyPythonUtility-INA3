import sys
from tem_numeros import *
from calculadora import *
from parouimpar import *
from dia_semana import *
from palindro import *
from ordenar_string import *
from pi import *
from mmc import *

print("Seleciona função \n" 
      "1 - Calculadora \n" 
      "2 - Inverte string \n"
      "3 - Ordena caracters da string \n"
      "4 - Retorna dia da semana para data \n"
      "5 - Detecta palíndromos \n"
      "6 - Retorna se é número é par ou impar \n"
      "7 - Sorteia um número aleatório para um dado intervalo numérico \n"
      "8 - Verifica se palavra/caracter existe na string \n"
      "9 - Imprime o número Pi com x casas decimais \n"
      "10 - Verifica se exitem numeros na string \n"
      "11 - Calcula qual o mmc entre dois numeros \n"
      "\nEnter - Sair")
funcao = input()
if (funcao == "1"):
    calculate()
elif (funcao == "2"):
    string = input("Digite a string a ser invertida: ")
    print(string[::-1])
elif (funcao == "3"):
    ordenar_string()
elif (funcao == "4"):
    dia_semana()
elif (funcao == "5"):
    palindromo()
elif (funcao =='6'):
    par_ou_impar()
elif (funcao == '9'):
    pi()
elif (funcao == "10"):
    tem_numeros()
elif (funcao == "11"):
    mmc()
else:
    print("Função não implementada!") 
print("Bye!")
