from src.DNI import *

def test_validarDNI():
    assert None == DNI('47273175').validarDNI()
    assert False == DNI('5394704').validarDNI()
    assert False == DNI('1529847963').validarDNI()
    assert False == DNI('43').validarDNI()

def test_obtenerLetra():
    assert 'D' == DNI('17614398').obtenerLetra()
    assert 'Y' == DNI('24043401').obtenerLetra()

def test_letra_correcta():
    assert 'M' == DNI('31434887').letra_correcta()
    assert 'D' == DNI('45191191').letra_correcta()

def test_DniConLetra():
    assert '45191191D' == DNI('45191191').DniConLetra()
    assert '98303284L' == DNI('98303284').DniConLetra()

def test_longitud_dni():
    assert 'lo has lograo campeón' == DNI('18469746').longitud_dni()
    assert 'prueba de nuevo' == DNI('6651279').longitud_dni()