from gui.screen_export import Ui_Form_export
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5 import QtCore
from util.static_functions import Functions
from numpy import ones, zeros
from os import path, mkdir
from util.static_functions import Progress
from PIL import Image
from xlsxwriter import Workbook


class ScreenExport(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_export()
        self.ui.setupUi(self)
        self.__folder = ''

        self.__check_ppd = False
        self.__check_ep = False

        self.ui.pushButton_export.clicked.connect(self.__get_folder)
        self.ui.checkBox_ppd_export.clicked.connect(self.__checked_ppd)
        self.ui.checkBox_ep_export.clicked.connect(self.__cheked_ep)
        self.ui.radioButton_effec_export.clicked.connect(self.__raddio_effec)
        self.ui.radioButton_all_eff_export.clicked.connect(self.__raddio_all_effc)

        self.ui.pushButton_ok_export.clicked.connect(self.__export)

    @property
    def lineEdit_save(self):
        return self.ui.lineEdit_path_save

    @QtCore.pyqtSlot()
    def __get_folder(self):

        directory = QFileDialog()
        self.__folder = directory.getExistingDirectory(self, 'Select Directory', 'C:\\Users\\Download\\')
        if self.__folder != '':
            self.ui.lineEdit_path_save.setText(self.__folder)

    @QtCore.pyqtSlot()
    def __checked_ppd(self):
        if self.ui.checkBox_ppd_export.isChecked():
            self.ui.frame_ppd.setEnabled(True)
            self.__check_ppd = True
        else:
            self.ui.frame_ppd.setEnabled(False)
            self.__check_ppd = False

    @QtCore.pyqtSlot()
    def __cheked_ep(self):
        if self.ui.checkBox_ep_export.isChecked():
            self.ui.frame_ep.setEnabled(True)
            self.__check_ep = True
            if len(Functions.EP) > 0:
                self.ui.label_total_effect.setText(f'Total Effective Pores: {len(Functions.voxels)}')
        else:
            self.ui.frame_ep.setEnabled(False)
            self.__check_ep = False

    @QtCore.pyqtSlot()
    def __raddio_effec(self):
        if self.ui.radioButton_effec_export.isChecked():
            self.ui.lineEdit_eff_export.setEnabled(True)

    @QtCore.pyqtSlot()
    def __raddio_all_effc(self):
        if self.ui.radioButton_all_eff_export.isChecked():
            self.ui.lineEdit_eff_export.setEnabled(False)

    @QtCore.pyqtSlot()
    def __export(self):
        img_extension = ''
        info_extension = ''
        if self.ui.radioButton_tiff_export.isChecked():
            img_extension = '.tif'
        elif self.ui.radioButton_jpg_export.isChecked():
            img_extension = '.jpg'
        elif self.ui.radioButton_png_export.isChecked():
            img_extension = '.png'

        if self.ui.radioButton_txt_export.isChecked():
            info_extension = '.txt'
        elif self.ui.radioButton_xls_export.isChecked():
            info_extension = '.xlsx'
        elif self.ui.radioButton_csv.isChecked():
            info_extension = '.csv'

        if self.__check_ppd:
            self.__export_ppd(img_extension, info_extension)

    def __export_ppd(self, img_extension, info_extension):

        op = ''
        if self.ui.radioButton_all.isChecked():
            op = 'all'
        elif self.ui.radioButton_all_directions.isChecked():
            op = 'all_directions'
        elif self.ui.radioButton_horizontal.isChecked():
            op = 'h'
        elif self.ui.radioButton_vertical.isChecked():
            op = 'v'
        elif self.ui.radioButton_diagonal.isChecked():
            op = 'd'

        section = 0
        I = []
        progress = Progress()
        progress.set_min_max(0, len(Functions.voxels_list_PPD[0]) - 1)
        for i, v in enumerate(Functions.voxels_list_PPD[0]):
            QApplication.processEvents()
            progress.set_value(i)

            if v[0][0] == section:
                I.append(v)
                if i < len(Functions.voxels_list_PPD[0]) - 1:
                    continue
                elif Functions.voxels_list_PPD[3] == 1:
                    section = Functions.ind_img

            A = ones((Functions.voxels_list_PPD[1], Functions.voxels_list_PPD[2], 3), 'float16')
            A2 = zeros((Functions.voxels_list_PPD[1], Functions.voxels_list_PPD[2], 3), 'float16')

            if op == 'all':
                for k in range(4):
                    if k == 0:
                        self.__save_ppd_imgs(A, A2, I, 'All_Directions', section, k, img_extension)
                    elif k == 1:
                        self.__save_ppd_imgs(A, A2, I, 'Horizontal', section, k, img_extension)
                    elif k == 2:
                        self.__save_ppd_imgs(A, A2, I, 'Vertical', section, k, img_extension)
                    elif k == 3:
                        self.__save_ppd_imgs(A, A2, I, 'Diagonal', section, k, img_extension)
                    A = ones((Functions.voxels_list_PPD[1], Functions.voxels_list_PPD[2], 3), 'float16')
                    A2 = zeros((Functions.voxels_list_PPD[1], Functions.voxels_list_PPD[2], 3), 'float16')

            elif op == 'all_directions':
                self.__save_ppd_imgs(A, A2, I, 'All_Directions', section, 0, img_extension)
            elif op == 'h':
                self.__save_ppd_imgs(A, A2, I, 'Horizontal', section, 1, img_extension)
            elif op == 'v':
                self.__save_ppd_imgs(A, A2, I, 'Vertical', section, 2, img_extension)
            elif op == 'd':
                self.__save_ppd_imgs(A, A2, I, 'Diagonal', section, 3, img_extension)

            section = v[0][0]
            I = []

        if info_extension == '.txt':
            self.__save_info_ppd_txt()
        elif info_extension == '.xlsx':
            self.__save_info_ppd_xlsx()

    def __save_ppd_imgs(self, A, A2, I, direction, section, k, img_extension):
        if not path.exists(self.ui.lineEdit_path_save.text() + '\\PPD'):
            mkdir(self.ui.lineEdit_path_save.text() + '\\PPD')

        if not path.exists(self.ui.lineEdit_path_save.text() + '\\PPD\\' + direction):
            mkdir(self.ui.lineEdit_path_save.text() + '\\PPD\\' + direction)

        if not path.exists(self.ui.lineEdit_path_save.text() + '\\PPD\\' + direction + ' 2'):
            mkdir(self.ui.lineEdit_path_save.text() + '\\PPD\\' + direction + ' 2')

        for p in I:
            if (k == 0 or k == 1) and p[1] == 'h':
                A[p[0][1]][p[0][2]] = (1, 0, 0)
                A2[p[0][1]][p[0][2]] = (1, 0, 0)
            elif (k == 0 or k == 2) and p[1] == 'v':
                A[p[0][1]][p[0][2]] = (0, 0, 1)
                A2[p[0][1]][p[0][2]] = (0, 0, 1)
            elif (k == 0 or k == 3) and p[1] == 'd':
                A[p[0][1]][p[0][2]] = (0, 1, 0)
                A2[p[0][1]][p[0][2]] = (0, 1, 0)
            else:
                A2[p[0][1]][p[0][2]] = (1, 1, 1)

        _ = self.__save_section(A, A2, section, direction, img_extension)

    @QtCore.pyqtSlot()
    def __save_section(self, A, A2, section, direction, img_extension):
        name_image = self.__name_img(section)
        im = Image.fromarray((A * 255).astype('uint8'))
        im.save(self.ui.lineEdit_path_save.text() + '\\PPD\\' + direction + '\\' + name_image + img_extension)

        im = Image.fromarray((A2 * 255).astype('uint8'))
        im.save(self.ui.lineEdit_path_save.text() + '\\PPD\\' + direction + ' 2\\' + name_image + img_extension)

    @QtCore.pyqtSlot()
    def __save_info_ppd_txt(self):
        if Functions.op_ppd == '3D':
            with open(self.ui.lineEdit_path_save.text() + '\\PPD\\Information.txt', 'w') as archive:
                archive.write(f'Number of Voxels:    {Functions.info_PPD_all[0]}\n')
                archive.write(f'Porosity:            {Functions.info_PPD_all[1]}\n')
                archive.write(f'Vertical Porosity:   {Functions.info_PPD_all[3]}\n')
                archive.write(f'Horizontal Porosity: {Functions.info_PPD_all[2]}\n')
                archive.write(f'Diagonal Porosity:   {Functions.info_PPD_all[4]}\n')
        elif Functions.op_ppd == '2D':
            for i, info in enumerate(Functions.info_PPD_2D):
                with open(self.ui.lineEdit_path_save.text() + '\\PPD\\Information.txt', 'a') as archive:
                    if Functions.voxels_list_PPD[3] > 1:
                        archive.write(f'{self.__name_img(i)}\n\n')
                    else:
                        archive.write(f'{self.__name_img(Functions.ind_img)}\n\n')
                    archive.write(f'Number of Pixels:    {info[0]}\n')
                    archive.write(f'Porosity:            {info[1]}\n')
                    archive.write(f'Vertical Porosity:   {info[3]}\n')
                    archive.write(f'Horizontal Porosity: {info[2]}\n')
                    archive.write(f'Diagonal Porosity:   {info[4]}\n')
                    archive.write('-' * 50 + '\n\n')
            if Functions.voxels_list_PPD[3] > 1:
                with open(self.ui.lineEdit_path_save.text() + '\\PPD\\Information.txt', 'a') as archive:
                    archive.write(f'{"3D Construction":-^50}\n')
                    archive.write(f'- Number of Voxels:    {Functions.info_PPD_all[0]:->4}\n')
                    archive.write(f'- Porosity:            {Functions.info_PPD_all[1]:->4}\n')
                    archive.write(f'- Vertical Porosity:   {Functions.info_PPD_all[3]:->4}\n')
                    archive.write(f'- Horizontal Porosity: {Functions.info_PPD_all[2]:->4}\n')
                    archive.write(f'- Diagonal Porosity:   {Functions.info_PPD_all[4]:->4}\n')
                    archive.write('-' * 50 + '\n')

    def __save_info_ppd_xlsx(self):
        workbook = Workbook(self.ui.lineEdit_path_save.text() + '\\PPD\\Information.xlsx')
        worksheet = workbook.add_worksheet()
        if Functions.op_ppd == '3D':
            # Header
            worksheet.write(0, 0, 'Number of Voxels')
            worksheet.write(0, 1, 'Porosity')
            worksheet.write(0, 2, 'Vertical Porosity')
            worksheet.write(0, 3, 'Horizontal Porosity')
            worksheet.write(0, 4, 'Diagonal Porosity')

            # Body
            worksheet.write(1, 0, Functions.info_PPD_all[0])
            worksheet.write(1, 1, Functions.info_PPD_all[1])
            worksheet.write(1, 2, Functions.info_PPD_all[3])
            worksheet.write(1, 3, Functions.info_PPD_all[2])
            worksheet.write(1, 4, Functions.info_PPD_all[4])
        elif Functions.op_ppd == '2D':
            # Header
            worksheet.write(0, 0, ' ')
            worksheet.write(0, 1, 'Number of Pixels')
            worksheet.write(0, 2, 'Porosity')
            worksheet.write(0, 3, 'Vertical Porosity')
            worksheet.write(0, 4, 'Horizontal Porosity')
            worksheet.write(0, 5, 'Diagonal Porosity')

            # Body
            for i, info in enumerate(Functions.info_PPD_2D):
                if Functions.voxels_list_PPD[3] > 1:
                    worksheet.write(i + 1, 0, self.__name_img(i))
                else:
                    worksheet.write(i + 1, 0, self.__name_img(Functions.ind_img))
                worksheet.write(i + 1, 1, info[0])
                worksheet.write(i + 1, 2, info[1])
                worksheet.write(i + 1, 3, info[3])
                worksheet.write(i + 1, 4, info[2])
                worksheet.write(i + 1, 5, info[4])
            if Functions.voxels_list_PPD[3] > 1:
                worksheet.write(Functions.voxels_list_PPD[3] + 1, 0, '3D Construction')
                worksheet.write(Functions.voxels_list_PPD[3] + 1, 1, Functions.info_PPD_all[0])
                worksheet.write(Functions.voxels_list_PPD[3] + 1, 2, Functions.info_PPD_all[1])
                worksheet.write(Functions.voxels_list_PPD[3] + 1, 3, Functions.info_PPD_all[3])
                worksheet.write(Functions.voxels_list_PPD[3] + 1, 4, Functions.info_PPD_all[2])
                worksheet.write(Functions.voxels_list_PPD[3] + 1, 5, Functions.info_PPD_all[4])
        workbook.close()

    def __name_img(self, section):
        name_image = Functions.folders[section].split('/')
        name_image = name_image[len(name_image) - 1].split('\\')
        name_image = name_image[len(name_image) - 1].split('.')[0]
        return name_image
