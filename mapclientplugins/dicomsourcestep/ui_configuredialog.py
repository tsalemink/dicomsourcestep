# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Sun Jun  7 17:40:39 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(494, 236)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.configGroupBox = QtGui.QGroupBox(Dialog)
        self.configGroupBox.setTitle("")
        self.configGroupBox.setObjectName("configGroupBox")
        self.formLayout = QtGui.QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.idLabel = QtGui.QLabel(self.configGroupBox)
        self.idLabel.setObjectName("idLabel")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.idLabel)
        self.idLineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.idLineEdit.setObjectName("idLineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.idLineEdit)
        self.dirLabel = QtGui.QLabel(self.configGroupBox)
        self.dirLabel.setObjectName("dirLabel")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.dirLabel)
        self.patternLlabel = QtGui.QLabel(self.configGroupBox)
        self.patternLlabel.setObjectName("patternLlabel")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.patternLlabel)
        self.patternLineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.patternLineEdit.setObjectName("patternLineEdit")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.patternLineEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dirLineEdit = QtGui.QLineEdit(self.configGroupBox)
        self.dirLineEdit.setObjectName("dirLineEdit")
        self.horizontalLayout.addWidget(self.dirLineEdit)
        self.dirButton = QtGui.QPushButton(self.configGroupBox)
        self.dirButton.setObjectName("dirButton")
        self.horizontalLayout.addWidget(self.dirButton)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.idLineEdit, self.dirLineEdit)
        Dialog.setTabOrder(self.dirLineEdit, self.dirButton)
        Dialog.setTabOrder(self.dirButton, self.patternLineEdit)
        Dialog.setTabOrder(self.patternLineEdit, self.buttonBox)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Configure Dicom Source Step", None, QtGui.QApplication.UnicodeUTF8))
        self.idLabel.setText(QtGui.QApplication.translate("Dialog", "identifier:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.dirLabel.setText(QtGui.QApplication.translate("Dialog", "Directory:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.patternLlabel.setText(QtGui.QApplication.translate("Dialog", "File Pattern:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.dirButton.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))

