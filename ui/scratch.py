# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\multi-port-gen\ui\scratch.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_scratch(object):
    def setupUi(self, scratch):
        scratch.setObjectName("scratch")
        scratch.resize(800, 553)
        self.centralwidget = QtWidgets.QWidget(scratch)
        self.centralwidget.setObjectName("centralwidget")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(110, 210, 91, 19))
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 260, 72, 15))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(360, 60, 321, 341))
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        scratch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(scratch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        scratch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(scratch)
        self.statusbar.setObjectName("statusbar")
        scratch.setStatusBar(self.statusbar)

        self.retranslateUi(scratch)
        QtCore.QMetaObject.connectSlotsByName(scratch)

    def retranslateUi(self, scratch):
        _translate = QtCore.QCoreApplication.translate
        scratch.setWindowTitle(_translate("scratch", "scratch"))
        self.checkBox.setText(_translate("scratch", "CheckBox"))
        self.label.setText(_translate("scratch", "TextLabel"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("scratch", "a"))
        item = self.listWidget.item(1)
        item.setText(_translate("scratch", "b"))
        item = self.listWidget.item(2)
        item.setText(_translate("scratch", "v"))
        item = self.listWidget.item(3)
        item.setText(_translate("scratch", "c"))
        item = self.listWidget.item(4)
        item.setText(_translate("scratch", "d"))
        item = self.listWidget.item(5)
        item.setText(_translate("scratch", "g"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
