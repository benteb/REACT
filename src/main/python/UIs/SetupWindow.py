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
        SetupWindow.resize(624, 645)
        font = QtGui.QFont()
        font.setPointSize(13)
        SetupWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(SetupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_main)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setContentsMargins(-1, 10, -1, -1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.basis_label_1 = QtWidgets.QLabel(self.tab_main)
        self.basis_label_1.setMinimumSize(QtCore.QSize(70, 0))
        self.basis_label_1.setMaximumSize(QtCore.QSize(70, 16777215))
        self.basis_label_1.setObjectName("basis_label_1")
        self.horizontalLayout_8.addWidget(self.basis_label_1)
        self.comboBox_basis1 = QtWidgets.QComboBox(self.tab_main)
        self.comboBox_basis1.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_basis1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_basis1.setEditable(False)
        self.comboBox_basis1.setObjectName("comboBox_basis1")
        self.horizontalLayout_8.addWidget(self.comboBox_basis1)
        self.comboBox_basis2 = QtWidgets.QComboBox(self.tab_main)
        self.comboBox_basis2.setMinimumSize(QtCore.QSize(53, 0))
        self.comboBox_basis2.setMaximumSize(QtCore.QSize(53, 16777215))
        self.comboBox_basis2.setEditable(False)
        self.comboBox_basis2.setObjectName("comboBox_basis2")
        self.horizontalLayout_8.addWidget(self.comboBox_basis2)
        self.label_5 = QtWidgets.QLabel(self.tab_main)
        self.label_5.setMinimumSize(QtCore.QSize(13, 26))
        self.label_5.setMaximumSize(QtCore.QSize(13, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.comboBox_basis3 = QtWidgets.QComboBox(self.tab_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_basis3.sizePolicy().hasHeightForWidth())
        self.comboBox_basis3.setSizePolicy(sizePolicy)
        self.comboBox_basis3.setMinimumSize(QtCore.QSize(65, 0))
        self.comboBox_basis3.setMaximumSize(QtCore.QSize(65, 16777215))
        self.comboBox_basis3.setEditable(False)
        self.comboBox_basis3.setObjectName("comboBox_basis3")
        self.horizontalLayout_8.addWidget(self.comboBox_basis3)
        self.label_7 = QtWidgets.QLabel(self.tab_main)
        self.label_7.setMinimumSize(QtCore.QSize(16, 26))
        self.label_7.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.comboBox_basis4 = QtWidgets.QComboBox(self.tab_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_basis4.sizePolicy().hasHeightForWidth())
        self.comboBox_basis4.setSizePolicy(sizePolicy)
        self.comboBox_basis4.setMinimumSize(QtCore.QSize(65, 0))
        self.comboBox_basis4.setMaximumSize(QtCore.QSize(65, 16777215))
        self.comboBox_basis4.setEditable(False)
        self.comboBox_basis4.setObjectName("comboBox_basis4")
        self.horizontalLayout_8.addWidget(self.comboBox_basis4)
        self.label_6 = QtWidgets.QLabel(self.tab_main)
        self.label_6.setMinimumSize(QtCore.QSize(12, 26))
        self.label_6.setMaximumSize(QtCore.QSize(12, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.gridLayout_10.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(-1, -1, 10, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Button_add_job = QtWidgets.QPushButton(self.tab_main)
        self.Button_add_job.setMinimumSize(QtCore.QSize(24, 24))
        self.Button_add_job.setMaximumSize(QtCore.QSize(24, 24))
        self.Button_add_job.setStyleSheet("QPushButton {\n"
"    background-color: rgb(143, 23, 119);\n"
"      color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:rgb(143, 23, 119);\n"
"\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius:10px;\n"
"\n"
"    \n"
"    /*border-color: rgb(12, 103, 213);*/\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"       /*background-color:rgb(17, 145, 255);\n"
"    color: black*/\n"
"    background-color: rgb(42, 42, 42);\n"
"}")
        self.Button_add_job.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/arrow-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_add_job.setIcon(icon)
        self.Button_add_job.setIconSize(QtCore.QSize(24, 24))
        self.Button_add_job.setFlat(True)
        self.Button_add_job.setObjectName("Button_add_job")
        self.verticalLayout_9.addWidget(self.Button_add_job)
        self.Button_del_job = QtWidgets.QPushButton(self.tab_main)
        self.Button_del_job.setMinimumSize(QtCore.QSize(24, 24))
        self.Button_del_job.setMaximumSize(QtCore.QSize(24, 24))
        self.Button_del_job.setStyleSheet("QPushButton {\n"
"    background-color: rgb(143, 23, 119);\n"
"      color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:rgb(143, 23, 119);\n"
"\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius:10px;\n"
"\n"
"    \n"
"    /*border-color: rgb(12, 103, 213);*/\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"       /*background-color:rgb(17, 145, 255);\n"
"    color: black*/\n"
"    background-color: rgb(42, 42, 42);\n"
"}")
        self.Button_del_job.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/arrow-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_del_job.setIcon(icon1)
        self.Button_del_job.setIconSize(QtCore.QSize(24, 24))
        self.Button_del_job.setFlat(True)
        self.Button_del_job.setObjectName("Button_del_job")
        self.verticalLayout_9.addWidget(self.Button_del_job)
        self.gridLayout_7.addLayout(self.verticalLayout_9, 1, 1, 2, 1)
        self.LineEdit_add_job = QtWidgets.QLineEdit(self.tab_main)
        self.LineEdit_add_job.setMinimumSize(QtCore.QSize(190, 21))
        self.LineEdit_add_job.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.LineEdit_add_job.setFont(font)
        self.LineEdit_add_job.setText("")
        self.LineEdit_add_job.setObjectName("LineEdit_add_job")
        self.gridLayout_7.addWidget(self.LineEdit_add_job, 1, 0, 1, 1)
        self.additional_job = QtWidgets.QLabel(self.tab_main)
        self.additional_job.setMinimumSize(QtCore.QSize(150, 15))
        self.additional_job.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setItalic(True)
        self.additional_job.setFont(font)
        self.additional_job.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.additional_job.setObjectName("additional_job")
        self.gridLayout_7.addWidget(self.additional_job, 0, 0, 1, 1)
        self.List_add_job = QtWidgets.QListWidget(self.tab_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.List_add_job.sizePolicy().hasHeightForWidth())
        self.List_add_job.setSizePolicy(sizePolicy)
        self.List_add_job.setMinimumSize(QtCore.QSize(200, 50))
        self.List_add_job.setMaximumSize(QtCore.QSize(1529996, 16777215))
        self.List_add_job.setStyleSheet("QListWidget{    \n"
" background-color: rgb(20,20,20);        \n"
"  border:None;\n"
"  margin-top:0px;    \n"
"  margin-left:0px;\n"
"  margin-right:0px;    \n"
" }")
        self.List_add_job.setObjectName("List_add_job")
        self.gridLayout_7.addWidget(self.List_add_job, 2, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_7, 4, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.funct_label_1 = QtWidgets.QLabel(self.tab_main)
        self.funct_label_1.setMinimumSize(QtCore.QSize(70, 0))
        self.funct_label_1.setMaximumSize(QtCore.QSize(70, 16777215))
        self.funct_label_1.setObjectName("funct_label_1")
        self.horizontalLayout_7.addWidget(self.funct_label_1)
        self.comboBox_funct = QtWidgets.QComboBox(self.tab_main)
        self.comboBox_funct.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_funct.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_funct.setEditable(False)
        self.comboBox_funct.setObjectName("comboBox_funct")
        self.horizontalLayout_7.addWidget(self.comboBox_funct)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.gridLayout_10.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.label_route_3 = QtWidgets.QLabel(self.tab_main)
        self.label_route_3.setMinimumSize(QtCore.QSize(90, 50))
        self.label_route_3.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_route_3.setFont(font)
        self.label_route_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_route_3.setObjectName("label_route_3")
        self.gridLayout_10.addWidget(self.label_route_3, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.tab_main)
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.lineEdit_filename = QtWidgets.QLineEdit(self.tab_main)
        self.lineEdit_filename.setPlaceholderText("")
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.horizontalLayout_9.addWidget(self.lineEdit_filename)
        self.label_3 = QtWidgets.QLabel(self.tab_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.comboBox_job_type = QtWidgets.QComboBox(self.tab_main)
        self.comboBox_job_type.setMinimumSize(QtCore.QSize(180, 0))
        self.comboBox_job_type.setObjectName("comboBox_job_type")
        self.horizontalLayout_9.addWidget(self.comboBox_job_type)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.gridLayout_10.addLayout(self.horizontalLayout_9, 0, 1, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.checkBox_placeholder1 = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_placeholder1.setObjectName("checkBox_placeholder1")
        self.horizontalLayout_10.addWidget(self.checkBox_placeholder1)
        self.checkBox_placeholder2 = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_placeholder2.setObjectName("checkBox_placeholder2")
        self.horizontalLayout_10.addWidget(self.checkBox_placeholder2)
        self.checkBox_placeholder3 = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_placeholder3.setObjectName("checkBox_placeholder3")
        self.horizontalLayout_10.addWidget(self.checkBox_placeholder3)
        self.checkBox_placeholder4 = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_placeholder4.setObjectName("checkBox_placeholder4")
        self.horizontalLayout_10.addWidget(self.checkBox_placeholder4)
        self.gridLayout_10.addLayout(self.horizontalLayout_10, 3, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_10)
        self.line = QtWidgets.QFrame(self.tab_main)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_mem = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_mem.setObjectName("checkBox_mem")
        self.horizontalLayout_3.addWidget(self.checkBox_mem)
        self.lineEdit_mem = QtWidgets.QLineEdit(self.tab_main)
        self.lineEdit_mem.setObjectName("lineEdit_mem")
        self.horizontalLayout_3.addWidget(self.lineEdit_mem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_chk = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_chk.setObjectName("checkBox_chk")
        self.horizontalLayout.addWidget(self.checkBox_chk)
        self.lineEdit_chk = QtWidgets.QLineEdit(self.tab_main)
        self.lineEdit_chk.setObjectName("lineEdit_chk")
        self.horizontalLayout.addWidget(self.lineEdit_chk)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_schk = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_schk.setObjectName("checkBox_schk")
        self.horizontalLayout_5.addWidget(self.checkBox_schk)
        self.lineEdit_schk = QtWidgets.QLineEdit(self.tab_main)
        self.lineEdit_schk.setObjectName("lineEdit_schk")
        self.horizontalLayout_5.addWidget(self.lineEdit_schk)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_oldchk = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_oldchk.setObjectName("checkBox_oldchk")
        self.horizontalLayout_6.addWidget(self.checkBox_oldchk)
        self.lineEdit_oldchk = QtWidgets.QLineEdit(self.tab_main)
        self.lineEdit_oldchk.setMinimumSize(QtCore.QSize(130, 21))
        self.lineEdit_oldchk.setObjectName("lineEdit_oldchk")
        self.horizontalLayout_6.addWidget(self.lineEdit_oldchk)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_rwf = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_rwf.setObjectName("checkBox_rwf")
        self.horizontalLayout_4.addWidget(self.checkBox_rwf)
        self.lineEdit_rwf = QtWidgets.QLineEdit(self.tab_main)
        self.lineEdit_rwf.setObjectName("lineEdit_rwf")
        self.horizontalLayout_4.addWidget(self.lineEdit_rwf)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 1, 3, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.button_add_link0 = QtWidgets.QPushButton(self.tab_main)
        self.button_add_link0.setMinimumSize(QtCore.QSize(24, 24))
        self.button_add_link0.setMaximumSize(QtCore.QSize(24, 24))
        self.button_add_link0.setStyleSheet("QPushButton {\n"
"    background-color: rgb(143, 23, 119);\n"
"      color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:rgb(143, 23, 119);\n"
"\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius:10px;\n"
"\n"
"    \n"
"    /*border-color: rgb(12, 103, 213);*/\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"       /*background-color:rgb(17, 145, 255);\n"
"    color: black*/\n"
"    background-color: rgb(42, 42, 42);\n"
"}")
        self.button_add_link0.setText("")
        self.button_add_link0.setIcon(icon)
        self.button_add_link0.setIconSize(QtCore.QSize(24, 24))
        self.button_add_link0.setFlat(True)
        self.button_add_link0.setObjectName("button_add_link0")
        self.verticalLayout_8.addWidget(self.button_add_link0)
        self.button_del_link0 = QtWidgets.QPushButton(self.tab_main)
        self.button_del_link0.setMinimumSize(QtCore.QSize(24, 24))
        self.button_del_link0.setMaximumSize(QtCore.QSize(24, 24))
        self.button_del_link0.setStyleSheet("QPushButton {\n"
"    background-color: rgb(143, 23, 119);\n"
"      color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:rgb(143, 23, 119);\n"
"\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius:10px;\n"
"\n"
"    \n"
"    /*border-color: rgb(12, 103, 213);*/\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"       /*background-color:rgb(17, 145, 255);\n"
"    color: black*/\n"
"    background-color: rgb(42, 42, 42);\n"
"}")
        self.button_del_link0.setText("")
        self.button_del_link0.setIcon(icon1)
        self.button_del_link0.setIconSize(QtCore.QSize(24, 24))
        self.button_del_link0.setFlat(True)
        self.button_del_link0.setObjectName("button_del_link0")
        self.verticalLayout_8.addWidget(self.button_del_link0)
        self.gridLayout_8.addLayout(self.verticalLayout_8, 2, 1, 2, 1)
        self.label_add_route = QtWidgets.QLabel(self.tab_main)
        self.label_add_route.setMaximumSize(QtCore.QSize(16777215, 10))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_add_route.setFont(font)
        self.label_add_route.setObjectName("label_add_route")
        self.gridLayout_8.addWidget(self.label_add_route, 1, 0, 1, 1)
        self.lineEdit_link0 = QtWidgets.QLineEdit(self.tab_main)
        self.lineEdit_link0.setMinimumSize(QtCore.QSize(190, 21))
        self.lineEdit_link0.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEdit_link0.setFont(font)
        self.lineEdit_link0.setText("")
        self.lineEdit_link0.setObjectName("lineEdit_link0")
        self.gridLayout_8.addWidget(self.lineEdit_link0, 2, 0, 1, 1)
        self.list_link0 = QtWidgets.QListWidget(self.tab_main)
        self.list_link0.setMinimumSize(QtCore.QSize(190, 50))
        self.list_link0.setMaximumSize(QtCore.QSize(190000, 16777215))
        self.list_link0.setStyleSheet("QListWidget{    \n"
" background-color: rgb(20,20,20);        \n"
"  border:None;\n"
"  margin-top:0px;    \n"
"  margin-left:0px;\n"
"  margin-right:0px;    \n"
" }")
        self.list_link0.setObjectName("list_link0")
        self.gridLayout_8.addWidget(self.list_link0, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem3, 0, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 2, 2, 1, 1)
        self.checkBox_errorsave = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_errorsave.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_errorsave.setObjectName("checkBox_errorsave")
        self.gridLayout_9.addWidget(self.checkBox_errorsave, 1, 2, 1, 1)
        self.label_route = QtWidgets.QLabel(self.tab_main)
        self.label_route.setMinimumSize(QtCore.QSize(90, 50))
        self.label_route.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_route.setFont(font)
        self.label_route.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_route.setObjectName("label_route")
        self.gridLayout_9.addWidget(self.label_route, 0, 0, 2, 1)
        self.checkBox_save = QtWidgets.QCheckBox(self.tab_main)
        self.checkBox_save.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox_save.setObjectName("checkBox_save")
        self.gridLayout_9.addWidget(self.checkBox_save, 0, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_9)
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_freeze = QtWidgets.QWidget()
        self.tab_freeze.setObjectName("tab_freeze")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_freeze)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.comboBox_freezetype = QtWidgets.QComboBox(self.tab_freeze)
        self.comboBox_freezetype.setObjectName("comboBox_freezetype")
        self.comboBox_freezetype.addItem("")
        self.comboBox_freezetype.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_freezetype, 0, 0, 1, 1)
        self.button_auto_freeze = QtWidgets.QPushButton(self.tab_freeze)
        self.button_auto_freeze.setObjectName("button_auto_freeze")
        self.gridLayout_6.addWidget(self.button_auto_freeze, 0, 1, 1, 1)
        self.button_add_from_pymol = QtWidgets.QPushButton(self.tab_freeze)
        self.button_add_from_pymol.setObjectName("button_add_from_pymol")
        self.gridLayout_6.addWidget(self.button_add_from_pymol, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_6)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab_freeze)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.list_model = QtWidgets.QListWidget(self.tab_freeze)
        self.list_model.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(11)
        self.list_model.setFont(font)
        self.list_model.setStyleSheet("border 2px solid rgb(143, 23, 119);\n"
"")
        self.list_model.setObjectName("list_model")
        self.gridLayout_2.addWidget(self.list_model, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 3, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem4, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab_freeze)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.list_freeze_atoms = QtWidgets.QListWidget(self.tab_freeze)
        self.list_freeze_atoms.setMinimumSize(QtCore.QSize(150, 0))
        self.list_freeze_atoms.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(11)
        self.list_freeze_atoms.setFont(font)
        self.list_freeze_atoms.setStyleSheet("border 2px solid rgb(143, 23, 119)")
        self.list_freeze_atoms.setObjectName("list_freeze_atoms")
        self.gridLayout_3.addWidget(self.list_freeze_atoms, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 2, 3, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.button_add_state = QtWidgets.QPushButton(self.tab_freeze)
        self.button_add_state.setMinimumSize(QtCore.QSize(24, 24))
        self.button_add_state.setMaximumSize(QtCore.QSize(24, 24))
        self.button_add_state.setStyleSheet("QPushButton {\n"
"    background-color: rgb(143, 23, 119);\n"
"      color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:rgb(143, 23, 119);\n"
"\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius:10px;\n"
"\n"
"    \n"
"    /*border-color: rgb(12, 103, 213);*/\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"       /*background-color:rgb(17, 145, 255);\n"
"    color: black*/\n"
"    background-color: rgb(42, 42, 42);\n"
"}")
        self.button_add_state.setText("")
        self.button_add_state.setIcon(icon)
        self.button_add_state.setIconSize(QtCore.QSize(24, 24))
        self.button_add_state.setFlat(True)
        self.button_add_state.setObjectName("button_add_state")
        self.gridLayout_4.addWidget(self.button_add_state, 0, 0, 1, 1)
        self.button_delete_state = QtWidgets.QPushButton(self.tab_freeze)
        self.button_delete_state.setMinimumSize(QtCore.QSize(24, 24))
        self.button_delete_state.setMaximumSize(QtCore.QSize(24, 24))
        self.button_delete_state.setStyleSheet("QPushButton {\n"
"    background-color: rgb(143, 23, 119);\n"
"      color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color:rgb(143, 23, 119);\n"
"\n"
"    border-style: outset;\n"
"    border-width: 0px;\n"
"    border-radius:10px;\n"
"\n"
"    \n"
"    /*border-color: rgb(12, 103, 213);*/\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"       /*background-color:rgb(17, 145, 255);\n"
"    color: black*/\n"
"    background-color: rgb(42, 42, 42);\n"
"}")
        self.button_delete_state.setText("")
        self.button_delete_state.setIcon(icon1)
        self.button_delete_state.setIconSize(QtCore.QSize(24, 24))
        self.button_delete_state.setFlat(True)
        self.button_delete_state.setObjectName("button_delete_state")
        self.gridLayout_4.addWidget(self.button_delete_state, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.tab_freeze, "")
        self.tab_scan = QtWidgets.QWidget()
        self.tab_scan.setObjectName("tab_scan")
        self.tabWidget.addTab(self.tab_scan, "")
        self.tab_view = QtWidgets.QWidget()
        self.tab_view.setObjectName("tab_view")
        self.tabWidget.addTab(self.tab_view, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(12, 1, -1, 1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button_cancel = QtWidgets.QPushButton(self.frame_2)
        self.button_cancel.setMinimumSize(QtCore.QSize(0, 40))
        self.button_cancel.setObjectName("button_cancel")
        self.gridLayout.addWidget(self.button_cancel, 0, 0, 1, 1)
        self.button_write = QtWidgets.QPushButton(self.frame_2)
        self.button_write.setMinimumSize(QtCore.QSize(0, 40))
        self.button_write.setObjectName("button_write")
        self.gridLayout.addWidget(self.button_write, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.frame_2)
        SetupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SetupWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SetupWindow)

    def retranslateUi(self, SetupWindow):
        _translate = QtCore.QCoreApplication.translate
        SetupWindow.setWindowTitle(_translate("SetupWindow", "MainWindow"))
        self.basis_label_1.setText(_translate("SetupWindow", "Basis set:"))
        self.label_5.setText(_translate("SetupWindow", "("))
        self.label_7.setText(_translate("SetupWindow", " ,"))
        self.label_6.setText(_translate("SetupWindow", " )"))
        self.additional_job.setText(_translate("SetupWindow", "Additional job details:"))
        self.funct_label_1.setText(_translate("SetupWindow", "Functional:"))
        self.label_route_3.setText(_translate("SetupWindow", "Job details"))
        self.label_4.setText(_translate("SetupWindow", "filename:"))
        self.label_3.setText(_translate("SetupWindow", "Job type:"))
        self.checkBox_placeholder1.setText(_translate("SetupWindow", "placeholder"))
        self.checkBox_placeholder2.setText(_translate("SetupWindow", "placeholder"))
        self.checkBox_placeholder3.setText(_translate("SetupWindow", "placeholder"))
        self.checkBox_placeholder4.setText(_translate("SetupWindow", "placeholder"))
        self.checkBox_mem.setText(_translate("SetupWindow", "Memory"))
        self.checkBox_chk.setText(_translate("SetupWindow", "Chk"))
        self.checkBox_schk.setText(_translate("SetupWindow", "SChk"))
        self.checkBox_oldchk.setText(_translate("SetupWindow", "OldChk"))
        self.checkBox_rwf.setText(_translate("SetupWindow", "RWF"))
        self.label_add_route.setText(_translate("SetupWindow", "Additional link 0 details:"))
        self.checkBox_errorsave.setText(_translate("SetupWindow", "ErrorSave"))
        self.label_route.setText(_translate("SetupWindow", "Link 0 details"))
        self.checkBox_save.setText(_translate("SetupWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("SetupWindow", "Main"))
        self.comboBox_freezetype.setItemText(0, _translate("SetupWindow", "Atom"))
        self.comboBox_freezetype.setItemText(1, _translate("SetupWindow", "Bond"))
        self.button_auto_freeze.setText(_translate("SetupWindow", "Auto-freeze"))
        self.button_add_from_pymol.setText(_translate("SetupWindow", "Add Pymol selected"))
        self.label.setText(_translate("SetupWindow", "Atoms in model"))
        self.label_2.setText(_translate("SetupWindow", "Atoms to freeze"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_freeze), _translate("SetupWindow", "Freeze"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scan), _translate("SetupWindow", "Scan"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_view), _translate("SetupWindow", "Preview"))
        self.button_cancel.setText(_translate("SetupWindow", "Cancel"))
        self.button_write.setText(_translate("SetupWindow", "Write"))
#import icons_rc
