def tem_numeros():
    vari=input("digite uma palavra e/ou número")
    print(ver_num(vari))
def ver_num(vari):
    string=list(vari)
    if any(char.isdigit() for char in string):
        return("true")
    else:
        return("false")