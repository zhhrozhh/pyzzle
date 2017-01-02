# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import subprocess
import pyhighlighter
from uniFunc import *
from linkstructure import *
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


class PY_TEST_Edit(QtGui.QPlainTextEdit):
    keyPressSignal = QtCore.pyqtSignal(object)
    def __init__(self,*args):
        self.currentLine = ''
        self.indent = 0
        self.NL = False
        
        QtGui.QPlainTextEdit.__init__(self,*args)
    def keyPressEvent(self,event):
        if event.modifiers() and QtCore.Qt.ControlModifier:
            if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
                self.keyPressSignal.emit('testQ')
        elif event.key() == QtCore.Qt.Key_Tab:
            self.insertPlainText('    ')
            return
        elif event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.currentLine = self.toPlainText().split('\n')[-1]
            self.indent = len(self.currentLine) - len(self.currentLine.lstrip())
            clToken = self.currentLine.split()
            if clToken[-1] in ['pass','break','continue']:
                self.indent -= 4
            elif 'return' in clToken:
                self.indent -= 4
            if clToken[-1][-1]==':':
                self.indent += 4
            self.NL = True
        elif event.key() == QtCore.Qt.Key_Backspace:
            if self.toPlainText()[-4:] == '    ':
                for i in range(3):
                    super(PY_TEST_Edit,self).keyPressEvent(event)
        super(PY_TEST_Edit,self).keyPressEvent(event)
        if self.NL:
            self.insertPlainText(' '*self.indent)
        self.NL = False

