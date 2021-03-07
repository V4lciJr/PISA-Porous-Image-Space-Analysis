from numpy import cos, sin, sqrt, zeros, power
from math import sqrt, cos, sin
from numba import jit, numba
from numba import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
from warnings import simplefilter

simplefilter('ignore', category=NumbaDeprecationWarning)
simplefilter('ignore', category=NumbaPendingDeprecationWarning)
simplefilter('ignore', category=NumbaPerformanceWarning)


@jit(nopython=True, parallel=True)
def busca_pixels(A, m, n, p0, incl, quadrante):
    k = step = 0.1
    x0 = p0[1]
    y0 = p0[0]
    L = 0
    if quadrante == 1 or quadrante == 4:
        while True:
            x = round(x0 + k)  # Obtendo as coordenadas do pixel preto
            y = round(abs(k * incl + y0))

            if y < 0 or y > m - 1 or x < 0 or x > n - 1:
                break

            if (A[y, x] == 0 or y == 0 or x == 0 or y == m - 1 or x == n - 1) and (x != x0 or y != y0):
                a = (incl * (y - y0 + (x / incl) + (incl * x0))) / (1 + incl ** 2)
                b = y + (x - a) / incl

                L = sqrt((a - x0) ** 2 + (b - y0) ** 2)
                break
            k += step

    elif quadrante == 2 or quadrante == 3:
        while True:
            x = round(abs(x0 - k))  # Obtendo as coordenadas do pixel preto
            y = round(abs(k * incl - y0))

            if y < 0 or y > m - 1 or x < 0 or x > n - 1:
                break

            if (A[y, x] == 0 or y == 0 or x == 0 or y == m - 1 or x == n - 1) and (x != x0 or y != y0):
                a = (incl * (y - y0 + (x / incl) + (incl * x0))) / (1 + incl ** 2)
                b = y + (x - a) / incl

                L = sqrt((a - x0) ** 2 + (b - y0) ** 2)
                break
            k += step

    return L


@jit(nopython=True, fastmath=True, cache=True)
def busca_voxel(A, m, n, s, phi, theta, v0):

    dist = 0
    t = 0.9
    v2 = v0
    v = zeros(3)

    while True:

        v[0] = v2[0] + t * cos(phi) * sin(theta)
        v[1] = v2[1] + t * sin(phi) * sin(theta)
        v[2] = v2[2] + t * cos(theta)

        for i in numba.prange(3):
           v[i] = round(v[i])

        if v[0] < 0 or v[0] > n - 1 or v[1] < 0 or v[1] > m - 1 or v[2] < 0 or v[2] > s - 1:
            break

        x, y, z = casting(v)

        if A[z][y][x] == 0 or x == 0 or x == n - 1 or y == 0 or y == m - 1 or z == 0 or z == s - 1:

            dist = sqrt(power(v - v0, 2).sum())

            break
        else:
            v2 = v

    return dist


@jit(nopython=True)
def casting(v):
    return int(v[0]), int(v[1]), int(v[2])
