from numpy.random import rand
from PyQt5.QtWidgets import QApplication
from numpy import array, ones
from static_functions import Progress
from static_functions import Functions
from os import path, mkdir
from time import time


class EP_2D:
    __color = []
    __s = None
    __m = None
    __n = None
    __A = None

    @classmethod
    def run(cls, A, pores, answer):

        start = time()

        cls.__A = A

        if not pores:
            cls.__A[cls.__A == 0] = 0.5
            cls.__A[cls.__A == 1] = 0
            cls.__A[cls.__A == 0.5] = 1

        cls.__s, cls.__m, cls.__n = len(A), len(A[0]), len(A[0][0])
        cls.__color = []
        neighbors_list = []

        progress = Progress()
        progress.set_min_max(1, cls.__s)

        for k in range(cls.__s):
            QApplication.processEvents()
            progress.set_value(k + 1)

            ngb = []

            for i in range(cls.__m):
                for j in range(cls.__n):
                    if cls.__A[k][i][j] == 1:  # white pixel found
                        if i == 0 or j == 0 or i == cls.__m - 1 or j == cls.__n - 1:
                            cls.__A, effective, neighbors = cls.__is_effective([k, i, j])

                            if not effective:
                                # removing the color from the list
                                for c in range(len(cls.__color)):
                                    if cls.__A[neighbors[0][0]][neighbors[0][1]][neighbors[0][2]] == cls.__color[c]:
                                        cls.__color.pop(c)
                                        break

                                # painting the pixels of black
                                for p in neighbors:
                                    cls.__A[p[0]][p[1]][p[2]] = 0

                            if effective:
                                neighbors_list.append(neighbors)
                                ngb.append(neighbors)

            if answer:
                cls.__save(ngb, k)

        cls.__A[cls.__A == 1] = 0
        cls.__A[cls.__A == 0] = 1

        end = time()
        progress.close()

        time_execution = end - start

        if answer:
            cls.__save_time(time_execution)

        return cls.__A, neighbors_list

    @classmethod
    def __is_effective(cls, p0):

        effective = False

        gray = rand(1).astype('float16')  # random color to paint the pixel

        # checking if the color already exists
        equal_color = True
        while equal_color:
            equal_color = False
            for c in cls.__color:
                if gray == c:
                    equal_color = True
                    gray = rand(1).astype('float16')  # new random color
                    break
        cls.__color.append(gray[0])  # adding color to the list

        cls.__A, neighbors = cls.__neighbors(p0, gray)  # getting the neighbors of p0 pixel

        # checking if it's an effective region
        for p in neighbors:
            if p[1] == 0 or p[1] == cls.__m - 1:
                if p[1] != p0[1]:
                    effective = True
                    break
            if p[2] == 0 or p[2] == cls.__n - 1:
                if p[2] != p0[2]:
                    effective = True
                    break

        return cls.__A, effective, neighbors

    @classmethod
    def __neighbors(cls, p0, gray):
        neighbor_list = [p0]
        neighbors = [p0]
        cls.__A[p0[0]][p0[1]][p0[2]] = gray  # painting the root pixel

        while neighbor_list:
            p = neighbor_list.pop(0)  # getting pixel

            # getting neighbors from p
            borders = cls.__borders(p)
            for i in range(borders[0], borders[1]):
                for j in range(borders[2], borders[3]):
                    # white neighbor
                    if cls.__A[p0[0]][i][j] == 1:
                        neighbor_list.append([p[0], i, j])  # adding to the list of neighbors
                        neighbors.append([p[0], i, j])
                        cls.__A[p[0]][i][j] = gray  # painting the neighbos

        return cls.__A, neighbors

    @classmethod
    def __borders(cls, p):

        if p[1] - 1 >= 0:
            ini_i = p[1] - 1
        else:
            ini_i = 0

        if p[1] + 1 < cls.__m:
            end_i = p[1] + 2
        else:
            end_i = cls.__m

        if p[2] - 1 >= 0:
            ini_j = p[2] - 1
        else:
            ini_j = 0

        if p[2] + 1 < cls.__n:
            end_j = p[2] + 2
        else:
            end_j = cls.__n

        return [ini_i, end_i, ini_j, end_j]

    @classmethod
    def __save(cls, ngb, section):
        if not path.exists(Functions.path + '\\All_Effectives'):
            mkdir(Functions.path + '\\All_Effectives')

        A = ones((cls.__m, cls.__n, 3), 'float16')
        effectives = 0

        for e in ngb:
            effectives += len(e)
            rgb = rand(3).astype('float16')

            for p in e:
                A[p[1]][p[2]] = rgb

        name = Functions.save_section(A, section, 'All_Effectives')
        cls.__save_info(effectives, name)

    @classmethod
    def __save_info(cls, effectives, name):
        effectives /= cls.__m * cls.__n
        with open(Functions.path + '\\All_Effectives\\Information.txt', 'a') as archive:
            archive.write(f'Effective Porosity in {name}:    {effectives}\n')

    @classmethod
    def __save_time(cls, time_exec):
        with open(Functions.path + '\\All_Effectives\\Information.txt', 'a') as archive:
            archive.write(f'\nTime Execution:               {Functions.calc_time(time_exec)}\n')


