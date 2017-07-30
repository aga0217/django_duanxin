# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xiugaimima_ui.ui'
#
# Created: Thu Jul 27 17:31:08 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_xiugaimima_Dialog(object):
    def setupUi(self, xiugaimima_Dialog):
        xiugaimima_Dialog.setObjectName("xiugaimima_Dialog")
        xiugaimima_Dialog.resize(240, 240)
        xiugaimima_Dialog.setMaximumSize(QtCore.QSize(240, 300))
        self.widget = QtGui.QWidget(xiugaimima_Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 30, 225, 149))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.yuanshimima = QtGui.QLineEdit(self.widget)
        self.yuanshimima.setEchoMode(QtGui.QLineEdit.Password)
        self.yuanshimima.setObjectName("yuanshimima")
        self.verticalLayout_2.addWidget(self.yuanshimima)
        self.xinmima1 = QtGui.QLineEdit(self.widget)
        self.xinmima1.setEchoMode(QtGui.QLineEdit.Password)
        self.xinmima1.setObjectName("xinmima1")
        self.verticalLayout_2.addWidget(self.xinmima1)
        self.xinmima2 = QtGui.QLineEdit(self.widget)
        self.xinmima2.setEchoMode(QtGui.QLineEdit.Password)
        self.xinmima2.setObjectName("xinmima2")
        self.verticalLayout_2.addWidget(self.xinmima2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.Button_gengtaimima = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Button_gengtaimima.setFont(font)
        self.Button_gengtaimima.setObjectName("Button_gengtaimima")
        self.verticalLayout_3.addWidget(self.Button_gengtaimima)

        self.retranslateUi(xiugaimima_Dialog)
        QtCore.QMetaObject.connectSlotsByName(xiugaimima_Dialog)

    def retranslateUi(self, xiugaimima_Dialog):
        xiugaimima_Dialog.setWindowTitle(QtGui.QApplication.translate("xiugaimima_Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("xiugaimima_Dialog", "原始密码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("xiugaimima_Dialog", "新密码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("xiugaimima_Dialog", "再输入一次", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_gengtaimima.setText(QtGui.QApplication.translate("xiugaimima_Dialog", "更改密码", None, QtGui.QApplication.UnicodeUTF8))

