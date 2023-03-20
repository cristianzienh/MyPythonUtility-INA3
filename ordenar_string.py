def ordenar_string(lista):
    lista_caracteres=list(lista)
    lista_caracteres.sort()
    nova_string = "".join(lista_caracteres)
    return(nova_string)
def aceita_ordena():
        lista=input("digite alguma palavra")
        print(ordenar_string(lista))
