# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ppd_visualizacao.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 700)
        Form.setMinimumSize(QtCore.QSize(750, 700))
        Form.setMaximumSize(QtCore.QSize(750, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/ppd_enhanced_colors_supreme-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.groupBox_opt_ppd = QtWidgets.QGroupBox(Form)
        self.groupBox_opt_ppd.setGeometry(QtCore.QRect(48, 15, 662, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.groupBox_opt_ppd.setFont(font)
        self.groupBox_opt_ppd.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_opt_ppd.setObjectName("groupBox_opt_ppd")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_opt_ppd)
        self.horizontalLayout.setContentsMargins(50, 0, 0, 7)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_all_directions = QtWidgets.QRadioButton(self.groupBox_opt_ppd)
        self.radioButton_all_directions.setStyleSheet("border:transparent;")
        self.radioButton_all_directions.setChecked(True)
        self.radioButton_all_directions.setObjectName("radioButton_all_directions")
        self.horizontalLayout.addWidget(self.radioButton_all_directions)
        self.radioButton_horizontal = QtWidgets.QRadioButton(self.groupBox_opt_ppd)
        self.radioButton_horizontal.setStyleSheet("border:transparent;")
        self.radioButton_horizontal.setObjectName("radioButton_horizontal")
        self.horizontalLayout.addWidget(self.radioButton_horizontal)
        self.radioButton_vertical = QtWidgets.QRadioButton(self.groupBox_opt_ppd)
        self.radioButton_vertical.setObjectName("radioButton_vertical")
        self.horizontalLayout.addWidget(self.radioButton_vertical)
        self.radioButton_diagonal = QtWidgets.QRadioButton(self.groupBox_opt_ppd)
        self.radioButton_diagonal.setObjectName("radioButton_diagonal")
        self.horizontalLayout.addWidget(self.radioButton_diagonal)
        self.horizontalSlider_ppd_view = QtWidgets.QSlider(Form)
        self.horizontalSlider_ppd_view.setEnabled(False)
        self.horizontalSlider_ppd_view.setGeometry(QtCore.QRect(233, 586, 295, 22))
        self.horizontalSlider_ppd_view.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_ppd_view.setObjectName("horizontalSlider_ppd_view")
        self.groupBox_perspect_ppd = QtWidgets.QGroupBox(Form)
        self.groupBox_perspect_ppd.setGeometry(QtCore.QRect(48, 84, 662, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox_perspect_ppd.setFont(font)
        self.groupBox_perspect_ppd.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_perspect_ppd.setObjectName("groupBox_perspect_ppd")
        self.radioButton_2d_perspect_ppd = QtWidgets.QRadioButton(self.groupBox_perspect_ppd)
        self.radioButton_2d_perspect_ppd.setGeometry(QtCore.QRect(189, 28, 82, 17))
        self.radioButton_2d_perspect_ppd.setObjectName("radioButton_2d_perspect_ppd")
        self.radioButton_3d_perspect_ppd = QtWidgets.QRadioButton(self.groupBox_perspect_ppd)
        self.radioButton_3d_perspect_ppd.setGeometry(QtCore.QRect(405, 28, 82, 17))
        self.radioButton_3d_perspect_ppd.setObjectName("radioButton_3d_perspect_ppd")
        self.label_ppd_view = QtWidgets.QLabel(Form)
        self.label_ppd_view.setGeometry(QtCore.QRect(233, 242, 295, 271))
        self.label_ppd_view.setStyleSheet("border:2px solid rgb(160, 160, 160);")
        self.label_ppd_view.setText("")
        self.label_ppd_view.setScaledContents(True)
        self.label_ppd_view.setObjectName("label_ppd_view")
        self.label_ppd_view_name = QtWidgets.QLabel(Form)
        self.label_ppd_view_name.setGeometry(QtCore.QRect(159, 200, 443, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.label_ppd_view_name.setFont(font)
        self.label_ppd_view_name.setText("")
        self.label_ppd_view_name.setScaledContents(False)
        self.label_ppd_view_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ppd_view_name.setObjectName("label_ppd_view_name")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(48, 155, 662, 522))
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
        self.lineEdit_ppd_view = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ppd_view.setEnabled(False)
        self.lineEdit_ppd_view.setGeometry(QtCore.QRect(303, 378, 58, 42))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_ppd_view.setFont(font)
        self.lineEdit_ppd_view.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_ppd_view.setObjectName("lineEdit_ppd_view")
        self.btn_ok_ppd_view = QtWidgets.QPushButton(Form)
        self.btn_ok_ppd_view.setGeometry(QtCore.QRect(353, 617, 54, 40))
        self.btn_ok_ppd_view.setStyleSheet("QPushButton{\n"
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
        self.btn_ok_ppd_view.setObjectName("btn_ok_ppd_view")
        self.groupBox.raise_()
        self.groupBox_opt_ppd.raise_()
        self.horizontalSlider_ppd_view.raise_()
        self.groupBox_perspect_ppd.raise_()
        self.label_ppd_view.raise_()
        self.label_ppd_view_name.raise_()
        self.btn_ok_ppd_view.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PPD View"))
        self.groupBox_opt_ppd.setTitle(_translate("Form", "Options"))
        self.radioButton_all_directions.setText(_translate("Form", "All Directions"))
        self.radioButton_horizontal.setText(_translate("Form", "Horizontal"))
        self.radioButton_vertical.setText(_translate("Form", "Vertical"))
        self.radioButton_diagonal.setText(_translate("Form", "Diagonal"))
        self.groupBox_perspect_ppd.setTitle(_translate("Form", "Perspective"))
        self.radioButton_2d_perspect_ppd.setText(_translate("Form", "2D"))
        self.radioButton_3d_perspect_ppd.setText(_translate("Form", "3D"))
        self.lineEdit_ppd_view.setPlaceholderText(_translate("Form", "1"))
        self.btn_ok_ppd_view.setText(_translate("Form", "OK"))
