from direcoes3D import *
from numpy import argmax, zeros
from util.static_functions import Progress
from PyQt5.QtWidgets import QApplication
from util.save_ppd import save_imgs, save_info
from time import time


def main_ppd_3d(A, pores, phi, theta, answer):
    start = time()

    total_porosity = total_porosity_v = total_porosity_h = total_porosity_d = 0
    A = (A * 255).astype('uint8')
    v0 = zeros(3)
    s, m, n = len(A), len(A[0]), len(A[0][0])
    I = []

    if not pores:
        A[A == 0] = 0.5
        A[A == 1] = 0
        A[A == 0.5] = 1

    for k in prange(s):

        progress = Progress()
        progress.set_min_max(1, m)
        progress.set_title(f'Section {k + 1}')

        quant_v = quant_h = quant_d = porosity = 0
        
        I2 = []

        for i in prange(m):

            QApplication.processEvents()
            progress.set_value(i)

            for j in prange(n):
                if A[k][i][j] == 255:  # Voxel branco encontrado
                    porosity += 1

                    v0[0], v0[1], v0[2] = j, i, k

                    h = horizontal_3d(A, m, n, s, v0, phi, theta)  # calculo da direacao horizontal
                    v = vertical_3d(A, m, n, s, v0, phi, theta)  # calculo da direcao vertical
                    d = diagonal_3d(A, m, n, s, v0, phi, theta)  # calculo da direcao diagonal

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

    progress.close()

    return [I, m, n, s], [total_voxels, total_porosity, total_porosity_h, total_porosity_v, total_porosity_d]



