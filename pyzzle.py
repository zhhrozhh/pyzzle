# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from pyblock import *
import sys
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
        MainWindow.resize(500, 400)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 95, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.bt_addBlock = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bt_addBlock.setObjectName(_fromUtf8("bt_addBlock"))
        self.verticalLayout.addWidget(self.bt_addBlock)
        self.bt_save = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bt_save.setObjectName(_fromUtf8("bt_save"))
        self.verticalLayout.addWidget(self.bt_save)
        self.bt_ld = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bt_ld.setObjectName(_fromUtf8("bt_ld"))
        self.verticalLayout.addWidget(self.bt_ld)
        self.bt_sp = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bt_sp.setObjectName(_fromUtf8("bt_sp"))
        self.verticalLayout.addWidget(self.bt_sp)

        self.bt_font = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bt_font.setObjectName(_fromUtf8("bt_font"))
        self.verticalLayout.addWidget(self.bt_font)

        self.bt_cmd = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bt_cmd.setObjectName(_fromUtf8("bt_cmd"))
        self.verticalLayout.addWidget(self.bt_cmd)

        #self.bt_G = QtGui.QPushButton(self.verticalLayoutWidget)
        #self.bt_G.setObjectName(_fromUtf8("bt_G"))
        #self.verticalLayout.addWidget(self.bt_G)


        self.currentStructure = QtGui.QLabel(MainWindow)
        self.showCurrentGraph()
        #self.pixmap = QtGui.QPixmap('currentStructure.png').scaled(350,350,QtCore.Qt.KeepAspectRatio)
        #self.currentStructure.setPixmap(self.pixmap)
        self.currentStructure.setGeometry(110,0,350,350)


        self.bt_exit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.bt_exit.setObjectName(_fromUtf8("bt_exit"))
        self.verticalLayout.addWidget(self.bt_exit)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 100, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtCore.QObject.connect(self.bt_addBlock,QtCore.SIGNAL(_fromUtf8('clicked()')),self.newPyBlockWindow)

        #QtCore.QObject.connect(self.bt_G,QtCore.SIGNAL(_fromUtf8('clicked()')),self.showCurrentGraph)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.bt_addBlock.setText(_translate("MainWindow", "Add Block", None))
        self.bt_save.setText(_translate("MainWindow", "Save", None))
        self.bt_ld.setText(_translate("MainWindow", "Load", None))
        self.bt_sp.setText(_translate("MainWindow", "switch python", None))
        self.bt_font.setText(_translate("MainWindow", "font", None))
        self.bt_cmd.setText(_translate("MainWindow","cmd mode",None))
        #self.bt_G.setText(_translate("MainWindow","show graph",None))
        self.bt_exit.setText(_translate("MainWindow", "exit", None))

    def newPyBlockWindow(self):
        PY_block = QtGui.QWidget()
        ui = Ui_PY_block(self)
        #ui.setMainWindow(self)
        ui.setupUi(PY_block)
        PY_block.show()
        global allWindow
        allWindow.append((ui,PY_block))
    def showCurrentGraph(self):
        getGraph()
        self.pixmap = QtGui.QPixmap('currentStructure.png').scaled(350,350,QtCore.Qt.KeepAspectRatio)
        self.currentStructure.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Pyzzle = QtGui.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Pyzzle)
    Pyzzle.show()
    sys.exit(app.exec_())
