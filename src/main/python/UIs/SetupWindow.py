# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetupWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetupWindow(object):
    def setupUi(self, SetupWindow):
        SetupWindow.setObjectName("SetupWindow")
        SetupWindow.resize(599, 500)
        self.centralwidget = QtWidgets.QWidget(SetupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_freeze = QtWidgets.QWidget()
        self.tab_freeze.setObjectName("tab_freeze")
        self.tabWidget.addTab(self.tab_freeze, "")
        self.tab_scan = QtWidgets.QWidget()
        self.tab_scan.setObjectName("tab_scan")
        self.tabWidget.addTab(self.tab_scan, "")
        self.tab_view = QtWidgets.QWidget()
        self.tab_view.setObjectName("tab_view")
        self.tabWidget.addTab(self.tab_view, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(183, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_cancel = QtWidgets.QPushButton(self.frame_2)
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout.addWidget(self.button_cancel, 0, 0, 1, 1)
        self.button_write = QtWidgets.QPushButton(self.frame_2)
        self.button_write.setObjectName("button_write")
        self.gridLayout.addWidget(self.button_write, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(182, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_2)
        SetupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SetupWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SetupWindow)

    def retranslateUi(self, SetupWindow):
        _translate = QtCore.QCoreApplication.translate
        SetupWindow.setWindowTitle(_translate("SetupWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("SetupWindow", "Main"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_freeze), _translate("SetupWindow", "Freeze"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scan), _translate("SetupWindow", "Scan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_view), _translate("SetupWindow", "Preview"))
        self.button_cancel.setText(_translate("SetupWindow", "Cancel"))
        self.button_write.setText(_translate("SetupWindow", "Write"))
