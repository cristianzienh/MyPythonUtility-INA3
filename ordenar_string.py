def ordenar_string():
    lista_caracteres = list(input("digite alguma palavra"))
    lista_caracteres.sort()
    nova_string = "".join(lista_caracteres)
    print(nova_string)
