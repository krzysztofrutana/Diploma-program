# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testParametrow.ui'
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


class Ui_FormTestParametrow(object):
    def setupUi(self, FormTestParametrow):
        if not FormTestParametrow.objectName():
            FormTestParametrow.setObjectName(u"FormTestParametrow")
        FormTestParametrow.resize(642, 549)
        self.gridLayout = QGridLayout(FormTestParametrow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(FormTestParametrow)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBoxKlasyfikatory = QComboBox(FormTestParametrow)
        self.comboBoxKlasyfikatory.setObjectName(u"comboBoxKlasyfikatory")
        self.comboBoxKlasyfikatory.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.comboBoxKlasyfikatory)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.btnTestuj = QPushButton(FormTestParametrow)
        self.btnTestuj.setObjectName(u"btnTestuj")

        self.horizontalLayout_2.addWidget(self.btnTestuj)

        self.btnZapiszWyniki = QPushButton(FormTestParametrow)
        self.btnZapiszWyniki.setObjectName(u"btnZapiszWyniki")

        self.horizontalLayout_2.addWidget(self.btnZapiszWyniki)

        self.btnPokazTabele = QPushButton(FormTestParametrow)
        self.btnPokazTabele.setObjectName(u"btnPokazTabele")

        self.horizontalLayout_2.addWidget(self.btnPokazTabele)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.checkBoxCriterion = QCheckBox(FormTestParametrow)
        self.checkBoxCriterion.setObjectName(u"checkBoxCriterion")

        self.horizontalLayout_13.addWidget(self.checkBoxCriterion)

        self.line = QFrame(FormTestParametrow)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line)

        self.label_12 = QLabel(FormTestParametrow)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_13.addWidget(self.label_12)

        self.lineEditCriterion_2 = QLineEdit(FormTestParametrow)
        self.lineEditCriterion_2.setObjectName(u"lineEditCriterion_2")
        self.lineEditCriterion_2.setMinimumSize(QSize(400, 0))

        self.horizontalLayout_13.addWidget(self.lineEditCriterion_2)


        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBoxMaxDepth = QCheckBox(FormTestParametrow)
        self.checkBoxMaxDepth.setObjectName(u"checkBoxMaxDepth")

        self.horizontalLayout_9.addWidget(self.checkBoxMaxDepth)

        self.line_2 = QFrame(FormTestParametrow)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_9.addWidget(self.line_2)

        self.label_8 = QLabel(FormTestParametrow)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.label_14 = QLabel(FormTestParametrow)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.spinBoxMaxDepthOd = QSpinBox(FormTestParametrow)
        self.spinBoxMaxDepthOd.setObjectName(u"spinBoxMaxDepthOd")

        self.horizontalLayout_9.addWidget(self.spinBoxMaxDepthOd)

        self.label_15 = QLabel(FormTestParametrow)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_9.addWidget(self.label_15)

        self.spinBoxMaxDepthDo = QSpinBox(FormTestParametrow)
        self.spinBoxMaxDepthDo.setObjectName(u"spinBoxMaxDepthDo")
        self.spinBoxMaxDepthDo.setMinimum(1)
        self.spinBoxMaxDepthDo.setMaximum(999)

        self.horizontalLayout_9.addWidget(self.spinBoxMaxDepthDo)

        self.label_16 = QLabel(FormTestParametrow)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_9.addWidget(self.label_16)

        self.spinBoxMaxDepthCo = QSpinBox(FormTestParametrow)
        self.spinBoxMaxDepthCo.setObjectName(u"spinBoxMaxDepthCo")
        self.spinBoxMaxDepthCo.setValue(1)

        self.horizontalLayout_9.addWidget(self.spinBoxMaxDepthCo)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.checkBoxRandomState = QCheckBox(FormTestParametrow)
        self.checkBoxRandomState.setObjectName(u"checkBoxRandomState")

        self.horizontalLayout_10.addWidget(self.checkBoxRandomState)

        self.line_3 = QFrame(FormTestParametrow)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_3)

        self.label_11 = QLabel(FormTestParametrow)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.spinBoxRandomState_2 = QSpinBox(FormTestParametrow)
        self.spinBoxRandomState_2.setObjectName(u"spinBoxRandomState_2")

        self.horizontalLayout_10.addWidget(self.spinBoxRandomState_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkBoxMinSamplesLeaf = QCheckBox(FormTestParametrow)
        self.checkBoxMinSamplesLeaf.setObjectName(u"checkBoxMinSamplesLeaf")

        self.horizontalLayout_11.addWidget(self.checkBoxMinSamplesLeaf)

        self.line_4 = QFrame(FormTestParametrow)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_4)

        self.label_10 = QLabel(FormTestParametrow)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_11.addWidget(self.label_10)

        self.label_18 = QLabel(FormTestParametrow)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)

        self.spinBoxMinSamplesLeafOd = QSpinBox(FormTestParametrow)
        self.spinBoxMinSamplesLeafOd.setObjectName(u"spinBoxMinSamplesLeafOd")

        self.horizontalLayout_11.addWidget(self.spinBoxMinSamplesLeafOd)

        self.label_19 = QLabel(FormTestParametrow)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_11.addWidget(self.label_19)

        self.spinBoxMinSamplesLeafDo = QSpinBox(FormTestParametrow)
        self.spinBoxMinSamplesLeafDo.setObjectName(u"spinBoxMinSamplesLeafDo")
        self.spinBoxMinSamplesLeafDo.setMinimum(1)
        self.spinBoxMinSamplesLeafDo.setMaximum(999)

        self.horizontalLayout_11.addWidget(self.spinBoxMinSamplesLeafDo)

        self.label_20 = QLabel(FormTestParametrow)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_11.addWidget(self.label_20)

        self.spinBoxMinSaplesLeafCo = QSpinBox(FormTestParametrow)
        self.spinBoxMinSaplesLeafCo.setObjectName(u"spinBoxMinSaplesLeafCo")
        self.spinBoxMinSaplesLeafCo.setValue(1)

        self.horizontalLayout_11.addWidget(self.spinBoxMinSaplesLeafCo)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.checkBoxMinSamplesSplit = QCheckBox(FormTestParametrow)
        self.checkBoxMinSamplesSplit.setObjectName(u"checkBoxMinSamplesSplit")

        self.horizontalLayout_12.addWidget(self.checkBoxMinSamplesSplit)

        self.line_5 = QFrame(FormTestParametrow)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_5)

        self.label_9 = QLabel(FormTestParametrow)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_12.addWidget(self.label_9)

        self.label_21 = QLabel(FormTestParametrow)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_12.addWidget(self.label_21)

        self.spinBoxMinSamplesSplitOd = QSpinBox(FormTestParametrow)
        self.spinBoxMinSamplesSplitOd.setObjectName(u"spinBoxMinSamplesSplitOd")

        self.horizontalLayout_12.addWidget(self.spinBoxMinSamplesSplitOd)

        self.label_22 = QLabel(FormTestParametrow)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_12.addWidget(self.label_22)

        self.spinBoxMinSaplesSplitDo = QSpinBox(FormTestParametrow)
        self.spinBoxMinSaplesSplitDo.setObjectName(u"spinBoxMinSaplesSplitDo")
        self.spinBoxMinSaplesSplitDo.setMinimum(1)
        self.spinBoxMinSaplesSplitDo.setMaximum(999)

        self.horizontalLayout_12.addWidget(self.spinBoxMinSaplesSplitDo)

        self.label_23 = QLabel(FormTestParametrow)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_12.addWidget(self.label_23)

        self.spinBoxMinSamplesSplitCo = QSpinBox(FormTestParametrow)
        self.spinBoxMinSamplesSplitCo.setObjectName(u"spinBoxMinSamplesSplitCo")
        self.spinBoxMinSamplesSplitCo.setValue(1)

        self.horizontalLayout_12.addWidget(self.spinBoxMinSamplesSplitCo)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.checkBoxSpliter = QCheckBox(FormTestParametrow)
        self.checkBoxSpliter.setObjectName(u"checkBoxSpliter")

        self.horizontalLayout_14.addWidget(self.checkBoxSpliter)

        self.line_6 = QFrame(FormTestParametrow)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_6)

        self.label_13 = QLabel(FormTestParametrow)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_14.addWidget(self.label_13)

        self.lineEditSpliter_2 = QLineEdit(FormTestParametrow)
        self.lineEditSpliter_2.setObjectName(u"lineEditSpliter_2")

        self.horizontalLayout_14.addWidget(self.lineEditSpliter_2)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.txtWyniki = QTextEdit(FormTestParametrow)
        self.txtWyniki.setObjectName(u"txtWyniki")

        self.verticalLayout.addWidget(self.txtWyniki)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(FormTestParametrow)

        QMetaObject.connectSlotsByName(FormTestParametrow)
    # setupUi

    def retranslateUi(self, FormTestParametrow):
        FormTestParametrow.setWindowTitle(QCoreApplication.translate("FormTestParametrow", u"Test parametr\u00f3w klasyfikatora", None))
        self.label.setText(QCoreApplication.translate("FormTestParametrow", u"Kt\u00f3ry klasyfikator testowa\u0107:", None))
        self.btnTestuj.setText(QCoreApplication.translate("FormTestParametrow", u"Testuj", None))
        self.btnZapiszWyniki.setText(QCoreApplication.translate("FormTestParametrow", u"Zapisz wyniki", None))
        self.btnPokazTabele.setText(QCoreApplication.translate("FormTestParametrow", u"Poka\u017c tabel\u0119 bazow\u0105", None))
        self.checkBoxCriterion.setText(QCoreApplication.translate("FormTestParametrow", u"Dodaj do sprawdzenia", None))
        self.label_12.setText(QCoreApplication.translate("FormTestParametrow", u"criterion:", None))
        self.checkBoxMaxDepth.setText(QCoreApplication.translate("FormTestParametrow", u"Dodaj do sprawdzenia", None))
        self.label_8.setText(QCoreApplication.translate("FormTestParametrow", u"max_depth:", None))
        self.label_14.setText(QCoreApplication.translate("FormTestParametrow", u"od:", None))
        self.label_15.setText(QCoreApplication.translate("FormTestParametrow", u"do:", None))
        self.label_16.setText(QCoreApplication.translate("FormTestParametrow", u"co:", None))
        self.checkBoxRandomState.setText(QCoreApplication.translate("FormTestParametrow", u"Dodaj do sprawdzenia", None))
        self.label_11.setText(QCoreApplication.translate("FormTestParametrow", u"random_state:", None))
        self.checkBoxMinSamplesLeaf.setText(QCoreApplication.translate("FormTestParametrow", u"Dodaj do sprawdzenia", None))
        self.label_10.setText(QCoreApplication.translate("FormTestParametrow", u"min_samples_leaf:", None))
        self.label_18.setText(QCoreApplication.translate("FormTestParametrow", u"od:", None))
        self.label_19.setText(QCoreApplication.translate("FormTestParametrow", u"do:", None))
        self.label_20.setText(QCoreApplication.translate("FormTestParametrow", u"co:", None))
        self.checkBoxMinSamplesSplit.setText(QCoreApplication.translate("FormTestParametrow", u"Dodaj do sprawdzenia", None))
        self.label_9.setText(QCoreApplication.translate("FormTestParametrow", u"min_samples_split:", None))
        self.label_21.setText(QCoreApplication.translate("FormTestParametrow", u"od:", None))
        self.label_22.setText(QCoreApplication.translate("FormTestParametrow", u"do:", None))
        self.label_23.setText(QCoreApplication.translate("FormTestParametrow", u"co:", None))
        self.checkBoxSpliter.setText(QCoreApplication.translate("FormTestParametrow", u"Dodaj do sprawdzenia", None))
        self.label_13.setText(QCoreApplication.translate("FormTestParametrow", u"splitter:", None))
    # retranslateUi

