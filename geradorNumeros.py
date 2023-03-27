import random

def random_number():
    num1 = float(input("escrevca um número para iniciar: "))
    num2 = float(input("escreva um número para fechar: "))
    print (gerador(num1, num2))

def gerador(num1, num2):
    return random.randint(num1, num2)