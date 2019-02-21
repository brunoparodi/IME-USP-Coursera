def fatorial (n):
    if n < 0:
        return 0
    fat = 1
    i = 1
    while i <= n:
        fat = fat * i
        i = i + 1
    return fat

import pytest

@pytest.mark.parametrize('entrada, esperado',[
    (  0,   1),
    (  1,   1),
    (-10,   0),
    (  4,  24),
    (  5,  120)
    ])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado

'''
def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial_negativo():
    assert fatorial(-10) == 0

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial5():
    assert fatorial(5) == 120
'''
