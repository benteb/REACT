# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 436)
        MainWindow.setStyleSheet("\n"
"QMainWindow{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(98, 114, 164);\n"
"}\n"
"\n"
"QScrollBar{\n"
"background-color:rgb(56,58,89);\n"
"\n"
"}\n"
"\n"
"\n"
"QFrame{\n"
"background-color: rgb(56,58,89);\n"
"border: 2px solid rgb(220,220,220);\n"
"border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"color:rgb(98, 114, 164);\n"
"border: 0px;\n"
"}\n"
"\n"
"/* IMPORTANT: 8< Add the code above here 8< */\n"
"QTabBar::tab:selected {\n"
"/* expand/overlap to the left and right by 4px */\n"
"margin-left: -4px;\n"
"margin-right: -4px;\n"
"}\n"
"QTabBar::tab:first:selected {\n"
"margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
"}\n"
"QTabBar::tab:last:selected {\n"
"margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"}\n"
"QTabBar::tab:only-one {\n"
"margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
"}\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"/*border-top: 2px solid #C2C7CB;*/\n"
"border-top:4px solid rgb(56,58,89);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"border: 2px solid rgb(98, 114, 164);\n"
"\n"
"border-bottom-color: rgb(98, 114, 164);\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 8ex;\n"
"padding: 2px;\n"
"color:rgb(220,220,220);\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"/*background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);*/\n"
"background-color:rgb(42,42,42);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"/*border-color: #9B9B9B;*/\n"
"\n"
"    border-color: rgb(98, 114, 164);\n"
"    border-bottom-color: rgb(56,58,89);\n"
"    border-width: 3px;\n"
"    color:rgb(220,220,220);\n"
"    background-color: rgb(56,58,89);\n"
"\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(143, 23, 119);\n"
"      color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:rgb(98, 114, 164);\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius:12px;\n"
"    \n"
"    /*border-color: rgb(12, 103, 213);*/\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"       /*background-color:rgb(17, 145, 255);\n"
"    color: black*/\n"
"    background-color: rgb(42, 42, 42);\n"
"}\n"
"\n"
"QTableView{\n"
"border:None;\n"
"}\n"
"\n"
"QListWidget{\n"
"border:None;\n"
"margin-top:5px;\n"
"margin-left:5px;\n"
"margin-right:5px;\n"
"\n"
"\n"
"\n"
"color:rgb(220,220,220);\n"
"\n"
"}\n"
"\n"
"/* Works for both QListView and QListWidget */\n"
"QListView::item {\n"
"    /* Won\'t work without borders set */\n"
"    padding-left:1px;\n"
"    padding-right:10px;\n"
"    padding-top:1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"QListView::item:hover{\n"
"background-color: rgb(98, 114, 164);\n"
"}\n"
"\n"
"QListView::item:selected{\n"
"color: rgb(42,42,42);\n"
"background-color:rgb(220,220,220);\n"
"padding-left:10px;\n"
"padding-right:-10px;\n"
"\n"
"}\n"
"\n"
"QPlainTextEdit{\n"
"border: None;\n"
"color:rgb(220,220,220);\n"
"}\n"
"\n"
"/*background-color: black;\n"
"color: rgb(220,220,220); */")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(150, 300))
        self.frame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(500, 50))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(500, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 3)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setMinimumSize(QtCore.QSize(200, 300))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser = QtWidgets.QPlainTextEdit(self.frame_5)
        self.textBrowser.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.gridLayout.addWidget(self.frame_5, 1, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMinimumSize(QtCore.QSize(300, 300))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(50, 0))
        self.label_2.setMaximumSize(QtCore.QSize(50, 20))
        self.label_2.setLineWidth(0)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_projectname = QtWidgets.QLabel(self.frame_4)
        self.label_projectname.setMinimumSize(QtCore.QSize(50, 0))
        self.label_projectname.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_projectname.setStyleSheet("color:rgb(200,200,200);")
        self.label_projectname.setObjectName("label_projectname")
        self.horizontalLayout.addWidget(self.label_projectname)
        self.button_open_project = QtWidgets.QPushButton(self.frame_4)
        self.button_open_project.setMinimumSize(QtCore.QSize(24, 24))
        self.button_open_project.setMaximumSize(QtCore.QSize(24, 24))
        self.button_open_project.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_open_project.setIcon(icon)
        self.button_open_project.setIconSize(QtCore.QSize(24, 24))
        self.button_open_project.setFlat(True)
        self.button_open_project.setObjectName("button_open_project")
        self.horizontalLayout.addWidget(self.button_open_project)
        self.button_save_project = QtWidgets.QPushButton(self.frame_4)
        self.button_save_project.setMinimumSize(QtCore.QSize(24, 24))
        self.button_save_project.setMaximumSize(QtCore.QSize(24, 24))
        self.button_save_project.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_save_project.setIcon(icon1)
        self.button_save_project.setIconSize(QtCore.QSize(24, 24))
        self.button_save_project.setFlat(True)
        self.button_save_project.setObjectName("button_save_project")
        self.horizontalLayout.addWidget(self.button_save_project)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.button_add_state = QtWidgets.QPushButton(self.frame_4)
        self.button_add_state.setMinimumSize(QtCore.QSize(24, 24))
        self.button_add_state.setMaximumSize(QtCore.QSize(24, 24))
        self.button_add_state.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/arrow-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add_state.setIcon(icon2)
        self.button_add_state.setIconSize(QtCore.QSize(24, 24))
        self.button_add_state.setFlat(True)
        self.button_add_state.setObjectName("button_add_state")
        self.horizontalLayout_2.addWidget(self.button_add_state)
        self.button_delete_state = QtWidgets.QPushButton(self.frame_4)
        self.button_delete_state.setMinimumSize(QtCore.QSize(24, 24))
        self.button_delete_state.setMaximumSize(QtCore.QSize(24, 24))
        self.button_delete_state.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/arrow-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_delete_state.setIcon(icon3)
        self.button_delete_state.setIconSize(QtCore.QSize(24, 24))
        self.button_delete_state.setFlat(True)
        self.button_delete_state.setObjectName("button_delete_state")
        self.horizontalLayout_2.addWidget(self.button_delete_state)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget.setStyleSheet("border-color:rgb(98, 114, 164);\n"
"")
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 5, 1)
        self.button_delete_file = QtWidgets.QPushButton(self.frame_4)
        self.button_delete_file.setMinimumSize(QtCore.QSize(24, 24))
        self.button_delete_file.setMaximumSize(QtCore.QSize(24, 24))
        self.button_delete_file.setText("")
        self.button_delete_file.setIcon(icon3)
        self.button_delete_file.setIconSize(QtCore.QSize(24, 24))
        self.button_delete_file.setFlat(True)
        self.button_delete_file.setObjectName("button_delete_file")
        self.gridLayout_2.addWidget(self.button_delete_file, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)
        self.button_add_file = QtWidgets.QPushButton(self.frame_4)
        self.button_add_file.setMinimumSize(QtCore.QSize(24, 24))
        self.button_add_file.setMaximumSize(QtCore.QSize(24, 24))
        self.button_add_file.setText("")
        self.button_add_file.setIcon(icon2)
        self.button_add_file.setIconSize(QtCore.QSize(24, 24))
        self.button_add_file.setFlat(True)
        self.button_add_file.setObjectName("button_add_file")
        self.gridLayout_2.addWidget(self.button_add_file, 1, 1, 1, 1)
        self.button_edit_file = QtWidgets.QPushButton(self.frame_4)
        self.button_edit_file.setMinimumSize(QtCore.QSize(24, 24))
        self.button_edit_file.setMaximumSize(QtCore.QSize(24, 24))
        self.button_edit_file.setStyleSheet("")
        self.button_edit_file.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/edit-pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_edit_file.setIcon(icon4)
        self.button_edit_file.setIconSize(QtCore.QSize(24, 24))
        self.button_edit_file.setFlat(True)
        self.button_edit_file.setObjectName("button_edit_file")
        self.gridLayout_2.addWidget(self.button_edit_file, 3, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.button_print_file_3 = QtWidgets.QPushButton(self.frame_4)
        self.button_print_file_3.setMinimumSize(QtCore.QSize(24, 24))
        self.button_print_file_3.setMaximumSize(QtCore.QSize(24, 24))
        self.button_print_file_3.setStyleSheet("")
        self.button_print_file_3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/view_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_print_file_3.setIcon(icon5)
        self.button_print_file_3.setIconSize(QtCore.QSize(24, 24))
        self.button_print_file_3.setFlat(True)
        self.button_print_file_3.setObjectName("button_print_file_3")
        self.gridLayout_3.addWidget(self.button_print_file_3, 0, 1, 1, 1)
        self.button_print_scf = QtWidgets.QPushButton(self.frame_4)
        self.button_print_scf.setMinimumSize(QtCore.QSize(24, 24))
        self.button_print_scf.setMaximumSize(QtCore.QSize(24, 24))
        self.button_print_scf.setStyleSheet("")
        self.button_print_scf.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/quick_print_SCF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_print_scf.setIcon(icon6)
        self.button_print_scf.setIconSize(QtCore.QSize(24, 24))
        self.button_print_scf.setFlat(True)
        self.button_print_scf.setObjectName("button_print_scf")
        self.gridLayout_3.addWidget(self.button_print_scf, 0, 2, 1, 1)
        self.button_print_energy = QtWidgets.QPushButton(self.frame_4)
        self.button_print_energy.setMinimumSize(QtCore.QSize(24, 24))
        self.button_print_energy.setMaximumSize(QtCore.QSize(24, 24))
        self.button_print_energy.setStyleSheet("")
        self.button_print_energy.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/quick_print_E.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_print_energy.setIcon(icon7)
        self.button_print_energy.setIconSize(QtCore.QSize(24, 24))
        self.button_print_energy.setFlat(True)
        self.button_print_energy.setObjectName("button_print_energy")
        self.gridLayout_3.addWidget(self.button_print_energy, 0, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 1, 1, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RE∆CT"))
        self.textBrowser.setPlainText(_translate("MainWindow", "RE∆CT"))
        self.label_2.setText(_translate("MainWindow", "Project:"))
        self.label_projectname.setText(_translate("MainWindow", "new_project"))
        self.label_3.setText(_translate("MainWindow", "States"))
        self.label_4.setText(_translate("MainWindow", "Quick launch"))
        self.pushButton_3.setText(_translate("MainWindow", "func1"))
        self.pushButton_4.setText(_translate("MainWindow", "func2"))

#import icons_rc
