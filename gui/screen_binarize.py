# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_binarizar.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_screen_binary(object):
    def setupUi(self, screen_binary):
        screen_binary.setObjectName("screen_binary")
        screen_binary.resize(750, 560)
        screen_binary.setMinimumSize(QtCore.QSize(750, 560))
        screen_binary.setMaximumSize(QtCore.QSize(750, 560))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/ppd_enhanced_colors_supreme-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        screen_binary.setWindowIcon(icon)
        screen_binary.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.label_binary = QtWidgets.QLabel(screen_binary)
        self.label_binary.setGeometry(QtCore.QRect(260, 127, 250, 250))
        self.label_binary.setMinimumSize(QtCore.QSize(250, 250))
        self.label_binary.setMaximumSize(QtCore.QSize(250, 250))
        self.label_binary.setStyleSheet("border:2px solid rgb(160, 160, 160);")
        self.label_binary.setText("")
        self.label_binary.setScaledContents(True)
        self.label_binary.setObjectName("label_binary")
        self.pushButton_view = QtWidgets.QPushButton(screen_binary)
        self.pushButton_view.setGeometry(QtCore.QRect(398, 490, 75, 36))
        self.pushButton_view.setStyleSheet("QPushButton{\n"
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
        self.pushButton_view.setObjectName("pushButton_view")
        self.pushButton_ok = QtWidgets.QPushButton(screen_binary)
        self.pushButton_ok.setGeometry(QtCore.QRect(304, 490, 75, 36))
        self.pushButton_ok.setStyleSheet("QPushButton{\n"
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
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalSlider_binary = QtWidgets.QSlider(screen_binary)
        self.horizontalSlider_binary.setGeometry(QtCore.QRect(225, 446, 320, 22))
        self.horizontalSlider_binary.setStyleSheet("border:transparent;")
        self.horizontalSlider_binary.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_binary.setObjectName("horizontalSlider_binary")
        self.lineEdit_binary = QtWidgets.QLineEdit(screen_binary)
        self.lineEdit_binary.setEnabled(True)
        self.lineEdit_binary.setGeometry(QtCore.QRect(355, 399, 61, 37))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.lineEdit_binary.setFont(font)
        self.lineEdit_binary.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_binary.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_binary.setObjectName("lineEdit_binary")
        self.groupBox = QtWidgets.QGroupBox(screen_binary)
        self.groupBox.setGeometry(QtCore.QRect(85, 13, 578, 73))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_white_back = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_white_back.setGeometry(QtCore.QRect(339, 22, 186, 37))
        self.radioButton_white_back.setStyleSheet("background:transparent;\n"
"font: 75 12pt \"Verdana\";\n"
"border:transparent;")
        self.radioButton_white_back.setObjectName("radioButton_white_back")
        self.radioButton_gray_level = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_gray_level.setGeometry(QtCore.QRect(62, 22, 134, 37))
        self.radioButton_gray_level.setStyleSheet("background:transparent;\n"
"font: 75 12pt \"Verdana\";\n"
"border:transparent;")
        self.radioButton_gray_level.setChecked(True)
        self.radioButton_gray_level.setObjectName("radioButton_gray_level")
        self.groupBox_2 = QtWidgets.QGroupBox(screen_binary)
        self.groupBox_2.setGeometry(QtCore.QRect(85, 99, 578, 446))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.raise_()
        self.label_binary.raise_()
        self.pushButton_view.raise_()
        self.pushButton_ok.raise_()
        self.horizontalSlider_binary.raise_()
        self.lineEdit_binary.raise_()
        self.groupBox.raise_()

        self.retranslateUi(screen_binary)
        QtCore.QMetaObject.connectSlotsByName(screen_binary)

    def retranslateUi(self, screen_binary):
        _translate = QtCore.QCoreApplication.translate
        screen_binary.setWindowTitle(_translate("screen_binary", "Binarize"))
        self.pushButton_view.setText(_translate("screen_binary", "View"))
        self.pushButton_ok.setText(_translate("screen_binary", "OK"))
        self.lineEdit_binary.setPlaceholderText(_translate("screen_binary", "1"))
        self.groupBox.setTitle(_translate("screen_binary", "Binarize Image From"))
        self.radioButton_white_back.setText(_translate("screen_binary", "White Background"))
        self.radioButton_gray_level.setText(_translate("screen_binary", "Gray Levels"))
