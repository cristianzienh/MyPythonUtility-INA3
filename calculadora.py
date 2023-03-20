def calculate():
    print("informe o cálculo a executar:")
    args = input().split()
    operacao = args[0]
    n1 = int(args[1])
    n2 = int(args[2])
    if (operacao == "+") :
        result = soma(n1, n2) 
    elif (operacao == "-") :
        result = subtracao(n1, n2)
    print("resultado: ", result )
    
def soma(n1, n2):
    return  n1+n2

def subtracao(n1, n2):
    return n1-n2


