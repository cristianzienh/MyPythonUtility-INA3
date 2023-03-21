import sys
from tem_numeros import *
from calculadora import *
from parouimpar import *
from dia_semana import *
from palindro import *
from ordenar_string import *
from pi import *
<<<<<<< HEAD
from verific_string import*
=======
from mmc import *
from invertida_string import *
from geradorNumeros import*

>>>>>>> 7e7727d09fe31708ad6720ba35d3e3b4c3680527
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
    string_inverter()
elif (funcao == "3"):
    aceita_ordena()
elif (funcao == "4"):
    dia_semana()
elif (funcao == "5"):
    palindromo()
<<<<<<< HEAD
elif (funcao  m=='6'                                                                                                                            ):
    par_ou_impar()
 elif (funcao == '8') 
    verific_string()  
=======
elif (funcao =='6'):
    executador()
>>>>>>> 7e7727d09fe31708ad6720ba35d3e3b4c3680527
elif (funcao == '9'):
    pi()
elif (funcao == "10"):
    tem_numeros()
<<<<<<< HEAD
elif (funcao == '8'):
    verific_string()
=======
elif (funcao == "7"):
    random_number()
elif (funcao == "11"):
    mmc()
>>>>>>> 7e7727d09fe31708ad6720ba35d3e3b4c3680527
else:
    print("Função não implementada!") 
print("Bye!")
