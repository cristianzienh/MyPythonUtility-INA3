def string_inverter():
    string = input('Digite a string a ser invertida: ')
    print('String invertida: ', func_inverter_string(string))

def func_inverter_string(string):
    return (string[::-1])

string_inverter()