from PySide2.QtCore import QSize
from PySide2.QtWidgets import QDialog, QTableView


class PodgladDanych(QDialog):
    def __init__(self, model):
        QDialog.__init__(self)
        self.resize(QSize(1081, 750))
        self.model = model
        self.tableViewPodgladDanych = QTableView(self)
        self.tableViewPodgladDanych.resize(QSize(1070, 740))
        self.tableViewPodgladDanych.setModel(model)
