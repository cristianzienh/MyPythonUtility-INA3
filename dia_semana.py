import datetime

def dia_semana():
    dias = ["segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sábado","domingo"]
    d, m, a = input("Informe uma data, no formato DD/MM/AAAA, incluindo as barras (/): ").split("/")
    print(f"O dia da semana é {dias[datetime.date(int(a),int(m),int(d)).weekday()]}.")
    
