import random

def random_number(start, end):
    return random.randint(start, end)
num1 = float(input("escrevca um número para iniciar: "))
num2 = float(input("escreva um número para fechar"))
print(random_number(num1,num2)) # Gera um número aleatório entre 1 e 100
#print(random_number(-50, 50)) # Gera um número aleatório entre -50 e 50
