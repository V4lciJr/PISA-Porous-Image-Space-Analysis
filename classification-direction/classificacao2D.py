from numpy import argmax
from direcoes2D import *
from util.static_functions import Progress
from PyQt5.QtWidgets import QApplication
from util.save_ppd import save_imgs, save_info
from time import time


def main_ppd_2d(A, pores, phi, answer):
    start = time()

    total_porosity = total_porosity_v = total_porosity_h = total_porosity_d = 0
    A = (A * 255).astype('uint8')
    s, m, n = len(A), len(A[0]), len(A[0][0])
    I = []
    info = []
    total_pixels = m * n

    if not pores:
        A[A == 0] = 100
        A[A == 255] = 0
        A[A == 100] = 255

    # Classificacao dos pixels brancos
    for k in range(s):
        progress = Progress()
        progress.set_min_max(0, m)
        progress.set_title(f'Image {k + 1}')
        quant_v = quant_h = quant_d = porosity = 0

        I2 = []

        for i in numba.prange(m):
            QApplication.processEvents()
            progress.set_value(i)
            for j in numba.prange(n):
                if A[k][i][j] == 255:  # encontrando o pixel branco
                    porosity += 1  # Numero de poros

                    p0 = [i, j]
                    h = horizontal_2d(p0, A[k], m, n, phi)  # calculo horizontal
                    v = vertical_2d(p0, A[k], m, n, phi)  # calculo vertical
                    d = diagonal_2d(p0, A[k], m, n, phi)  # calculo diagonal

                    # Verficando qual direcao eh a maior
                    # Verificando qual posicao eh melhor
                    maior = argmax([h, d, v])
                    if maior == 0:
                        quant_h += 1
                        I.append(([k, i, j], 'h'))
                        I2.append(([k, i, j], 'h'))
                    elif maior == 1:
                        quant_d += 1
                        I.append(([k, i, j], 'd'))
                        I2.append(([k, i, j], 'd'))
                    elif maior == 2:
                        quant_v += 1
                        I.append(([k, i, j], 'v'))
                        I2.append(([k, i, j], 'v'))

        total_porosity += porosity
        total_porosity_v += quant_v
        total_porosity_h += quant_h
        total_porosity_d += quant_d
        info.append([total_pixels,
                     total_porosity / total_pixels,
                     total_porosity_h / total_pixels,
                     total_porosity_v / total_pixels,
                     total_porosity_d / total_pixels])

        if answer:
            save_imgs(I2, m, n, k)

    total_voxels = s * m * n
    total_porosity /= total_voxels
    total_porosity_h /= total_voxels
    total_porosity_v /= total_voxels
    total_porosity_d /= total_voxels

    end = time()
    time_execution = end - start

    if answer:
        save_info(total_voxels, total_porosity, total_porosity_h, total_porosity_v, total_porosity_d, time_execution)

    return [I, m, n, s], [total_voxels, total_porosity, total_porosity_h, total_porosity_v, total_porosity_d], info
