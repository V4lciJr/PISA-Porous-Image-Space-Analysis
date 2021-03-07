from numpy import ones
from util.static_functions import Functions
from os import mkdir, path


def save_imgs(I, m, n, section):
    for k in range(4):
        A = ones((m, n, 3), 'float16')

        if k == 0:
            save(A, I, 'All_Directions', section, k)
        elif k == 1:
            save(A, I, 'Horizontal', section, k)
        elif k == 2:
            save(A, I, 'Vertical', section, k)
        elif k == 3:
            save(A, I, 'Diagonal', section, k)


def save(A, I, direction, section, k):
    if not path.exists(Functions.path + '\\' + direction):
        mkdir(Functions.path + '\\' + direction)

    for p in I:
        if (k == 0 or k == 1) and p[1] == 'h':
            A[p[0][1]][p[0][2]] = (1, 0, 0)
        elif (k == 0 or k == 2) and p[1] == 'v':
            A[p[0][1]][p[0][2]] = (0, 0, 1)
        elif (k == 0 or k == 3) and p[1] == 'd':
            A[p[0][1]][p[0][2]] = (0, 1, 0)

    _ = Functions.save_section(A, section, direction)


def save_info(tv, tp, tp_h, tp_v, tp_d, time_exec):
    with open(Functions.path + '\\Information.txt', 'w') as archive:
        archive.write(f'Number of Voxels:    {tv}\n')
        archive.write(f'Porosity:            {tp}\n')
        archive.write(f'Vertical Porosity:   {tp_v}\n')
        archive.write(f'Horizontal Porosity: {tp_h}\n')
        archive.write(f'Diagonal Porosity:   {tp_d}\n')
        archive.write(f'\nTime Execution:      {Functions.calc_time(time_exec)}\n')



