def calculate():
    print("informe o cálculo a executar:")
    args = input().split()
    operacao = args[1]
    n1 = int(args[0])
    n2 = int(args[2])
    if (operacao == "+") :
        print("soma:", n1 + n2) 
    elif (operacao == "-") :
        print("subtracao:", n1 - n2)  


