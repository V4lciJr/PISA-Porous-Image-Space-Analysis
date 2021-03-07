from gui.screen_ppd import Ui_janela_ppd
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore
from util.static_functions import Functions
from classificaco3D import main_ppd_3d
from classificacao2D import main_ppd_2d
from view_ppd_control import ScreenViewPpd


class ScreenPpd(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_janela_ppd()
        self.ui.setupUi(self)

        self.screen_view_ppd = ScreenViewPpd()

        self.ui.label_erro_2d_ppd_one.hide()
        self.ui.label_erro_2dN_ppd.hide()
        self.ui.groupBox_theta.setEnabled(False)

        self.ui.lineEdit_2D_ppd_one.setValidator(QIntValidator(1, 9999))
        self.ui.lineEdit_ppd_n_img.setValidator(QIntValidator(1, 9999))

        self.__checked_dims()
        self.ui.radioButton_ppd_2d.clicked.connect(self.__checked_dims)
        self.ui.radioButton_3d_ppd.clicked.connect(self.__checked_dims)
        self.ui.radioButton_ppd_n_imgs.clicked.connect(self.__checked_dims)
        self.ui.radioButton_ppd_one_image.clicked.connect(self.__checked_dims)

        self.ui.btn_run_ppd.clicked.connect(lambda: self.run_ppd(Functions.view.copy()))

        self.ui.btn_ppd_view.clicked.connect(self._show_view_ppd)

    @QtCore.pyqtSlot()
    def __checked_dims(self):
        dim = ''
        self.ui.label_erro_2dN_ppd.hide()
        self.ui.label_erro_2d_ppd_one.hide()
        self.screen_view_ppd.label_img_view.clear()
        self.screen_view_ppd.label_name_view.clear()

        if self.ui.radioButton_ppd_2d.isChecked():
            self.ui.radioButton_ppd_n_imgs.setEnabled(True)
            self.ui.radioButton_ppd_one_image.setEnabled(True)
            if self.ui.radioButton_ppd_one_image.isChecked():
                self.ui.lineEdit_ppd_n_img.clear()
                self.ui.lineEdit_2D_ppd_one.setEnabled(True)
                self.ui.lineEdit_ppd_n_img.setEnabled(False)
                Functions.enable_color(self.ui.lineEdit_2D_ppd_one)
                Functions.disable_color(self.ui.lineEdit_ppd_n_img, [150, 150, 150])
            elif self.ui.radioButton_ppd_n_imgs.isChecked():
                self.ui.lineEdit_2D_ppd_one.clear()
                self.ui.lineEdit_2D_ppd_one.setEnabled(False)
                self.ui.lineEdit_ppd_n_img.setEnabled(True)
                Functions.enable_color(self.ui.lineEdit_ppd_n_img)
                Functions.disable_color(self.ui.lineEdit_2D_ppd_one, [150, 150, 150])
            self.ui.groupBox_theta.setEnabled(False)

            dim = '2D'

        elif self.ui.radioButton_3d_ppd.isChecked():
            self.ui.lineEdit_2D_ppd_one.setEnabled(False)
            self.ui.lineEdit_ppd_n_img.setEnabled(False)
            self.ui.radioButton_ppd_n_imgs.setEnabled(False)
            self.ui.radioButton_ppd_one_image.setEnabled(False)
            Functions.disable_color(self.ui.lineEdit_2D_ppd_one, [150, 150, 150])
            Functions.disable_color(self.ui.lineEdit_ppd_n_img, [150, 150, 150])
            self.ui.groupBox_theta.setEnabled(True)
            self.ui.label_erro_2d_ppd_one.hide()
            self.ui.label_erro_2dN_ppd.hide()
            self.ui.lineEdit_2D_ppd_one.clear()
            self.ui.lineEdit_ppd_n_img.clear()
            dim = '3D'

        return dim

    @QtCore.pyqtSlot()
    def run_ppd(self, A):
        try:
            dim = self.__checked_dims()
            if self.ui.radioButton_pores.isChecked():
                pores = True
            else:
                pores = False

            if self.ui.radioButton_phi_48.isChecked():
                phi = 48
            elif self.ui.radioButton_phi_96.isChecked():
                phi = 96
            elif self.ui.radioButton_phi_192.isChecked():
                phi = 192

            if self.ui.radioButton_theta_24.isChecked():
                theta = 24
            elif self.ui.radioButton_theta_48.isChecked():
                theta = 48
            elif self.ui.radioButton_theta_96.isChecked():
                theta = 96

            if dim == '2D':

                I = Functions.run_2d(self.ui.radioButton_ppd_one_image, self.ui.radioButton_ppd_n_imgs,
                                     self.ui.lineEdit_2D_ppd_one, self.ui.lineEdit_ppd_n_img, A)

                answer = self.__reply_save()

                Functions.op_ppd = '2D'
                Functions.voxels_list_PPD, Functions.info_PPD_all, Functions.info_PPD_2D = main_ppd_2d(I, pores, phi, answer)
            elif dim == '3D':

                answer = self.__reply_save()

                Functions.ind_img = 0
                Functions.op_ppd = '3D'
                Functions.voxels_list_PPD, Functions.info_PPD_all = main_ppd_3d(A, pores, phi, theta, answer)

        except ValueError:
            if self.ui.radioButton_ppd_2d.isChecked():
                self.ui.label_erro_2d_ppd_one.show()
                self.ui.label_erro_2dN_ppd.hide()
            if self.ui.radioButton_ppd_n_imgs.isChecked():
                self.ui.label_erro_2dN_ppd.show()
                self.ui.label_erro_2d_ppd_one.hide()
        except IndexError:
            Functions.msgbox(f'Invalid Value.\nThe value must be between 1 and {len(Functions.view)}',
                             'Invalid ', 'Interval Error', 'warning')
            self.ui.lineEdit_2D_ppd_one.clear()
            self.ui.lineEdit_ppd_n_img.clear()

    @QtCore.pyqtSlot()
    def _show_view_ppd(self):
        if Functions.voxels_list_PPD:
            if self.ui.radioButton_ppd_2d.isChecked():
                if self.ui.radioButton_ppd_one_image.isChecked():
                    self.screen_view_ppd.show()
                    self.screen_view_ppd.options_2d()
                    self.screen_view_ppd.resize_label_image(450, 450)
                    self.screen_view_ppd.move_label_image(160, 150)
                    self.screen_view_ppd.move_label_name(150, 100)
                    self.screen_view_ppd.btn_left.hide()
                    self.screen_view_ppd.btn_right.hide()
                    self.screen_view_ppd.slider.hide()
                    self.screen_view_ppd.lineEdit_view.hide()

                elif self.ui.radioButton_ppd_n_imgs.isChecked():
                    self.screen_view_ppd.show()
                    self.screen_view_ppd.btn_left.show()
                    self.screen_view_ppd.btn_right.show()
                    self.screen_view_ppd.slider.show()
                    self.screen_view_ppd.lineEdit_view.show()
                    self.screen_view_ppd.options_3d()

                self.screen_view_ppd.PPD = '2D'
            elif self.ui.radioButton_3d_ppd.isChecked():
                self.screen_view_ppd.show()
                self.screen_view_ppd.options_3d()
                self.screen_view_ppd.PPD = '3D'

        else:
            Functions.msgbox('You must run PPD before.', 'Warning', 'warning')

    def __reply_save(self):
        answer = Functions.question_save(self, 'Save or Not',
                                         'Do you want to save while running? (recommended)')

        if answer == QMessageBox.Yes:
            answer = True
        else:
            answer = False

        return answer