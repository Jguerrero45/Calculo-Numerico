import numpy as np


def decimal_bin(n):
    n = bin(n)[2:]
    return n


def decimal_terciario(n):
    return np.base_repr(n, base=3)


def decimal_cuartenario(n):
    return np.base_repr(n, base=4)


def decimal_octal(n):
    n = oct(n)[2:]
    return n


def decimal_hexadecimal(n):
    n = hex(n)[2:]
    return n


def bin_decimal(n):
    n = str(n)
    return int(n, 2)


def terciario_decimal(n):
    n = str(n)
    return int(n, 3)


def cuartenario_decimal(n):
    n = str(n)
    return int(n, 4)


def octal_decimal(n):
    n = str(n)
    return int(n, 8)


def hexadecimal_decimal(n):
    n = str(n)
    return int(n, 16)
