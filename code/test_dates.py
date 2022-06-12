import dates


# Prueba inicial de fecha_es_valida para validar las funciones que lo utilizan

def test_fecha_es_valida():
    # Tests for cases R0-1-01, R0-1-02, R0-1-03, R0-1-04
    fechas = [(1582, 10, 15), (2022, 10, 40), (1582, 13, 15), (1582, 13)]
    expect = [True, False, False, False]

    for fecha, expectVal in zip(fechas, expect):
        result = dates.fecha_es_valida(fecha)
        assert result is expectVal


# Prueba de fecha_es_tupla para validar las funciones que lo utilizan
def test_fecha_es_tupla():
    # Tests for cases R0-2-01, R0-2-02
    tuples = [(1582, 13, 24), (1582, 13)]
    expect = [True, False]

    for singleTuple, expectVal in zip(tuples, expect):
        result = dates.fecha_es_tupla(singleTuple)
        assert result is expectVal


def test_dia_siguiente():
    # Primero consiste en los casos donde es valido
    fechas = [(1582, 10, 15), (2020, 12, 31), (2020, 2, 28)]
    expect = [(1582, 10, 16), (2021, 1, 1), (2020, 2, 29)]

    for fecha, expectVal in zip(fechas, expect):
        result = dates.dia_siguiente(fecha)
        assert result == expectVal

    # Segundo se probarán los casos donde se debe obtener el mensaje "Error, la fecha no es valida"
    # Estos casos consisten en: R3-02, R3-03, R3-05, R3-06, R3-07, R3-08, R3-09, R3-10
    fechas = [(1581, 1, 20), (1582, 10, 14), (2020, 13, 1), (2000, -1, 1), (1200, 2, 28), (2000, 2), "(2000)",
              (2000 - 12 - 1), (2002, 2, 31), (1990, 2, 30), (1900, 2, 0), (2000, 2, "dia")]

    for fecha in fechas:
        result = dates.dia_siguiente(fecha)
        assert result == "Error, la fecha no es valida"


def test_fecha_futura():
    # Primero consiste en los casos donde es valido
    fechas = [(1582, 10, 15), (1582, 10, 15), (1582, 10, 17), (1582, 10, 17), (1600, 1, 20), (2000, 2, 28),
              (2000, 2, 29)]

    dias = [1, 2, 1, 2, 1, 1, 1]

    expect = [(1582, 10, 16), (1582, 10, 17), (1582, 10, 18), (1582, 10, 19), (1600, 1, 21), (2000, 2, 29),
              (2000, 3, 1)]

    for fecha, expectVal, dia in zip(fechas, expect, dias):
        result = dates.fecha_futura(fecha, dia)
        assert result == expectVal

    # Segundo se probarán los casos donde se debe obtener el mensaje "Error, la fecha no es valida"
    # Estos casos consisten en: R3-02, R3-03, R3-05, R3-06, R3-07, R3-08, R3-09, R3-10
    fechas = [(1500, 1, 20), (4, 4), (2001, 2, 29)]
    dias = [1, 1, 1]

    for fecha, dia in zip(fechas, dias):
        result = dates.fecha_futura(fecha, dia)
        assert result == "Error, la fecha no es valida"

    # Tercero se probará el caso con días negativos
    result = dates.fecha_futura((1600, 1, 20), -1)
    assert result == "Error, los dias deben ser positivos"


def test_edad_al_01():
    result = dates.edad_al((1582, 10, 15), (1586, 10, 15))
    assert result == (4, 0, 0)


def test_edad_al_02():
    result = dates.edad_al((2000, 2, 25), (2022, 5, 30))
    assert result == (22, 3, 5)


def test_edad_al_03():
    result = dates.edad_al((2022, 5, 30), (2000, 2, 25))
    assert result == "f1 debe ser menor que f2"


def test_edad_al_04():
    result = dates.edad_al((4, 4), 1)
    assert result == "Error, la fecha 1 no es valida"