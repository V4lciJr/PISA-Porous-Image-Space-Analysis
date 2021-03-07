# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_ppd.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janela_ppd(object):
    def setupUi(self, janela_ppd):
        janela_ppd.setObjectName("janela_ppd")
        janela_ppd.resize(620, 550)
        janela_ppd.setMinimumSize(QtCore.QSize(620, 550))
        janela_ppd.setMaximumSize(QtCore.QSize(620, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/ppd_enhanced_colors_supreme-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janela_ppd.setWindowIcon(icon)
        janela_ppd.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(janela_ppd)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_pores = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_pores.setGeometry(QtCore.QRect(23, 19, 577, 65))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox_pores.setFont(font)
        self.groupBox_pores.setTitle("")
        self.groupBox_pores.setObjectName("groupBox_pores")
        self.radioButton_pores = QtWidgets.QRadioButton(self.groupBox_pores)
        self.radioButton_pores.setGeometry(QtCore.QRect(26, 23, 82, 17))
        self.radioButton_pores.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_pores.setChecked(True)
        self.radioButton_pores.setObjectName("radioButton_pores")
        self.radioButton_grains = QtWidgets.QRadioButton(self.groupBox_pores)
        self.radioButton_grains.setGeometry(QtCore.QRect(260, 23, 82, 17))
        self.radioButton_grains.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_grains.setObjectName("radioButton_grains")
        self.groupBox_dimension = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_dimension.setGeometry(QtCore.QRect(23, 96, 577, 153))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox_dimension.setFont(font)
        self.groupBox_dimension.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_dimension.setObjectName("groupBox_dimension")
        self.frame = QtWidgets.QFrame(self.groupBox_dimension)
        self.frame.setGeometry(QtCore.QRect(17, 55, 356, 87))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_erro_2dN_ppd = QtWidgets.QLabel(self.frame)
        self.label_erro_2dN_ppd.setGeometry(QtCore.QRect(210, 50, 139, 20))
        self.label_erro_2dN_ppd.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 9pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.label_erro_2dN_ppd.setObjectName("label_erro_2dN_ppd")
        self.radioButton_ppd_n_imgs = QtWidgets.QRadioButton(self.frame)
        self.radioButton_ppd_n_imgs.setGeometry(QtCore.QRect(6, 48, 112, 22))
        self.radioButton_ppd_n_imgs.setObjectName("radioButton_ppd_n_imgs")
        self.lineEdit_2D_ppd_one = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2D_ppd_one.setEnabled(True)
        self.lineEdit_2D_ppd_one.setGeometry(QtCore.QRect(140, 8, 57, 28))
        self.lineEdit_2D_ppd_one.setMinimumSize(QtCore.QSize(57, 28))
        self.lineEdit_2D_ppd_one.setMaximumSize(QtCore.QSize(57, 28))
        self.lineEdit_2D_ppd_one.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Verdana\";\n"
"border:1px solid rgb(150, 150, 150);\n"
"")
        self.lineEdit_2D_ppd_one.setInputMask("")
        self.lineEdit_2D_ppd_one.setMaxLength(4)
        self.lineEdit_2D_ppd_one.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2D_ppd_one.setCursorPosition(0)
        self.lineEdit_2D_ppd_one.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2D_ppd_one.setDragEnabled(False)
        self.lineEdit_2D_ppd_one.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_2D_ppd_one.setObjectName("lineEdit_2D_ppd_one")
        self.lineEdit_ppd_n_img = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_ppd_n_img.setEnabled(False)
        self.lineEdit_ppd_n_img.setGeometry(QtCore.QRect(140, 47, 57, 28))
        self.lineEdit_ppd_n_img.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Verdana\";\n"
"border:1px solid rgb(150, 150, 150);\n"
"")
        self.lineEdit_ppd_n_img.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ppd_n_img.setObjectName("lineEdit_ppd_n_img")
        self.radioButton_ppd_one_image = QtWidgets.QRadioButton(self.frame)
        self.radioButton_ppd_one_image.setGeometry(QtCore.QRect(6, 11, 126, 23))
        self.radioButton_ppd_one_image.setChecked(True)
        self.radioButton_ppd_one_image.setObjectName("radioButton_ppd_one_image")
        self.label_erro_2d_ppd_one = QtWidgets.QLabel(self.frame)
        self.label_erro_2d_ppd_one.setGeometry(QtCore.QRect(210, 12, 120, 20))
        self.label_erro_2d_ppd_one.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 9pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.label_erro_2d_ppd_one.setObjectName("label_erro_2d_ppd_one")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_dimension)
        self.frame_2.setGeometry(QtCore.QRect(17, 14, 361, 37))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton_3d_ppd = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3d_ppd.setGeometry(QtCore.QRect(241, 5, 60, 30))
        self.radioButton_3d_ppd.setMaximumSize(QtCore.QSize(60, 30))
        self.radioButton_3d_ppd.setSizeIncrement(QtCore.QSize(60, 30))
        self.radioButton_3d_ppd.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_3d_ppd.setObjectName("radioButton_3d_ppd")
        self.radioButton_ppd_2d = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_ppd_2d.setGeometry(QtCore.QRect(6, 5, 60, 30))
        self.radioButton_ppd_2d.setMinimumSize(QtCore.QSize(60, 30))
        self.radioButton_ppd_2d.setMaximumSize(QtCore.QSize(60, 30))
        self.radioButton_ppd_2d.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_ppd_2d.setChecked(True)
        self.radioButton_ppd_2d.setObjectName("radioButton_ppd_2d")
        self.frame_2.raise_()
        self.frame.raise_()
        self.btn_ppd_view = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ppd_view.setGeometry(QtCore.QRect(330, 483, 100, 40))
        self.btn_ppd_view.setStyleSheet("QPushButton{\n"
"    font: 75 11pt \"Verdana\";\n"
"    color: rgb(255, 255, 255);\n"
"    border:1px solid rgb(0, 0, 0, 60);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 60));\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(0, 85, 255);\n"
"}")
        self.btn_ppd_view.setObjectName("btn_ppd_view")
        self.btn_run_ppd = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run_ppd.setEnabled(True)
        self.btn_run_ppd.setGeometry(QtCore.QRect(185, 483, 100, 40))
        self.btn_run_ppd.setStyleSheet("QPushButton{\n"
"    font: 75 11pt \"Verdana\";\n"
"    color: rgb(0, 255, 0);\n"
"    border:1px solid rgb(0, 0, 0, 60);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 60));\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(0, 152, 0);\n"
"}\n"
"\n"
"")
        self.btn_run_ppd.setObjectName("btn_run_ppd")
        self.groupBox_theta = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_theta.setGeometry(QtCore.QRect(20, 367, 577, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox_theta.setFont(font)
        self.groupBox_theta.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_theta.setObjectName("groupBox_theta")
        self.radioButton_theta_24 = QtWidgets.QRadioButton(self.groupBox_theta)
        self.radioButton_theta_24.setGeometry(QtCore.QRect(26, 35, 82, 17))
        self.radioButton_theta_24.setChecked(True)
        self.radioButton_theta_24.setObjectName("radioButton_theta_24")
        self.radioButton_theta_48 = QtWidgets.QRadioButton(self.groupBox_theta)
        self.radioButton_theta_48.setGeometry(QtCore.QRect(210, 35, 82, 17))
        self.radioButton_theta_48.setObjectName("radioButton_theta_48")
        self.radioButton_theta_96 = QtWidgets.QRadioButton(self.groupBox_theta)
        self.radioButton_theta_96.setGeometry(QtCore.QRect(390, 35, 82, 17))
        self.radioButton_theta_96.setObjectName("radioButton_theta_96")
        self.groupBox_phi = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_phi.setGeometry(QtCore.QRect(24, 268, 577, 80))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox_phi.setFont(font)
        self.groupBox_phi.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_phi.setObjectName("groupBox_phi")
        self.radioButton_phi_48 = QtWidgets.QRadioButton(self.groupBox_phi)
        self.radioButton_phi_48.setGeometry(QtCore.QRect(26, 35, 82, 17))
        self.radioButton_phi_48.setChecked(True)
        self.radioButton_phi_48.setObjectName("radioButton_phi_48")
        self.radioButton_phi_96 = QtWidgets.QRadioButton(self.groupBox_phi)
        self.radioButton_phi_96.setGeometry(QtCore.QRect(210, 35, 82, 17))
        self.radioButton_phi_96.setObjectName("radioButton_phi_96")
        self.radioButton_phi_192 = QtWidgets.QRadioButton(self.groupBox_phi)
        self.radioButton_phi_192.setGeometry(QtCore.QRect(390, 35, 82, 17))
        self.radioButton_phi_192.setObjectName("radioButton_phi_192")
        janela_ppd.setCentralWidget(self.centralwidget)

        self.retranslateUi(janela_ppd)
        QtCore.QMetaObject.connectSlotsByName(janela_ppd)
        janela_ppd.setTabOrder(self.radioButton_pores, self.radioButton_grains)
        janela_ppd.setTabOrder(self.radioButton_grains, self.radioButton_ppd_2d)
        janela_ppd.setTabOrder(self.radioButton_ppd_2d, self.radioButton_3d_ppd)
        janela_ppd.setTabOrder(self.radioButton_3d_ppd, self.btn_run_ppd)

    def retranslateUi(self, janela_ppd):
        _translate = QtCore.QCoreApplication.translate
        janela_ppd.setWindowTitle(_translate("janela_ppd", "Predominant  Pore Directions"))
        self.radioButton_pores.setText(_translate("janela_ppd", "Pores"))
        self.radioButton_grains.setText(_translate("janela_ppd", "Grains"))
        self.groupBox_dimension.setTitle(_translate("janela_ppd", "Dimension"))
        self.label_erro_2dN_ppd.setText(_translate("janela_ppd", "Enter the quantity"))
        self.radioButton_ppd_n_imgs.setText(_translate("janela_ppd", "N Images"))
        self.radioButton_ppd_one_image.setText(_translate("janela_ppd", "Single Image"))
        self.label_erro_2d_ppd_one.setText(_translate("janela_ppd", "Enter the index"))
        self.radioButton_3d_ppd.setText(_translate("janela_ppd", "3D"))
        self.radioButton_ppd_2d.setText(_translate("janela_ppd", "2D"))
        self.btn_ppd_view.setText(_translate("janela_ppd", "VIEW"))
        self.btn_run_ppd.setText(_translate("janela_ppd", "RUN"))
        self.groupBox_theta.setTitle(_translate("janela_ppd", "Number of Theta Rays"))
        self.radioButton_theta_24.setText(_translate("janela_ppd", "24"))
        self.radioButton_theta_48.setText(_translate("janela_ppd", "48"))
        self.radioButton_theta_96.setText(_translate("janela_ppd", "96"))
        self.groupBox_phi.setTitle(_translate("janela_ppd", "Number of Phi Rays"))
        self.radioButton_phi_48.setText(_translate("janela_ppd", "48"))
        self.radioButton_phi_96.setText(_translate("janela_ppd", "96"))
        self.radioButton_phi_192.setText(_translate("janela_ppd", "192"))
