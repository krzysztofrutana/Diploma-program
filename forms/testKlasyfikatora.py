# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testKlasyfikatora.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_TestKlasyfikatoraForm(object):
    def setupUi(self, TestKlasyfikatoraForm):
        if not TestKlasyfikatoraForm.objectName():
            TestKlasyfikatoraForm.setObjectName(u"TestKlasyfikatoraForm")
        TestKlasyfikatoraForm.resize(894, 638)
        self.gridLayout = QGridLayout(TestKlasyfikatoraForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(TestKlasyfikatoraForm)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBoxKlasyfikatory = QComboBox(TestKlasyfikatoraForm)
        self.comboBoxKlasyfikatory.setObjectName(u"comboBoxKlasyfikatory")
        self.comboBoxKlasyfikatory.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.comboBoxKlasyfikatory)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.btnTestuj = QPushButton(TestKlasyfikatoraForm)
        self.btnTestuj.setObjectName(u"btnTestuj")

        self.horizontalLayout_2.addWidget(self.btnTestuj)

        self.btnZmienUstawieniaKlasyfikatora = QPushButton(TestKlasyfikatoraForm)
        self.btnZmienUstawieniaKlasyfikatora.setObjectName(u"btnZmienUstawieniaKlasyfikatora")

        self.horizontalLayout_2.addWidget(self.btnZmienUstawieniaKlasyfikatora)

        self.btnPokazTabele = QPushButton(TestKlasyfikatoraForm)
        self.btnPokazTabele.setObjectName(u"btnPokazTabele")

        self.horizontalLayout_2.addWidget(self.btnPokazTabele)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.txtWyniki = QTextEdit(TestKlasyfikatoraForm)
        self.txtWyniki.setObjectName(u"txtWyniki")

        self.verticalLayout.addWidget(self.txtWyniki)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(TestKlasyfikatoraForm)

        QMetaObject.connectSlotsByName(TestKlasyfikatoraForm)
    # setupUi

    def retranslateUi(self, TestKlasyfikatoraForm):
        TestKlasyfikatoraForm.setWindowTitle(QCoreApplication.translate("TestKlasyfikatoraForm", u"Test Leave Out klasyfikatora", None))
        self.label.setText(QCoreApplication.translate("TestKlasyfikatoraForm", u"Kt\u00f3ry klasyfikator testowa\u0107:", None))
        self.btnTestuj.setText(QCoreApplication.translate("TestKlasyfikatoraForm", u"Testuj", None))
        self.btnZmienUstawieniaKlasyfikatora.setText(QCoreApplication.translate("TestKlasyfikatoraForm", u"Zmie\u0144 ustawienia klasyfikatora", None))
        self.btnPokazTabele.setText(QCoreApplication.translate("TestKlasyfikatoraForm", u"Poka\u017c tabel\u0119 bazow\u0105", None))
    # retranslateUi

