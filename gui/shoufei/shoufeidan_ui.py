# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shoufeidanyulan_ui.ui'
#
# Created: Sat Jul 29 23:31:10 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Ui_shoufeidanyulan_Dialog(object):
    def setupUi(self, Ui_shoufeidanyulan_Dialog):
        Ui_shoufeidanyulan_Dialog.setObjectName("Ui_shoufeidanyulan_Dialog")
        Ui_shoufeidanyulan_Dialog.resize(700, 600)
        Ui_shoufeidanyulan_Dialog.setMaximumSize(QtCore.QSize(700, 600))
        self.widget = QtGui.QWidget(Ui_shoufeidanyulan_Dialog)
        self.widget.setGeometry(QtCore.QRect(6, 0, 691, 589))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.webView = QtWebKit.QWebView(self.widget)
        self.webView.setMinimumSize(QtCore.QSize(679, 550))
        self.webView.setMaximumSize(QtCore.QSize(679, 550))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(Ui_shoufeidanyulan_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Ui_shoufeidanyulan_Dialog)

    def retranslateUi(self, Ui_shoufeidanyulan_Dialog):
        Ui_shoufeidanyulan_Dialog.setWindowTitle(QtGui.QApplication.translate("Ui_shoufeidanyulan_Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Ui_shoufeidanyulan_Dialog", "打印", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
