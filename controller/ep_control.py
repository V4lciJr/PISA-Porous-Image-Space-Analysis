from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore
from util.static_functions import *
from util.ep import EP_2D, EP_3D
from gui.screen_ep import Ui_janela_ep
from view_ep_control import ScreenViewEp


class ScreenEp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_janela_ep()
        self.ui.setupUi(self)
        self.screen_view_ep = ScreenViewEp()

        self.ui.radioButton_ep_2d.setChecked(True)
        self.ui.lineEdit_2D_ep_one.setValidator(QIntValidator(1, 9999))
        self.ui.lineEdit_ep_n_img.setValidator(QIntValidator(1, 9999))

        self.__checked_dims()
        self.ui.label_erro_2d_ep.hide()
        self.ui.label_erro_2dN_ep_.hide()

        self.ui.radioButton_ep_2d.clicked.connect(self.__checked_dims)
        self.ui.radioButton_3d_ep.clicked.connect(self.__checked_dims)
        self.ui.radioButton_one_image.clicked.connect(self.__checked_dims)
        self.ui.radioButton_n_imgs.clicked.connect(self.__checked_dims)

        self.ui.btn_run_ep.clicked.connect(lambda: self.run_ep(Functions.view.copy()))
        self.ui.btn_ep_view.clicked.connect(self._show_view_ep)

    @QtCore.pyqtSlot()
    def __checked_dims(self):
        dim = ''
        self.ui.label_erro_2dN_ep_.hide()
        self.ui.label_erro_2d_ep.hide()
        self.screen_view_ep.label_image_ep_view.clear()
        self.screen_view_ep.label_name_view.clear()

        if self.ui.radioButton_ep_2d.isChecked():
            self.ui.radioButton_one_image.setEnabled(True)
            self.ui.radioButton_n_imgs.setEnabled(True)

            if self.ui.radioButton_one_image.isChecked():
                self.ui.lineEdit_2D_ep_one.setEnabled(True)
                self.ui.lineEdit_ep_n_img.setEnabled(False)
                self.ui.groupBox_ngb.setEnabled(False)
                self.ui.lineEdit_ep_n_img.clear()
                Functions.enable_color(self.ui.lineEdit_2D_ep_one)
                Functions.disable_color(self.ui.lineEdit_ep_n_img, [150, 150, 150])
            elif self.ui.radioButton_n_imgs.isChecked():
                self.ui.lineEdit_2D_ep_one.setEnabled(False)
                self.ui.lineEdit_ep_n_img.setEnabled(True)
                self.ui.groupBox_ngb.setEnabled(False)
                self.ui.lineEdit_2D_ep_one.clear()
                Functions.enable_color(self.ui.lineEdit_ep_n_img)
                Functions.disable_color(self.ui.lineEdit_2D_ep_one, [150, 150, 150])

            dim = '2D'

        elif self.ui.radioButton_3d_ep.isChecked():
            self.ui.lineEdit_2D_ep_one.setEnabled(False)
            self.ui.lineEdit_ep_n_img.setEnabled(False)
            self.ui.radioButton_one_image.setEnabled(False)
            self.ui.radioButton_n_imgs.setEnabled(False)
            self.ui.groupBox_ngb.setEnabled(True)
            Functions.disable_color(self.ui.lineEdit_2D_ep_one, [150, 150, 150])
            Functions.disable_color(self.ui.lineEdit_ep_n_img, [150, 150, 150])
            self.ui.label_erro_2d_ep.hide()
            self.ui.lineEdit_ep_n_img.clear()
            self.ui.lineEdit_2D_ep_one.clear()
            dim = '3D'

        return dim

    @QtCore.pyqtSlot()
    def run_ep(self, A):
        try:
            dim = self.__checked_dims()
            qt_ngh = 0
            if self.ui.radioButton_pore_ep.isChecked():
                pores = True
            else:
                pores = False

            if self.ui.radioButton_N_6.isChecked():
                qt_ngh = 6
            elif self.ui.radioButton_N_18.isChecked():
                qt_ngh = 18
            elif self.ui.radioButton_N_26.isChecked():
                qt_ngh = 26

            if dim == '2D':
                I = Functions.run_2d(self.ui.radioButton_one_image, self.ui.radioButton_n_imgs,
                                     self.ui.lineEdit_2D_ep_one, self.ui.lineEdit_ep_n_img, A)

                answer = self.__reply_save()

                Functions.EP, Functions.voxels = EP_2D.run(I, pores, answer)
                Functions.op_ep = '2D'

            elif dim == '3D':

                answer = self.__reply_save()

                Functions.EP, Functions.voxels = EP_3D.run(A, pores, qt_ngh, answer)
                Functions.op_ep = '3D'
                Functions.ind_img = 0
        except ValueError:
            if self.ui.radioButton_ep_2d.isChecked():
                self.ui.label_erro_2d_ep.show()
                self.ui.label_erro_2dN_ep_.hide()
            if self.ui.radioButton_n_imgs.isChecked():
                self.ui.label_erro_2dN_ep_.show()
                self.ui.label_erro_2d_ep.hide()
        except IndexError:
            Functions.msgbox(f'Invalid range.\nThe value must be between 1 and {len(Functions.view)}',
                             'Invalid ', 'Interval error', 'warning')
            self.ui.lineEdit_2D_ep_one.clear()
            self.ui.lineEdit_ep_n_img.clear()

    @QtCore.pyqtSlot()
    def close_screen(self):
        self.close()

    @QtCore.pyqtSlot()
    def _show_view_ep(self):

        # if Functions.EP:
        if self.ui.radioButton_ep_2d.isChecked():
            if self.ui.radioButton_one_image.isChecked():
                self.screen_view_ep.show()
                self.screen_view_ep.options_2d()
                self.screen_view_ep.resize_label_image(400, 400)
                self.screen_view_ep.move_label_image(180, 150)
                self.screen_view_ep.move_label_name(150, 100)
                Functions.pos_processing_all_ep()
                Functions.show_image(self.screen_view_ep.label_image_ep_view, Functions.EP)
                Functions.name_img(self.screen_view_ep.label_name_view)
            elif self.ui.radioButton_n_imgs.isChecked():
                self.screen_view_ep.show()
                self.screen_view_ep.options_3d()
        elif self.ui.radioButton_3d_ep.isChecked():
            self.screen_view_ep.show()
            self.screen_view_ep.options_3d()
            self.screen_view_ep.label_qtd_effective.setText(f'Total Effective Pores: {len(Functions.voxels)}')

    @QtCore.pyqtSlot()
    def __reply_save(self):
        answer = Functions.question_save(self, 'Save or Not',
                                         'Do you want to save while running?(not recommended)')

        if answer == QMessageBox.Yes:
            answer = True
        else:
            answer = False

        return answer

    # else:
    #     Functions.msgbox('You must run EP before.', 'Warning', 'warning')




    # Faces:
    # (x + 1, y, z);
    # (x - 1, y, z);
    # (x, y + 1, z);
    # (x, y - 1, z);
    # (x, y, z + 1);
    # (x, y, z - 1)

    # Arestas:
    # (x + 1, y + 1, z);
    # (x + 1, y - 1, z);
    # (x + 1, y, z + 1);
    # (x + 1, y, z - 1);
    # (x - 1, y + 1, z);
    # (x - 1, y - 1, z);
    # (x - 1, y, z + 1);
    # (x - 1, y, z - 1);
    # (x, y + 1, z + 1);
    # (x, y + 1, z - 1);
    # (x, y - 1, z + 1);
    # (x, y - 1, z - 1)

