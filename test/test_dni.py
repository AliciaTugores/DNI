from src.letra_dni import *

def test_validarDNI():
    assert None == letra_dni('47273175').validarDNI()
    assert False == letra_dni('5394704').validarDNI()
    assert False == letra_dni('1529847963').validarDNI()
    assert False == letra_dni('43').validarDNI()

def test_obtenerLetra():
    assert 'D' == letra_dni('17614398').obtenerLetra()
    assert 'Y' == letra_dni('24043401').obtenerLetra()

def test_letra_correcta():
    assert 'M' == letra_dni('31434887').letra_correcta()
    assert 'D' == letra_dni('45191191').letra_correcta()

def test_DniConLetra():
    assert '45191191D' == letra_dni('45191191').DniConLetra()
    assert '98303284L' == letra_dni('98303284').DniConLetra()

def test_longitud_dni():
    assert 'lo has lograo campeón' == letra_dni('18469746').longitud_dni()
    assert 'prueba de nuevo' == letra_dni('6651279').longitud_dni()