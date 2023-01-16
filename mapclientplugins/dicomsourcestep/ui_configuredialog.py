# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(494, 236)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.idLabel = QLabel(self.configGroupBox)
        self.idLabel.setObjectName(u"idLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.idLabel)

        self.idLineEdit = QLineEdit(self.configGroupBox)
        self.idLineEdit.setObjectName(u"idLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.idLineEdit)

        self.dirLabel = QLabel(self.configGroupBox)
        self.dirLabel.setObjectName(u"dirLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.dirLabel)

        self.patternLlabel = QLabel(self.configGroupBox)
        self.patternLlabel.setObjectName(u"patternLlabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.patternLlabel)

        self.patternLineEdit = QLineEdit(self.configGroupBox)
        self.patternLineEdit.setObjectName(u"patternLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.patternLineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dirLineEdit = QLineEdit(self.configGroupBox)
        self.dirLineEdit.setObjectName(u"dirLineEdit")

        self.horizontalLayout.addWidget(self.dirLineEdit)

        self.dirButton = QPushButton(self.configGroupBox)
        self.dirButton.setObjectName(u"dirButton")

        self.horizontalLayout.addWidget(self.dirButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.idLineEdit, self.dirLineEdit)
        QWidget.setTabOrder(self.dirLineEdit, self.dirButton)
        QWidget.setTabOrder(self.dirButton, self.patternLineEdit)
        QWidget.setTabOrder(self.patternLineEdit, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configure Dicom Source Step", None))
        self.configGroupBox.setTitle("")
        self.idLabel.setText(QCoreApplication.translate("Dialog", u"identifier:  ", None))
        self.dirLabel.setText(QCoreApplication.translate("Dialog", u"Directory:  ", None))
        self.patternLlabel.setText(QCoreApplication.translate("Dialog", u"File Pattern:  ", None))
        self.dirButton.setText(QCoreApplication.translate("Dialog", u"...", None))
    # retranslateUi

