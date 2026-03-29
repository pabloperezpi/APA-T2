"""
primos.py

Autor: Pablo Pérez Pi

Módulo para el manejo de números primos.

Tests unitarios (ejecutar con: python -m doctest -v primos.py)

>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210
"""


def esPrimo(numero):
    """
    Determina si un número es primo.

    Args:
        numero (int): Número natural mayor que 1.

    Returns:
        bool: True si es primo, False en caso contrario.

    Raises:
        TypeError: Si numero no es natural mayor que 1.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El número debe ser natural y mayor que 1")

    if numero <= 3:
        return True

    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True


def primos(numero):
    """
    Devuelve una tupla con los números primos menores que numero.

    Args:
        numero (int): Número límite.

    Returns:
        tuple: Tupla de números primos menores que numero.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El número debe ser mayor que 1")

    return tuple(n for n in range(2, numero) if esPrimo(n))


def descompon(numero):
    """
    Devuelve la descomposición en factores primos de un número.

    Args:
        numero (int): Número natural mayor que 1.

    Returns:
        tuple: Factores primos ordenados.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El número debe ser natural y mayor que 1")

    factores = []
    divisor = 2

    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1

    return tuple(factores)


def contar_factores(factores):
    """
    Cuenta cuántas veces aparece cada factor primo.

    Args:
        factores (tuple): Factores primos.

    Returns:
        dict: Diccionario {primo: exponente}
    """
    conteo = {}
    for f in factores:
        if f in conteo:
            conteo[f] += 1
        else:
            conteo[f] = 1
    return conteo


def mcd(*numeros):
    """
    Calcula el máximo común divisor de varios números.

    Args:
        *numeros: Enteros mayores que 1.

    Returns:
        int: Máximo común divisor.
    """
    if len(numeros) == 0:
        raise TypeError("Se requiere al menos un número")

    for n in numeros:
        if not isinstance(n, int) or n <= 1:
            raise TypeError("Todos los números deben ser enteros > 1")

    factorizaciones = [contar_factores(descompon(n)) for n in numeros]

    comunes = factorizaciones[0].copy()

    for f in factorizaciones[1:]:
        nuevos = {}
        for primo in comunes:
            if primo in f:
                nuevos[primo] = min(comunes[primo], f[primo])
        comunes = nuevos

    resultado = 1
    for primo, exp in comunes.items():
        resultado *= primo ** exp

    return resultado


def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo de varios números.

    Args:
        *numeros: Enteros mayores que 1.

    Returns:
        int: Mínimo común múltiplo.
    """
    if len(numeros) == 0:
        raise TypeError("Se requiere al menos un número")

    for n in numeros:
        if not isinstance(n, int) or n <= 1:
            raise TypeError("Todos los números deben ser enteros > 1")

    factorizaciones = [contar_factores(descompon(n)) for n in numeros]

    comunes = {}

    for f in factorizaciones:
        for primo, exp in f.items():
            if primo in comunes:
                comunes[primo] = max(comunes[primo], exp)
            else:
                comunes[primo] = exp

    resultado = 1
    for primo, exp in comunes.items():
        resultado *= primo ** exp

    return resultado


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)