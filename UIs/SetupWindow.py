# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetupWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SetupWindow(object):
    def setupUi(self, SetupWindow):
        SetupWindow.setObjectName("SetupWindow")
        SetupWindow.resize(792, 715)
        font = QtGui.QFont()
        font.setPointSize(13)
        SetupWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(SetupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("\n"
"QListWidget\n"
"{\n"
"border : 2px solid rgb(143, 23, 119);\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"border : 2px solid rgb(143, 23, 119);\n"
"background-color: rgb(20,20,20);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: rgb(20,20,20);\n"
"}\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_main)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_main)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 705, 802))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.lineEdit_filename = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_filename.setMinimumSize(QtCore.QSize(220, 0))
        self.lineEdit_filename.setPlaceholderText("")
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.horizontalLayout_9.addWidget(self.lineEdit_filename)
        self.checkBox_cp_to_reactmain = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_cp_to_reactmain.setChecked(True)
        self.checkBox_cp_to_reactmain.setObjectName("checkBox_cp_to_reactmain")
        self.horizontalLayout_9.addWidget(self.checkBox_cp_to_reactmain)
        spacerItem = QtWidgets.QSpacerItem(162, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setMaximumSize(QtCore.QSize(127, 96))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_27.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_33 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.gridLayout_27.addWidget(self.label_33, 1, 1, 1, 1)
        self.lineEdit_charge = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_charge.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEdit_charge.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_charge.setFont(font)
        self.lineEdit_charge.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_charge.setObjectName("lineEdit_charge")
        self.gridLayout_27.addWidget(self.lineEdit_charge, 1, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.gridLayout_27.addWidget(self.label_34, 2, 1, 1, 1)
        self.lineEdit_multiplicity = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_multiplicity.setMinimumSize(QtCore.QSize(25, 25))
        self.lineEdit_multiplicity.setMaximumSize(QtCore.QSize(25, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_multiplicity.setFont(font)
        self.lineEdit_multiplicity.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_multiplicity.setObjectName("lineEdit_multiplicity")
        self.gridLayout_27.addWidget(self.lineEdit_multiplicity, 2, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_27.addWidget(self.label_32, 0, 1, 1, 2)
        self.horizontalLayout_9.addWidget(self.frame)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem1)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_25.addWidget(self.label_31)
        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_25.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_25.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_25.addWidget(self.radioButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.funct_label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.funct_label_1.setMinimumSize(QtCore.QSize(70, 0))
        self.funct_label_1.setMaximumSize(QtCore.QSize(70, 16777215))
        self.funct_label_1.setObjectName("funct_label_1")
        self.horizontalLayout_7.addWidget(self.funct_label_1)
        self.comboBox_funct = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_funct.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_funct.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_funct.setEditable(False)
        self.comboBox_funct.setObjectName("comboBox_funct")
        self.horizontalLayout_7.addWidget(self.comboBox_funct)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.basis_label_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.basis_label_1.setMinimumSize(QtCore.QSize(70, 0))
        self.basis_label_1.setMaximumSize(QtCore.QSize(70, 16777215))
        self.basis_label_1.setObjectName("basis_label_1")
        self.horizontalLayout_8.addWidget(self.basis_label_1)
        self.comboBox_basis1 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_basis1.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_basis1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_basis1.setEditable(False)
        self.comboBox_basis1.setObjectName("comboBox_basis1")
        self.horizontalLayout_8.addWidget(self.comboBox_basis1)
        self.comboBox_basis2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_basis2.setMinimumSize(QtCore.QSize(53, 0))
        self.comboBox_basis2.setMaximumSize(QtCore.QSize(53, 16777215))
        self.comboBox_basis2.setEditable(False)
        self.comboBox_basis2.setObjectName("comboBox_basis2")
        self.horizontalLayout_8.addWidget(self.comboBox_basis2)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setMinimumSize(QtCore.QSize(13, 26))
        self.label_5.setMaximumSize(QtCore.QSize(13, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.comboBox_basis3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
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
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setMinimumSize(QtCore.QSize(16, 26))
        self.label_7.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.comboBox_basis4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
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
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setMinimumSize(QtCore.QSize(12, 26))
        self.label_6.setMaximumSize(QtCore.QSize(12, 16))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setContentsMargins(-1, -1, 10, -1)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Button_add_job_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_add_job_2.setMinimumSize(QtCore.QSize(24, 24))
        self.Button_add_job_2.setMaximumSize(QtCore.QSize(24, 24))
        self.Button_add_job_2.setStyleSheet("QPushButton {\n"
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
        self.Button_add_job_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/arrow-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_add_job_2.setIcon(icon)
        self.Button_add_job_2.setIconSize(QtCore.QSize(24, 24))
        self.Button_add_job_2.setFlat(True)
        self.Button_add_job_2.setObjectName("Button_add_job_2")
        self.verticalLayout_10.addWidget(self.Button_add_job_2)
        self.Button_del_job_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_del_job_2.setMinimumSize(QtCore.QSize(24, 24))
        self.Button_del_job_2.setMaximumSize(QtCore.QSize(24, 24))
        self.Button_del_job_2.setStyleSheet("QPushButton {\n"
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
        self.Button_del_job_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/arrow-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_del_job_2.setIcon(icon1)
        self.Button_del_job_2.setIconSize(QtCore.QSize(24, 24))
        self.Button_del_job_2.setFlat(True)
        self.Button_del_job_2.setObjectName("Button_del_job_2")
        self.verticalLayout_10.addWidget(self.Button_del_job_2)
        self.gridLayout_10.addLayout(self.verticalLayout_10, 1, 1, 2, 1)
        self.LineEdit_add_job_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.LineEdit_add_job_2.setMinimumSize(QtCore.QSize(100, 21))
        self.LineEdit_add_job_2.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.LineEdit_add_job_2.setFont(font)
        self.LineEdit_add_job_2.setText("")
        self.LineEdit_add_job_2.setObjectName("LineEdit_add_job_2")
        self.gridLayout_10.addWidget(self.LineEdit_add_job_2, 1, 0, 1, 1)
        self.additional_job_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.additional_job_2.setMinimumSize(QtCore.QSize(150, 15))
        self.additional_job_2.setMaximumSize(QtCore.QSize(100, 15))
        font = QtGui.QFont()
        font.setItalic(True)
        self.additional_job_2.setFont(font)
        self.additional_job_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.additional_job_2.setObjectName("additional_job_2")
        self.gridLayout_10.addWidget(self.additional_job_2, 0, 0, 1, 1)
        self.List_add_job_2 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.List_add_job_2.sizePolicy().hasHeightForWidth())
        self.List_add_job_2.setSizePolicy(sizePolicy)
        self.List_add_job_2.setMinimumSize(QtCore.QSize(0, 0))
        self.List_add_job_2.setMaximumSize(QtCore.QSize(16777215, 888888))
        self.List_add_job_2.setStyleSheet("QListWidget{    \n"
" background-color: rgb(20,20,20);        \n"
"  border:None;\n"
"  margin-top:0px;    \n"
"  margin-left:0px;\n"
"  margin-right:0px;    \n"
" }")
        self.List_add_job_2.setObjectName("List_add_job_2")
        self.gridLayout_10.addWidget(self.List_add_job_2, 2, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_10)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.comboBox_job_type = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_job_type.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_job_type.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_job_type.setObjectName("comboBox_job_type")
        self.horizontalLayout_10.addWidget(self.comboBox_job_type)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.checkbox_freq = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkbox_freq.setEnabled(True)
        self.checkbox_freq.setObjectName("checkbox_freq")
        self.horizontalLayout_10.addWidget(self.checkbox_freq)
        self.checkBox_raman = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_raman.setObjectName("checkBox_raman")
        self.horizontalLayout_10.addWidget(self.checkBox_raman)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setContentsMargins(-1, -1, 10, -1)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Button_add_job = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
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
        self.Button_add_job.setIcon(icon)
        self.Button_add_job.setIconSize(QtCore.QSize(24, 24))
        self.Button_add_job.setFlat(True)
        self.Button_add_job.setObjectName("Button_add_job")
        self.verticalLayout_9.addWidget(self.Button_add_job)
        self.Button_del_job = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
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
        self.Button_del_job.setIcon(icon1)
        self.Button_del_job.setIconSize(QtCore.QSize(24, 24))
        self.Button_del_job.setFlat(True)
        self.Button_del_job.setObjectName("Button_del_job")
        self.verticalLayout_9.addWidget(self.Button_del_job)
        self.gridLayout_7.addLayout(self.verticalLayout_9, 1, 1, 2, 1)
        self.LineEdit_add_job = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.LineEdit_add_job.setMinimumSize(QtCore.QSize(100, 21))
        self.LineEdit_add_job.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.LineEdit_add_job.setFont(font)
        self.LineEdit_add_job.setText("")
        self.LineEdit_add_job.setObjectName("LineEdit_add_job")
        self.gridLayout_7.addWidget(self.LineEdit_add_job, 1, 0, 1, 1)
        self.additional_job = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.additional_job.setMinimumSize(QtCore.QSize(150, 0))
        self.additional_job.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setItalic(True)
        self.additional_job.setFont(font)
        self.additional_job.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.additional_job.setObjectName("additional_job")
        self.gridLayout_7.addWidget(self.additional_job, 0, 0, 1, 1)
        self.List_add_job = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.List_add_job.sizePolicy().hasHeightForWidth())
        self.List_add_job.setSizePolicy(sizePolicy)
        self.List_add_job.setMinimumSize(QtCore.QSize(0, 0))
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
        self.verticalLayout_4.addLayout(self.gridLayout_7)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.checkbox_SCRF = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkbox_SCRF.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.checkbox_SCRF.setFont(font)
        self.checkbox_SCRF.setObjectName("checkbox_SCRF")
        self.horizontalLayout_13.addWidget(self.checkbox_SCRF)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.comboBox_SCRF = QtWidgets.QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_SCRF.setMinimumSize(QtCore.QSize(120, 0))
        self.comboBox_SCRF.setMaximumSize(QtCore.QSize(120, 16777215))
        self.comboBox_SCRF.setObjectName("comboBox_SCRF")
        self.horizontalLayout_13.addWidget(self.comboBox_SCRF)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_13.addWidget(self.label_16)
        self.lineEdit_solvent = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_solvent.setObjectName("lineEdit_solvent")
        self.horizontalLayout_13.addWidget(self.lineEdit_solvent)
        self.checkbox_eps = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkbox_eps.setEnabled(True)
        self.checkbox_eps.setObjectName("checkbox_eps")
        self.horizontalLayout_13.addWidget(self.checkbox_eps)
        self.lineEdit_eps = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_eps.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_eps.setObjectName("lineEdit_eps")
        self.horizontalLayout_13.addWidget(self.lineEdit_eps)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBox_mem_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_mem_2.setMinimumSize(QtCore.QSize(80, 0))
        self.checkBox_mem_2.setObjectName("checkBox_mem_2")
        self.gridLayout_9.addWidget(self.checkBox_mem_2, 0, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setContentsMargins(-1, -1, 10, -1)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.Button_add_link0 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_add_link0.setMinimumSize(QtCore.QSize(24, 24))
        self.Button_add_link0.setMaximumSize(QtCore.QSize(24, 24))
        self.Button_add_link0.setStyleSheet("QPushButton {\n"
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
        self.Button_add_link0.setText("")
        self.Button_add_link0.setIcon(icon)
        self.Button_add_link0.setIconSize(QtCore.QSize(24, 24))
        self.Button_add_link0.setFlat(True)
        self.Button_add_link0.setObjectName("Button_add_link0")
        self.verticalLayout_12.addWidget(self.Button_add_link0)
        self.Button_del_link0 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_del_link0.setMinimumSize(QtCore.QSize(24, 24))
        self.Button_del_link0.setMaximumSize(QtCore.QSize(24, 24))
        self.Button_del_link0.setStyleSheet("QPushButton {\n"
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
        self.Button_del_link0.setText("")
        self.Button_del_link0.setIcon(icon1)
        self.Button_del_link0.setIconSize(QtCore.QSize(24, 24))
        self.Button_del_link0.setFlat(True)
        self.Button_del_link0.setObjectName("Button_del_link0")
        self.verticalLayout_12.addWidget(self.Button_del_link0)
        self.gridLayout_12.addLayout(self.verticalLayout_12, 1, 1, 2, 1)
        self.LineEdit_link0 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.LineEdit_link0.setMinimumSize(QtCore.QSize(100, 21))
        self.LineEdit_link0.setMaximumSize(QtCore.QSize(16777215, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.LineEdit_link0.setFont(font)
        self.LineEdit_link0.setText("")
        self.LineEdit_link0.setObjectName("LineEdit_link0")
        self.gridLayout_12.addWidget(self.LineEdit_link0, 1, 0, 1, 1)
        self.additional_job_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.additional_job_4.setMinimumSize(QtCore.QSize(150, 0))
        self.additional_job_4.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setItalic(True)
        self.additional_job_4.setFont(font)
        self.additional_job_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.additional_job_4.setObjectName("additional_job_4")
        self.gridLayout_12.addWidget(self.additional_job_4, 0, 0, 1, 1)
        self.list_link0 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_link0.sizePolicy().hasHeightForWidth())
        self.list_link0.setSizePolicy(sizePolicy)
        self.list_link0.setMinimumSize(QtCore.QSize(0, 0))
        self.list_link0.setMaximumSize(QtCore.QSize(1529996, 16777215))
        self.list_link0.setStyleSheet("QListWidget{    \n"
" background-color: rgb(20,20,20);        \n"
"  border:None;\n"
"  margin-top:0px;    \n"
"  margin-left:0px;\n"
"  margin-right:0px;    \n"
" }")
        self.list_link0.setObjectName("list_link0")
        self.gridLayout_12.addWidget(self.list_link0, 2, 0, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_12, 0, 2, 3, 1)
        self.checkBox_chk = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_chk.setMinimumSize(QtCore.QSize(80, 0))
        self.checkBox_chk.setObjectName("checkBox_chk")
        self.gridLayout_9.addWidget(self.checkBox_chk, 1, 0, 1, 1)
        self.lineEdit_chk = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_chk.setObjectName("lineEdit_chk")
        self.gridLayout_9.addWidget(self.lineEdit_chk, 1, 1, 1, 1)
        self.checkBox_oldchk = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_oldchk.setMinimumSize(QtCore.QSize(80, 0))
        self.checkBox_oldchk.setObjectName("checkBox_oldchk")
        self.gridLayout_9.addWidget(self.checkBox_oldchk, 2, 0, 1, 1)
        self.lineEdit_oldchk = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_oldchk.setMinimumSize(QtCore.QSize(0, 21))
        self.lineEdit_oldchk.setObjectName("lineEdit_oldchk")
        self.gridLayout_9.addWidget(self.lineEdit_oldchk, 2, 1, 1, 1)
        self.lineEdit_mem_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.lineEdit_mem_2.setObjectName("lineEdit_mem_2")
        self.gridLayout_9.addWidget(self.lineEdit_mem_2, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_9)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_14.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_movepair = QtWidgets.QWidget()
        self.tab_movepair.setObjectName("tab_movepair")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab_movepair)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_21 = QtWidgets.QLabel(self.tab_movepair)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_15.addWidget(self.label_21, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_24 = QtWidgets.QLabel(self.tab_movepair)
        self.label_24.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_6.addWidget(self.label_24)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.radioButton_plus_mv = QtWidgets.QRadioButton(self.tab_movepair)
        self.radioButton_plus_mv.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_plus_mv.setChecked(True)
        self.radioButton_plus_mv.setObjectName("radioButton_plus_mv")
        self.horizontalLayout_11.addWidget(self.radioButton_plus_mv)
        self.radioButton_minus_mv = QtWidgets.QRadioButton(self.tab_movepair)
        self.radioButton_minus_mv.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_minus_mv.setObjectName("radioButton_minus_mv")
        self.horizontalLayout_11.addWidget(self.radioButton_minus_mv)
        self.gridLayout_20.addLayout(self.horizontalLayout_11, 0, 2, 1, 1)
        self.spinbox_mv_bonds = QtWidgets.QDoubleSpinBox(self.tab_movepair)
        self.spinbox_mv_bonds.setDecimals(2)
        self.spinbox_mv_bonds.setMinimum(-99.0)
        self.spinbox_mv_bonds.setMaximum(99.0)
        self.spinbox_mv_bonds.setSingleStep(0.1)
        self.spinbox_mv_bonds.setProperty("value", 1.0)
        self.spinbox_mv_bonds.setObjectName("spinbox_mv_bonds")
        self.gridLayout_20.addWidget(self.spinbox_mv_bonds, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_movepair)
        self.label_9.setObjectName("label_9")
        self.gridLayout_20.addWidget(self.label_9, 0, 0, 1, 1)
        self.spinbox_curr_mv = QtWidgets.QDoubleSpinBox(self.tab_movepair)
        self.spinbox_curr_mv.setObjectName("spinbox_curr_mv")
        self.gridLayout_20.addWidget(self.spinbox_curr_mv, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_20)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_21.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem8)
        self.gridLayout_21.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.checkBox_moveboth_mv = QtWidgets.QCheckBox(self.tab_movepair)
        self.checkBox_moveboth_mv.setEnabled(True)
        self.checkBox_moveboth_mv.setObjectName("checkBox_moveboth_mv")
        self.gridLayout_21.addWidget(self.checkBox_moveboth_mv, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_21)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.pushButton_create_mv = QtWidgets.QPushButton(self.tab_movepair)
        self.pushButton_create_mv.setMinimumSize(QtCore.QSize(400, 50))
        self.pushButton_create_mv.setObjectName("pushButton_create_mv")
        self.verticalLayout_6.addWidget(self.pushButton_create_mv)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.Button_save_new_geometry = QtWidgets.QPushButton(self.tab_movepair)
        self.Button_save_new_geometry.setMinimumSize(QtCore.QSize(400, 50))
        self.Button_save_new_geometry.setObjectName("Button_save_new_geometry")
        self.verticalLayout_5.addWidget(self.Button_save_new_geometry)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout_15.addLayout(self.verticalLayout_6, 0, 1, 2, 1)
        self.list_model_mv = QtWidgets.QListWidget(self.tab_movepair)
        self.list_model_mv.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(11)
        self.list_model_mv.setFont(font)
        self.list_model_mv.setStyleSheet("border 2px solid rgb(143, 23, 119);\n"
"\n"
"")
        self.list_model_mv.setObjectName("list_model_mv")
        self.gridLayout_15.addWidget(self.list_model_mv, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_movepair, "")
        self.tab_freeze = QtWidgets.QWidget()
        self.tab_freeze.setObjectName("tab_freeze")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_freeze)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.comboBox_freezetype = QtWidgets.QComboBox(self.tab_freeze)
        self.comboBox_freezetype.setObjectName("comboBox_freezetype")
        self.comboBox_freezetype.addItem("")
        self.comboBox_freezetype.addItem("")
        self.comboBox_freezetype.addItem("")
        self.comboBox_freezetype.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_freezetype)
        self.button_auto_freeze = QtWidgets.QPushButton(self.tab_freeze)
        self.button_auto_freeze.setObjectName("button_auto_freeze")
        self.horizontalLayout_5.addWidget(self.button_auto_freeze)
        spacerItem10 = QtWidgets.QSpacerItem(349, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.gridLayout_8.addLayout(self.horizontalLayout_5, 0, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.list_model = QtWidgets.QListWidget(self.tab_freeze)
        self.list_model.setMinimumSize(QtCore.QSize(300, 500))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(11)
        self.list_model.setFont(font)
        self.list_model.setStyleSheet("border 2px solid rgb(143, 23, 119);\n"
"\n"
"")
        self.list_model.setObjectName("list_model")
        self.gridLayout_4.addWidget(self.list_model, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_freeze)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_4, 1, 0, 5, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.tab_freeze)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem11, 0, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem12, 0, 2, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_5)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.list_freeze_atoms = QtWidgets.QListWidget(self.tab_freeze)
        self.list_freeze_atoms.setMinimumSize(QtCore.QSize(150, 0))
        self.list_freeze_atoms.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(11)
        self.list_freeze_atoms.setFont(font)
        self.list_freeze_atoms.setStyleSheet("border 2px solid rgb(143, 23, 119)")
        self.list_freeze_atoms.setObjectName("list_freeze_atoms")
        self.gridLayout_2.addWidget(self.list_freeze_atoms, 0, 1, 4, 1)
        self.button_add_freeze = QtWidgets.QPushButton(self.tab_freeze)
        self.button_add_freeze.setMinimumSize(QtCore.QSize(24, 24))
        self.button_add_freeze.setMaximumSize(QtCore.QSize(24, 24))
        self.button_add_freeze.setStyleSheet("QPushButton {\n"
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
        self.button_add_freeze.setText("")
        self.button_add_freeze.setIcon(icon)
        self.button_add_freeze.setIconSize(QtCore.QSize(24, 24))
        self.button_add_freeze.setFlat(True)
        self.button_add_freeze.setObjectName("button_add_freeze")
        self.gridLayout_2.addWidget(self.button_add_freeze, 1, 0, 1, 1)
        self.button_delete_freeze = QtWidgets.QPushButton(self.tab_freeze)
        self.button_delete_freeze.setMinimumSize(QtCore.QSize(24, 24))
        self.button_delete_freeze.setMaximumSize(QtCore.QSize(24, 24))
        self.button_delete_freeze.setStyleSheet("QPushButton {\n"
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
        self.button_delete_freeze.setText("")
        self.button_delete_freeze.setIcon(icon1)
        self.button_delete_freeze.setIconSize(QtCore.QSize(24, 24))
        self.button_delete_freeze.setFlat(True)
        self.button_delete_freeze.setObjectName("button_delete_freeze")
        self.gridLayout_2.addWidget(self.button_delete_freeze, 2, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(21, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem13, 3, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem14, 0, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_2)
        self.gridLayout_8.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem15, 2, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem16 = QtWidgets.QSpacerItem(242, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.label_27 = QtWidgets.QLabel(self.tab_freeze)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_4.addWidget(self.label_27)
        spacerItem17 = QtWidgets.QSpacerItem(267, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.gridLayout_8.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.button_add_scan = QtWidgets.QPushButton(self.tab_freeze)
        self.button_add_scan.setMinimumSize(QtCore.QSize(24, 24))
        self.button_add_scan.setMaximumSize(QtCore.QSize(24, 24))
        self.button_add_scan.setStyleSheet("QPushButton {\n"
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
        self.button_add_scan.setText("")
        self.button_add_scan.setIcon(icon)
        self.button_add_scan.setIconSize(QtCore.QSize(24, 24))
        self.button_add_scan.setFlat(True)
        self.button_add_scan.setObjectName("button_add_scan")
        self.verticalLayout_8.addWidget(self.button_add_scan)
        self.button_delete_scan = QtWidgets.QPushButton(self.tab_freeze)
        self.button_delete_scan.setMinimumSize(QtCore.QSize(24, 24))
        self.button_delete_scan.setMaximumSize(QtCore.QSize(24, 24))
        self.button_delete_scan.setStyleSheet("QPushButton {\n"
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
        self.button_delete_scan.setText("")
        self.button_delete_scan.setIcon(icon1)
        self.button_delete_scan.setIconSize(QtCore.QSize(24, 24))
        self.button_delete_scan.setFlat(True)
        self.button_delete_scan.setObjectName("button_delete_scan")
        self.verticalLayout_8.addWidget(self.button_delete_scan)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_25 = QtWidgets.QLabel(self.tab_freeze)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_3.addWidget(self.label_25)
        self.lineEdit_freeze = QtWidgets.QLineEdit(self.tab_freeze)
        self.lineEdit_freeze.setEnabled(True)
        self.lineEdit_freeze.setMaximumSize(QtCore.QSize(29, 16777215))
        self.lineEdit_freeze.setText("")
        self.lineEdit_freeze.setReadOnly(True)
        self.lineEdit_freeze.setObjectName("lineEdit_freeze")
        self.horizontalLayout_3.addWidget(self.lineEdit_freeze)
        self.label_26 = QtWidgets.QLabel(self.tab_freeze)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_3.addWidget(self.label_26)
        self.lineEdit_move = QtWidgets.QLineEdit(self.tab_freeze)
        self.lineEdit_move.setEnabled(True)
        self.lineEdit_move.setMaximumSize(QtCore.QSize(29, 16777215))
        self.lineEdit_move.setText("")
        self.lineEdit_move.setReadOnly(True)
        self.lineEdit_move.setObjectName("lineEdit_move")
        self.horizontalLayout_3.addWidget(self.lineEdit_move)
        self.button_invert = QtWidgets.QPushButton(self.tab_freeze)
        self.button_invert.setEnabled(True)
        self.button_invert.setObjectName("button_invert")
        self.horizontalLayout_3.addWidget(self.button_invert)
        self.checkBox_moveboth = QtWidgets.QCheckBox(self.tab_freeze)
        self.checkBox_moveboth.setEnabled(True)
        self.checkBox_moveboth.setObjectName("checkBox_moveboth")
        self.horizontalLayout_3.addWidget(self.checkBox_moveboth)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.gridLayout_8.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_23 = QtWidgets.QLabel(self.tab_freeze)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.tab_freeze)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 0, 2, 1, 1)
        self.spinbox_radius = QtWidgets.QDoubleSpinBox(self.tab_freeze)
        self.spinbox_radius.setObjectName("spinbox_radius")
        self.gridLayout_3.addWidget(self.spinbox_radius, 1, 0, 1, 1)
        self.spinbox_scan_pm = QtWidgets.QDoubleSpinBox(self.tab_freeze)
        self.spinbox_scan_pm.setDecimals(2)
        self.spinbox_scan_pm.setMinimum(-99.0)
        self.spinbox_scan_pm.setMaximum(99.0)
        self.spinbox_scan_pm.setSingleStep(0.1)
        self.spinbox_scan_pm.setProperty("value", 1.0)
        self.spinbox_scan_pm.setObjectName("spinbox_scan_pm")
        self.gridLayout_3.addWidget(self.spinbox_scan_pm, 1, 1, 1, 1)
        self.spinbox_scan_increment = QtWidgets.QDoubleSpinBox(self.tab_freeze)
        self.spinbox_scan_increment.setDecimals(2)
        self.spinbox_scan_increment.setMinimum(0.01)
        self.spinbox_scan_increment.setMaximum(99.99)
        self.spinbox_scan_increment.setSingleStep(0.05)
        self.spinbox_scan_increment.setProperty("value", 0.1)
        self.spinbox_scan_increment.setObjectName("spinbox_scan_increment")
        self.gridLayout_3.addWidget(self.spinbox_scan_increment, 1, 2, 1, 1)
        self.verticalLayout_11.addLayout(self.gridLayout_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem18)
        self.radioButton_plus = QtWidgets.QRadioButton(self.tab_freeze)
        self.radioButton_plus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_plus.setObjectName("radioButton_plus")
        self.horizontalLayout_15.addWidget(self.radioButton_plus)
        self.radioButton_minus = QtWidgets.QRadioButton(self.tab_freeze)
        self.radioButton_minus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_minus.setObjectName("radioButton_minus")
        self.horizontalLayout_15.addWidget(self.radioButton_minus)
        self.radioButton_both = QtWidgets.QRadioButton(self.tab_freeze)
        self.radioButton_both.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_both.setChecked(True)
        self.radioButton_both.setObjectName("radioButton_both")
        self.horizontalLayout_15.addWidget(self.radioButton_both)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem19)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.checkBox_switchXB = QtWidgets.QCheckBox(self.tab_freeze)
        self.checkBox_switchXB.setEnabled(True)
        self.checkBox_switchXB.setAutoFillBackground(False)
        self.checkBox_switchXB.setChecked(True)
        self.checkBox_switchXB.setObjectName("checkBox_switchXB")
        self.verticalLayout_11.addWidget(self.checkBox_switchXB)
        self.gridLayout_8.addLayout(self.verticalLayout_11, 5, 1, 1, 1)
        self.tabWidget.addTab(self.tab_freeze, "")
        self.tab_view = QtWidgets.QWidget()
        self.tab_view.setObjectName("tab_view")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_view)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem20)
        self.label_file_number = QtWidgets.QLabel(self.tab_view)
        self.label_file_number.setObjectName("label_file_number")
        self.horizontalLayout_12.addWidget(self.label_file_number)
        self.ComboBox_files = QtWidgets.QComboBox(self.tab_view)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ComboBox_files.sizePolicy().hasHeightForWidth())
        self.ComboBox_files.setSizePolicy(sizePolicy)
        self.ComboBox_files.setObjectName("ComboBox_files")
        self.horizontalLayout_12.addWidget(self.ComboBox_files)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.text_preview = QtWidgets.QPlainTextEdit(self.tab_view)
        font = QtGui.QFont()
        font.setFamily("PT Mono")
        self.text_preview.setFont(font)
        self.text_preview.setObjectName("text_preview")
        self.verticalLayout_2.addWidget(self.text_preview)
        self.gridLayout_13.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_view, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
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
        self.button_close = QtWidgets.QPushButton(self.frame_2)
        self.button_close.setMinimumSize(QtCore.QSize(0, 40))
        self.button_close.setObjectName("button_close")
        self.gridLayout.addWidget(self.button_close, 0, 0, 1, 1)
        self.button_write = QtWidgets.QPushButton(self.frame_2)
        self.button_write.setMinimumSize(QtCore.QSize(0, 40))
        self.button_write.setObjectName("button_write")
        self.gridLayout.addWidget(self.button_write, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.gridLayout_6.addWidget(self.frame_2, 1, 0, 1, 1)
        SetupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SetupWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SetupWindow)

    def retranslateUi(self, SetupWindow):
        _translate = QtCore.QCoreApplication.translate
        SetupWindow.setWindowTitle(_translate("SetupWindow", "MainWindow"))
        self.label_4.setText(_translate("SetupWindow", "Filename:"))
        self.checkBox_cp_to_reactmain.setText(_translate("SetupWindow", "Add to project table"))
        self.label_33.setText(_translate("SetupWindow", "Charge:"))
        self.lineEdit_charge.setText(_translate("SetupWindow", "0"))
        self.label_34.setText(_translate("SetupWindow", "Multiplicity:"))
        self.lineEdit_multiplicity.setText(_translate("SetupWindow", "1"))
        self.label_32.setText(_translate("SetupWindow", "Molecule"))
        self.label_31.setText(_translate("SetupWindow", "Output print level:"))
        self.radioButton.setText(_translate("SetupWindow", "Low"))
        self.radioButton_2.setText(_translate("SetupWindow", "Normal"))
        self.radioButton_3.setText(_translate("SetupWindow", "High"))
        self.funct_label_1.setText(_translate("SetupWindow", "Functional:"))
        self.basis_label_1.setText(_translate("SetupWindow", "Basis set:"))
        self.label_5.setText(_translate("SetupWindow", "("))
        self.label_7.setText(_translate("SetupWindow", " ,"))
        self.label_6.setText(_translate("SetupWindow", " )"))
        self.additional_job_2.setText(_translate("SetupWindow", "Additional keywords:"))
        self.label_3.setText(_translate("SetupWindow", "Job type:"))
        self.checkbox_freq.setText(_translate("SetupWindow", "Freq   "))
        self.checkBox_raman.setText(_translate("SetupWindow", "Raman"))
        self.additional_job.setText(_translate("SetupWindow", "Additional job details:"))
        self.checkbox_SCRF.setText(_translate("SetupWindow", "SCRF"))
        self.label_15.setText(_translate("SetupWindow", "Method:"))
        self.label_16.setText(_translate("SetupWindow", "Solvent:"))
        self.checkbox_eps.setText(_translate("SetupWindow", "Eps:"))
        self.checkBox_mem_2.setText(_translate("SetupWindow", "Memory"))
        self.additional_job_4.setText(_translate("SetupWindow", "Additional link0 details:"))
        self.checkBox_chk.setText(_translate("SetupWindow", "Chk"))
        self.checkBox_oldchk.setText(_translate("SetupWindow", "OldChk"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("SetupWindow", "Main"))
        self.label_21.setText(_translate("SetupWindow", "Atoms in model"))
        self.label_24.setText(_translate("SetupWindow", "Move atom pair"))
        self.radioButton_plus_mv.setText(_translate("SetupWindow", "+"))
        self.radioButton_minus_mv.setText(_translate("SetupWindow", "-"))
        self.label_9.setText(_translate("SetupWindow", "Current distance:"))
        self.checkBox_moveboth_mv.setText(_translate("SetupWindow", "Move both"))
        self.pushButton_create_mv.setText(_translate("SetupWindow", "Create new geometry"))
        self.Button_save_new_geometry.setText(_translate("SetupWindow", "Save new geometry as xyz file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_movepair), _translate("SetupWindow", "Move atom pair"))
        self.comboBox_freezetype.setItemText(0, _translate("SetupWindow", "Atom"))
        self.comboBox_freezetype.setItemText(1, _translate("SetupWindow", "Bond"))
        self.comboBox_freezetype.setItemText(2, _translate("SetupWindow", "Angle"))
        self.comboBox_freezetype.setItemText(3, _translate("SetupWindow", "Dihedral"))
        self.button_auto_freeze.setText(_translate("SetupWindow", "Auto-freeze"))
        self.label.setText(_translate("SetupWindow", "Atoms in model"))
        self.label_2.setText(_translate("SetupWindow", "Atoms to freeze"))
        self.label_27.setText(_translate("SetupWindow", "Bond distance scan"))
        self.label_25.setText(_translate("SetupWindow", "Freeze:"))
        self.label_26.setText(_translate("SetupWindow", "Move:"))
        self.button_invert.setText(_translate("SetupWindow", "Invert"))
        self.checkBox_moveboth.setText(_translate("SetupWindow", "Move both"))
        self.label_23.setText(_translate("SetupWindow", "Current distance (Å)"))
        self.label_22.setText(_translate("SetupWindow", "Increment"))
        self.radioButton_plus.setText(_translate("SetupWindow", "+"))
        self.radioButton_minus.setText(_translate("SetupWindow", "-"))
        self.radioButton_both.setText(_translate("SetupWindow", "+/-"))
        self.checkBox_switchXB.setText(_translate("SetupWindow", "Constrain atoms instead of bond"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_freeze), _translate("SetupWindow", "Constraints"))
        self.label_file_number.setText(_translate("SetupWindow", "File:"))
        self.text_preview.setPlainText(_translate("SetupWindow", "< insert preview of gaussian input file here >"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_view), _translate("SetupWindow", "Preview"))
        self.button_close.setText(_translate("SetupWindow", "Close"))
        self.button_write.setText(_translate("SetupWindow", "Write"))

#import icons_rc
