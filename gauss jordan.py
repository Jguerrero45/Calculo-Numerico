import numpy as np


def gauss_jordan(A, B):
    # evitar truncamiento en operaciones
    A = np.array(A, dtype=float)

    # matriz aumentada
    AB = np.concatenate((A, B), axis=1)
    AB0 = np.copy(AB)

    # eliminacion hacia adelante
    AB = eliminacion_hacia_adelante(AB)

    # eimina hacia atras
    AB = eliminacion_hacia_atras(AB)

    # solución de X
    X = solucion(AB)

    return AB0, AB, X


def pivoteo_parcial_por_filas(AB):
    tamaño = np.shape(AB)
    n = tamaño[0]
    m = tamaño[1]

    # para cada fila en AB
    for i in range(0, n-1):  # columna desde diagonal i en adelante
        columna = abs(AB[i:, i])
        dondemax = np.argmax(columna)

    return AB


def eliminacion_hacia_adelante(AB):
    tamaño = np.shape(AB)
    n = tamaño[0]
    m = tamaño[1]

    for i in range(0, n-1):
        pivote = AB[i, i]
        adelante = i + 1
        for k in range(adelante, n, 1):
            factor = AB[k, i]/pivote
            AB[k, :] = AB[k, :] - AB[i, :]*factor

    return AB


def eliminacion_hacia_atras(AB):
    tamaño = np.shape(AB)
    n = tamaño[0]
    m = tamaño[1]

    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila, 0-1, -1):
        pivote = AB[i, i]
        atras = i-1
        for k in range(atras, 0-1, -1):
            factor = AB[k, i]/pivote
            AB[k, :] = AB[k, :] - AB[i, :]*factor

    # diagonal a unos
    for i in range(n):
        AB[i, :] = AB[i, :]/AB[i, i]

    return AB


def solucion(AB):
    tamaño = np.shape(AB)
    n = tamaño[0]
    m = tamaño[1]

    X = np.copy(AB[:, m-1])
    X = np.transpose([X])

    return X


# INGRESO
A = np.array([[4, 2, 5], [2, 5, 8], [5, 4, 3]])
B = np.array([[60.70], [92.90], [56.30]])


AB0, AB, X = gauss_jordan(A, B)

print('Matriz aumentada:')
print(AB0)
print('solución de X: ')
print(X)
