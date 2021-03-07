from math import tan, pi
from busca import busca_pixels
from numba import numba, jit
from numba import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
import warnings

warnings.simplefilter('ignore', category=NumbaDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPendingDeprecationWarning)
warnings.simplefilter('ignore', category=NumbaPerformanceWarning)


@jit(nopython=True)
def horizontal_2d(p0, A, m, n, phi):
    N = phi
    h = 0
    x0 = p0[1]
    y0 = p0[0]
    L = 0

    # Primeiro somatorio
    for i in numba.prange(N // 12):
        if x0 == n - 1 or (y0 == m - 1 and i != 0):
            continue
        elif i == 0:  # o raio esta num angulo de 0 graus
            for j in numba.prange(x0 + 1, n + 1):
                if A[y0][j] == 0 or j == n - 1:
                    L = j - x0
                    break
        else:
            incl = calcula_tangente(i, N)
            L = busca_pixels(A, m, n, p0, incl, 1)

        h += L

    # Segundo somatorio
    for i in numba.prange(5 * N // 12, 7 * N // 12):
        if x0 == 0 or (y0 == 0 and i > 96) or (y0 == m - 1 and i < 96):
            continue
        elif i == 96:
            for j in numba.prange(x0 - 1, -1, -1):
                if A[y0][j] == 0 or j == 0:
                    L = x0 - j
                    break
        else:
            incl = calcula_tangente(i, N)
            if i < 96:
                L = busca_pixels(A, m, n, p0, incl, 2)
            else:
                L = busca_pixels(A, m, n, p0, incl, 3)

        h += L

    # Terceiro somatorio
    for i in numba.prange(11 * N // 12, N):
        if x0 == n - 1 or y0 == 0:
            continue
        else:
            incl = calcula_tangente(i, N)

            L = busca_pixels(A, m, n, p0, incl, 4)

        h += L

    return h


@jit(nopython=True)
def vertical_2d(p0, A, m, n, phi):
    N = phi
    v = 0
    L = 0
    x0 = p0[1]
    y0 = p0[0]

    # Primeiro somatorio
    for i in numba.prange(N // 6, N // 3):
        if (x0 == 0 and i > 48) or (x0 == n - 1 and i < 48) or y0 == m - 1:
            continue
        elif i == 48:
            for j in numba.prange(y0 + 1, m + 1):
                if A[j][x0] == 0 or j == m - 1:
                    L = j - y0
                    break
        else:
            incl = calcula_tangente(i, N)
            if i < 48:
                L = busca_pixels(A, m, n, p0, incl, 1)
            else:
                L = busca_pixels(A, m, n, p0, incl, 2)

        v += L

    # Segundo somatorio
    for i in numba.prange(2 * N // 3, 5 * N // 6):
        if (x0 == 0 and i < 144) or (x0 == n - 1 and i > 144) or y0 == 0:
            continue
        elif i == 144:
            for j in numba.prange(y0 - 1, -1, -1):
                if A[j][x0] == 0 or j == 0:
                    L = y0 - j
                    break
        else:
            incl = calcula_tangente(i, N)
            if i < 144:
                L = busca_pixels(A, m, n, p0, incl, 3)
            else:
                L = busca_pixels(A, m, n, p0, incl, 4)

        v += L

    return v


@jit(nopython=True)
def diagonal_2d(p0, A, m, n, phi):
    N = phi
    d = 0
    x0 = p0[1]
    y0 = p0[0]
    L = 0

    # Primeiro somatorio
    for i in numba.prange(N // 3, 5 * N // 12):
        if x0 == 0 or y0 == m - 1:
            continue
        else:
            incl = calcula_tangente(i, N)
            L = busca_pixels(A, m, n, p0, incl, 2)

        d += L

    # Segundo somatorio
    for i in numba.prange(5 * N // 6, 11 * N // 12):
        if x0 == n - 1 or y0 == 0:
            continue
        else:
            incl = calcula_tangente(i, N)
            L = busca_pixels(A, m, n, p0, incl, 4)

        d += L

    # Terceiro somatorio
    for i in numba.prange(N // 12, N // 6):
        if x0 == n - 1 or y0 == m - 1:
            continue
        else:
            incl = calcula_tangente(i, N)
            L = busca_pixels(A, m, n, p0, incl, 1)

        d += L

    # Quarto somatorio
    for i in numba.prange(7 * N // 12, 2 * N // 3):
        if x0 == 0 or y0 == 0:
            continue
        else:
            incl = calcula_tangente(i, N)
            L = busca_pixels(A, m, n, p0, incl, 3)

        d += L

    return d


@jit(nopython=True)
def calcula_tangente(i, N):
    return tan(2 * pi * i / N)
