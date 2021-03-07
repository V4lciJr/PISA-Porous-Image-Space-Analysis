# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_screen_info(object):
    def setupUi(self, screen_info):
        screen_info.setObjectName("screen_info")
        screen_info.resize(545, 450)
        screen_info.setMinimumSize(QtCore.QSize(545, 450))
        screen_info.setMaximumSize(QtCore.QSize(545, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("FotoJet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        screen_info.setWindowIcon(icon)
        screen_info.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(160, 160, 160, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.centralwidget = QtWidgets.QWidget(screen_info)
        self.centralwidget.setObjectName("centralwidget")
        self.label_grais_pixels = QtWidgets.QLabel(self.centralwidget)
        self.label_grais_pixels.setGeometry(QtCore.QRect(15, 207, 205, 30))
        self.label_grais_pixels.setStyleSheet("background-color:transparent;\n"
"font: 75 11pt \"Verdana\";\n"
"color:rgb(0, 0, 0)")
        self.label_grais_pixels.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_grais_pixels.setObjectName("label_grais_pixels")
        self.label_number_pores_pixels = QtWidgets.QLabel(self.centralwidget)
        self.label_number_pores_pixels.setGeometry(QtCore.QRect(15, 258, 206, 30))
        self.label_number_pores_pixels.setStyleSheet("background-color:transparent;\n"
"font: 75 11pt \"Verdana\";\n"
"color:rgb(0, 0, 0)")
        self.label_number_pores_pixels.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_number_pores_pixels.setObjectName("label_number_pores_pixels")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(15, 306, 127, 30))
        self.label_3.setStyleSheet("background-color:transparent;\n"
"font: 75 11pt \"Verdana\";\n"
"color:rgb(0, 0, 0)")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2D_info = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2D_info.setEnabled(False)
        self.lineEdit_2D_info.setGeometry(QtCore.QRect(51, 68, 57, 28))
        self.lineEdit_2D_info.setMinimumSize(QtCore.QSize(57, 28))
        self.lineEdit_2D_info.setMaximumSize(QtCore.QSize(57, 28))
        self.lineEdit_2D_info.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Verdana\";\n"
"border:1px solid rgb(150, 150, 150);\n"
"")
        self.lineEdit_2D_info.setInputMask("")
        self.lineEdit_2D_info.setMaxLength(4)
        self.lineEdit_2D_info.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2D_info.setCursorPosition(0)
        self.lineEdit_2D_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2D_info.setDragEnabled(False)
        self.lineEdit_2D_info.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_2D_info.setObjectName("lineEdit_2D_info")
        self.radioButton_2d_sections_info = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2d_sections_info.setGeometry(QtCore.QRect(190, 40, 180, 30))
        self.radioButton_2d_sections_info.setMinimumSize(QtCore.QSize(180, 30))
        self.radioButton_2d_sections_info.setMaximumSize(QtCore.QSize(180, 30))
        self.radioButton_2d_sections_info.setSizeIncrement(QtCore.QSize(30, 30))
        self.radioButton_2d_sections_info.setBaseSize(QtCore.QSize(30, 30))
        self.radioButton_2d_sections_info.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.radioButton_2d_sections_info.setObjectName("radioButton_2d_sections_info")
        self.label_erro_2d_thin_info = QtWidgets.QLabel(self.centralwidget)
        self.label_erro_2d_thin_info.setGeometry(QtCore.QRect(211, 99, 121, 20))
        self.label_erro_2d_thin_info.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 9pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.label_erro_2d_thin_info.setObjectName("label_erro_2d_thin_info")
        self.lineEdit_range_left_info = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_range_left_info.setEnabled(False)
        self.lineEdit_range_left_info.setGeometry(QtCore.QRect(190, 68, 57, 28))
        self.lineEdit_range_left_info.setMinimumSize(QtCore.QSize(57, 28))
        self.lineEdit_range_left_info.setMaximumSize(QtCore.QSize(57, 28))
        self.lineEdit_range_left_info.setMouseTracking(True)
        self.lineEdit_range_left_info.setTabletTracking(False)
        self.lineEdit_range_left_info.setAcceptDrops(True)
        self.lineEdit_range_left_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_range_left_info.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 10pt \"Verdana\";\n"
"border:1px solid rgb(180, 180, 180);\n"
"")
        self.lineEdit_range_left_info.setInputMask("")
        self.lineEdit_range_left_info.setMaxLength(4)
        self.lineEdit_range_left_info.setCursorPosition(0)
        self.lineEdit_range_left_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_range_left_info.setObjectName("lineEdit_range_left_info")
        self.radioButton_info_2d = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_info_2d.setGeometry(QtCore.QRect(51, 40, 60, 30))
        self.radioButton_info_2d.setMinimumSize(QtCore.QSize(60, 30))
        self.radioButton_info_2d.setMaximumSize(QtCore.QSize(60, 30))
        self.radioButton_info_2d.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_info_2d.setObjectName("radioButton_info_2d")
        self.lineEdit_range_right_info = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_range_right_info.setEnabled(False)
        self.lineEdit_range_right_info.setGeometry(QtCore.QRect(274, 68, 57, 28))
        self.lineEdit_range_right_info.setMinimumSize(QtCore.QSize(57, 28))
        self.lineEdit_range_right_info.setMaximumSize(QtCore.QSize(57, 28))
        self.lineEdit_range_right_info.setMouseTracking(True)
        self.lineEdit_range_right_info.setTabletTracking(False)
        self.lineEdit_range_right_info.setAcceptDrops(True)
        self.lineEdit_range_right_info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_range_right_info.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 75 10pt \"Verdana\";\n"
"border:1px solid rgb(190, 190, 190);")
        self.lineEdit_range_right_info.setInputMask("")
        self.lineEdit_range_right_info.setMaxLength(4)
        self.lineEdit_range_right_info.setCursorPosition(0)
        self.lineEdit_range_right_info.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_range_right_info.setObjectName("lineEdit_range_right_info")
        self.radioButton_3d_info = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3d_info.setGeometry(QtCore.QRect(419, 40, 60, 30))
        self.radioButton_3d_info.setMinimumSize(QtCore.QSize(60, 30))
        self.radioButton_3d_info.setMaximumSize(QtCore.QSize(60, 40))
        self.radioButton_3d_info.setStyleSheet("font: 75 11pt \"Verdana\";\n"
"background-color:transparent;")
        self.radioButton_3d_info.setObjectName("radioButton_3d_info")
        self.label_erro_2d_info = QtWidgets.QLabel(self.centralwidget)
        self.label_erro_2d_info.setGeometry(QtCore.QRect(29, 99, 120, 20))
        self.label_erro_2d_info.setStyleSheet("color:rgb(255, 0, 0);\n"
"font: 9pt \"Verdana\";\n"
"background-color:transparent;\n"
"")
        self.label_erro_2d_info.setObjectName("label_erro_2d_info")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 68, 20, 28))
        self.label_4.setStyleSheet("background-color:transparent;\n"
"font: 75 14pt \"Verdana\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calculate.setGeometry(QtCore.QRect(215, 380, 110, 40))
        self.pushButton_calculate.setStyleSheet("QPushButton{\n"
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
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.lineEdit_grains = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_grains.setEnabled(False)
        self.lineEdit_grains.setGeometry(QtCore.QRect(222, 207, 216, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lineEdit_grains.setFont(font)
        self.lineEdit_grains.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.lineEdit_grains.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_grains.setObjectName("lineEdit_grains")
        self.lineEdit_pores = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pores.setEnabled(False)
        self.lineEdit_pores.setGeometry(QtCore.QRect(222, 258, 216, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lineEdit_pores.setFont(font)
        self.lineEdit_pores.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.lineEdit_pores.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pores.setObjectName("lineEdit_pores")
        self.lineEdit_porosity = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_porosity.setEnabled(False)
        self.lineEdit_porosity.setGeometry(QtCore.QRect(182, 306, 291, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lineEdit_porosity.setFont(font)
        self.lineEdit_porosity.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.lineEdit_porosity.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_porosity.setObjectName("lineEdit_porosity")
        self.lineEdit_percent_grains = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_percent_grains.setEnabled(False)
        self.lineEdit_percent_grains.setGeometry(QtCore.QRect(451, 207, 63, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lineEdit_percent_grains.setFont(font)
        self.lineEdit_percent_grains.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.lineEdit_percent_grains.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_percent_grains.setObjectName("lineEdit_percent_grains")
        self.lineEdit_percent_pores = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_percent_pores.setEnabled(False)
        self.lineEdit_percent_pores.setGeometry(QtCore.QRect(451, 258, 63, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lineEdit_percent_pores.setFont(font)
        self.lineEdit_percent_pores.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.lineEdit_percent_pores.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_percent_pores.setObjectName("lineEdit_percent_pores")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(520, 207, 19, 30))
        self.label_5.setStyleSheet("background-color:transparent;\n"
"font: 75 11pt \"Verdana\";\n"
"color:rgb(0, 0, 0)")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 258, 19, 30))
        self.label_7.setStyleSheet("background-color:transparent;\n"
"font: 75 11pt \"Verdana\";\n"
"color:rgb(0, 0, 0)")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_pixels = QtWidgets.QLabel(self.centralwidget)
        self.label_pixels.setGeometry(QtCore.QRect(15, 163, 193, 30))
        self.label_pixels.setStyleSheet("background-color:transparent;\n"
"font: 75 11pt \"Verdana\";\n"
"color:rgb(0, 0, 0)")
        self.label_pixels.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_pixels.setObjectName("label_pixels")
        self.lineEdit_pixels = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pixels.setEnabled(False)
        self.lineEdit_pixels.setGeometry(QtCore.QRect(222, 163, 216, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lineEdit_pixels.setFont(font)
        self.lineEdit_pixels.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.lineEdit_pixels.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_pixels.setObjectName("lineEdit_pixels")
        screen_info.setCentralWidget(self.centralwidget)

        self.retranslateUi(screen_info)
        QtCore.QMetaObject.connectSlotsByName(screen_info)

    def retranslateUi(self, screen_info):
        _translate = QtCore.QCoreApplication.translate
        screen_info.setWindowTitle(_translate("screen_info", "Image Information"))
        self.label_grais_pixels.setText(_translate("screen_info", "Number of Grains Pixels:"))
        self.label_number_pores_pixels.setText(_translate("screen_info", "Number of Pores Pixels:"))
        self.label_3.setText(_translate("screen_info", "Porosity: "))
        self.radioButton_2d_sections_info.setText(_translate("screen_info", "2D Thin Sections"))
        self.label_erro_2d_thin_info.setText(_translate("screen_info", "Enter the Range"))
        self.radioButton_info_2d.setText(_translate("screen_info", "2D"))
        self.radioButton_3d_info.setText(_translate("screen_info", "3D"))
        self.label_erro_2d_info.setText(_translate("screen_info", "Enter the image"))
        self.label_4.setText(_translate("screen_info", "-"))
        self.pushButton_calculate.setText(_translate("screen_info", "CALCULATE"))
        self.label_5.setText(_translate("screen_info", "%"))
        self.label_7.setText(_translate("screen_info", "%"))
        self.label_pixels.setText(_translate("screen_info", "Number of Voxels:"))
