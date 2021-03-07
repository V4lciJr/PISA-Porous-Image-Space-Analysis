# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_export.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_export(object):
    def setupUi(self, Form_export):
        Form_export.setObjectName("Form_export")
        Form_export.resize(730, 566)
        Form_export.setMinimumSize(QtCore.QSize(730, 566))
        Form_export.setMaximumSize(QtCore.QSize(730, 566))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        Form_export.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/ppd_enhanced_colors_supreme-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_export.setWindowIcon(icon)
        self.lineEdit_path_save = QtWidgets.QLineEdit(Form_export)
        self.lineEdit_path_save.setGeometry(QtCore.QRect(26, 36, 566, 27))
        self.lineEdit_path_save.setReadOnly(True)
        self.lineEdit_path_save.setObjectName("lineEdit_path_save")
        self.pushButton_export = QtWidgets.QPushButton(Form_export)
        self.pushButton_export.setGeometry(QtCore.QRect(611, 28, 47, 43))
        self.pushButton_export.setStyleSheet("QPushButton{\n"
"    border:transparent;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(226, 226, 226);\n"
"}\n"
"")
        self.pushButton_export.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/593eab2b18a32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_export.setIcon(icon1)
        self.pushButton_export.setIconSize(QtCore.QSize(60, 30))
        self.pushButton_export.setObjectName("pushButton_export")
        self.groupBox = QtWidgets.QGroupBox(Form_export)
        self.groupBox.setGeometry(QtCore.QRect(26, 90, 663, 200))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.checkBox_ppd_export = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_ppd_export.setGeometry(QtCore.QRect(19, 11, 83, 36))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.checkBox_ppd_export.setFont(font)
        self.checkBox_ppd_export.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_ppd_export.setAutoFillBackground(True)
        self.checkBox_ppd_export.setShortcut("")
        self.checkBox_ppd_export.setCheckable(True)
        self.checkBox_ppd_export.setTristate(False)
        self.checkBox_ppd_export.setObjectName("checkBox_ppd_export")
        self.checkBox_ep_export = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_ep_export.setGeometry(QtCore.QRect(19, 99, 70, 34))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.checkBox_ep_export.setFont(font)
        self.checkBox_ep_export.setObjectName("checkBox_ep_export")
        self.frame_ep = QtWidgets.QFrame(self.groupBox)
        self.frame_ep.setEnabled(False)
        self.frame_ep.setGeometry(QtCore.QRect(7, 128, 616, 56))
        self.frame_ep.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ep.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ep.setObjectName("frame_ep")
        self.radioButton_all_eff_export = QtWidgets.QRadioButton(self.frame_ep)
        self.radioButton_all_eff_export.setGeometry(QtCore.QRect(12, 13, 146, 27))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.radioButton_all_eff_export.setFont(font)
        self.radioButton_all_eff_export.setChecked(True)
        self.radioButton_all_eff_export.setObjectName("radioButton_all_eff_export")
        self.radioButton_effec_export = QtWidgets.QRadioButton(self.frame_ep)
        self.radioButton_effec_export.setGeometry(QtCore.QRect(362, 13, 110, 27))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.radioButton_effec_export.setFont(font)
        self.radioButton_effec_export.setObjectName("radioButton_effec_export")
        self.lineEdit_eff_export = QtWidgets.QLineEdit(self.frame_ep)
        self.lineEdit_eff_export.setEnabled(False)
        self.lineEdit_eff_export.setGeometry(QtCore.QRect(479, 13, 55, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.lineEdit_eff_export.setFont(font)
        self.lineEdit_eff_export.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_eff_export.setObjectName("lineEdit_eff_export")
        self.frame_ppd = QtWidgets.QFrame(self.groupBox)
        self.frame_ppd.setEnabled(False)
        self.frame_ppd.setGeometry(QtCore.QRect(16, 47, 644, 42))
        self.frame_ppd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ppd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ppd.setObjectName("frame_ppd")
        self.radioButton_all = QtWidgets.QRadioButton(self.frame_ppd)
        self.radioButton_all.setGeometry(QtCore.QRect(3, 15, 82, 17))
        self.radioButton_all.setChecked(True)
        self.radioButton_all.setObjectName("radioButton_all")
        self.radioButton_all_directions = QtWidgets.QRadioButton(self.frame_ppd)
        self.radioButton_all_directions.setGeometry(QtCore.QRect(103, 15, 140, 17))
        self.radioButton_all_directions.setObjectName("radioButton_all_directions")
        self.radioButton_horizontal = QtWidgets.QRadioButton(self.frame_ppd)
        self.radioButton_horizontal.setGeometry(QtCore.QRect(262, 15, 102, 17))
        self.radioButton_horizontal.setObjectName("radioButton_horizontal")
        self.radioButton_vertical = QtWidgets.QRadioButton(self.frame_ppd)
        self.radioButton_vertical.setGeometry(QtCore.QRect(409, 15, 82, 17))
        self.radioButton_vertical.setObjectName("radioButton_vertical")
        self.radioButton_diagonal = QtWidgets.QRadioButton(self.frame_ppd)
        self.radioButton_diagonal.setGeometry(QtCore.QRect(518, 15, 121, 21))
        self.radioButton_diagonal.setObjectName("radioButton_diagonal")
        self.label_total_effect = QtWidgets.QLabel(self.groupBox)
        self.label_total_effect.setGeometry(QtCore.QRect(119, 106, 307, 20))
        self.label_total_effect.setStyleSheet("color:rgb(0, 170, 0);\n"
"font: 11pt \"Verdana\";")
        self.label_total_effect.setText("")
        self.label_total_effect.setObjectName("label_total_effect")
        self.groupBox_2 = QtWidgets.QGroupBox(Form_export)
        self.groupBox_2.setGeometry(QtCore.QRect(26, 310, 665, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_tiff_export = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_tiff_export.setGeometry(QtCore.QRect(23, 23, 82, 27))
        self.radioButton_tiff_export.setChecked(True)
        self.radioButton_tiff_export.setObjectName("radioButton_tiff_export")
        self.radioButton_jpg_export = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_jpg_export.setGeometry(QtCore.QRect(196, 23, 82, 27))
        self.radioButton_jpg_export.setObjectName("radioButton_jpg_export")
        self.radioButton_png_export = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_png_export.setGeometry(QtCore.QRect(372, 23, 82, 27))
        self.radioButton_png_export.setObjectName("radioButton_png_export")
        self.groupBox_3 = QtWidgets.QGroupBox(Form_export)
        self.groupBox_3.setGeometry(QtCore.QRect(26, 390, 669, 65))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_txt_export = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_txt_export.setGeometry(QtCore.QRect(20, 25, 82, 27))
        self.radioButton_txt_export.setChecked(True)
        self.radioButton_txt_export.setObjectName("radioButton_txt_export")
        self.radioButton_xls_export = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_xls_export.setGeometry(QtCore.QRect(196, 25, 82, 27))
        self.radioButton_xls_export.setObjectName("radioButton_xls_export")
        self.radioButton_csv = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_csv.setGeometry(QtCore.QRect(372, 25, 82, 27))
        self.radioButton_csv.setObjectName("radioButton_csv")
        self.pushButton_ok_export = QtWidgets.QPushButton(Form_export)
        self.pushButton_ok_export.setGeometry(QtCore.QRect(302, 490, 110, 43))
        self.pushButton_ok_export.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_ok_export.setObjectName("pushButton_ok_export")

        self.retranslateUi(Form_export)
        QtCore.QMetaObject.connectSlotsByName(Form_export)

    def retranslateUi(self, Form_export):
        _translate = QtCore.QCoreApplication.translate
        Form_export.setWindowTitle(_translate("Form_export", "Export"))
        self.checkBox_ppd_export.setText(_translate("Form_export", " PPD"))
        self.checkBox_ep_export.setText(_translate("Form_export", "EP"))
        self.radioButton_all_eff_export.setText(_translate("Form_export", "All Effectives"))
        self.radioButton_effec_export.setText(_translate("Form_export", "Effective"))
        self.lineEdit_eff_export.setPlaceholderText(_translate("Form_export", "1"))
        self.radioButton_all.setText(_translate("Form_export", "All"))
        self.radioButton_all_directions.setText(_translate("Form_export", "All Directions"))
        self.radioButton_horizontal.setText(_translate("Form_export", "Horizontal"))
        self.radioButton_vertical.setText(_translate("Form_export", "Vertical"))
        self.radioButton_diagonal.setText(_translate("Form_export", "Diagonal"))
        self.groupBox_2.setTitle(_translate("Form_export", "Image Type"))
        self.radioButton_tiff_export.setText(_translate("Form_export", ".tiff"))
        self.radioButton_jpg_export.setText(_translate("Form_export", ".jpg"))
        self.radioButton_png_export.setText(_translate("Form_export", ".png"))
        self.groupBox_3.setTitle(_translate("Form_export", "Data File Type"))
        self.radioButton_txt_export.setText(_translate("Form_export", ".txt"))
        self.radioButton_xls_export.setText(_translate("Form_export", ".xlsx"))
        self.radioButton_csv.setText(_translate("Form_export", ".csv"))
        self.pushButton_ok_export.setText(_translate("Form_export", "Export"))
