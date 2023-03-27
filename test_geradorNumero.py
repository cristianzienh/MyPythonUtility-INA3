from geradorNumeros import *

def test_gerador():
    resultado = gerador(1, 10)
    assert resultado <= 10
    assert resultado >= 1