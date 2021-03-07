from numpy import pi
from numba import jit, prange
from busca import busca_voxel
from numba import NumbaDeprecationWarning, NumbaPendingDeprecationWarning, NumbaPerformanceWarning
from warnings import simplefilter

simplefilter('ignore', category=NumbaDeprecationWarning)
simplefilter('ignore', category=NumbaPendingDeprecationWarning)
simplefilter('ignore', category=NumbaPerformanceWarning)


@jit(nopython=True, fastmath=True, cache=True)
def horizontal_3d(A, m, n, s, v0, n_phi, n_theta):
    N_THETA = n_theta
    N_PHI = n_phi

    h = 0
    # Unico Somatorio
    for i in prange(N_THETA // 3, 2 * N_THETA // 3):
        theta = pi * i / N_THETA
        for j in prange(N_PHI):
            phi = 2 * pi * j / N_PHI
            dist = busca_voxel(A, m, n, s, phi, theta, v0)

            h += dist

    return h


@jit(nopython=True, fastmath=True, cache=True)
def vertical_3d(A, m, n, s, v0, n_phi, n_theta):
    N_THETA = n_theta
    N_PHI = n_phi
    v = 0

    # Primeiro Somatorio
    for i in prange(N_THETA // 6):
        theta = pi * i / N_THETA
        
        for j in prange(N_PHI):
            phi = 2 * pi * j / N_PHI
            dist = busca_voxel(A, m, n, s, phi, theta, v0)

            v += dist

    # Segundo Somatorio
    for i in prange(5 * N_THETA // 6, N_THETA):
        theta = pi * i / N_THETA
        for j in prange(N_PHI):
            phi = 2 * pi * j / N_PHI

            dist = busca_voxel(A, m, n, s, phi, theta, v0)
            v += dist

    return v


@jit(nopython=True, fastmath=True, cache=True)
def diagonal_3d(A, m, n, s, v0, n_phi, n_theta):
    N_THETA = n_theta
    N_PHI = n_phi
    d = 0

    # Primeiro Somatorio
    for i in prange(N_THETA // 6, N_THETA // 3):
        theta = pi * i / N_THETA

        for j in prange(N_PHI):
            phi = 2 * pi * j / N_PHI

            dist = busca_voxel(A, m, n, s, phi, theta, v0)

            d += dist

    # Segundo Somatorio
    for i in prange(2 * N_THETA // 3, 5 * N_THETA // 6):
        theta = pi * i / N_THETA
        for j in prange(N_PHI):
            phi = 2 * pi * j / N_PHI
            dist = busca_voxel(A, m, n, s, phi, theta, v0)

            d += dist

    return d