class Ui_PY_block(object):
    def __init__(self,mainWindow):
        self.mainWindow = mainWindow
        self.relationSize = (162,460)
        self.inpSize = (440,410)
        self.testSize = (270,460)
        self.anc = []
        self.toDel = None
        x = 'untitled_'
        ini = 0
        global allName
        while x+str(ini) in allName:
            ini+=1
        self.bName = x+str(ini)
        addNode(self)
        mainWindow.showCurrentGraph()
        allName.append(self.bName)
    def setMainWindow(self,mainWindow):
        self.mainWindow = mainWindow
    def setupUi(self, PY_block):
        self.PY_block = PY_block
        PY_block.setObjectName(_fromUtf8("PY_block"))
        PY_block.resize(961, 653)
        print(PY_block.sizeHint())
        print(PY_block.minimumSizeHint())
        font = QtGui.QFont()
        font.setPointSize(10)
        PY_block.setFont(font)
        self.lIn = []
        self.lOut = []
        self.Relation = QtGui.QGroupBox(PY_block)
        self.Relation.setGeometry(QtCore.QRect(0, 10, 162, 460))
        self.Relation.setObjectName(_fromUtf8("Relation"))
        self.linkedIn = QtGui.QListWidget(self.Relation)
        self.linkedIn.setGeometry(QtCore.QRect(10, 40, 140, 151))
        self.linkedIn.setObjectName(_fromUtf8("linkedIn"))
        self.linkedOut = QtGui.QListWidget(self.Relation)
        self.linkedOut.setGeometry(QtCore.QRect(10, 240, 140, 151))
        self.linkedOut.setObjectName(_fromUtf8("linkedOut"))

        self.linkin = QtGui.QPushButton(self.Relation)
        self.linkin.setGeometry(QtCore.QRect(10, 390, 90, 28))
        self.linkin.setObjectName(_fromUtf8("linkin"))
        self.linkout = QtGui.QPushButton(self.Relation)
        self.linkout.setGeometry(QtCore.QRect(10, 190, 90, 28))
        self.linkout.setObjectName(_fromUtf8("linkout"))
        self.label_2 = QtGui.QLabel(self.Relation)
        self.label_2.setGeometry(QtCore.QRect(60, 220, 53, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.Relation)
        self.label_3.setGeometry(QtCore.QRect(60, 20, 53, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self._del = QtGui.QPushButton(self.Relation)
        self._del.setGeometry(QtCore.QRect(10, 420, 40, 20))
        self._del.setObjectName(_fromUtf8("_del"))
        self._del.setText('del')

        self._show = QtGui.QPushButton(self.Relation)
        self._show.setGeometry(QtCore.QRect(50, 420, 50, 20))
        self._show.setObjectName(_fromUtf8("_show"))
        self._show.setText('show')



        self.test = QtGui.QGroupBox(PY_block)
        self.test.setGeometry(QtCore.QRect(600, 10, 270, 460))
        self.test.setObjectName(_fromUtf8("test"))
        self.plainTextEdit = PY_TEST_Edit(self.test)
        self.hi = pyhighlighter.PythonHighlighter(self.plainTextEdit.document())
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 20, 261, 221))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        font.setBold(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setTabStopWidth(52)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.TestResult = QtGui.QTextBrowser(self.test)
        self.TestResult.setGeometry(QtCore.QRect(0, 260, 261, 180))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        font.setBold(False)
        font.setWeight(50)
        self.TestResult.setFont(font)
        self.TestResult.setTabStopWidth(52)
        self.TestResult.setObjectName(_fromUtf8("TestResult"))

        self.titleBox = QtGui.QGroupBox(PY_block)
        self.titleBox.setGeometry(QtCore.QRect(160,20,440,40) )

        self.blockName = QtGui.QLineEdit(self.titleBox)
        self.blockName.setGeometry(QtCore.QRect(60, 0, 113, 28))
        self.blockName.setObjectName(_fromUtf8("blockName"))
        self.blockName.setText(self.bName)
        self.label = QtGui.QLabel(self.titleBox)
        self.label.setGeometry(QtCore.QRect(0, 0, 53, 28))
        self.label.setObjectName(_fromUtf8("label"))
        self.min = QtGui.QPushButton(self.titleBox)
        self.min.setGeometry(QtCore.QRect(180, 0, 31, 28))
        self.min.setObjectName(_fromUtf8("min"))
        self.max = QtGui.QPushButton(self.titleBox)
        self.max.setGeometry(QtCore.QRect(180, 0, 31, 28))
        self.max.setObjectName(_fromUtf8("max"))

        self.pin = QtGui.QPushButton(self.titleBox)
        self.pin.setGeometry(QtCore.QRect(210, 0, 32, 28))
        self.pin.setObjectName(_fromUtf8("pin"))
        self.pin.setText('pin')

        self.merge = QtGui.QPushButton(self.titleBox)
        self.merge.setGeometry(QtCore.QRect(240, 0, 60, 28))
        self.merge.setObjectName(_fromUtf8("merge"))
        self.merge.setText('merge')

        self.groupBox = QtGui.QGroupBox(PY_block)
        self.groupBox.setGeometry(QtCore.QRect(160, 60, 440, 410))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pyInput = PY_TEST_Edit(self.groupBox)
        self.hinp = pyhighlighter.PythonHighlighter(self.pyInput.document())
        self.pyInput.setGeometry(QtCore.QRect(20, 20, 401, 351))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Terminal"))
        font.setBold(False)
        font.setWeight(50)
        self.pyInput.setFont(font)
        self.pyInput.setAutoFillBackground(False)
        self.pyInput.setTabChangesFocus(False)
        self.pyInput.setTabStopWidth(52)
        self.pyInput.setCursorWidth(2)
        self.pyInput.setObjectName(_fromUtf8("pyInput"))
        self.showRelation = QtGui.QPushButton(self.groupBox)
        self.showRelation.setGeometry(QtCore.QRect(0, 50, 16, 81))
        self.showRelation.setObjectName(_fromUtf8("showRelation"))
        self.hideRelation = QtGui.QPushButton(self.groupBox)
        self.hideRelation.setGeometry(QtCore.QRect(0, 50, 16, 81))
        self.hideRelation.setObjectName(_fromUtf8("hideRelation"))
        self.showTestField = QtGui.QPushButton(self.groupBox)
        self.showTestField.setGeometry(QtCore.QRect(420, 50, 16, 81))
        self.showTestField.setObjectName(_fromUtf8("showTestField"))
        self.hideTestField = QtGui.QPushButton(self.groupBox)
        self.hideTestField.setGeometry(QtCore.QRect(420, 50, 16, 81))
        self.hideTestField.setObjectName(_fromUtf8("hideTestField"))

        self.retranslateUi(PY_block)
        QtCore.QObject.connect(self.hideTestField, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f_hideTest)
        QtCore.QObject.connect(self.hideRelation, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f_hideRelation)
        QtCore.QObject.connect(self.hideRelation, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showRelation.show)
        QtCore.QObject.connect(self.hideRelation, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hideRelation.hide)
        QtCore.QObject.connect(self.hideTestField, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hideTestField.hide)
        QtCore.QObject.connect(self.showTestField, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showTestField.hide)
        QtCore.QObject.connect(self.showTestField, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f_showTest)
        QtCore.QObject.connect(self.showTestField, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hideTestField.show)
        
        QtCore.QObject.connect(self.showRelation, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f_showRelation)
        QtCore.QObject.connect(self.showRelation, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hideRelation.show)
        QtCore.QObject.connect(self.showRelation, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showRelation.hide)
        QtCore.QObject.connect(self.hideTestField, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showTestField.show)

        QtCore.QObject.connect(self.min, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f_hideInp)
        QtCore.QObject.connect(self.min, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f_hideTest)
        QtCore.QObject.connect(self.min, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f_hideRelation)
        QtCore.QObject.connect(self.min, QtCore.SIGNAL(_fromUtf8("clicked()")), self.max.show)
        QtCore.QObject.connect(self.min, QtCore.SIGNAL(_fromUtf8("clicked()")), self.min.hide)
        self.blockName.returnPressed.connect(self.setName)
        self.plainTextEdit.keyPressSignal.connect(self.keyHandle)

        QtCore.QObject.connect(self.max, QtCore.SIGNAL(_fromUtf8("clicked()")), self.min.show)
        QtCore.QObject.connect(self.max, QtCore.SIGNAL(_fromUtf8("clicked()")), self.max.hide)
        QtCore.QObject.connect(self.max, QtCore.SIGNAL(_fromUtf8("clicked()")), self.f_showInp)
        QtCore.QObject.connect(self.max, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showRelation.show)
        QtCore.QObject.connect(self.max, QtCore.SIGNAL(_fromUtf8("clicked()")), self.showTestField.show)
        QtCore.QObject.connect(self.max, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hideRelation.hide)
        QtCore.QObject.connect(self.max, QtCore.SIGNAL(_fromUtf8("clicked()")), self.hideTestField.hide)

        QtCore.QObject.connect(self.linkedIn,QtCore.SIGNAL(_fromUtf8('itemActivated(QListWidgetItem*)')),self.toDelNode)
        QtCore.QObject.connect(self.linkedOut,QtCore.SIGNAL(_fromUtf8('itemActivated(QListWidgetItem*)')),self.toDelNode)

        QtCore.QObject.connect(self.linkin,QtCore.SIGNAL(_fromUtf8('clicked()')),self.linkToRequest)
        QtCore.QObject.connect(self.linkout,QtCore.SIGNAL(_fromUtf8('clicked()')),self.linkFromRequest)

        QtCore.QObject.connect(self._del,QtCore.SIGNAL(_fromUtf8('clicked()')),self.delNode)
        QtCore.QMetaObject.connectSlotsByName(PY_block)

        self.f_hideRelation()
        self.hideRelation.hide()
        self.f_hideTest()
        self.hideTestField.hide()
        self.max.hide()
        print(self.Relation.size())

    def retranslateUi(self, PY_block):
        PY_block.setWindowTitle(_translate("PY_block", self.bName, None))
        self.Relation.setTitle(_translate("PY_block", "Relation", None))
        self.linkin.setText(_translate("PY_block", "@==>", None))
        self.linkout.setText(_translate("PY_block", "==>@", None))
        self.label_2.setText(_translate("PY_block", "out", None))
        self.label_3.setText(_translate("PY_block", "in", None))
        self.test.setTitle(_translate("PY_block", "Test", None))
        self.label.setText(_translate("PY_block", "name", None))
        self.min.setText(_translate("PY_block", "_", None))
        self.max.setText(_translate("PY_block", "+", None))
        self.groupBox.setTitle(_translate("PY_block", "------------------", None))
        self.showRelation.setText(_translate("PY_block", "<", None))
        self.hideRelation.setText(_translate("PY_block", ">", None))
        self.showTestField.setText(_translate("PY_block", ">", None))
        self.hideTestField.setText(_translate("PY_block", "<", None))
    def f_hideRelation(self):
        self.Relation.resize(0,0)
        self._resize()
    def f_showRelation(self):
        self.Relation.resize(*self.relationSize)
        self._resize()
        print(self.Relation.size())
    def f_hideTest(self):
        self.test.resize(0,0)
        self._resize()
    def f_showTest(self):
        self.test.resize(*self.testSize)
        self._resize()
    def f_hideInp(self):
        self.groupBox.resize(0,0)
        self._resize()
    def f_showInp(self):
        self.groupBox.resize(*self.inpSize)
        self._resize()
    def _resize(self):
        r = self.Relation.size()
        t = self.test.size()
        i = self.groupBox.size()
        tt = self.titleBox.size()
        w = r.width()+t.width()+max(i.width(),tt.width())
        h = max(r.height(),t.height(),tt.height()+i.height()+20)
        self.Relation.setGeometry(QtCore.QRect(0,10,r.width(),r.height()))
        self.titleBox.setGeometry(QtCore.QRect(r.width(),20,tt.width(),tt.height()))
        self.groupBox.setGeometry(QtCore.QRect(r.width(),20+tt.height(),i.width(),i.height()))
        self.test.setGeometry(QtCore.QRect(r.width()+max(tt.width(),i.width()),10,t.width(),t.height()))
        self.PY_block.resize(w,h)
    def getUnlinkedSource(self):
        return str(self.pyInput.toPlainText())
    def getLinkedSource(self):
        dep = getDep(self)
        res = ''
        for node in dep:
            res += node.getUnlinkedSource()
            res += '\n'
        res += self.getUnlinkedSource()
        return res
    def getSourceText(self):
        return self.getLinkedSource()
    def testQ(self):
        testText = self.getSourceText()+'\n'+str(self.plainTextEdit.toPlainText())
        tf = open('test.py','w')
        tf.write(testText)
        tf.close()
        pipes = subprocess.Popen(['python','test.py'],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        std_out,std_err = pipes.communicate()
        res = std_out.decode('utf-8')
        if pipes.returncode != 0:
            res += std_err.decode('utf-8')
        #else:
        self.TestResult.setText(res)
    def keyHandle(self,event):
        if event=='testQ':
            self.testQ()
    def setName(self):
        fname = self.bName
        if isInt(fname[8:]) and fname[:8]=='untitled':
            returnLabel(fname[8:])
        xname = self.blockName.text()
        ini = 0
        global allName
        if xname == fname:
            return
        while xname+str(ini) in allName:
            ini+=1
        if ini:
            self.bName = xname+str(ini)
        else:
            self.bName = xname
        allName.remove(fname)
        allName.append(self.bName)
        self.PY_block.setWindowTitle(_translate("PY_block", self.bName, None))
        for i in range(self.linkedIn.count()):
            name2node[self.linkedIn.item(i).text()].reName(fname,self.bName)
        for i in range(self.linkedOut.count()):
            name2node[self.linkedOut.item(i).text()].reName(fname,self.bName)
        nodeRename(fname,self.bName)
        self.mainWindow.showCurrentGraph()
    def linkToRequest(self):
        global linkObj,linkTarget
        overwriteWarning = False
        if linkObj != None:
            overwriteWarning = True
        if linkTarget == None:
            linkObj = self
        else:
            addEdge(self,linkTarget)
            self.mainWindow.showCurrentGraph()
            self.f_linkOut(linkTarget)
            linkTarget.f_linkIn(self)
            linkTarget = None
        if overwriteWarning:
            raise Exception('linkObjOW')
    def linkFromRequest(self):
        global linkObj,linkTarget
        overwriteWarning = False
        if linkTarget != None:
            overwriteWarning = True
        if linkObj == None:
            linkTarget = self
        else:
            addEdge(linkObj,self)
            self.mainWindow.showCurrentGraph()
            self.f_linkIn(linkObj)
            linkObj.f_linkOut(self)
            linkObj = None
        if overwriteWarning:
            raise Exception('linkTargOW')
    def f_linkIn(self,oth):
        item = QtGui.QListWidgetItem()
        item.setText(oth.bName)
        self.linkedIn.addItem(item)
    def f_linkOut(self,oth):
        item = QtGui.QListWidgetItem()
        item.setText(oth.bName)
        self.linkedOut.addItem(item)
    def toDelNode(self,w):
        self.toDel = w
    def delNode(self):
        if self.toDel == None:
            raise('Nothing to del')
        xname = self.toDel.text()
        tdNode = name2node[xname]
        if self.linkedIn.row(self.toDel)!=-1:
            self.linkedIn.takeItem(self.linkedIn.row(self.toDel))
        else:
            self.linkedOut.takeItem(self.linkedOut.row(self.toDel))
        for index in range(tdNode.linkedIn.count()):
            if tdNode.linkedIn.item(index).text() == self.bName:
                tdNode.linkedIn.takeItem(index)
                break
        for index in range(tdNode.linkedOut.count()):
            if tdNode.linkedOut.item(index).text() == self.bName:
                tdNode.linkedOut.takeItem(index)
                break
        try:
            delEdge(self,tdNode)
        except:
            delEdge(tdNode,self)
        self.toDel = None
        self.mainWindow.showCurrentGraph()
    def reName(self,fname,tname):
        for i in range(self.linkedIn.count()):
            if self.linkedIn.item(i).text() == fname:
                self.linkedIn.item(i).setText(tname)
                break
        for i in range(self.linkedOut.count()):
            if self.linkedOut.item(i).text() == fname:
                self.linkedOut.item(i).setText(tname)
                break
    def copyBlock(self):
        self.mainWindow.copyBlock(self)
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    PY_block = QtGui.QWidget()
    ui = Ui_PY_block()
    ui.setMainWindow(1)
    ui.setupUi(PY_block)
    PY_block.show()
    sys.exit(app.exec_())