import random

def random_number():
    num1 = float(input("escrevca um número para iniciar: "))
    num2 = float(input("escreva um número para fechar: "))
    print (random.randint(num1, num2))


