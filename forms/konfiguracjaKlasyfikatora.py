# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'konfiguracjaKlasyfikatora.ui'
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


class Ui_FormKonfiguracjaKlasyfikatora(object):
    def setupUi(self, FormKonfiguracjaKlasyfikatora):
        if not FormKonfiguracjaKlasyfikatora.objectName():
            FormKonfiguracjaKlasyfikatora.setObjectName(u"FormKonfiguracjaKlasyfikatora")
        FormKonfiguracjaKlasyfikatora.resize(523, 415)
        self.gridLayout = QGridLayout(FormKonfiguracjaKlasyfikatora)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(FormKonfiguracjaKlasyfikatora)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.comboBoxWyborKlasyfikatora = QComboBox(FormKonfiguracjaKlasyfikatora)
        self.comboBoxWyborKlasyfikatora.setObjectName(u"comboBoxWyborKlasyfikatora")
        self.comboBoxWyborKlasyfikatora.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_7.addWidget(self.comboBoxWyborKlasyfikatora)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(FormKonfiguracjaKlasyfikatora)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.comboBoxWyborMiar = QComboBox(FormKonfiguracjaKlasyfikatora)
        self.comboBoxWyborMiar.setObjectName(u"comboBoxWyborMiar")
        self.comboBoxWyborMiar.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_8.addWidget(self.comboBoxWyborMiar)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButtonWczytajKonfiguracje = QPushButton(FormKonfiguracjaKlasyfikatora)
        self.pushButtonWczytajKonfiguracje.setObjectName(u"pushButtonWczytajKonfiguracje")

        self.verticalLayout.addWidget(self.pushButtonWczytajKonfiguracje)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(FormKonfiguracjaKlasyfikatora)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditCriterion = QLineEdit(FormKonfiguracjaKlasyfikatora)
        self.lineEditCriterion.setObjectName(u"lineEditCriterion")

        self.horizontalLayout.addWidget(self.lineEditCriterion)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(FormKonfiguracjaKlasyfikatora)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBoxMaxDepth = QSpinBox(FormKonfiguracjaKlasyfikatora)
        self.spinBoxMaxDepth.setObjectName(u"spinBoxMaxDepth")

        self.horizontalLayout_2.addWidget(self.spinBoxMaxDepth)

        self.checkBoxMaxDepthNone = QCheckBox(FormKonfiguracjaKlasyfikatora)
        self.checkBoxMaxDepthNone.setObjectName(u"checkBoxMaxDepthNone")

        self.horizontalLayout_2.addWidget(self.checkBoxMaxDepthNone)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(FormKonfiguracjaKlasyfikatora)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBoxRandomState = QSpinBox(FormKonfiguracjaKlasyfikatora)
        self.spinBoxRandomState.setObjectName(u"spinBoxRandomState")

        self.horizontalLayout_3.addWidget(self.spinBoxRandomState)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(FormKonfiguracjaKlasyfikatora)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.spinBoxMinSamplesLeaf = QSpinBox(FormKonfiguracjaKlasyfikatora)
        self.spinBoxMinSamplesLeaf.setObjectName(u"spinBoxMinSamplesLeaf")

        self.horizontalLayout_4.addWidget(self.spinBoxMinSamplesLeaf)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(FormKonfiguracjaKlasyfikatora)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.spinBoxMinSamplesSplit = QSpinBox(FormKonfiguracjaKlasyfikatora)
        self.spinBoxMinSamplesSplit.setObjectName(u"spinBoxMinSamplesSplit")

        self.horizontalLayout_5.addWidget(self.spinBoxMinSamplesSplit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(FormKonfiguracjaKlasyfikatora)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEditSpliter = QLineEdit(FormKonfiguracjaKlasyfikatora)
        self.lineEditSpliter.setObjectName(u"lineEditSpliter")

        self.horizontalLayout_6.addWidget(self.lineEditSpliter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_11)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.btnZapisz = QPushButton(FormKonfiguracjaKlasyfikatora)
        self.btnZapisz.setObjectName(u"btnZapisz")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnZapisz.sizePolicy().hasHeightForWidth())
        self.btnZapisz.setSizePolicy(sizePolicy)
        self.btnZapisz.setMinimumSize(QSize(100, 0))
        self.btnZapisz.setMaximumSize(QSize(100, 16777215))
        self.btnZapisz.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_2.addWidget(self.btnZapisz)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.retranslateUi(FormKonfiguracjaKlasyfikatora)

        QMetaObject.connectSlotsByName(FormKonfiguracjaKlasyfikatora)
    # setupUi

    def retranslateUi(self, FormKonfiguracjaKlasyfikatora):
        FormKonfiguracjaKlasyfikatora.setWindowTitle(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"Konfiguracja parametr\u00f3w klasyfikatora", None))
        self.label_7.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"Wybierz klasyfikator:", None))
        self.label_8.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"Wybierz miar\u0119:", None))
        self.pushButtonWczytajKonfiguracje.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"Wczytaj konfiguracj\u0119", None))
        self.label.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"criterion:", None))
        self.label_2.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"max_depth:", None))
        self.checkBoxMaxDepthNone.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"zaznacz je\u015bli None", None))
        self.label_3.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"random_state:", None))
        self.label_4.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"min_samples_leaf:", None))
        self.label_5.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"min_samples_split:", None))
        self.label_6.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"splitter:", None))
        self.btnZapisz.setText(QCoreApplication.translate("FormKonfiguracjaKlasyfikatora", u"Zapisz", None))
    # retranslateUi

