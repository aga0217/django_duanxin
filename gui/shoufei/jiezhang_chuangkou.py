# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jiezhang_chuangkou.ui'
#
# Created: Sun Jul 30 00:13:59 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Ui_jiezhang_Dialog(object):
    def setupUi(self, Ui_jiezhang_Dialog):
        Ui_jiezhang_Dialog.setObjectName("Ui_jiezhang_Dialog")
        Ui_jiezhang_Dialog.resize(700, 600)
        self.layoutWidget = QtGui.QWidget(Ui_jiezhang_Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 699, 594))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.anjian_radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.anjian_radioButton.setObjectName("anjian_radioButton")
        self.horizontalLayout.addWidget(self.anjian_radioButton)
        self.weiqi_radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.weiqi_radioButton.setObjectName("weiqi_radioButton")
        self.horizontalLayout.addWidget(self.weiqi_radioButton)
        self.zongjian_radioButton = QtGui.QRadioButton(self.layoutWidget)
        self.zongjian_radioButton.setEnabled(False)
        self.zongjian_radioButton.setObjectName("zongjian_radioButton")
        self.horizontalLayout.addWidget(self.zongjian_radioButton)
        self.Button_dayin = QtGui.QPushButton(self.layoutWidget)
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
        self.Button_dayin.setText(QtGui.QApplication.translate("Ui_jiezhang_Dialog", "打印", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