#########################################################
# Class 3D
#########################################################


class EP_3D:
    __A = array([])
    __s, __m, __n = None, None, None
    __colors, __voxels_list = [], []
    __cont = 0

    @classmethod
    def run(cls, A, pores, ngb, answer):

        start = time()

        cls.__A = A
        cls.__s, cls.__m, cls.__n = cls.__A.shape[0], cls.__A.shape[1], cls.__A.shape[2]
        cls.__colors = []  # random color list to paint effective pores
        cls.__voxels_list = []
        cls.__cont = 0

        if not pores:
            cls.__A[cls.__A == 0] = 0.5
            cls.__A[cls.__A == 1] = 0
            cls.__A[cls.__A == 0.5] = 1

        progress = Progress()
        progress.set_min_max(1, cls.__s)

        progress.setWindowTitle('Running')

        # Calculate effective pores
        for k in range(cls.__s):
            QApplication.processEvents()
            progress.set_value(k + 1)

            for i in range(cls.__m):
                for j in range(cls.__n):
                    if k == 0:
                        if cls.__A[k][i][j] == 1:
                            v0 = [i, j, k]  # root vertex

                            # Getting effective and non-effective voxels
                            voxels = cls.__neighbors(v0, ngb)

                            # Painting the effective and non-effective voxels
                            cls.__effectiveness(v0, voxels, answer)
                    else:
                        if i == 0 or i == cls.__m - 1 or j == 0 or j == cls.__n - 1:
                            if cls.__A[k][i][j] == 1:
                                v0 = [i, j, k]

                                voxels = cls.__neighbors(v0, ngb)

                                cls.__effectiveness(v0, voxels, answer)

        cls.__A[cls.__A == 0] = 1
        end = time()
        time_execution = end - start
        if answer:
            cls.__save_all(cls.__voxels_list, time_execution)

        progress.close()

        return cls.__A, cls.__voxels_list

    @classmethod
    def __neighbors(cls, v0, ngb):

        cls.__A[v0[2]][v0[0]][v0[1]] = 0.5  # painting the root voxel

        voxel_list = [v0]  # auxiliary variable to add the voxels that belong to the pores
        voxels = []  # getting all the voxels to then paint with a random color

        while True:
            v = voxel_list.pop(0)  # v = [i j k]

            border = cls.__neighbors_border(v)

            if ngb == 6:
                voxel_list, voxels = cls.__neighbor_6(v, border, voxel_list, voxels)
            elif ngb == 18:
                voxel_list, voxels = cls.__neighbor_18(v, border, voxel_list, voxels)
            elif ngb == 26:
                voxel_list, voxels = cls.__neighbor_26(border, voxel_list, voxels)

            # If you have no more voxels, exit the loop
            if not voxel_list:
                break

        return voxels

    @classmethod
    def __neighbors_border(cls, v):

        if v[0] - 1 < 0:
            ini_i = 0
        else:
            ini_i = v[0] - 1

        if v[0] + 1 > cls.__m - 1:
            end_i = cls.__m - 1
        else:
            end_i = v[0] + 1

        if v[1] - 1 < 0:
            ini_j = 0
        else:
            ini_j = v[1] - 1

        if v[1] + 1 > cls.__n - 1:
            end_j = cls.__n - 1
        else:
            end_j = v[1] + 1

        if v[2] - 1 < 0:
            ini_k = 0
        else:
            ini_k = v[2] - 1

        if v[2] + 1 > cls.__s - 1:
            end_k = cls.__s - 1
        else:
            end_k = v[2] + 1

        return [ini_i, ini_j, ini_k, end_i, end_j, end_k]

    @classmethod
    def __neighbor_6(cls, v, border, voxel_list, voxels):

        for k in range(border[2], border[5] + 1):
            if k != v[2]:
                i, j = v[0], v[1]
                voxel_list, voxels = cls.__add_neighbor(voxel_list, voxels, [k, i, j])
                continue
            else:
                for i in range(border[0], border[3] + 1):
                    if i < v[0] or i > v[0]:
                        j = v[1]
                        voxel_list, voxels = cls.__add_neighbor(voxel_list, voxels, [k, i, j])
                    else:
                        for j in range(border[1], border[4] + 1):
                            voxel_list, voxels = cls.__add_neighbor(voxel_list, voxels, [k, i, j])

        return voxel_list, voxels

    @classmethod
    def __neighbor_18(cls, v, border, voxel_list, voxels):

        for k in range(border[2], border[5] + 1):
            for i in range(border[0], border[3] + 1):
                if (k != v[2]) and (i < v[0] or i > v[0]):
                    j = v[1]
                    voxel_list, voxels = cls.__add_neighbor(voxel_list, voxels, [k, i, j])
                else:
                    for j in range(border[1], border[4] + 1):
                        voxel_list, voxels = cls.__add_neighbor(voxel_list, voxels, [k, i, j])

        return voxel_list, voxels

    @classmethod
    def __neighbor_26(cls, border, voxel_list, voxels):

        for k in range(border[2], border[5] + 1):
            for i in range(border[0], border[3] + 1):
                for j in range(border[1], border[4] + 1):
                    voxel_list, voxels = cls.__add_neighbor(voxel_list, voxels, [k, i, j])

        return voxel_list, voxels

    @classmethod
    def __add_neighbor(cls, voxel_list, voxels, ind):

        if cls.__A[ind[0]][ind[1]][ind[2]] == 1:
            voxel_list.append([ind[1], ind[2], ind[0]])  # adding the neighboring voxel found to the list
            voxels.append([ind[1], ind[2], ind[0]])
            cls.__A[ind[0]][ind[1]][ind[2]] = 0.5  # painting the found voxel

        return voxel_list, voxels

    @classmethod
    def __effectiveness(cls, v0, voxels, answer, time_exec=''):

        effective = cls.__eh_efetivo(v0, voxels)
        rgb = None

        # Painting the effective voxels randomly
        if effective:
            cls.__cont += 1
            cls.__voxels_list.append(voxels)

            while True:
                equal_color = False
                rgb = rand(1).astype('float16')  # new random color

                for color in cls.__colors:
                    if rgb == color:
                        equal_color = True
                        break

                if equal_color:
                    continue

                cls.__colors.append(rgb)
                break

            cls.__A[v0[2]][v0[0]][v0[1]] = rgb  # painting the root voxel

            for v in voxels:
                cls.__A[v[2]][v[0]][v[1]] = rgb  # painting the other voxels

            if answer:
                cls.__save_one(voxels, time_exec)

        # Painting the non-effective voxels yellow
        else:
            cls.__A[v0[2]][v0[0]][v0[1]] = 0

            for v in voxels:
                cls.__A[v[2]][v[0]][v[1]] = 0

    @classmethod
    def __eh_efetivo(cls, v0, voxels):

        """
        Returns True if the pores are effective or False otherwise
        """

        effective = False

        # running through all the voxels that were painted red
        for v in voxels:
            # checks if the root voxel (v0) is in the first slice of the cube
            if v0[2] == 0:
                if v[2] == cls.__s - 1:  # check if the voxel v of the cluster is in the last slice
                    effective = True
                    break
                elif cls.__s - 1 > v[2] > 0:  # checks if the voxel v of the cluster is in any internal slice
                    # checks if component i is on the edge and is different from component i of v0
                    if v[0] == 0 or v[0] == cls.__m - 1:
                        if v[0] != v0[0]:
                            effective = True
                            break
                    # checks if component j is on the edge and is different from component j of v0
                    elif v[1] == 0 or v[1] == cls.__n - 1:
                        if v[1] != v0[1]:
                            effective = True
                            break
            else:
                if v[2] > v0[2]:
                    if v[0] == 0 or v[0] == cls.__m - 1:
                        if v[0] != v0[0]:
                            effective = True
                            break
                    elif v[1] == 0 or v[1] == cls.__n - 1:
                        if v[1] != v0[1]:
                            effective = True
                            break

        return effective

    @classmethod
    def __save_one(cls, ngb, time_exec):
        if not path.exists(Functions.path + f'\\Effectives_{cls.__cont}'):
            mkdir(Functions.path + f'\\Effectives_{cls.__cont}')

        A = ones((cls.__s, cls.__m, cls.__n, 3), 'float16')
        effectives = len(ngb)
        rgb = rand(3).astype('float16')

        for v in ngb:
            A[v[2]][v[0]][v[1]] = rgb

        for k in range(cls.__s):
            _ = Functions.save_section(A[k], k, f'\\Effectives_{cls.__cont}')
        cls.__save_info(effectives, f'\\Effectives_{cls.__cont}', time_exec)

    @classmethod
    def __save_all(cls, ngb, time_exec):
        if not path.exists(Functions.path + '\\All_Effectives'):
            mkdir(Functions.path + '\\All_Effectives')

        A = ones((cls.__s, cls.__m, cls.__n, 3), 'float16')
        effectives = 0

        for e in ngb:
            effectives += len(e)
            rgb = rand(3).astype('float16')

            for v in e:
                A[v[2]][v[0]][v[1]] = rgb

        for k in range(cls.__s):
            _ = Functions.save_section(A[k], k, '\\All_Effectives')
        cls.__save_info(effectives, '\\All_Effectives', time_exec)

    @classmethod
    def __save_info(cls, effectives, direction, time_exec):
        effectives /= cls.__s * cls.__m * cls.__n
        with open(Functions.path + direction + '\\Information.txt', 'w') as archive:
            archive.write(f'Effective Porosity:    {effectives}\n')
            if time_exec:
                archive.write(f'Time Execution:        {Functions.calc_time(time_exec)}\n')
