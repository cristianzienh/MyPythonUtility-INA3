def has_numbers(input_string):
    return any(char.isdigit() for char in input_string)

input_string = input("Digite uma string para verificar se há números: ")
if has_numbers(input_string):
    print("A string contém números.")
else:
    print("A string não contém números.")
    