def tem_numeros():
    string = input("Digite a string a ser verificada: ")
    if any(char.isdigit() for char in string):
        print("A string contém números.")
    else:
        print("A string não contém números.")
