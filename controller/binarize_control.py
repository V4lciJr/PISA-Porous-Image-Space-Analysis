from gui.screen_binarize import Ui_screen_binary
from PyQt5.QtWidgets import QMainWindow, QApplication, QSlider
from PyQt5 import QtGui, QtCore
from numpy import zeros
from exceptions.exceptions import GrayLevelsError
from util.static_functions import Functions, Progress
from PIL import Image


class ScreenBinary(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_screen_binary()
        self.ui.setupUi(self)

        self.__op = ''

        self.ui.horizontalSlider_binary.setTickPosition(QSlider.TicksBelow)

        self.ui.pushButton_view.clicked.connect(self.__view_button)
        self.ui.pushButton_ok.clicked.connect(self.__btn_ok_binary)
        self.ui.radioButton_gray_level.clicked.connect(lambda: self.__enable_raddio(True))
        self.ui.radioButton_white_back.clicked.connect(lambda: self.__enable_raddio(False))
        self.ui.horizontalSlider_binary.valueChanged.connect(lambda: Functions.set_value_slider(
                                                                                        self.ui.horizontalSlider_binary,
                                                                                        self.ui.lineEdit_binary,
                                                                                        self.ui.label_binary,
                                                                                        Functions.view.copy))

    def getLabel(self):
        return self.ui.label_binary

    @QtCore.pyqtSlot()
    def __white_back(self, I):
        if len(I.shape) == 3:
            A = zeros((len(I), len(I[0])), 'uint8')
            A = I[:, :, 0] + I[:, :, 1] + I[:, :, 2]
            A[A == 3] = 0
            A[A > 0] = 1
            self.show_image_binary(A)
            return None
        else:
            progress = Progress()
            progress.set_min_max(1, len(I))
            progress.set_title('Binarizing')
            A = zeros((len(I), len(I[0]), len(I[0][0])), 'uint8')
            for k in range(len(I)):
                QApplication.processEvents()
                progress.set_value(k)
                A[k] = I[k, :, :, 0] + I[k, :, :, 1] + I[k, :, :, 2]
                A[k][A[k] == 3] = 0
                A[k][A[k] > 0] = 1
            progress.close()
            return A

    @QtCore.pyqtSlot()
    def __gray_levels(self, I):
        value = int(self.ui.lineEdit_binary.text()) / 255
        I[I < value] = 0
        I[I >= value] = 1
        if self.__op == 'view':
            if len(I.shape) == 2:
                self.show_image_binary(I)
            else:
                raise GrayLevelsError
        elif self.__op == 'ok':
            if len(I.shape) > 3:
                raise GrayLevelsError
        return I

    @QtCore.pyqtSlot()
    def show_image_binary(self, I):
        im = Image.fromarray((I * 255).astype('uint8'))
        im = im.convert("RGBA")
        data = im.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGBA8888)

        self.getLabel().setPixmap(QtGui.QPixmap(qim))

    @QtCore.pyqtSlot()
    def __view_button(self):
        try:
            self.__op = 'view'
            if self.ui.radioButton_white_back.isChecked():
                self.__white_back(Functions.view[0])
            elif self.ui.radioButton_gray_level.isChecked():
                _ = self.__gray_levels(Functions.view[0].copy())
        except GrayLevelsError:
            Functions.msgbox('Your Image must be in Gray Levels', ' ', 'warning', 'ok')
            self.ui.lineEdit_binary.clear()
        except ValueError:
            Functions.msgbox('You need to enter the threshold', ' ', 'warning', 'ok')

    @QtCore.pyqtSlot()
    def __btn_ok_binary(self):
        try:
            self.__op = 'ok'
            if self.ui.radioButton_white_back.isChecked():
                Functions.view = self.__white_back(Functions.view)
            elif self.ui.radioButton_gray_level.isChecked():
                Functions.view = self.__gray_levels(Functions.view.copy())
            Functions.show_image(Functions.label_interface, Functions.view)
            Functions.label_interface = None
            self.close()
        except GrayLevelsError:
            Functions.msgbox('Your Image must be in Gray Levels', ' ', 'warning', 'ok')
            self.ui.lineEdit_binary.clear()
        except ValueError:
            Functions.msgbox('You need to enter the threshold', ' ', 'warning', 'ok')

    @QtCore.pyqtSlot()
    def __enable_raddio(self, op):
        self.ui.horizontalSlider_binary.setEnabled(op)
        self.ui.lineEdit_binary.setEnabled(op)
        if op:
            self.ui.lineEdit_binary.setStyleSheet("background-color: rgb(255, 255, 255);")
        else:
            self.ui.lineEdit_binary.setStyleSheet("background-color: transparent;")


