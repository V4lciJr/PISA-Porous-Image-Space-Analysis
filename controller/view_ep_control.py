from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtCore
from gui.screen_ep_view import Ui_Form_ep_view
from util.static_functions import Functions


class ScreenViewEp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_ep_view()
        self.ui.setupUi(self)

        self.ui.lineEdit_effective_pore.setValidator(QIntValidator(1, 9999))
        self.ui.radioButton_effective_pore.clicked.connect(lambda: self.ui.lineEdit_effective_pore.setEnabled(True))
        self.ui.radioButton_all_effective_pores.clicked.connect(
            lambda: self.ui.lineEdit_effective_pore.setEnabled(False))

        self.ui.lineEdit_effective_pore.returnPressed.connect(self.btn_ok_ep_view)

        self.ui.radioButton_all_effective_pores.setChecked(True)
        self.ui.btn_ok_ep_view.clicked.connect(self.btn_ok_ep_view)

        self.ui.pushButton_arrow_left.clicked.connect(lambda: Functions.show_img_left(self.ui.lineEdit_ep_view,
                                                                                      self.ui.label_ep_view,
                                                                                      self.ui.label_ep_view_name,
                                                                                      Functions.EP))

        self.ui.pushButton_arrow_right.clicked.connect(lambda: Functions.show_img_right(self.ui.lineEdit_ep_view,
                                                                                        self.ui.label_ep_view,
                                                                                        self.ui.label_ep_view_name,
                                                                                        Functions.EP))

        self.ui.lineEdit_ep_view.returnPressed.connect(lambda: Functions.get_ind_image(self.ui.lineEdit_ep_view,
                                                                                       self.ui.label_ep_view,
                                                                                       self.ui.label_ep_view_name,
                                                                                       Functions.EP))

        self.ui.horizontalSlider_ep_view.valueChanged.connect(lambda: Functions.set_value_slider(
                                                                                    self.ui.horizontalSlider_ep_view,
                                                                                    self.ui.lineEdit_ep_view,
                                                                                    self.ui.label_ep_view,
                                                                                    Functions.EP,
                                                                                    self.ui.label_ep_view_name))

    @property
    def label_image_ep_view(self):
        return self.ui.label_ep_view

    @property
    def label_name_view(self):
        return self.ui.label_ep_view_name

    @property
    def label_qtd_effective(self):
        return self.ui.label_qtd_effectives

    @QtCore.pyqtSlot()
    def options_2d(self):
        self.ui.groupBox_opt_ep.hide()
        self.ui.groupBox_perspect_ep.hide()
        self.ui.horizontalSlider_ep_view.hide()
        self.ui.groupBox.hide()
        self.ui.btn_ok_ep_view.hide()
        self.ui.label_ep_view_name.show()
        self.ui.label_ep_view.show()

    @QtCore.pyqtSlot()
    def options_3d(self):
        self.ui.groupBox_opt_ep.show()
        self.ui.groupBox_opt_ep.show()
        self.ui.groupBox.show()
        self.ui.groupBox_perspect_ep.show()
        self.ui.horizontalSlider_ep_view.show()
        self.ui.label_ep_view_name.show()
        self.ui.label_ep_view.show()
        self.ui.btn_ok_ep_view.show()
        self.ui.label_ep_view.setGeometry(QtCore.QRect(237, 240, 295, 271))
        self.ui.label_ep_view_name.setGeometry(QtCore.QRect(163, 200, 443, 20))

    @QtCore.pyqtSlot()
    def resize_label_image(self, width, heigth):
        self.ui.label_ep_view.resize(width, heigth)

    @QtCore.pyqtSlot()
    def move_label_image(self, x, y):
        self.ui.label_ep_view.move(x, y)

    @QtCore.pyqtSlot()
    def move_label_name(self, x, y):
        self.ui.label_ep_view_name.move(x, y)

    @QtCore.pyqtSlot()
    def btn_ok_ep_view(self):
        if self.ui.radioButton_all_effective_pores.isChecked():
            Functions.pos_processing_all_ep()
            Functions.show_image(self.label_image_ep_view, Functions.EP)
            Functions.name_img(self.ui.label_ep_view_name)
        if self.ui.radioButton_effective_pore.isChecked():
            try:
                Functions.pos_processing_one_ep_3d(int(self.ui.lineEdit_effective_pore.text()))
                Functions.show_image(self.label_image_ep_view, Functions.EP)
                Functions.name_img(self.ui.label_ep_view_name)
            except IndexError:
                Functions.msgbox(f'Enter between 1 and {len(Functions.voxels)}', 'Index Erro', 'Info', 'ok')

        Functions.enable_view(self.ui.pushButton_arrow_left, self.ui.pushButton_arrow_right, self.ui.lineEdit_ep_view,
                              self.ui.horizontalSlider_ep_view)
