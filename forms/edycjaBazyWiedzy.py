# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edycjaBazyWiedzy.ui'
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


class Ui_edycjaBazyWiedzy(object):
    def setupUi(self, edycjaBazyWiedzy):
        if not edycjaBazyWiedzy.objectName():
            edycjaBazyWiedzy.setObjectName(u"edycjaBazyWiedzy")
        edycjaBazyWiedzy.resize(1491, 597)
        self.gridLayout = QGridLayout(edycjaBazyWiedzy)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableViewTabelaNauki = QTableView(edycjaBazyWiedzy)
        self.tableViewTabelaNauki.setObjectName(u"tableViewTabelaNauki")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewTabelaNauki.sizePolicy().hasHeightForWidth())
        self.tableViewTabelaNauki.setSizePolicy(sizePolicy)
        self.tableViewTabelaNauki.setMinimumSize(QSize(300, 300))
        self.tableViewTabelaNauki.setMaximumSize(QSize(16777215, 1600))
        self.tableViewTabelaNauki.setAutoFillBackground(False)
        self.tableViewTabelaNauki.horizontalHeader().setCascadingSectionResizes(True)
        self.tableViewTabelaNauki.verticalHeader().setVisible(True)
        self.tableViewTabelaNauki.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_2.addWidget(self.tableViewTabelaNauki)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_24 = QLabel(edycjaBazyWiedzy)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_21.addWidget(self.label_24)

        self.spinBoxUsuwanieIndeksu = QSpinBox(edycjaBazyWiedzy)
        self.spinBoxUsuwanieIndeksu.setObjectName(u"spinBoxUsuwanieIndeksu")
        self.spinBoxUsuwanieIndeksu.setMinimum(-1000)
        self.spinBoxUsuwanieIndeksu.setMaximum(1000)

        self.horizontalLayout_21.addWidget(self.spinBoxUsuwanieIndeksu)

        self.btnUsunWiersz = QPushButton(edycjaBazyWiedzy)
        self.btnUsunWiersz.setObjectName(u"btnUsunWiersz")

        self.horizontalLayout_21.addWidget(self.btnUsunWiersz)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_21)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_10 = QLabel(edycjaBazyWiedzy)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.spinBoxMaxIterMC = QSpinBox(edycjaBazyWiedzy)
        self.spinBoxMaxIterMC.setObjectName(u"spinBoxMaxIterMC")
        self.spinBoxMaxIterMC.setMaximum(10000)
        self.spinBoxMaxIterMC.setValue(1000)

        self.horizontalLayout_12.addWidget(self.spinBoxMaxIterMC)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.label_11 = QLabel(edycjaBazyWiedzy)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.spinBoxIleKlastrowMC = QSpinBox(edycjaBazyWiedzy)
        self.spinBoxIleKlastrowMC.setObjectName(u"spinBoxIleKlastrowMC")
        self.spinBoxIleKlastrowMC.setValue(25)

        self.horizontalLayout_13.addWidget(self.spinBoxIleKlastrowMC)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_28 = QSpacerItem(154, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_28)

        self.checkBoxWylaczPoTescie = QCheckBox(edycjaBazyWiedzy)
        self.checkBoxWylaczPoTescie.setObjectName(u"checkBoxWylaczPoTescie")

        self.horizontalLayout_14.addWidget(self.checkBoxWylaczPoTescie)

        self.btnTestuj = QPushButton(edycjaBazyWiedzy)
        self.btnTestuj.setObjectName(u"btnTestuj")
        self.btnTestuj.setMinimumSize(QSize(179, 0))

        self.horizontalLayout_14.addWidget(self.btnTestuj)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.textWynikiMonteCarlo = QTextBrowser(edycjaBazyWiedzy)
        self.textWynikiMonteCarlo.setObjectName(u"textWynikiMonteCarlo")

        self.verticalLayout.addWidget(self.textWynikiMonteCarlo)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnDodajDoBazy = QPushButton(edycjaBazyWiedzy)
        self.btnDodajDoBazy.setObjectName(u"btnDodajDoBazy")

        self.horizontalLayout.addWidget(self.btnDodajDoBazy)

        self.btnZapiszPlik = QPushButton(edycjaBazyWiedzy)
        self.btnZapiszPlik.setObjectName(u"btnZapiszPlik")

        self.horizontalLayout.addWidget(self.btnZapiszPlik)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(edycjaBazyWiedzy)

        QMetaObject.connectSlotsByName(edycjaBazyWiedzy)
    # setupUi

    def retranslateUi(self, edycjaBazyWiedzy):
        edycjaBazyWiedzy.setWindowTitle(QCoreApplication.translate("edycjaBazyWiedzy", u"Edycja bazy wiedzy", None))
        self.label_24.setText(QCoreApplication.translate("edycjaBazyWiedzy", u"Usu\u0144 indeks:", None))
        self.btnUsunWiersz.setText(QCoreApplication.translate("edycjaBazyWiedzy", u"Usu\u0144", None))
        self.label_10.setText(QCoreApplication.translate("edycjaBazyWiedzy", u"Liczba iteracji kMeans:", None))
        self.label_11.setText(QCoreApplication.translate("edycjaBazyWiedzy", u"Ile klastr\u00f3w:", None))
        self.checkBoxWylaczPoTescie.setText(QCoreApplication.translate("edycjaBazyWiedzy", u"Wy\u0142\u0105cz komputer po te\u015bcie", None))
        self.btnTestuj.setText(QCoreApplication.translate("edycjaBazyWiedzy", u"Test", None))
        self.btnDodajDoBazy.setText(QCoreApplication.translate("edycjaBazyWiedzy", u"Dodaj do bazy", None))
        self.btnZapiszPlik.setText(QCoreApplication.translate("edycjaBazyWiedzy", u"Zapisz tabele", None))
    # retranslateUi

