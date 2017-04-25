# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'touchgui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1920, 1200)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushBtn1 = QtGui.QPushButton(self.centralwidget)
        self.pushBtn1.setGeometry(QtCore.QRect(0, 0, 171, 171))
        self.pushBtn1.setObjectName(_fromUtf8("pushBtn1"))
        self.pushBtn3 = QtGui.QPushButton(self.centralwidget)
        self.pushBtn3.setGeometry(QtCore.QRect(1750, 0, 171, 171))
        self.pushBtn3.setObjectName(_fromUtf8("pushBtn3"))
        self.pushBtn9 = QtGui.QPushButton(self.centralwidget)
        self.pushBtn9.setGeometry(QtCore.QRect(1750, 980, 171, 171))
        self.pushBtn9.setObjectName(_fromUtf8("pushBtn9"))
        self.pushBtn7 = QtGui.QPushButton(self.centralwidget)
        self.pushBtn7.setGeometry(QtCore.QRect(0, 980, 171, 171))
        self.pushBtn7.setObjectName(_fromUtf8("pushBtn7"))
        self.pushBtn4 = QtGui.QPushButton(self.centralwidget)
        self.pushBtn4.setGeometry(QtCore.QRect(0, 490, 171, 171))
        self.pushBtn4.setObjectName(_fromUtf8("pushBtn4"))
        self.pushBtn6 = QtGui.QPushButton(self.centralwidget)
        self.pushBtn6.setGeometry(QtCore.QRect(1750, 490, 171, 171))
        self.pushBtn6.setObjectName(_fromUtf8("pushBtn6"))
        self.pushBtn2 = QtGui.QPushButton(self.centralwidget)
        self.pushBtn2.setGeometry(QtCore.QRect(880, 0, 171, 171))
        self.pushBtn2.setObjectName(_fromUtf8("pushBtn2"))
        self.pushBtn5 = QtGui.QPushButton(self.centralwidget)
        self.pushBtn5.setGeometry(QtCore.QRect(880, 490, 171, 171))
        self.pushBtn5.setObjectName(_fromUtf8("pushBtn5"))
        self.pushBtn8 = QtGui.QPushButton(self.centralwidget)
        self.pushBtn8.setGeometry(QtCore.QRect(880, 980, 171, 171))
        self.pushBtn8.setObjectName(_fromUtf8("pushBtn8"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushBtn1.setText(_translate("MainWindow", "PushButton", None))
        self.pushBtn3.setText(_translate("MainWindow", "PushButton", None))
        self.pushBtn9.setText(_translate("MainWindow", "PushButton", None))
        self.pushBtn7.setText(_translate("MainWindow", "PushButton", None))
        self.pushBtn4.setText(_translate("MainWindow", "PushButton", None))
        self.pushBtn6.setText(_translate("MainWindow", "PushButton", None))
        self.pushBtn2.setText(_translate("MainWindow", "PushButton", None))
        self.pushBtn5.setText(_translate("MainWindow", "PushButton", None))
        self.pushBtn8.setText(_translate("MainWindow", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

