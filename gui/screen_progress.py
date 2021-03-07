# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'barra_progresso.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_progress(object):
    def setupUi(self, Form_progress):
        Form_progress.setObjectName("Form_progress")
        Form_progress.resize(300, 80)
        Form_progress.setMinimumSize(QtCore.QSize(300, 80))
        Form_progress.setMaximumSize(QtCore.QSize(300, 80))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/ppd_enhanced_colors_supreme-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_progress.setWindowIcon(icon)
        Form_progress.setStyleSheet("background-color: rgb(83, 83, 83);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_progress)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(Form_progress)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Form_progress)
        QtCore.QMetaObject.connectSlotsByName(Form_progress)

    def retranslateUi(self, Form_progress):
        _translate = QtCore.QCoreApplication.translate
        Form_progress.setWindowTitle(_translate("Form_progress", "Progress"))
