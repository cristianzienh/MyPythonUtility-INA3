def tem_numeros():
    vari=input("digite uma palavra e/ou número")
    print(ver_num(vari))
def ver_num(vari):
    string = input("Digite a string a ser verificada: ")
    if any(char.isdigit() for char in string):
        print("A string contém números.")
    else:
        print("A string não contém números.")