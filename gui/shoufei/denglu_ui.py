# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denglu_ui.ui'
#
# Created: Thu Jul 13 14:38:41 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_denglu_Dialog(object):
    def setupUi(self, denglu_Dialog):
        denglu_Dialog.setObjectName("denglu_Dialog")
        denglu_Dialog.resize(320, 240)
        self.layoutWidget = QtGui.QWidget(denglu_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 281, 149))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.username = QtGui.QLineEdit(self.layoutWidget)
        self.username.setObjectName("username")
        self.horizontalLayout_2.addWidget(self.username)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.password = QtGui.QLineEdit(self.layoutWidget)
        self.password.setAutoFillBackground(False)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName("password")
        self.horizontalLayout_3.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.denglu_Button = QtGui.QPushButton(self.layoutWidget)
        self.denglu_Button.setObjectName("denglu_Button")
        self.verticalLayout_2.addWidget(self.denglu_Button)

        self.retranslateUi(denglu_Dialog)
        QtCore.QMetaObject.connectSlotsByName(denglu_Dialog)

    def retranslateUi(self, denglu_Dialog):
        denglu_Dialog.setWindowTitle(QtGui.QApplication.translate("denglu_Dialog", "登录", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("denglu_Dialog", "用户名：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("denglu_Dialog", "密   码：", None, QtGui.QApplication.UnicodeUTF8))
        self.denglu_Button.setText(QtGui.QApplication.translate("denglu_Dialog", "登录", None, QtGui.QApplication.UnicodeUTF8))

