# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushAdd.setObjectName("pushAdd")
        self.gridLayout_2.addWidget(self.pushAdd, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 2, 1, 1)
        self.linePatient = QtWidgets.QLineEdit(self.centralwidget)
        self.linePatient.setObjectName("linePatient")
        self.gridLayout_2.addWidget(self.linePatient, 2, 0, 1, 1)
        self.lineDisease = QtWidgets.QLineEdit(self.centralwidget)
        self.lineDisease.setObjectName("lineDisease")
        self.gridLayout_2.addWidget(self.lineDisease, 2, 1, 1, 1)
        self.comboPhysician = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboPhysician.sizePolicy().hasHeightForWidth())
        self.comboPhysician.setSizePolicy(sizePolicy)
        self.comboPhysician.setMinimumSize(QtCore.QSize(50, 10))
        self.comboPhysician.setMaximumSize(QtCore.QSize(200, 100))
        self.comboPhysician.setObjectName("comboPhysician")
        self.gridLayout_2.addWidget(self.comboPhysician, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.textResults = QtWidgets.QTextEdit(self.centralwidget)
        self.textResults.setObjectName("textResults")
        self.gridLayout.addWidget(self.textResults, 1, 0, 1, 1)
        self.pushShow = QtWidgets.QPushButton(self.centralwidget)
        self.pushShow.setObjectName("pushShow")
        self.gridLayout.addWidget(self.pushShow, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushAdd.setText(_translate("MainWindow", "Add"))
        self.label.setText(_translate("MainWindow", "Patient"))
        self.label_2.setText(_translate("MainWindow", "Disease"))
        self.label_3.setText(_translate("MainWindow", "Physician"))
        self.label_4.setText(_translate("MainWindow", "Results"))
        self.pushShow.setText(_translate("MainWindow", "Show"))

