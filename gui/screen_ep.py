# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_ep.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_janela_ep(object):
    def setupUi(self, janela_ep):
        janela_ep.setObjectName("janela_ep")
        janela_ep.resize(598, 440)
        janela_ep.setMinimumSize(QtCore.QSize(598, 440))
        janela_ep.setMaximumSize(QtCore.QSize(598, 440))
        janela_ep.setSizeIncrement(QtCore.QSize(340, 282))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/ppd_enhanced_colors_supreme-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        janela_ep.setWindowIcon(icon)
        janela_ep.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(janela_ep)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_run_ep = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run_ep.setGeometry(QtCore.QRect(173, 376, 100, 40))
        self.btn_run_ep.setStyleSheet("QPushButton{\n"
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
"")
        self.btn_run_ep.setObjectName("btn_run_ep")
        self.btn_ep_view = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ep_view.setGeometry(QtCore.QRect(331, 376, 100, 40))
        self.btn_ep_view.setStyleSheet("QPushButton{\n"
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
"}\n"
"")
        self.btn_ep_view.setObjectName("btn_ep_view")
        self.groupBox_pore = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_pore.setGeometry(QtCore.QRect(12, 22, 575, 80))
        self.groupBox_pore.setTitle("")
        self.groupBox_pore.setObjectName("groupBox_pore")
        self.radioButton_grains_ep = QtWidgets.QRadioButton(self.groupBox_pore)
        self.radioButton_grains_ep.setGeometry(QtCore.QRect(262, 28, 82, 17))
        self.radioButton_grains_ep.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_grains_ep.setObjectName("radioButton_grains_ep")
        self.radioButton_pore_ep = QtWidgets.QRadioButton(self.groupBox_pore)
        self.radioButton_pore_ep.setGeometry(QtCore.QRect(29, 32, 82, 17))
        self.radioButton_pore_ep.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_pore_ep.setChecked(True)
        self.radioButton_pore_ep.setObjectName("radioButton_pore_ep")
        self.groupBox_dimen = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_dimen.setGeometry(QtCore.QRect(12, 113, 575, 142))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox_dimen.setFont(font)
        self.groupBox_dimen.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_dimen.setObjectName("groupBox_dimen")
        self.frame = QtWidgets.QFrame(self.groupBox_dimen)
        self.frame.setGeometry(QtCore.QRect(21, 59, 333, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_erro_2dN_ep_ = QtWidgets.QLabel(self.frame)
        self.label_erro_2dN_ep_.setGeometry(QtCore.QRect(204, 45, 139, 20))
        self.label_erro_2dN_ep_.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 9pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.label_erro_2dN_ep_.setObjectName("label_erro_2dN_ep_")
        self.lineEdit_ep_n_img = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_ep_n_img.setEnabled(False)
        self.lineEdit_ep_n_img.setGeometry(QtCore.QRect(130, 42, 57, 28))
        self.lineEdit_ep_n_img.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Verdana\";\n"
"border:1px solid rgb(150, 150, 150);\n"
"")
        self.lineEdit_ep_n_img.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ep_n_img.setObjectName("lineEdit_ep_n_img")
        self.label_erro_2d_ep = QtWidgets.QLabel(self.frame)
        self.label_erro_2d_ep.setGeometry(QtCore.QRect(204, 7, 120, 20))
        self.label_erro_2d_ep.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 9pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.label_erro_2d_ep.setObjectName("label_erro_2d_ep")
        self.lineEdit_2D_ep_one = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2D_ep_one.setEnabled(True)
        self.lineEdit_2D_ep_one.setGeometry(QtCore.QRect(130, 3, 57, 28))
        self.lineEdit_2D_ep_one.setMinimumSize(QtCore.QSize(57, 28))
        self.lineEdit_2D_ep_one.setMaximumSize(QtCore.QSize(57, 28))
        self.lineEdit_2D_ep_one.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Verdana\";\n"
"border:1px solid rgb(150, 150, 150);\n"
"")
        self.lineEdit_2D_ep_one.setInputMask("")
        self.lineEdit_2D_ep_one.setMaxLength(4)
        self.lineEdit_2D_ep_one.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2D_ep_one.setCursorPosition(0)
        self.lineEdit_2D_ep_one.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2D_ep_one.setDragEnabled(False)
        self.lineEdit_2D_ep_one.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_2D_ep_one.setObjectName("lineEdit_2D_ep_one")
        self.radioButton_one_image = QtWidgets.QRadioButton(self.frame)
        self.radioButton_one_image.setGeometry(QtCore.QRect(6, 6, 121, 23))
        self.radioButton_one_image.setChecked(True)
        self.radioButton_one_image.setObjectName("radioButton_one_image")
        self.radioButton_n_imgs = QtWidgets.QRadioButton(self.frame)
        self.radioButton_n_imgs.setGeometry(QtCore.QRect(6, 43, 123, 22))
        self.radioButton_n_imgs.setObjectName("radioButton_n_imgs")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_dimen)
        self.frame_2.setGeometry(QtCore.QRect(21, 16, 349, 39))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton_ep_2d = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_ep_2d.setGeometry(QtCore.QRect(6, 8, 60, 30))
        self.radioButton_ep_2d.setMinimumSize(QtCore.QSize(60, 30))
        self.radioButton_ep_2d.setMaximumSize(QtCore.QSize(60, 30))
        self.radioButton_ep_2d.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_ep_2d.setChecked(True)
        self.radioButton_ep_2d.setObjectName("radioButton_ep_2d")
        self.radioButton_3d_ep = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3d_ep.setGeometry(QtCore.QRect(240, 8, 60, 30))
        self.radioButton_3d_ep.setMinimumSize(QtCore.QSize(60, 30))
        self.radioButton_3d_ep.setMaximumSize(QtCore.QSize(60, 40))
        self.radioButton_3d_ep.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_3d_ep.setObjectName("radioButton_3d_ep")
        self.frame_2.raise_()
        self.frame.raise_()
        self.groupBox_ngb = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ngb.setGeometry(QtCore.QRect(12, 267, 575, 86))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox_ngb.setFont(font)
        self.groupBox_ngb.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_ngb.setObjectName("groupBox_ngb")
        self.radioButton_N_26 = QtWidgets.QRadioButton(self.groupBox_ngb)
        self.radioButton_N_26.setGeometry(QtCore.QRect(355, 36, 73, 17))
        self.radioButton_N_26.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.radioButton_N_26.setObjectName("radioButton_N_26")
        self.radioButton_N_6 = QtWidgets.QRadioButton(self.groupBox_ngb)
        self.radioButton_N_6.setGeometry(QtCore.QRect(29, 36, 63, 17))
        self.radioButton_N_6.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.radioButton_N_6.setChecked(True)
        self.radioButton_N_6.setObjectName("radioButton_N_6")
        self.radioButton_N_18 = QtWidgets.QRadioButton(self.groupBox_ngb)
        self.radioButton_N_18.setGeometry(QtCore.QRect(189, 36, 61, 17))
        self.radioButton_N_18.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.radioButton_N_18.setObjectName("radioButton_N_18")
        janela_ep.setCentralWidget(self.centralwidget)

        self.retranslateUi(janela_ep)
        QtCore.QMetaObject.connectSlotsByName(janela_ep)
        janela_ep.setTabOrder(self.radioButton_ep_2d, self.lineEdit_2D_ep_one)
        janela_ep.setTabOrder(self.lineEdit_2D_ep_one, self.radioButton_3d_ep)
        janela_ep.setTabOrder(self.radioButton_3d_ep, self.btn_run_ep)

    def retranslateUi(self, janela_ep):
        _translate = QtCore.QCoreApplication.translate
        janela_ep.setWindowTitle(_translate("janela_ep", "Effective Pores"))
        self.btn_run_ep.setText(_translate("janela_ep", "RUN"))
        self.btn_ep_view.setText(_translate("janela_ep", "VIEW"))
        self.radioButton_grains_ep.setText(_translate("janela_ep", "Grains"))
        self.radioButton_pore_ep.setText(_translate("janela_ep", "Pores"))
        self.groupBox_dimen.setTitle(_translate("janela_ep", "Dimension"))
        self.label_erro_2dN_ep_.setText(_translate("janela_ep", "Enter the quantity"))
        self.label_erro_2d_ep.setText(_translate("janela_ep", "Enter the index"))
        self.radioButton_one_image.setText(_translate("janela_ep", "Single Image"))
        self.radioButton_n_imgs.setText(_translate("janela_ep", "N Images"))
        self.radioButton_ep_2d.setText(_translate("janela_ep", "2D"))
        self.radioButton_3d_ep.setText(_translate("janela_ep", "3D"))
        self.groupBox_ngb.setTitle(_translate("janela_ep", "Neighbors"))
        self.radioButton_N_26.setText(_translate("janela_ep", "26"))
        self.radioButton_N_6.setText(_translate("janela_ep", "6"))
        self.radioButton_N_18.setText(_translate("janela_ep", "18"))
