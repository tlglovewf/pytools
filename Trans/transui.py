# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trans.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 325)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txInput = QtWidgets.QTextEdit(Form)
        self.txInput.setObjectName("txInput")
        self.verticalLayout.addWidget(self.txInput)
        self.btnTrans = QtWidgets.QPushButton(Form)
        self.btnTrans.setObjectName("btnTrans")
        self.verticalLayout.addWidget(self.btnTrans)
        self.txOutput = QtWidgets.QTextEdit(Form)
        self.txOutput.setObjectName("txOutput")
        self.verticalLayout.addWidget(self.txOutput)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btnTrans.setText(_translate("Form", "翻译"))
