from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from gui.screen_ppd_view import Ui_Form
from util.static_functions import Functions


class ScreenViewPpd(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.radioButton_2d_perspect_ppd.setChecked(True)
        self.ui.btn_ok_ppd_view.clicked.connect(self.btn_ok_ppd)
        self.ui.pushButton_arrow_left.clicked.connect(lambda: Functions.show_img_left(self.ui.lineEdit_ppd_view,
                                                                                      self.ui.label_ppd_view,
                                                                                      self.ui.label_ppd_view_name,
                                                                                      Functions.PPD))
        self.ui.pushButton_arrow_right.clicked.connect(lambda: Functions.show_img_right(self.ui.lineEdit_ppd_view,
                                                                                        self.ui.label_ppd_view,
                                                                                        self.ui.label_ppd_view_name,
                                                                                        Functions.PPD))

        self.ui.lineEdit_ppd_view.returnPressed.connect(lambda: Functions.get_ind_image(self.ui.lineEdit_ppd_view,
                                                                                        self.ui.label_ppd_view,
                                                                                        self.ui.label_ppd_view_name,
                                                                                        Functions.PPD))

        self.ui.horizontalSlider_ppd_view.valueChanged.connect(lambda: Functions.set_value_slider(
                                                                                    self.ui.horizontalSlider_ppd_view,
                                                                                    self.ui.lineEdit_ppd_view,
                                                                                    self.ui.label_ppd_view,
                                                                                    Functions.PPD,
                                                                                    self.ui.label_ppd_view_name))


    @property
    def label_img_view(self):
        return self.ui.label_ppd_view

    @property
    def label_name_view(self):
        return self.ui.label_ppd_view_name

    @property
    def btn_ok(self):
        return self.ui.btn_ok_ppd_view

    @property
    def btn_left(self):
        return self.ui.pushButton_arrow_left

    @property
    def btn_right(self):
        return self.ui.pushButton_arrow_right

    @property
    def slider(self):
        return self.ui.horizontalSlider_ppd_view

    @property
    def lineEdit_view(self):
        return self.ui.lineEdit_ppd_view

    @QtCore.pyqtSlot()
    def options_2d(self):
        self.ui.groupBox_perspect_ppd.hide()
        self.ui.horizontalSlider_ppd_view.hide()
        self.ui.groupBox.setGeometry(QtCore.QRect(48, 80, 662, 600))
        self.ui.btn_ok_ppd_view.setGeometry(QtCore.QRect(355, 620, 54, 40))
        self.ui.label_ppd_view_name.show()
        self.ui.label_ppd_view.show()

    @QtCore.pyqtSlot()
    def options_3d(self):
        self.ui.groupBox_opt_ppd.show()
        self.ui.groupBox_perspect_ppd.show()
        self.ui.horizontalSlider_ppd_view.show()
        self.ui.label_ppd_view_name.show()
        self.ui.label_ppd_view.show()
        self.ui.groupBox.show()
        self.ui.label_ppd_view.setGeometry(QtCore.QRect(237, 240, 295, 271))
        self.ui.label_ppd_view_name.setGeometry(QtCore.QRect(163, 200, 443, 20))

    @QtCore.pyqtSlot()
    def resize_label_image(self, width, heigth):
        self.ui.label_ppd_view.resize(width, heigth)

    @QtCore.pyqtSlot()
    def move_label_image(self, x, y):
        self.ui.label_ppd_view.move(x, y)

    @QtCore.pyqtSlot()
    def move_label_name(self, x, y):
        self.ui.label_ppd_view_name.move(x, y)

    @QtCore.pyqtSlot()
    def btn_ok_ppd(self):
        if self.ui.radioButton_all_directions.isChecked():
            Functions.pos_processing_ppd()
            Functions.show_image(self.ui.label_ppd_view, Functions.PPD)
            Functions.name_img(self.ui.label_ppd_view_name)
        elif self.ui.radioButton_horizontal.isChecked():
            Functions.pos_processing_ppd('h')
            Functions.show_image(self.ui.label_ppd_view, Functions.PPD)
            Functions.name_img(self.ui.label_ppd_view_name)
        elif self.ui.radioButton_vertical.isChecked():
            Functions.pos_processing_ppd('v')
            Functions.show_image(self.ui.label_ppd_view, Functions.PPD)
            Functions.name_img(self.ui.label_ppd_view_name)
        elif self.ui.radioButton_diagonal.isChecked():
            Functions.pos_processing_ppd('d')
            Functions.show_image(self.ui.label_ppd_view, Functions.PPD)
            Functions.name_img(self.ui.label_ppd_view_name)

        Functions.enable_view(self.ui.pushButton_arrow_right, self.ui.pushButton_arrow_left, self.ui.lineEdit_ppd_view,
                              self.ui.horizontalSlider_ppd_view)
