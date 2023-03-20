def executador():
    numero = int(input("Digite um número: "))
    if e_par(numero):
      print("É par")
    else: 
      print("Impar ")
def e_par(numero):
    return (numero % 2 ==0) 
    