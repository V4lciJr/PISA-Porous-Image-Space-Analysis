from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore
from gui.screen_info import Ui_screen_info
from util.static_functions import Functions, Progress


class ScreenInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_screen_info()
        self.ui.setupUi(self)

        self.progress = Progress()

        self.ui.label_erro_2d_info.hide()
        self.ui.label_erro_2d_thin_info.hide()

        self.ui.lineEdit_2D_info.setValidator(QIntValidator(0, 9999))
        self.ui.lineEdit_range_left_info.setValidator(QIntValidator(0, 9999))
        self.ui.lineEdit_range_right_info.setValidator(QIntValidator(0, 9999))

        _ = self.__checked_dims()

        self.ui.radioButton_info_2d.clicked.connect(self.__checked_dims)
        self.ui.radioButton_2d_sections_info.clicked.connect(self.__checked_dims)
        self.ui.radioButton_3d_info.clicked.connect(self.__checked_dims)

        self.ui.pushButton_calculate.clicked.connect(lambda: self.__pre_processing_matrix(Functions.view))

    def __calculate_button(self, A, dim):
        grains = 0
        pores = 0

        if dim == '2D':
            s, m, n = 1, len(A), len(A[0])
            self.progress.set_min_max(1, m)
            print(type(A))
            print(type(A[0][0]))
            for i in range(m):
                QApplication.processEvents()
                self.progress.set_value(i + 1)
                for j in range(n):
                    if A[i][j] == 0:
                        grains += 1
                    else:
                        pores += 1
            self.progress.close()
            self.__enable_line_edit()
        else:
            s, m, n = len(A), len(A[0]), len(A[0][0])
            self.progress.set_min_max(1, s)
            for k in range(s):
                QApplication.processEvents()
                self.progress.set_value(k + 1)
                for i in range(m):
                    for j in range(n):
                        if A[k][i][j] == 0:
                            grains += 1
                        else:
                            pores += 1

            self.progress.close()
            self.__enable_line_edit()

        pixels = s * m * n
        porosity = pores / pixels

        percent_grains = grains / pixels * 100
        percent_pores = pores / pixels * 100

        self.ui.lineEdit_grains.setText(str(grains))
        self.ui.lineEdit_pores.setText(str(pores))
        self.ui.lineEdit_porosity.setText(str(porosity))
        self.ui.lineEdit_pixels.setText(str(pixels))
        self.ui.lineEdit_percent_grains.setText(str(f'{percent_grains :.2f}'))
        self.ui.lineEdit_percent_pores.setText(str(f'{percent_pores : .2f}'))

    def __pre_processing_matrix(self, A):
        Functions.run((self.ui.radioButton_info_2d, self.ui.lineEdit_2D_info, self.ui.label_erro_2d_info),
                      self.ui.radioButton_3d_info,
                      (self.ui.radioButton_2d_sections_info, self.ui.lineEdit_range_left_info,
                       self.ui.lineEdit_range_right_info, self.ui.label_erro_2d_thin_info))
        try:

            dim = self.__checked_dims()

            if dim == '2D':
                self.__calculate_button(A[int(self.ui.lineEdit_2D_info.text()) - 1], dim)

            elif dim == '2D sections':
                self.__calculate_button(
                    A[int(self.ui.lineEdit_range_left_info.text()) - 1: int(self.ui.lineEdit_range_right_info.text())],
                    dim)

            elif dim == '3D':
                self.__calculate_button(A, dim)

        except ValueError:
            if self.ui.radioButton_info_2d.isChecked():
                self.ui.label_erro_2d_info.show()
            else:
                self.ui.label_erro_2d_thin_info.show()
        except IndexError:
            Functions.msgbox('Invalid range.\nFinal value must be greater than the initial value',
                             'Invalid ', 'Interval error', 'warning')
            self.ui.lineEdit_range_left_info.clear()
            self.ui.lineEdit_range_right_info.clear()

    @QtCore.pyqtSlot()
    def __checked_dims(self):

        dim = ''

        if self.ui.radioButton_info_2d.isChecked():
            self.ui.lineEdit_2D_info.setEnabled(True)
            Functions.enable_color(self.ui.lineEdit_2D_info)
            self.ui.lineEdit_range_right_info.setEnabled(False)
            Functions.disable_color(self.ui.lineEdit_range_right_info, [180, 180, 180])
            self.ui.lineEdit_range_left_info.setEnabled(False)
            Functions.disable_color(self.ui.lineEdit_range_left_info, [190, 190, 190])
            self.ui.lineEdit_range_right_info.setText('')
            self.ui.lineEdit_range_left_info.setText('')
            self.ui.label_pixels.setText('Number of Pixels:')
            self.ui.label_grais_pixels.setText('Number of Grains:')
            self.ui.label_number_pores_pixels.setText('Number of Pores:')
            dim = '2D'

        elif self.ui.radioButton_2d_sections_info.isChecked():
            self.ui.lineEdit_2D_info.setEnabled(False)
            Functions.disable_color(self.ui.lineEdit_2D_info, [150, 150, 150])
            self.ui.lineEdit_range_left_info.setEnabled(True)
            Functions.enable_color(self.ui.lineEdit_range_left_info)
            self.ui.lineEdit_range_right_info.setEnabled(True)
            Functions.enable_color(self.ui.lineEdit_range_right_info)
            self.ui.lineEdit_2D_info.setText('')
            self.ui.label_pixels.setText('Number of Voxels:')
            self.ui.label_grais_pixels.setText('Number of Grains Voxels:')
            self.ui.label_number_pores_pixels.setText('Number of Pore Voxels:')
            dim = '2D sections'

        elif self.ui.radioButton_3d_info.isChecked():
            self.ui.lineEdit_2D_info.setEnabled(False)
            Functions.disable_color(self.ui.lineEdit_2D_info, [150, 150, 150])
            self.ui.lineEdit_range_left_info.setEnabled(False)
            Functions.disable_color(self.ui.lineEdit_range_left_info, [180, 180, 180])
            self.ui.lineEdit_range_right_info.setEnabled(False)
            Functions.disable_color(self.ui.lineEdit_range_right_info, [190, 190, 190])
            self.ui.lineEdit_2D_info.setText('')
            self.ui.lineEdit_range_left_info.setText('')
            self.ui.lineEdit_range_right_info.setText('')
            self.ui.label_pixels.setText('Number of Voxels:')
            self.ui.label_grais_pixels.setText('Number of Grains Voxels:')
            self.ui.label_number_pores_pixels.setText('Number of Pore Voxels:')
            dim = '3D'

        return dim

    @QtCore.pyqtSlot()
    def clear_lide_edit(self):
        self.ui.lineEdit_pores.clear()
        self.ui.lineEdit_grains.clear()
        self.ui.lineEdit_porosity.clear()
        self.ui.lineEdit_percent_pores.clear()
        self.ui.lineEdit_percent_grains.clear()
        self.ui.lineEdit_pixels.clear()
        self.ui.lineEdit_2D_info.clear()
        self.ui.lineEdit_range_right_info.clear()
        self.ui.lineEdit_range_left_info.clear()
        self.ui.radioButton_info_2d.setChecked(True)
        _ = self.__checked_dims()

    @QtCore.pyqtSlot()
    def __enable_line_edit(self):
        self.ui.lineEdit_porosity.setEnabled(True)
        self.ui.lineEdit_porosity.setReadOnly(True)
        self.ui.lineEdit_pores.setEnabled(True)
        self.ui.lineEdit_pores.setReadOnly(True)
        self.ui.lineEdit_grains.setEnabled(True)
        self.ui.lineEdit_grains.setReadOnly(True)
        self.ui.lineEdit_percent_pores.setEnabled(True)
        self.ui.lineEdit_percent_pores.setReadOnly(True)
        self.ui.lineEdit_percent_grains.setEnabled(True)
        self.ui.lineEdit_percent_grains.setReadOnly(True)
        self.ui.lineEdit_pixels.setEnabled(True)
        self.ui.lineEdit_pixels.setReadOnly(True)
