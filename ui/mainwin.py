# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Administrator\Desktop\PQv2ray\ui\mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setVerticalSpacing(8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.nodeSelectorPane = QtWidgets.QWidget(self.centralwidget)
        self.nodeSelectorPane.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeSelectorPane.sizePolicy().hasHeightForWidth())
        self.nodeSelectorPane.setSizePolicy(sizePolicy)
        self.nodeSelectorPane.setObjectName("nodeSelectorPane")
        self.gridLayout = QtWidgets.QGridLayout(self.nodeSelectorPane)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btnAppendToRight = QtWidgets.QPushButton(self.nodeSelectorPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAppendToRight.sizePolicy().hasHeightForWidth())
        self.btnAppendToRight.setSizePolicy(sizePolicy)
        self.btnAppendToRight.setMinimumSize(QtCore.QSize(40, 40))
        self.btnAppendToRight.setObjectName("btnAppendToRight")
        self.verticalLayout_2.addWidget(self.btnAppendToRight)
        self.btnDeleteFromRight = QtWidgets.QPushButton(self.nodeSelectorPane)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeleteFromRight.sizePolicy().hasHeightForWidth())
        self.btnDeleteFromRight.setSizePolicy(sizePolicy)
        self.btnDeleteFromRight.setMinimumSize(QtCore.QSize(40, 40))
        self.btnDeleteFromRight.setObjectName("btnDeleteFromRight")
        self.verticalLayout_2.addWidget(self.btnDeleteFromRight)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnCheckAllRight = QtWidgets.QPushButton(self.nodeSelectorPane)
        self.btnCheckAllRight.setObjectName("btnCheckAllRight")
        self.horizontalLayout_2.addWidget(self.btnCheckAllRight)
        self.btnUncheckAllRight = QtWidgets.QPushButton(self.nodeSelectorPane)
        self.btnUncheckAllRight.setObjectName("btnUncheckAllRight")
        self.horizontalLayout_2.addWidget(self.btnUncheckAllRight)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.listViewLeft = MyListView(self.nodeSelectorPane)
        self.listViewLeft.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewLeft.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listViewLeft.setResizeMode(QtWidgets.QListView.Adjust)
        self.listViewLeft.setObjectName("listViewLeft")
        self.gridLayout.addWidget(self.listViewLeft, 1, 0, 1, 1)
        self.listViewRight = MyListView(self.nodeSelectorPane)
        self.listViewRight.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listViewRight.setDragDropOverwriteMode(False)
        self.listViewRight.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listViewRight.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listViewRight.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listViewRight.setResizeMode(QtWidgets.QListView.Adjust)
        self.listViewRight.setObjectName("listViewRight")
        self.gridLayout.addWidget(self.listViewRight, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btnCheckAllLeft = QtWidgets.QPushButton(self.nodeSelectorPane)
        self.btnCheckAllLeft.setObjectName("btnCheckAllLeft")
        self.horizontalLayout.addWidget(self.btnCheckAllLeft)
        self.btnUncheckAllLeft = QtWidgets.QPushButton(self.nodeSelectorPane)
        self.btnUncheckAllLeft.setObjectName("btnUncheckAllLeft")
        self.horizontalLayout.addWidget(self.btnUncheckAllLeft)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, -1, 4, -1)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labFilter = QtWidgets.QLabel(self.nodeSelectorPane)
        self.labFilter.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labFilter.setObjectName("labFilter")
        self.horizontalLayout_6.addWidget(self.labFilter)
        self.editFilter = QtWidgets.QLineEdit(self.nodeSelectorPane)
        self.editFilter.setObjectName("editFilter")
        self.horizontalLayout_6.addWidget(self.editFilter)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.nodeSelectorPane, 2, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setContentsMargins(14, -1, 14, -1)
        self.horizontalLayout_5.setSpacing(24)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.comboGroups = QtWidgets.QComboBox(self.groupBox_2)
        self.comboGroups.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboGroups.sizePolicy().hasHeightForWidth())
        self.comboGroups.setSizePolicy(sizePolicy)
        self.comboGroups.setMinimumSize(QtCore.QSize(200, 0))
        self.comboGroups.setObjectName("comboGroups")
        self.horizontalLayout_4.addWidget(self.comboGroups)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.editQvConfigFolder = QtWidgets.QLineEdit(self.groupBox_2)
        self.editQvConfigFolder.setObjectName("editQvConfigFolder")
        self.horizontalLayout_3.addWidget(self.editQvConfigFolder)
        self.btnBrwsQvConfigFolder = QtWidgets.QPushButton(self.groupBox_2)
        self.btnBrwsQvConfigFolder.setObjectName("btnBrwsQvConfigFolder")
        self.horizontalLayout_3.addWidget(self.btnBrwsQvConfigFolder)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 2)
        self.groupBoxBtns = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxBtns.setEnabled(False)
        self.groupBoxBtns.setTitle("")
        self.groupBoxBtns.setObjectName("groupBoxBtns")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBoxBtns)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.btnQv2rayMultiPort = QtWidgets.QPushButton(self.groupBoxBtns)
        self.btnQv2rayMultiPort.setObjectName("btnQv2rayMultiPort")
        self.verticalLayout.addWidget(self.btnQv2rayMultiPort)
        self.btnQv2rayBalancer = QtWidgets.QPushButton(self.groupBoxBtns)
        self.btnQv2rayBalancer.setObjectName("btnQv2rayBalancer")
        self.verticalLayout.addWidget(self.btnQv2rayBalancer)
        self.btnQv2rayMultiPortBalancer = QtWidgets.QPushButton(self.groupBoxBtns)
        self.btnQv2rayMultiPortBalancer.setEnabled(False)
        self.btnQv2rayMultiPortBalancer.setObjectName("btnQv2rayMultiPortBalancer")
        self.verticalLayout.addWidget(self.btnQv2rayMultiPortBalancer)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.gridLayout_3.addWidget(self.groupBoxBtns, 2, 2, 1, 2)
        self.btnSettings = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSettings.sizePolicy().hasHeightForWidth())
        self.btnSettings.setSizePolicy(sizePolicy)
        self.btnSettings.setText("")
        self.btnSettings.setIconSize(QtCore.QSize(30, 30))
        self.btnSettings.setObjectName("btnSettings")
        self.gridLayout_3.addWidget(self.btnSettings, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qv2ray 复杂配置小工具"))
        self.btnCheckAllRight.setText(_translate("MainWindow", "全选"))
        self.btnUncheckAllRight.setText(_translate("MainWindow", "全不选"))
        self.btnCheckAllLeft.setText(_translate("MainWindow", "全选"))
        self.btnUncheckAllLeft.setText(_translate("MainWindow", "全不选"))
        self.labFilter.setText(_translate("MainWindow", "筛选"))
        self.label_2.setText(_translate("MainWindow", "节点组"))
        self.label.setText(_translate("MainWindow", "Qv2ray 配置目录"))
        self.btnBrwsQvConfigFolder.setText(_translate("MainWindow", "浏览"))
        self.btnQv2rayMultiPort.setText(_translate("MainWindow", "多端口"))
        self.btnQv2rayBalancer.setText(_translate("MainWindow", "负载均衡"))
        self.btnQv2rayMultiPortBalancer.setText(_translate("MainWindow", "多端口负载均衡"))
from ui.mylistview import MyListView
