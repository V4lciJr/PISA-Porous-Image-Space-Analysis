from PyQt5.QtWidgets import QMessageBox, QWidget, QApplication
from PyQt5.QtGui import QIcon, QPixmap, QImage
from gui.screen_progress import Ui_Form_progress
from numpy import ones, array
from numpy.random import rand
from PIL import Image


class Progress(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form_progress()
        self.ui.setupUi(self)

    def set_value(self, value):
        self.ui.progressBar.setValue(value)

    def set_min_max(self, min, max):
        self.ui.progressBar.setMinimum(min)
        self.ui.progressBar.setMaximum(max)
        self.show()

    def set_title(self, title):
        self.setWindowTitle(title)


class Functions:
    folders = []
    view = []
    PPD = []
    EP = []
    voxels = []
    info_PPD_all = []
    info_PPD_2D = []
    ind_img = 0
    op_ep = ''
    op_ppd = ''
    voxels_list_PPD = []
    name_image = ''
    label_interface = None
    path = ''

    @staticmethod
    def run(radio_2d, radio_3d, radio_2d_ts=None):
        if radio_2d[0].isChecked():
            if radio_2d[1].text() != '':
                radio_2d[2].hide()
            else:
                radio_2d_ts[3].hide()
                radio_2d[2].show()
        elif radio_2d_ts[0].isChecked():
            if radio_2d_ts[1].text() and radio_2d_ts[2].text() != '':
                radio_2d_ts[3].hide()
            else:
                radio_2d[2].hide()
                radio_2d_ts[3].show()
        elif radio_3d.isChecked():
            radio_2d[2].hide()
            radio_2d_ts[3].hide()

    @staticmethod
    def enable_color(nome):
        nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "font: 75 10pt \"Verdana\";\n"
                           "border:1px solid rgb(0, 0, 0);\n"
                           "")
        return nome

    @staticmethod
    def disable_color(line_edit, rgb):
        line_edit.setStyleSheet("background-color: transparent; color: rgb(0, 0, 0);\n"
                                "font: 75 10pt \"Verdana\";\n"
                                f"border:1px solid rgb({rgb[0]}, {rgb[1]}, {rgb[2]});\n"
                                "")
        return line_edit

    @staticmethod
    def msgbox(mesage, title, tp, confirm='ok'):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QIcon(QPixmap('../Icons/FotoJet.png')))
        msg.setText(mesage)
        if tp in 'Wwarning':
            msg.setIcon(QMessageBox.Warning)
        elif tp in 'Info':
            msg.setIcon(QMessageBox.Information)
        if confirm in 'ok':
            msg.setStandardButtons(QMessageBox.Ok)
        elif confirm in 'yes':
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        msg.exec()

    @staticmethod
    def pos_processing_all_ep():

        Functions.EP = ones((len(Functions.EP), len(Functions.EP[0]), len(Functions.EP[0][0]), 3), 'float16')
        progress = Progress()
        progress.set_min_max(1, len(Functions.voxels))
        progress.set_title('Loading...')
        for c in range(len(Functions.voxels)):
            QApplication.processEvents()
            progress.set_value(c)
            rgb = rand(3).astype('float16')
            if Functions.op_ep == '3D':
                for v in Functions.voxels[c]:
                    Functions.EP[v[2]][v[0]][v[1]][:] = rgb
            else:
                for v in Functions.voxels[c]:
                    Functions.EP[v[0]][v[1]][v[2]][:] = rgb
        progress.close()

    @staticmethod
    def pos_processing_one_ep_3d(ind):
        Functions.EP = ones((len(Functions.EP), len(Functions.EP[0]), len(Functions.EP[0][0]), 3), 'float16')
        rgb = rand(3).astype('float16')
        progress = Progress()
        progress.set_min_max(1, len(Functions.voxels))
        progress.set_title('Loading...')
        count = 0
        for v in Functions.voxels[ind - 1]:
            QApplication.processEvents()
            progress.set_value(count)
            count += 1
            Functions.EP[v[2]][v[0]][v[1]][:] = rgb

        progress.close()

    @staticmethod
    def pos_processing_ppd(op='all'):
        Functions.PPD = ones(
            (Functions.voxels_list_PPD[3], Functions.voxels_list_PPD[1], Functions.voxels_list_PPD[2], 3), 'float16')
        progress = Progress()
        progress.set_min_max(1, len(Functions.PPD))
        progress.set_title('Loading...')
        cont = 1
        for v in Functions.voxels_list_PPD[0]:
            if v[1] == 'h' and (op == 'all' or op == 'h'):
                Functions.PPD[v[0][0]][v[0][1]][v[0][2]] = [1, 0, 0]
            elif v[1] == 'd' and (op == 'all' or op == 'd'):
                Functions.PPD[v[0][0]][v[0][1]][v[0][2]] = [0, 1, 0]
            elif v[1] == 'v' and (op == 'all' or op == 'v'):
                Functions.PPD[v[0][0]][v[0][1]][v[0][2]] = [0, 0, 1]
            QApplication.processEvents()
            progress.set_value(cont)
            cont += 1
        progress.close()

    @staticmethod
    def show_image(label_image, A):

        if A.shape[0] > 1:
            im = Image.fromarray((A[Functions.ind_img] * 255).astype('uint8'))
        else:
            im = Image.fromarray((A[0] * 255).astype('uint8'))
        im = im.convert("RGBA")
        data = im.tobytes("raw", "RGBA")
        qim = QImage(data, im.size[0], im.size[1], QImage.Format_RGBA8888)

        label_image.setPixmap(QPixmap.fromImage(qim))

    @staticmethod
    def name_img(label_name_image):
        Functions.name_image = Functions.folders[Functions.ind_img].split('/')
        Functions.name_image = Functions.name_image[len(Functions.name_image) - 1].split('\\')
        Functions.name_image = Functions.name_image[len(Functions.name_image) - 1].split('.')
        label_name_image.setText(Functions.name_image[0])

    @staticmethod
    def run_2d(rb_one, rb_n, ln_one, ln_n, A):
        I = None
        if rb_one.isChecked():
            if int(ln_one.text()) <= 0:
                ln_one.clear()
                raise IndexError

            else:
                I = array([A[int(ln_one.text()) - 1]])
                Functions.ind_img = int(ln_one.text()) - 1
        elif rb_n.isChecked():
            if int(ln_n.text()) > len(A) or int(ln_n.text()) <= 0:
                ln_n.clear()
                raise IndexError
            else:
                I = A[0: int(ln_n.text())]
                Functions.ind_img = 0
        return I

    @staticmethod
    def show_img_right(lineEdit, label_image, label_name_img, A):
        Functions.ind_img += 1
        if Functions.ind_img > len(A) - 1:
            Functions.ind_img = 0

        Functions.show_image(label_image, A)
        lineEdit.setText(str(Functions.ind_img + 1))
        Functions.name_img(label_name_img)

    @staticmethod
    def show_img_left(lineEdit, label_image, label_name_img, A):
        Functions.ind_img -= 1
        if Functions.ind_img < 0:
            Functions.ind_img = len(A) - 1

        Functions.show_image(label_image, A)
        lineEdit.setText(str(Functions.ind_img + 1))
        Functions.name_img(label_name_img)

    @staticmethod
    def get_ind_image(lineEdit, label_image, label_name_img, A):

        try:

            if int(lineEdit.text()) < 1 or int(lineEdit.text()) > len(A):
                raise IndexError

            Functions.ind_img = int(lineEdit.text()) - 1
            Functions.show_image(label_image, A)
            Functions.name_img(label_name_img)
        except ValueError:
            Functions.msgbox('Enter the number of the image', 'Invalid value', 'warning', 'ok')
            lineEdit.setText(str(Functions.ind_img + 1))
        except IndexError:
            Functions.msgbox(f'Enter Between 1 and {len(A)}', 'Invalid Value', 'warning', 'ok')
            lineEdit.setText(str(Functions.ind_img + 1))

    @staticmethod
    def enable_view(btn_right, btn_left, lineEdit, slider):
        btn_right.setEnabled(True)
        btn_left.setEnabled(True)
        lineEdit.setEnabled(True)
        slider.setEnabled(True)

    @staticmethod
    def question_save(obj, title, msg):
        answer = QMessageBox.question(obj, title, msg, QMessageBox.Yes | QMessageBox.No)
        return answer

    @staticmethod
    def save_section(A, section, direction):
        name_image = Functions.folders[section].split('/')
        name_image = name_image[len(name_image) - 1].split('\\')
        name_image = name_image[len(name_image) - 1].split('.')[0]
        im = Image.fromarray((A * 255).astype('uint8'))
        im.save(Functions.path + '\\' + direction + '\\' + name_image + '.tif')

        return name_image

    @staticmethod
    def set_value_slider(slider, line_Edit, label_image, A, label_name=None):
        slider.setMinimum(1)
        slider.setMaximum(len(A))
        line_Edit.setText(str(slider.value()))
        Functions.ind_img = slider.value() - 1
        Functions.show_image(label_image, A)
        if label_name:
            Functions.name_img(label_name)

    @staticmethod
    def calc_time(time_exec):
        hours, r = divmod(time_exec, 3600)
        minutes, seconds = divmod(r, 60)
        if hours > 0:
            text = f'{hours:0>1} hours, {minutes:0>1} minutes and {seconds:05.3f} seconds'
        elif minutes > 0:
            text = f'{minutes:0>1} minutes and {seconds:05.3f} seconds'
        else:
            text = f'{seconds:05.3f} seconds'

        return text
