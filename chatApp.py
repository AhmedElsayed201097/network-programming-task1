# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(10, 50, 371, 131))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.t1 = QtWidgets.QLineEdit(self.splitter)
        self.t1.setObjectName("t1")
        self.send = QtWidgets.QPushButton(self.splitter)
        self.send.setObjectName("send")
        self.l1 = QtWidgets.QLabel(self.splitter_2)
        self.l1.setText("")
        self.l1.setObjectName("l1")
        self.rec = QtWidgets.QPushButton(self.splitter_2)
        self.rec.setObjectName("rec")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.send.setText(_translate("Form", "send"))
        self.rec.setText(_translate("Form", "read"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

