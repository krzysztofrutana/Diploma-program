# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1193, 892)
        MainWindow.setMinimumSize(QSize(1193, 887))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.actionPodgladTabeliTreningowej = QAction(MainWindow)
        self.actionPodgladTabeliTreningowej.setObjectName(u"actionPodgladTabeliTreningowej")
        self.actionCzyszczenie = QAction(MainWindow)
        self.actionCzyszczenie.setObjectName(u"actionCzyszczenie")
        self.actionUsuwanieAtrybutu = QAction(MainWindow)
        self.actionUsuwanieAtrybutu.setObjectName(u"actionUsuwanieAtrybutu")
        self.actionWariancja_kolumn = QAction(MainWindow)
        self.actionWariancja_kolumn.setObjectName(u"actionWariancja_kolumn")
        self.actionBadanie_atrybutow = QAction(MainWindow)
        self.actionBadanie_atrybutow.setObjectName(u"actionBadanie_atrybutow")
        self.actionRedukuj = QAction(MainWindow)
        self.actionRedukuj.setObjectName(u"actionRedukuj")
        self.actionReczne_wyznaczanie_miary = QAction(MainWindow)
        self.actionReczne_wyznaczanie_miary.setObjectName(u"actionReczne_wyznaczanie_miary")
        self.actionEdycja_bazy_wiedzy = QAction(MainWindow)
        self.actionEdycja_bazy_wiedzy.setObjectName(u"actionEdycja_bazy_wiedzy")
        self.actionTest_Leave_Out_klasyfikatora = QAction(MainWindow)
        self.actionTest_Leave_Out_klasyfikatora.setObjectName(u"actionTest_Leave_Out_klasyfikatora")
        self.actionTest_parametr_w_klasyfikatora = QAction(MainWindow)
        self.actionTest_parametr_w_klasyfikatora.setObjectName(u"actionTest_parametr_w_klasyfikatora")
        self.actionKonfiguracja_klasyfikatora = QAction(MainWindow)
        self.actionKonfiguracja_klasyfikatora.setObjectName(u"actionKonfiguracja_klasyfikatora")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_26)

        self.line_19 = QFrame(self.centralwidget)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.VLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_19)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEditSciezkaPliku = QLineEdit(self.centralwidget)
        self.lineEditSciezkaPliku.setObjectName(u"lineEditSciezkaPliku")
        self.lineEditSciezkaPliku.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditSciezkaPliku)

        self.btnWybierzPlik = QPushButton(self.centralwidget)
        self.btnWybierzPlik.setObjectName(u"btnWybierzPlik")

        self.horizontalLayout.addWidget(self.btnWybierzPlik)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButtonCSVzNaglowkami = QRadioButton(self.centralwidget)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radioButtonCSVzNaglowkami)
        self.radioButtonCSVzNaglowkami.setObjectName(u"radioButtonCSVzNaglowkami")
        self.radioButtonCSVzNaglowkami.setChecked(True)

        self.horizontalLayout_2.addWidget(self.radioButtonCSVzNaglowkami)

        self.radioButtonCSVbezNaglowkow = QRadioButton(self.centralwidget)
        self.buttonGroup_2.addButton(self.radioButtonCSVbezNaglowkow)
        self.radioButtonCSVbezNaglowkow.setObjectName(u"radioButtonCSVbezNaglowkow")

        self.horizontalLayout_2.addWidget(self.radioButtonCSVbezNaglowkow)

        self.radioButtonPlikTAB = QRadioButton(self.centralwidget)
        self.buttonGroup_2.addButton(self.radioButtonPlikTAB)
        self.radioButtonPlikTAB.setObjectName(u"radioButtonPlikTAB")

        self.horizontalLayout_2.addWidget(self.radioButtonPlikTAB)

        self.btnPodgladNotepad = QPushButton(self.centralwidget)
        self.btnPodgladNotepad.setObjectName(u"btnPodgladNotepad")

        self.horizontalLayout_2.addWidget(self.btnPodgladNotepad)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)


        self.horizontalLayout_8.addLayout(self.verticalLayout_6)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_2)

        self.line_12 = QFrame(self.centralwidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_12)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.line_13 = QFrame(self.centralwidget)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.VLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_13)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_12)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_22.addWidget(self.label_4)

        self.txtJakiSeparator = QLineEdit(self.centralwidget)
        self.txtJakiSeparator.setObjectName(u"txtJakiSeparator")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtJakiSeparator.sizePolicy().hasHeightForWidth())
        self.txtJakiSeparator.setSizePolicy(sizePolicy)
        self.txtJakiSeparator.setMinimumSize(QSize(30, 0))
        self.txtJakiSeparator.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_22.addWidget(self.txtJakiSeparator)


        self.verticalLayout_4.addLayout(self.horizontalLayout_22)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_11)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)

        self.line_14 = QFrame(self.centralwidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_14)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_22)

        self.btnOtworzPlik = QPushButton(self.centralwidget)
        self.btnOtworzPlik.setObjectName(u"btnOtworzPlik")

        self.horizontalLayout_8.addWidget(self.btnOtworzPlik)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_21)

        self.line_17 = QFrame(self.centralwidget)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.VLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_17)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_13)

        self.btnPodgladDanych = QPushButton(self.centralwidget)
        self.btnPodgladDanych.setObjectName(u"btnPodgladDanych")

        self.verticalLayout_20.addWidget(self.btnPodgladDanych)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_21.addWidget(self.label_24)

        self.spinBoxUsuwanieKolumny = QSpinBox(self.centralwidget)
        self.spinBoxUsuwanieKolumny.setObjectName(u"spinBoxUsuwanieKolumny")
        self.spinBoxUsuwanieKolumny.setMinimum(-1000)
        self.spinBoxUsuwanieKolumny.setMaximum(1000)

        self.horizontalLayout_21.addWidget(self.spinBoxUsuwanieKolumny)


        self.verticalLayout_20.addLayout(self.horizontalLayout_21)

        self.btnUsunKolumne = QPushButton(self.centralwidget)
        self.btnUsunKolumne.setObjectName(u"btnUsunKolumne")

        self.verticalLayout_20.addWidget(self.btnUsunKolumne)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_14)


        self.horizontalLayout_8.addLayout(self.verticalLayout_20)

        self.line_18 = QFrame(self.centralwidget)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.VLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_18)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_24)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")

        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_21)

        self.radioButtonMiaraSilhouette = QRadioButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButtonMiaraSilhouette)
        self.radioButtonMiaraSilhouette.setObjectName(u"radioButtonMiaraSilhouette")
        self.radioButtonMiaraSilhouette.setChecked(True)

        self.horizontalLayout_19.addWidget(self.radioButtonMiaraSilhouette)

        self.radioButtonMiaraDaviesBoudlin = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.radioButtonMiaraDaviesBoudlin)
        self.radioButtonMiaraDaviesBoudlin.setObjectName(u"radioButtonMiaraDaviesBoudlin")

        self.horizontalLayout_19.addWidget(self.radioButtonMiaraDaviesBoudlin)

        self.radioButtonMiaraCelinskiHarabasz = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.radioButtonMiaraCelinskiHarabasz)
        self.radioButtonMiaraCelinskiHarabasz.setObjectName(u"radioButtonMiaraCelinskiHarabasz")

        self.horizontalLayout_19.addWidget(self.radioButtonMiaraCelinskiHarabasz)


        self.verticalLayout_16.addLayout(self.horizontalLayout_19)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 29))
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_22)


        self.verticalLayout_15.addLayout(self.verticalLayout_3)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_9)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_7)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer)

        self.label_33 = QLabel(self.centralwidget)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_32.addWidget(self.label_33)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_34 = QLabel(self.centralwidget)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_15.addWidget(self.label_34)

        self.spinBoxIleWierszy = QSpinBox(self.centralwidget)
        self.spinBoxIleWierszy.setObjectName(u"spinBoxIleWierszy")
        self.spinBoxIleWierszy.setReadOnly(False)
        self.spinBoxIleWierszy.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBoxIleWierszy.setMaximum(999999)

        self.horizontalLayout_15.addWidget(self.spinBoxIleWierszy)


        self.verticalLayout_31.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_35 = QLabel(self.centralwidget)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_28.addWidget(self.label_35)

        self.spinBoxIleKolumn = QSpinBox(self.centralwidget)
        self.spinBoxIleKolumn.setObjectName(u"spinBoxIleKolumn")
        self.spinBoxIleKolumn.setReadOnly(False)
        self.spinBoxIleKolumn.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBoxIleKolumn.setMaximum(999999)

        self.horizontalLayout_28.addWidget(self.spinBoxIleKolumn)


        self.verticalLayout_31.addLayout(self.horizontalLayout_28)


        self.verticalLayout_32.addLayout(self.verticalLayout_31)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_2)


        self.horizontalLayout_29.addLayout(self.verticalLayout_32)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_2)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_5)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_3)

        self.checkBoxAtrybutDecyzyjny = QCheckBox(self.centralwidget)
        self.checkBoxAtrybutDecyzyjny.setObjectName(u"checkBoxAtrybutDecyzyjny")
        self.checkBoxAtrybutDecyzyjny.setLayoutDirection(Qt.RightToLeft)
        self.checkBoxAtrybutDecyzyjny.setTristate(False)

        self.verticalLayout_29.addWidget(self.checkBoxAtrybutDecyzyjny)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_24.addWidget(self.label_23)

        self.spinBoxIndexAtrybutu = QSpinBox(self.centralwidget)
        self.spinBoxIndexAtrybutu.setObjectName(u"spinBoxIndexAtrybutu")
        self.spinBoxIndexAtrybutu.setMinimum(-1000)
        self.spinBoxIndexAtrybutu.setMaximum(1000)

        self.horizontalLayout_24.addWidget(self.spinBoxIndexAtrybutu)


        self.verticalLayout_29.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_4)


        self.horizontalLayout_29.addLayout(self.verticalLayout_29)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_3)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_8)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_5)

        self.checkBoxAtrybutIndeksujacy = QCheckBox(self.centralwidget)
        self.checkBoxAtrybutIndeksujacy.setObjectName(u"checkBoxAtrybutIndeksujacy")
        self.checkBoxAtrybutIndeksujacy.setLayoutDirection(Qt.RightToLeft)
        self.checkBoxAtrybutIndeksujacy.setTristate(False)

        self.verticalLayout_30.addWidget(self.checkBoxAtrybutIndeksujacy)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_32 = QLabel(self.centralwidget)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_26.addWidget(self.label_32)

        self.spinBoxIndexIndeksujacy = QSpinBox(self.centralwidget)
        self.spinBoxIndexIndeksujacy.setObjectName(u"spinBoxIndexIndeksujacy")
        self.spinBoxIndexIndeksujacy.setMinimum(-1000)
        self.spinBoxIndexIndeksujacy.setMaximum(1000)
        self.spinBoxIndexIndeksujacy.setValue(1)

        self.horizontalLayout_26.addWidget(self.spinBoxIndexIndeksujacy)


        self.verticalLayout_30.addLayout(self.horizontalLayout_26)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_6)


        self.horizontalLayout_29.addLayout(self.verticalLayout_30)

        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_9)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_8)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_10)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.btnLiczCechy = QPushButton(self.centralwidget)
        self.btnLiczCechy.setObjectName(u"btnLiczCechy")

        self.verticalLayout_2.addWidget(self.btnLiczCechy)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)


        self.horizontalLayout_29.addLayout(self.verticalLayout_2)

        self.line_11 = QFrame(self.centralwidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_29.addWidget(self.line_11)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_16)

        self.label_36 = QLabel(self.centralwidget)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_33.addWidget(self.label_36)

        self.lineEditPostep = QLineEdit(self.centralwidget)
        self.lineEditPostep.setObjectName(u"lineEditPostep")
        self.lineEditPostep.setMinimumSize(QSize(350, 0))

        self.verticalLayout_33.addWidget(self.lineEditPostep)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_15)


        self.horizontalLayout_29.addLayout(self.verticalLayout_33)


        self.gridLayout.addLayout(self.horizontalLayout_29, 4, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 29))
        font2 = QFont()
        font2.setPointSize(18)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_3)

        self.tableViewCechyDanych = QTableView(self.centralwidget)
        self.tableViewCechyDanych.setObjectName(u"tableViewCechyDanych")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableViewCechyDanych.sizePolicy().hasHeightForWidth())
        self.tableViewCechyDanych.setSizePolicy(sizePolicy1)
        self.tableViewCechyDanych.setMinimumSize(QSize(350, 50))
        self.tableViewCechyDanych.setMaximumSize(QSize(350, 582))
        self.tableViewCechyDanych.setAutoFillBackground(False)
        self.tableViewCechyDanych.horizontalHeader().setCascadingSectionResizes(True)
        self.tableViewCechyDanych.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_21.addWidget(self.tableViewCechyDanych)


        self.horizontalLayout_27.addLayout(self.verticalLayout_21)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(27, 0))
        self.label_25.setMaximumSize(QSize(16777215, 27))
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_25)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.verticalLayout_22.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)

        self.btnKlasyfikuj = QPushButton(self.centralwidget)
        self.btnKlasyfikuj.setObjectName(u"btnKlasyfikuj")
        self.btnKlasyfikuj.setMinimumSize(QSize(200, 0))
        self.btnKlasyfikuj.setFont(font)

        self.horizontalLayout_16.addWidget(self.btnKlasyfikuj)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_13)


        self.verticalLayout_22.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.AutoText)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.txtProponowanaMetoda = QLineEdit(self.centralwidget)
        self.txtProponowanaMetoda.setObjectName(u"txtProponowanaMetoda")
        self.txtProponowanaMetoda.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_6.addWidget(self.txtProponowanaMetoda)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_22.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(14)
        self.label_6.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.txtWynikProponowanaMetoda = QLineEdit(self.centralwidget)
        self.txtWynikProponowanaMetoda.setObjectName(u"txtWynikProponowanaMetoda")
        self.txtWynikProponowanaMetoda.setMinimumSize(QSize(100, 0))
        self.txtWynikProponowanaMetoda.setMaximumSize(QSize(100, 16777215))
        self.txtWynikProponowanaMetoda.setMaxLength(10000000)

        self.horizontalLayout_4.addWidget(self.txtWynikProponowanaMetoda)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)


        self.verticalLayout_22.addLayout(self.horizontalLayout_4)


        self.verticalLayout_25.addLayout(self.verticalLayout_22)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setFont(font2)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_7)

        self.btnSzukajBruteForce = QPushButton(self.centralwidget)
        self.btnSzukajBruteForce.setObjectName(u"btnSzukajBruteForce")
        self.btnSzukajBruteForce.setFont(font)

        self.verticalLayout_25.addWidget(self.btnSzukajBruteForce)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_17)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.horizontalLayout_17.addWidget(self.label_8)

        self.txtZnalezionaMetodaBF = QLineEdit(self.centralwidget)
        self.txtZnalezionaMetodaBF.setObjectName(u"txtZnalezionaMetodaBF")
        self.txtZnalezionaMetodaBF.setMinimumSize(QSize(250, 0))
        self.txtZnalezionaMetodaBF.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_17.addWidget(self.txtZnalezionaMetodaBF)


        self.verticalLayout_36.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.horizontalLayout_18.addWidget(self.label_20)

        self.txtZnalezionyWynikBF = QLineEdit(self.centralwidget)
        self.txtZnalezionyWynikBF.setObjectName(u"txtZnalezionyWynikBF")
        self.txtZnalezionyWynikBF.setMinimumSize(QSize(100, 0))
        self.txtZnalezionyWynikBF.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_18.addWidget(self.txtZnalezionyWynikBF)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_15)


        self.verticalLayout_36.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_18)


        self.horizontalLayout_34.addLayout(self.verticalLayout_36)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_35.addWidget(self.label_12)

        self.textEditBFGui = QTextEdit(self.centralwidget)
        self.textEditBFGui.setObjectName(u"textEditBFGui")
        self.textEditBFGui.setMinimumSize(QSize(400, 80))
        self.textEditBFGui.setMaximumSize(QSize(16777215, 80))

        self.verticalLayout_35.addWidget(self.textEditBFGui)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_19)


        self.horizontalLayout_34.addLayout(self.verticalLayout_35)


        self.verticalLayout_25.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")

        self.horizontalLayout_33.addLayout(self.verticalLayout_34)


        self.verticalLayout_25.addLayout(self.horizontalLayout_33)


        self.verticalLayout_26.addLayout(self.verticalLayout_25)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_26 = QLabel(self.centralwidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(16777215, 29))
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_26)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)

        self.line_29 = QFrame(self.centralwidget)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_29)

        self.line_30 = QFrame(self.centralwidget)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.VLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_30)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_28 = QLabel(self.centralwidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font3)

        self.verticalLayout_19.addWidget(self.label_28)

        self.txtWynikMetodaZKlasyfikacji = QLineEdit(self.centralwidget)
        self.txtWynikMetodaZKlasyfikacji.setObjectName(u"txtWynikMetodaZKlasyfikacji")

        self.verticalLayout_19.addWidget(self.txtWynikMetodaZKlasyfikacji)


        self.horizontalLayout_20.addLayout(self.verticalLayout_19)

        self.line_21 = QFrame(self.centralwidget)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.VLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_21)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_23)

        self.line_22 = QFrame(self.centralwidget)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.VLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_22)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_27 = QLabel(self.centralwidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.verticalLayout_27.addWidget(self.label_27)

        self.txtWynikZBruteForce = QLineEdit(self.centralwidget)
        self.txtWynikZBruteForce.setObjectName(u"txtWynikZBruteForce")

        self.verticalLayout_27.addWidget(self.txtWynikZBruteForce)


        self.horizontalLayout_20.addLayout(self.verticalLayout_27)

        self.line_23 = QFrame(self.centralwidget)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.VLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_23)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_25)

        self.line_24 = QFrame(self.centralwidget)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.VLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_24)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_29 = QLabel(self.centralwidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.verticalLayout_28.addWidget(self.label_29)

        self.txtBladKlasyfikacji = QLineEdit(self.centralwidget)
        self.txtBladKlasyfikacji.setObjectName(u"txtBladKlasyfikacji")

        self.verticalLayout_28.addWidget(self.txtBladKlasyfikacji)


        self.horizontalLayout_20.addLayout(self.verticalLayout_28)


        self.horizontalLayout_23.addLayout(self.horizontalLayout_20)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_23)

        self.line_31 = QFrame(self.centralwidget)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.VLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_25.addWidget(self.line_31)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_27)


        self.verticalLayout_23.addLayout(self.horizontalLayout_25)


        self.verticalLayout_24.addLayout(self.verticalLayout_23)


        self.verticalLayout_26.addLayout(self.verticalLayout_24)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_19)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_28)

        self.line_32 = QFrame(self.centralwidget)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.VLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_32)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font3)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_9)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)

        self.doubleSpinBoxDBScanEps = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxDBScanEps.setObjectName(u"doubleSpinBoxDBScanEps")
        self.doubleSpinBoxDBScanEps.setMaximum(99999999.000000000000000)

        self.horizontalLayout_11.addWidget(self.doubleSpinBoxDBScanEps)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_13.addWidget(self.label_15)

        self.comboBoxDBScanMetryka = QComboBox(self.centralwidget)
        self.comboBoxDBScanMetryka.setObjectName(u"comboBoxDBScanMetryka")

        self.horizontalLayout_13.addWidget(self.comboBoxDBScanMetryka)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.btnDBScanSprawdz = QPushButton(self.centralwidget)
        self.btnDBScanSprawdz.setObjectName(u"btnDBScanSprawdz")
        self.btnDBScanSprawdz.setFont(font)

        self.verticalLayout_9.addWidget(self.btnDBScanSprawdz)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)


        self.horizontalLayout_12.addLayout(self.verticalLayout_7)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_3)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.line_15 = QFrame(self.centralwidget)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_15)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_14.addWidget(self.label_16)

        self.spinBoxKMeansIloscKlastrow = QSpinBox(self.centralwidget)
        self.spinBoxKMeansIloscKlastrow.setObjectName(u"spinBoxKMeansIloscKlastrow")

        self.horizontalLayout_14.addWidget(self.spinBoxKMeansIloscKlastrow)


        self.verticalLayout_10.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_30.addWidget(self.label_17)

        self.comboBoxKMeansMetryka = QComboBox(self.centralwidget)
        self.comboBoxKMeansMetryka.setObjectName(u"comboBoxKMeansMetryka")

        self.horizontalLayout_30.addWidget(self.comboBoxKMeansMetryka)


        self.verticalLayout_10.addLayout(self.horizontalLayout_30)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.pushButtonKMeansSprawdz = QPushButton(self.centralwidget)
        self.pushButtonKMeansSprawdz.setObjectName(u"pushButtonKMeansSprawdz")
        self.pushButtonKMeansSprawdz.setFont(font)

        self.verticalLayout_11.addWidget(self.pushButtonKMeansSprawdz)


        self.verticalLayout_14.addLayout(self.verticalLayout_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_14)

        self.line_16 = QFrame(self.centralwidget)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.VLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_16)

        self.horizontalSpacer_5 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.line_20 = QFrame(self.centralwidget)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.VLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_20)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_31.addWidget(self.label_18)

        self.spinBoxAgglomerativeIloscKlastrow = QSpinBox(self.centralwidget)
        self.spinBoxAgglomerativeIloscKlastrow.setObjectName(u"spinBoxAgglomerativeIloscKlastrow")

        self.horizontalLayout_31.addWidget(self.spinBoxAgglomerativeIloscKlastrow)


        self.verticalLayout_12.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_32.addWidget(self.label_30)

        self.comboBoxAgglomerativeMetryka = QComboBox(self.centralwidget)
        self.comboBoxAgglomerativeMetryka.setObjectName(u"comboBoxAgglomerativeMetryka")

        self.horizontalLayout_32.addWidget(self.comboBoxAgglomerativeMetryka)


        self.verticalLayout_12.addLayout(self.horizontalLayout_32)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)

        self.pushButtonAgglomerativeSprawdz = QPushButton(self.centralwidget)
        self.pushButtonAgglomerativeSprawdz.setObjectName(u"pushButtonAgglomerativeSprawdz")
        self.pushButtonAgglomerativeSprawdz.setFont(font)

        self.verticalLayout_13.addWidget(self.pushButtonAgglomerativeSprawdz)


        self.verticalLayout_17.addLayout(self.verticalLayout_13)


        self.horizontalLayout_12.addLayout(self.verticalLayout_17)

        self.line_33 = QFrame(self.centralwidget)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.VLine)
        self.line_33.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_33)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_29)


        self.verticalLayout_18.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_19)

        self.label_31 = QLabel(self.centralwidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 200))
        self.label_31.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_31)

        self.txtWynikSprawdzenia = QLineEdit(self.centralwidget)
        self.txtWynikSprawdzenia.setObjectName(u"txtWynikSprawdzenia")

        self.horizontalLayout_9.addWidget(self.txtWynikSprawdzenia)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_20)


        self.verticalLayout_18.addLayout(self.horizontalLayout_9)


        self.verticalLayout_26.addLayout(self.verticalLayout_18)


        self.horizontalLayout_27.addLayout(self.verticalLayout_26)


        self.gridLayout.addLayout(self.horizontalLayout_27, 5, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1193, 20))
        self.menuOpcje = QMenu(self.menubar)
        self.menuOpcje.setObjectName(u"menuOpcje")
        self.menuObliczenia_na_zbiorze = QMenu(self.menubar)
        self.menuObliczenia_na_zbiorze.setObjectName(u"menuObliczenia_na_zbiorze")
        self.menuDzia_ania_na_bazie_wiedzy = QMenu(self.menubar)
        self.menuDzia_ania_na_bazie_wiedzy.setObjectName(u"menuDzia_ania_na_bazie_wiedzy")
        self.menuTesty = QMenu(self.menubar)
        self.menuTesty.setObjectName(u"menuTesty")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuOpcje.menuAction())
        self.menubar.addAction(self.menuObliczenia_na_zbiorze.menuAction())
        self.menubar.addAction(self.menuDzia_ania_na_bazie_wiedzy.menuAction())
        self.menubar.addAction(self.menuTesty.menuAction())
        self.menuOpcje.addAction(self.actionPodgladTabeliTreningowej)
        self.menuOpcje.addAction(self.actionKonfiguracja_klasyfikatora)
        self.menuOpcje.addSeparator()
        self.menuOpcje.addAction(self.actionCzyszczenie)
        self.menuObliczenia_na_zbiorze.addAction(self.actionWariancja_kolumn)
        self.menuDzia_ania_na_bazie_wiedzy.addAction(self.actionEdycja_bazy_wiedzy)
        self.menuTesty.addAction(self.actionTest_Leave_Out_klasyfikatora)
        self.menuTesty.addAction(self.actionTest_parametr_w_klasyfikatora)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Por\u00f3wnanie metod grupowania i przewidywanie metody grupowania dla nowych zbior\u00f3w", None))
        self.actionPodgladTabeliTreningowej.setText(QCoreApplication.translate("MainWindow", u"Podgl\u0105d tabeli treningowej", None))
        self.actionCzyszczenie.setText(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 pola", None))
        self.actionUsuwanieAtrybutu.setText(QCoreApplication.translate("MainWindow", u"Usuwanie atrybutu", None))
        self.actionWariancja_kolumn.setText(QCoreApplication.translate("MainWindow", u"Wariancja kolumn", None))
        self.actionBadanie_atrybutow.setText(QCoreApplication.translate("MainWindow", u"Badanie optymalnego zbioru atrybut\u00f3w", None))
        self.actionRedukuj.setText(QCoreApplication.translate("MainWindow", u"Redukuj", None))
        self.actionReczne_wyznaczanie_miary.setText(QCoreApplication.translate("MainWindow", u"R\u0119czne wyznaczanie miary", None))
        self.actionEdycja_bazy_wiedzy.setText(QCoreApplication.translate("MainWindow", u"Edycja bazy wiedzy", None))
        self.actionTest_Leave_Out_klasyfikatora.setText(QCoreApplication.translate("MainWindow", u"Test Leave Out klasyfikatora", None))
        self.actionTest_parametr_w_klasyfikatora.setText(QCoreApplication.translate("MainWindow", u"Test parametr\u00f3w klasyfikatora", None))
        self.actionKonfiguracja_klasyfikatora.setText(QCoreApplication.translate("MainWindow", u"Konfiguracja klasyfikatora", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wybierz plik", None))
        self.btnWybierzPlik.setText(QCoreApplication.translate("MainWindow", u"Wybierz", None))
        self.radioButtonCSVzNaglowkami.setText(QCoreApplication.translate("MainWindow", u"CSV z nag\u0142owkami", None))
        self.radioButtonCSVbezNaglowkow.setText(QCoreApplication.translate("MainWindow", u"CSV bez nag\u0142owk\u00f3w", None))
        self.radioButtonPlikTAB.setText(QCoreApplication.translate("MainWindow", u"Plik. TAB", None))
        self.btnPodgladNotepad.setText(QCoreApplication.translate("MainWindow", u"Podgl\u0105d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Separator:", None))
        self.btnOtworzPlik.setText(QCoreApplication.translate("MainWindow", u"Otw\u00f3rz", None))
        self.btnPodgladDanych.setText(QCoreApplication.translate("MainWindow", u"Podglad danych", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144 kolumne:", None))
        self.btnUsunKolumne.setText(QCoreApplication.translate("MainWindow", u"Usu\u0144", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Wybierz miar\u0119 jako\u015bci</span></p></body></html>", None))
        self.radioButtonMiaraSilhouette.setText(QCoreApplication.translate("MainWindow", u"Silhouette", None))
        self.radioButtonMiaraDaviesBoudlin.setText(QCoreApplication.translate("MainWindow", u"Davies Bouldin", None))
        self.radioButtonMiaraCelinskiHarabasz.setText(QCoreApplication.translate("MainWindow", u"Calinski Harabasz", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Wyb\u00f3r pliku</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Kszta\u0142t danych", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015bc wierszy", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 kolumn", None))
        self.checkBoxAtrybutDecyzyjny.setText(QCoreApplication.translate("MainWindow", u"Atrybut decyzyjny:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Kt\u00f3ry atrybut:", None))
        self.checkBoxAtrybutIndeksujacy.setText(QCoreApplication.translate("MainWindow", u"Atrybut indeksuj\u0105cy:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Kt\u00f3ry atrybut:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Oblicz cechy zbioru", None))
        self.btnLiczCechy.setText(QCoreApplication.translate("MainWindow", u"Licz cechy", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Post\u0119p oblicze\u0144:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Cechy zbioru</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Klasyfikacja</span></p></body></html>", None))
        self.btnKlasyfikuj.setText(QCoreApplication.translate("MainWindow", u"Klasyfikuj", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Proponowana metoda:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Wynik proponowan\u0105 metod\u0105:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Sprawdzenie metod\u0105 brute force</span></p></body></html>", None))
        self.btnSzukajBruteForce.setText(QCoreApplication.translate("MainWindow", u"Szukaj", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Znaleziona metoda:</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Najlepszy wynik:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Post\u0119p:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">B\u0142\u0105d klasyfikacji</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Wynik metod\u0105 </span></p><p align=\"center\"><span style=\" font-size:12pt;\">z klasyfikacji</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Najlepszy wynik </span></p><p align=\"center\"><span style=\" font-size:12pt;\">metod\u0105 Brute Force:</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">B\u0142\u0105d <br/>klasyfikacji</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Sprawdzenie r\u0119czne</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">DBScan</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"eps", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Metryka", None))
        self.btnDBScanSprawdz.setText(QCoreApplication.translate("MainWindow", u"Sprawd\u017a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">KMeans</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 klastr\u00f3w", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Metryka", None))
        self.pushButtonKMeansSprawdz.setText(QCoreApplication.translate("MainWindow", u"Sprawd\u017a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Agglomerative</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 klastr\u00f3w", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Metryka", None))
        self.pushButtonAgglomerativeSprawdz.setText(QCoreApplication.translate("MainWindow", u"Sprawd\u017a", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Wynik sprawdzenia:</span></p></body></html>", None))
        self.menuOpcje.setTitle(QCoreApplication.translate("MainWindow", u"Opcje", None))
        self.menuObliczenia_na_zbiorze.setTitle(QCoreApplication.translate("MainWindow", u"Obliczenia na zbiorze", None))
        self.menuDzia_ania_na_bazie_wiedzy.setTitle(QCoreApplication.translate("MainWindow", u"Dzia\u0142ania na bazie wiedzy", None))
        self.menuTesty.setTitle(QCoreApplication.translate("MainWindow", u"Testy", None))
    # retranslateUi

