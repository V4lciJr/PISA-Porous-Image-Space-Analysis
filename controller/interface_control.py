import sys
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIntValidator
from PyQt5 import QtTest
from gui.main_screen import *
from ppd_control import ScreenPpd
from controller.ep_control import ScreenEp
from controller.info_control import ScreenInfo
from controller.binarize_control import ScreenBinary
from controller.export_control import ScreenExport
from util.static_functions import Functions, Progress
from os import scandir, mkdir, path
from numpy import array
from PIL import Image, UnidentifiedImageError
import ctypes


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__pause = False

        self.progress = Progress()
        self.screen_ep = ScreenEp()
        self.screen_ppd = ScreenPpd()
        self.screen_info = ScreenInfo()
        self.screen_export = ScreenExport()

        self.ui.lineEdit_quantity.setValidator(QIntValidator(0, 9999))
        self.ui.pushButton_pause.hide()

        self.__all_setEnable(False)
        self.ui.pushButton_play.setEnabled(False)

        self.ui.pushButton_save.clicked.connect(self.__export)
        self.ui.pushButton_open.clicked.connect(self.__get_folder)
        self.ui.actionOpen.triggered.connect(self.__get_folder)
        self.ui.actionQuit.triggered.connect(self.__quit_aplication)

        self.ui.pushButton_ep.clicked.connect(self.__show_ep)
        self.ui.pushButton_infomation.clicked.connect(self.__show_info)

        self.ui.pushButton_seta_direita.clicked.connect(self.__show_img_right)
        self.ui.pushButton_seta_esquerda.clicked.connect(self.__show_img_left)

        self.ui.pushButton_pause.clicked.connect(self.__pauseButton)
        self.ui.pushButton_play.clicked.connect(self.__play)

        self.ui.lineEdit_quantity.returnPressed.connect(self.__get_ind_image)

        self.ui.pushButton_ppd.clicked.connect(self.__show_ppd)

        self.ui.pushButton_binary.clicked.connect(self.__show_binary)

        self.ui.pushButton_2d_view.clicked.connect(self.__function_2d_view)
        self.ui.pushButton_3d_view.clicked.connect(self.__function_3d_view)

    @property
    def ind_image(self):
        return self.__ind_image

    @QtCore.pyqtSlot()
    def __show_ep(self):
        self.screen_ep.show()
        self.screen_ppd.hide()
        self.screen_info.hide()

    @QtCore.pyqtSlot()
    def __show_ppd(self):
        self.screen_ppd.show()
        self.screen_ep.hide()
        self.screen_info.hide()
        self.screen_binary.hide()

    @QtCore.pyqtSlot()
    def __show_info(self):
        self.screen_info.show()
        self.screen_info.clear_lide_edit()
        self.screen_ppd.hide()
        self.screen_ep.hide()
        self.screen_binary.hide()

    @QtCore.pyqtSlot()
    def __show_binary(self):
        Functions.label_interface = self.ui.label_image
        self.screen_info.hide()
        self.screen_info.clear_lide_edit()
        self.screen_ppd.hide()
        self.screen_ep.hide()
        self.screen_binary.show()
        self.screen_binary.show_image_binary(Functions.view[0])

    @QtCore.pyqtSlot()
    def __get_folder(self):
        directory = QFileDialog()

        try:

            self.__open_close_screens()

            Functions.path = directory.getExistingDirectory(self, 'Select Directory', 'C:\\Users\\Download\\')

            paath = list(scandir(Functions.path))

            Functions.folders = []
            Functions.view = []
            Functions.EP = []
            Functions.PPD = []
            Functions.voxels = []
            Functions.colors_ep = []
            Functions.ind_img = 0

            for folder in paath:
                Functions.folders.append(folder.path)

            self.progress.set_min_max(1, len(Functions.folders))
            self.progress.set_title('Loading Images...')

            del paath

            for i in range(len(Functions.folders)):
                QApplication.processEvents()
                self.progress.set_value(i + 1)
                Functions.view.append(array(Image.open(Functions.folders[i])))

            Functions.view = (array(Functions.view) / 255).astype('float16')

            Functions.show_image(self.ui.label_image, Functions.view)
            self.ui.lineEdit_quantity.setText(str(Functions.ind_img + 1))
            self.__name_img()
            self.progress.close()
            self.__function_2d_view()
            self.__disable_pause()
            self.__all_setEnable(True)
            self.screen_binary = ScreenBinary()

        except FileNotFoundError:
            pass
        except PermissionError:
            self.progress.close()
            Functions.msgbox('Your folder must contain only images', ' ', 'warning', 'ok')
        except UnidentifiedImageError:
            self.progress.close()
            Functions.msgbox('Your folder must contain only images', ' ', 'warning', 'ok')
        except ValueError:
            self.progress.close()
            Functions.msgbox('All images must have the same dimension', ' ', 'warning', 'ok')

    @QtCore.pyqtSlot()
    def __show_img_right(self):
        Functions.ind_img += 1
        if Functions.ind_img > len(Functions.view) - 1:
            Functions.ind_img = 0

        Functions.show_image(self.ui.label_image, Functions.view)
        self.ui.lineEdit_quantity.setText(str(Functions.ind_img + 1))
        self.__name_img()

    @QtCore.pyqtSlot()
    def __show_img_left(self):
        Functions.ind_img -= 1
        if Functions.ind_img < 0:
            Functions.ind_img = len(Functions.view) - 1

        Functions.show_image(self.ui.label_image, Functions.view)
        self.ui.lineEdit_quantity.setText(str(Functions.ind_img + 1))
        self.__name_img()

    @QtCore.pyqtSlot()
    def __disable_pause(self):
        self.ui.pushButton_pause.setEnabled(False)
        self.ui.pushButton_seta_esquerda.setEnabled(True)
        self.ui.pushButton_seta_direita.setEnabled(True)
        self.ui.lineEdit_quantity.setEnabled(True)
        self.ui.pushButton_play.setEnabled(True)

    @QtCore.pyqtSlot()
    def __all_setEnable(self, op):
        self.ui.pushButton_save.setEnabled(op)
        self.ui.pushButton_ep.setEnabled(op)
        self.ui.pushButton_ppd.setEnabled(op)
        self.ui.pushButton_infomation.setEnabled(op)
        self.ui.pushButton_binary.setEnabled(op)
        self.ui.pushButton_seta_esquerda.setEnabled(op)
        self.ui.pushButton_seta_direita.setEnabled(op)
        self.ui.lineEdit_quantity.setEnabled(op)
        self.ui.pushButton_3d_view.setEnabled(op)
        self.ui.pushButton_2d_view.setEnabled(op)

    @QtCore.pyqtSlot()
    def __enable_pause(self):
        self.ui.pushButton_pause.setEnabled(True)
        self.ui.pushButton_seta_esquerda.setEnabled(False)
        self.ui.pushButton_seta_direita.setEnabled(False)
        self.ui.lineEdit_quantity.setEnabled(False)
        self.ui.pushButton_play.setEnabled(False)

    @QtCore.pyqtSlot()
    def __play(self):
        self.__enable_pause()
        self.__all_setEnable(False)
        self.__set_enable_open_about(False)
        self.__pause = False
        self.ui.pushButton_pause.show()
        self.ui.pushButton_play.hide()

        while self.__ind_image < len(Functions.folders):
            Functions.show_image(self.ui.label_image, Functions.view)
            self.ui.lineEdit_quantity.setText(str(Functions.ind_img + 1))
            self.__name_img()
            QtTest.QTest.qWait(1500)
            Functions.ind_img += 1
            if self.__pause:
                self.__disable_pause()
                break
            if Functions.ind_img == len(Functions.folders):
                Functions.ind_img = 0

    @QtCore.pyqtSlot()
    def __pauseButton(self):
        if self.ui.pushButton_pause.clicked:
            self.ui.pushButton_pause.hide()
            self.ui.pushButton_play.show()
            self.__pause = True

        self.__all_setEnable(True)
        self.__disable_pause()
        self.__set_enable_open_about(True)

    @QtCore.pyqtSlot()
    def __get_ind_image(self):

        if self.ui.lineEdit_quantity.text() == '':
            Functions.msgbox('Enter the number of the image', 'Invalid value', 'warning', 'ok')
            self.ui.lineEdit_quantity.setText(str(Functions.ind_img + 1))
        elif int(self.ui.lineEdit_quantity.text()) < 1 or int(self.ui.lineEdit_quantity.text()) > len(Functions.view):
            Functions.msgbox(f'Enter Between 1 and {len(Functions.view)}', 'Invalid Value', 'warning', 'ok')
            self.ui.lineEdit_quantity.setText(str(Functions.ind_img + 1))
        else:
            Functions.ind_img = int(self.ui.lineEdit_quantity.text()) - 1
            Functions.show_image(self.ui.label_image, Functions.view)
            self.__name_img()

    @QtCore.pyqtSlot()
    def __function_2d_view(self):
        self.ui.frame_setas.show()
        self.ui.label_image.show()
        self.ui.label_name_image.show()
        self.ui.frame_playPause.show()
        self.ui.frame_image.show()

    @QtCore.pyqtSlot()
    def __function_3d_view(self):
        self.ui.frame_setas.hide()
        self.ui.label_image.hide()
        self.ui.label_name_image.hide()
        self.ui.frame_playPause.hide()
        self.ui.frame_image.show()

    @QtCore.pyqtSlot()
    def __set_enable_open_about(self, op):
        self.ui.menuFile.setEnabled(op)
        self.ui.menuAbout.setEnabled(op)
        self.ui.menuHelp.setEnabled(op)
        self.ui.pushButton_open.setEnabled(op)

    @QtCore.pyqtSlot()
    def __name_img(self):
        Functions.name_image = Functions.folders[Functions.ind_img].split('/')
        Functions.name_image = Functions.name_image[len(Functions.name_image) - 1].split('\\')
        Functions.name_image = Functions.name_image[len(Functions.name_image) - 1].split('.')
        self.ui.label_name_image.setText(Functions.name_image[0])
        self.ui.label_quantity_images.setText(
            f'Dimension: {str(len(Functions.view[0]))} x {str(len(Functions.view[0][0]))} x'
            f' {str(len(Functions.view))}')

    @QtCore.pyqtSlot()
    def __quit_aplication(self):
        msg = QMessageBox.question(self, 'Save or Quit',
                                   'Are you sure you want to close the application without saving?',
                                   QMessageBox.Yes | QMessageBox.No)

        if msg == QMessageBox.Yes:
            QApplication.instance().quit()
        else:
            pass

    @QtCore.pyqtSlot()
    def __open_close_screens(self):
        self.screen_ep.close()
        self.screen_info.close()
        self.screen_ep.close()

    @QtCore.pyqtSlot()
    def __show_aux(self):
        Functions.ind_img = 0
        self.ui.lineEdit_quantity.setText('1')
        self.__name_img()
        Functions.show_image(self.ui.label_image, Functions.view)
        self.__function_2d_view()

    @QtCore.pyqtSlot()
    def __export(self):
        self.screen_export.lineEdit_save.setText(Functions.path)
        self.screen_export.show()

    @QtCore.pyqtSlot()
    def __save_images(self, paath, direction):
        if not path.exists(paath + '\\' + direction):
            mkdir(paath + '\\' + direction)
        for k in range(len(Functions.view)):
            self.__ind_image = k
            self.__name_img()
            img = Image.fromarray((Functions.view[k] * 255).astype('uint8'))
            img.save(paath + '\\' + direction + '\\' + Functions.name_image[0] + '.tif')


# Set the exception hook to our wrapping function
sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    w = MainWindow()
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    largura, altura = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    left = (largura - w.width()) // 2
    top = (altura - w.height()) // 2
    w.left = left
    w.top = top
    w.move(left, top)
    w.show()
    sys.excepthook = my_exception_hook
    sys.exit(app.exec_())
