import datetime

def c_dia(d,m,a):
    dias = ["segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sábado","domingo"]
    return dias[datetime.date(int(a),int(m),int(d)).weekday()]

def dia_semana():
    d, m, a = input("Informe uma data, no formato DD/MM/AAAA, incluindo as barras (/): ").split("/")
    print(f"O dia da semana é {c_dia(d,m,a)}.")
