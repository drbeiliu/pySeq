# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pySeq.ui'
#
# Created: Sun Apr 28 16:35:32 2013
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(817, 250)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 121, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.patternEdit = QtGui.QLineEdit(self.centralwidget)
        self.patternEdit.setGeometry(QtCore.QRect(150, 20, 251, 31))
        self.patternEdit.setObjectName(_fromUtf8("patternEdit"))
        self.databaseEdit = QtGui.QLineEdit(self.centralwidget)
        self.databaseEdit.setGeometry(QtCore.QRect(150, 70, 251, 31))
        self.databaseEdit.setObjectName(_fromUtf8("databaseEdit"))
        self.setDatabase = QtGui.QPushButton(self.centralwidget)
        self.setDatabase.setGeometry(QtCore.QRect(50, 70, 75, 23))
        self.setDatabase.setObjectName(_fromUtf8("setDatabase"))
        self.go = QtGui.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(50, 120, 351, 31))
        self.go.setObjectName(_fromUtf8("go"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(410, 20, 391, 131))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Your Pattern Here:", None, QtGui.QApplication.UnicodeUTF8))
        self.setDatabase.setText(QtGui.QApplication.translate("MainWindow", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.go.setText(QtGui.QApplication.translate("MainWindow", "Go !!", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hint:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. ABCDEFG</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. A[BCD]EFG will match ABEFG, ACEFG, ADEFG</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. A[BCD]{m,n}EFG, m means the minimum repeat time</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                   n means the maximum repeat time</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. A(BCD){m,n}EFG, with match AEFG, ABCDEFP, ABCDBCDEFG(if m=0)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. A[A-Z]BCD, [A-Z] means to match all</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

