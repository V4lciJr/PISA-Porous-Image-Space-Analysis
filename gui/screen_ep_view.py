# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ep_visualização.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_ep_view(object):
    def setupUi(self, Form_ep_view):
        Form_ep_view.setObjectName("Form_ep_view")
        Form_ep_view.resize(750, 700)
        Form_ep_view.setMinimumSize(QtCore.QSize(750, 700))
        Form_ep_view.setMaximumSize(QtCore.QSize(750, 700))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        Form_ep_view.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/ppd_enhanced_colors_supreme-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_ep_view.setWindowIcon(icon)
        self.label_ep_view = QtWidgets.QLabel(Form_ep_view)
        self.label_ep_view.setGeometry(QtCore.QRect(233, 242, 295, 271))
        self.label_ep_view.setStyleSheet("border:2px solid rgb(160, 160, 160);")
        self.label_ep_view.setText("")
        self.label_ep_view.setScaledContents(True)
        self.label_ep_view.setObjectName("label_ep_view")
        self.horizontalSlider_ep_view = QtWidgets.QSlider(Form_ep_view)
        self.horizontalSlider_ep_view.setEnabled(False)
        self.horizontalSlider_ep_view.setGeometry(QtCore.QRect(233, 586, 295, 22))
        self.horizontalSlider_ep_view.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_ep_view.setObjectName("horizontalSlider_ep_view")
        self.label_ep_view_name = QtWidgets.QLabel(Form_ep_view)
        self.label_ep_view_name.setGeometry(QtCore.QRect(159, 200, 443, 20))
        self.label_ep_view_name.setText("")
        self.label_ep_view_name.setScaledContents(False)
        self.label_ep_view_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ep_view_name.setObjectName("label_ep_view_name")
        self.groupBox_opt_ep = QtWidgets.QGroupBox(Form_ep_view)
        self.groupBox_opt_ep.setGeometry(QtCore.QRect(44, 17, 662, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.groupBox_opt_ep.setFont(font)
        self.groupBox_opt_ep.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_opt_ep.setObjectName("groupBox_opt_ep")
        self.radioButton_all_effective_pores = QtWidgets.QRadioButton(self.groupBox_opt_ep)
        self.radioButton_all_effective_pores.setGeometry(QtCore.QRect(81, 22, 152, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_all_effective_pores.setFont(font)
        self.radioButton_all_effective_pores.setStyleSheet("border:transparent;")
        self.radioButton_all_effective_pores.setChecked(True)
        self.radioButton_all_effective_pores.setObjectName("radioButton_all_effective_pores")
        self.radioButton_effective_pore = QtWidgets.QRadioButton(self.groupBox_opt_ep)
        self.radioButton_effective_pore.setGeometry(QtCore.QRect(431, 22, 123, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_effective_pore.setFont(font)
        self.radioButton_effective_pore.setStyleSheet("border:transparent;")
        self.radioButton_effective_pore.setObjectName("radioButton_effective_pore")
        self.lineEdit_effective_pore = QtWidgets.QLineEdit(self.groupBox_opt_ep)
        self.lineEdit_effective_pore.setEnabled(False)
        self.lineEdit_effective_pore.setGeometry(QtCore.QRect(570, 16, 61, 30))
        self.lineEdit_effective_pore.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"")
        self.lineEdit_effective_pore.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_effective_pore.setObjectName("lineEdit_effective_pore")
        self.groupBox_perspect_ep = QtWidgets.QGroupBox(Form_ep_view)
        self.groupBox_perspect_ep.setGeometry(QtCore.QRect(44, 82, 662, 60))
        self.groupBox_perspect_ep.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_perspect_ep.setObjectName("groupBox_perspect_ep")
        self.radioButton_2d_perspect_ep = QtWidgets.QRadioButton(self.groupBox_perspect_ep)
        self.radioButton_2d_perspect_ep.setGeometry(QtCore.QRect(189, 28, 82, 17))
        self.radioButton_2d_perspect_ep.setChecked(True)
        self.radioButton_2d_perspect_ep.setObjectName("radioButton_2d_perspect_ep")
        self.radioButton_3D_perspect_ep = QtWidgets.QRadioButton(self.groupBox_perspect_ep)
        self.radioButton_3D_perspect_ep.setGeometry(QtCore.QRect(405, 28, 82, 17))
        self.radioButton_3D_perspect_ep.setObjectName("radioButton_3D_perspect_ep")
        self.btn_ok_ep_view = QtWidgets.QPushButton(Form_ep_view)
        self.btn_ok_ep_view.setGeometry(QtCore.QRect(353, 617, 54, 40))
        self.btn_ok_ep_view.setStyleSheet("QPushButton{\n"
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
        self.btn_ok_ep_view.setObjectName("btn_ok_ep_view")
        self.groupBox = QtWidgets.QGroupBox(Form_ep_view)
        self.groupBox.setGeometry(QtCore.QRect(44, 155, 662, 522))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_arrow_left = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_arrow_left.setEnabled(False)
        self.pushButton_arrow_left.setGeometry(QtCore.QRect(130, 420, 45, 46))
        self.pushButton_arrow_left.setStyleSheet("QPushButton{\n"
"    background-position:center-low;\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(0, 0, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(205, 239, 255);\n"
"}")
        self.pushButton_arrow_left.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/left_arrow (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_arrow_left.setIcon(icon1)
        self.pushButton_arrow_left.setIconSize(QtCore.QSize(45, 42))
        self.pushButton_arrow_left.setObjectName("pushButton_arrow_left")
        self.pushButton_arrow_right = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_arrow_right.setEnabled(False)
        self.pushButton_arrow_right.setGeometry(QtCore.QRect(496, 420, 45, 46))
        self.pushButton_arrow_right.setStyleSheet("QPushButton{\n"
"    background-position:center-low;\n"
"    background-color:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border:2px solid rgb(0, 0, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(205, 239, 255);\n"
"}")
        self.pushButton_arrow_right.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Icons/right_arrow (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_arrow_right.setIcon(icon2)
        self.pushButton_arrow_right.setIconSize(QtCore.QSize(45, 42))
        self.pushButton_arrow_right.setObjectName("pushButton_arrow_right")
        self.lineEdit_ep_view = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ep_view.setEnabled(False)
        self.lineEdit_ep_view.setGeometry(QtCore.QRect(307, 378, 58, 42))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_ep_view.setFont(font)
        self.lineEdit_ep_view.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ep_view.setObjectName("lineEdit_ep_view")
        self.label_qtd_effectives = QtWidgets.QLabel(Form_ep_view)
        self.label_qtd_effectives.setGeometry(QtCore.QRect(60, 163, 287, 22))
        self.label_qtd_effectives.setStyleSheet("color: rgb(0, 157, 76);")
        self.label_qtd_effectives.setText("")
        self.label_qtd_effectives.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_qtd_effectives.setObjectName("label_qtd_effectives")
        self.groupBox.raise_()
        self.label_ep_view.raise_()
        self.horizontalSlider_ep_view.raise_()
        self.label_ep_view_name.raise_()
        self.groupBox_opt_ep.raise_()
        self.groupBox_perspect_ep.raise_()
        self.btn_ok_ep_view.raise_()
        self.label_qtd_effectives.raise_()

        self.retranslateUi(Form_ep_view)
        QtCore.QMetaObject.connectSlotsByName(Form_ep_view)

    def retranslateUi(self, Form_ep_view):
        _translate = QtCore.QCoreApplication.translate
        Form_ep_view.setWindowTitle(_translate("Form_ep_view", "Effective Pores View"))
        self.groupBox_opt_ep.setTitle(_translate("Form_ep_view", "Options"))
        self.radioButton_all_effective_pores.setText(_translate("Form_ep_view", "All Effective Pores"))
        self.radioButton_effective_pore.setText(_translate("Form_ep_view", "Effective Pore"))
        self.lineEdit_effective_pore.setPlaceholderText(_translate("Form_ep_view", "1"))
        self.groupBox_perspect_ep.setTitle(_translate("Form_ep_view", "Perspective"))
        self.radioButton_2d_perspect_ep.setText(_translate("Form_ep_view", "2D"))
        self.radioButton_3D_perspect_ep.setText(_translate("Form_ep_view", "3D"))
        self.btn_ok_ep_view.setText(_translate("Form_ep_view", "OK"))
        self.lineEdit_ep_view.setPlaceholderText(_translate("Form_ep_view", "1"))
