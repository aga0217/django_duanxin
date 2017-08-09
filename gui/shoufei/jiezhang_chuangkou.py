# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jiezhang_chuangkou.ui'
#
# Created: Wed Aug  2 23:06:42 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Ui_jiezhang_Dialog(object):
    def setupUi(self, Ui_jiezhang_Dialog):
        Ui_jiezhang_Dialog.setObjectName("Ui_jiezhang_Dialog")
        Ui_jiezhang_Dialog.resize(700, 600)
        self.layoutWidget = QtGui.QWidget(Ui_jiezhang_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 725, 598))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.anjian_radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.anjian_radioButton.setMaximumSize(QtCore.QSize(60, 23))
        self.anjian_radioButton.setObjectName("anjian_radioButton")
        self.horizontalLayout.addWidget(self.anjian_radioButton)
        self.weiqi_radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.weiqi_radioButton.setMaximumSize(QtCore.QSize(60, 23))
        self.weiqi_radioButton.setObjectName("weiqi_radioButton")
        self.horizontalLayout.addWidget(self.weiqi_radioButton)
        self.zongjian_radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.zongjian_radioButton.setEnabled(False)
        self.zongjian_radioButton.setMaximumSize(QtCore.QSize(60, 23))
        self.zongjian_radioButton.setObjectName("zongjian_radioButton")
        self.horizontalLayout.addWidget(self.zongjian_radioButton)
        self.jiezhang_dateEdit = QtGui.QDateEdit(self.layoutWidget)
        self.jiezhang_dateEdit.setMaximumSize(QtCore.QSize(90, 16777215))
        self.jiezhang_dateEdit.setObjectName("jiezhang_dateEdit")
        self.horizontalLayout.addWidget(self.jiezhang_dateEdit)
        self.Button_chazhaojiehangdan = QtGui.QPushButton(self.layoutWidget)
        self.Button_chazhaojiehangdan.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Button_chazhaojiehangdan.setObjectName("Button_chazhaojiehangdan")
        self.horizontalLayout.addWidget(self.Button_chazhaojiehangdan)
        self.Button_chongxindayin = QtGui.QPushButton(self.layoutWidget)
        self.Button_chongxindayin.setMaximumSize(QtCore.QSize(80, 16777215))
        self.Button_chongxindayin.setObjectName("Button_chongxindayin")
        self.horizontalLayout.addWidget(self.Button_chongxindayin)
        self.Button_dayin = QtGui.QPushButton(self.layoutWidget)
        self.Button_dayin.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Button_dayin.setObjectName("Button_dayin")
        self.horizontalLayout.addWidget(self.Button_dayin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = QtWebKit.QWebView(self.layoutWidget)
        self.webView.setMinimumSize(QtCore.QSize(679, 550))
        self.webView.setMaximumSize(QtCore.QSize(697, 550))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(Ui_jiezhang_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Ui_jiezhang_Dialog)

    def retranslateUi(self, Ui_jiezhang_Dialog):
        Ui_jiezhang_Dialog.setWindowTitle(QtGui.QApplication.translate("Ui_jiezhang_Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.anjian_radioButton.setText(QtGui.QApplication.translate("Ui_jiezhang_Dialog", "安检", None, QtGui.QApplication.UnicodeUTF8))
        self.weiqi_radioButton.setText(QtGui.QApplication.translate("Ui_jiezhang_Dialog", "尾气", None, QtGui.QApplication.UnicodeUTF8))
        self.zongjian_radioButton.setText(QtGui.QApplication.translate("Ui_jiezhang_Dialog", "综检", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_chazhaojiehangdan.setText(QtGui.QApplication.translate("Ui_jiezhang_Dialog", "查找结账单", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_chongxindayin.setText(QtGui.QApplication.translate("Ui_jiezhang_Dialog", "重新打印", None, QtGui.QApplication.UnicodeUTF8))
        self.Button_dayin.setText(QtGui.QApplication.translate("Ui_jiezhang_Dialog", "当日结账并打印", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
