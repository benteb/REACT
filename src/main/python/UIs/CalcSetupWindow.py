# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalcSetupWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalcSetupWindow(object):
    def setupUi(self, CalcSetupWindow):
        CalcSetupWindow.setObjectName("CalcSetupWindow")
        CalcSetupWindow.resize(341, 621)
        CalcSetupWindow.setMinimumSize(QtCore.QSize(0, 621))
        CalcSetupWindow.setMaximumSize(QtCore.QSize(66666, 621))
        CalcSetupWindow.setStyleSheet("QPushButton {\n"
"     background-color: rgb(143, 23, 119);\n"
"       color: white;\n"
" }\n"
" QPushButton:hover{\n"
" background-color:rgb(143, 23, 119);\n"
" border-style: outset;\n"
" border-width: 0px;\n"
" /*border-color: rgb(12, 103, 213);*/\n"
" }\n"
" QPushButton:pressed\n"
" {\n"
" /*background-color:rgb(17, 145, 255);\n"
"  color: black*/\n"
"  background-color: rgb(42, 42, 42);\n"
" }\n"
" QListWidget{\n"
" background-color: rgb(20,20,20);\n"
" border:None;\n"
" margin-top:0px;\n"
" margin-left:0px;\n"
" margin-right:0px;\n"
" }\n"
" QTextBrowser{\n"
" background-color: rgb(20,20,20);\n"
" border:None;\n"
" margin-top:0px;\n"
" margin-left:0px;\n"
" margin-right:0px;\n"
" }")
        self.centralwidget = QtWidgets.QWidget(CalcSetupWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 601))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setMinimumSize(QtCore.QSize(319, 140))
        self.frame.setMaximumSize(QtCore.QSize(319, 140))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.linedit_jobkey = QtWidgets.QLineEdit(self.frame)
        self.linedit_jobkey.setGeometry(QtCore.QRect(90, 50, 179, 21))
        self.linedit_jobkey.setMinimumSize(QtCore.QSize(179, 21))
        self.linedit_jobkey.setMaximumSize(QtCore.QSize(179, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.linedit_jobkey.setFont(font)
        self.linedit_jobkey.setText("")
        self.linedit_jobkey.setObjectName("linedit_jobkey")
        self.label1 = QtWidgets.QLabel(self.frame)
        self.label1.setGeometry(QtCore.QRect(10, 50, 70, 50))
        self.label1.setMinimumSize(QtCore.QSize(70, 50))
        self.label1.setMaximumSize(QtCore.QSize(70, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label1.setObjectName("label1")
        self.job_keys = QtWidgets.QListWidget(self.frame)
        self.job_keys.setGeometry(QtCore.QRect(90, 80, 179, 50))
        self.job_keys.setMinimumSize(QtCore.QSize(179, 50))
        self.job_keys.setMaximumSize(QtCore.QSize(179, 50))
        self.job_keys.setObjectName("job_keys")
        self.job_type_combobox = QtWidgets.QComboBox(self.frame)
        self.job_type_combobox.setGeometry(QtCore.QRect(90, 10, 179, 26))
        self.job_type_combobox.setMinimumSize(QtCore.QSize(179, 0))
        self.job_type_combobox.setMaximumSize(QtCore.QSize(179, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.job_type_combobox.setFont(font)
        self.job_type_combobox.setEditable(True)
        self.job_type_combobox.setObjectName("job_type_combobox")
        self.layoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_4.setGeometry(QtCore.QRect(280, 50, 31, 71))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.add_button1 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.add_button1.setMinimumSize(QtCore.QSize(24, 24))
        self.add_button1.setMaximumSize(QtCore.QSize(24, 24))
        self.add_button1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/arrow-plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_button1.setIcon(icon)
        self.add_button1.setIconSize(QtCore.QSize(24, 24))
        self.add_button1.setFlat(True)
        self.add_button1.setObjectName("add_button1")
        self.verticalLayout_6.addWidget(self.add_button1)
        self.del_button1 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.del_button1.setMinimumSize(QtCore.QSize(24, 24))
        self.del_button1.setMaximumSize(QtCore.QSize(24, 24))
        self.del_button1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/24x24/resources/icons/arrow-minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_button1.setIcon(icon1)
        self.del_button1.setIconSize(QtCore.QSize(24, 24))
        self.del_button1.setFlat(True)
        self.del_button1.setObjectName("del_button1")
        self.verticalLayout_6.addWidget(self.del_button1)
        self.label0 = QtWidgets.QLabel(self.frame)
        self.label0.setGeometry(QtCore.QRect(10, 10, 70, 26))
        self.label0.setMinimumSize(QtCore.QSize(70, 0))
        self.label0.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label0.setFont(font)
        self.label0.setObjectName("label0")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setMinimumSize(QtCore.QSize(319, 290))
        self.frame_2.setMaximumSize(QtCore.QSize(319, 290))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.add_keys = QtWidgets.QListWidget(self.frame_2)
        self.add_keys.setGeometry(QtCore.QRect(90, 140, 179, 50))
        self.add_keys.setMinimumSize(QtCore.QSize(179, 50))
        self.add_keys.setMaximumSize(QtCore.QSize(179, 50))
        self.add_keys.setObjectName("add_keys")
        self.label2 = QtWidgets.QLabel(self.frame_2)
        self.label2.setGeometry(QtCore.QRect(10, 110, 70, 50))
        self.label2.setMinimumSize(QtCore.QSize(70, 50))
        self.label2.setMaximumSize(QtCore.QSize(70, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label2.setObjectName("label2")
        self.func_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.func_comboBox.setGeometry(QtCore.QRect(90, 10, 100, 26))
        self.func_comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.func_comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.func_comboBox.setEditable(True)
        self.func_comboBox.setObjectName("func_comboBox")
        self.linedit_link0 = QtWidgets.QLineEdit(self.frame_2)
        self.linedit_link0.setGeometry(QtCore.QRect(90, 200, 179, 21))
        self.linedit_link0.setMinimumSize(QtCore.QSize(179, 21))
        self.linedit_link0.setMaximumSize(QtCore.QSize(179, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.linedit_link0.setFont(font)
        self.linedit_link0.setText("")
        self.linedit_link0.setObjectName("linedit_link0")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(280, 70, 12, 26))
        self.label_8.setMinimumSize(QtCore.QSize(12, 26))
        self.label_8.setMaximumSize(QtCore.QSize(12, 16))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_8.setObjectName("label_8")
        self.basis1_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.basis1_comboBox.setGeometry(QtCore.QRect(90, 40, 100, 26))
        self.basis1_comboBox.setMinimumSize(QtCore.QSize(100, 0))
        self.basis1_comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.basis1_comboBox.setEditable(True)
        self.basis1_comboBox.setObjectName("basis1_comboBox")
        self.label4 = QtWidgets.QLabel(self.frame_2)
        self.label4.setGeometry(QtCore.QRect(10, 40, 70, 26))
        self.label4.setMinimumSize(QtCore.QSize(70, 0))
        self.label4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label4.setObjectName("label4")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(210, 70, 16, 26))
        self.label_9.setMinimumSize(QtCore.QSize(16, 26))
        self.label_9.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName("label_9")
        self.layoutWidget_5 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(280, 200, 31, 71))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.add_button_3 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.add_button_3.setMinimumSize(QtCore.QSize(24, 24))
        self.add_button_3.setMaximumSize(QtCore.QSize(24, 24))
        self.add_button_3.setText("")
        self.add_button_3.setIcon(icon)
        self.add_button_3.setIconSize(QtCore.QSize(24, 24))
        self.add_button_3.setFlat(True)
        self.add_button_3.setObjectName("add_button_3")
        self.verticalLayout_7.addWidget(self.add_button_3)
        self.del_button_3 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.del_button_3.setMinimumSize(QtCore.QSize(24, 24))
        self.del_button_3.setMaximumSize(QtCore.QSize(24, 24))
        self.del_button_3.setText("")
        self.del_button_3.setIcon(icon1)
        self.del_button_3.setIconSize(QtCore.QSize(24, 24))
        self.del_button_3.setFlat(True)
        self.del_button_3.setObjectName("del_button_3")
        self.verticalLayout_7.addWidget(self.del_button_3)
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(140, 70, 16, 26))
        self.label_10.setMinimumSize(QtCore.QSize(16, 26))
        self.label_10.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_10.setObjectName("label_10")
        self.basis3_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.basis3_comboBox.setGeometry(QtCore.QRect(150, 70, 65, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basis3_comboBox.sizePolicy().hasHeightForWidth())
        self.basis3_comboBox.setSizePolicy(sizePolicy)
        self.basis3_comboBox.setMinimumSize(QtCore.QSize(65, 0))
        self.basis3_comboBox.setMaximumSize(QtCore.QSize(65, 16777215))
        self.basis3_comboBox.setEditable(True)
        self.basis3_comboBox.setObjectName("basis3_comboBox")
        self.layoutWidget_6 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_6.setGeometry(QtCore.QRect(280, 110, 31, 71))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_button_2 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.add_button_2.setMinimumSize(QtCore.QSize(24, 24))
        self.add_button_2.setMaximumSize(QtCore.QSize(24, 24))
        self.add_button_2.setText("")
        self.add_button_2.setIcon(icon)
        self.add_button_2.setIconSize(QtCore.QSize(24, 24))
        self.add_button_2.setFlat(True)
        self.add_button_2.setObjectName("add_button_2")
        self.verticalLayout_3.addWidget(self.add_button_2)
        self.del_button_2 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.del_button_2.setMinimumSize(QtCore.QSize(24, 24))
        self.del_button_2.setMaximumSize(QtCore.QSize(24, 24))
        self.del_button_2.setText("")
        self.del_button_2.setIcon(icon1)
        self.del_button_2.setIconSize(QtCore.QSize(24, 24))
        self.del_button_2.setFlat(True)
        self.del_button_2.setObjectName("del_button_2")
        self.verticalLayout_3.addWidget(self.del_button_2)
        self.basis4_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.basis4_comboBox.setGeometry(QtCore.QRect(220, 70, 65, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basis4_comboBox.sizePolicy().hasHeightForWidth())
        self.basis4_comboBox.setSizePolicy(sizePolicy)
        self.basis4_comboBox.setMinimumSize(QtCore.QSize(65, 0))
        self.basis4_comboBox.setMaximumSize(QtCore.QSize(51, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.basis4_comboBox.setFont(font)
        self.basis4_comboBox.setEditable(True)
        self.basis4_comboBox.setObjectName("basis4_comboBox")
        self.label3 = QtWidgets.QLabel(self.frame_2)
        self.label3.setGeometry(QtCore.QRect(10, 200, 70, 41))
        self.label3.setMinimumSize(QtCore.QSize(70, 21))
        self.label3.setMaximumSize(QtCore.QSize(128, 500))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label3.setFont(font)
        self.label3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label3.setObjectName("label3")
        self.link0_keys = QtWidgets.QListWidget(self.frame_2)
        self.link0_keys.setGeometry(QtCore.QRect(90, 230, 179, 50))
        self.link0_keys.setMinimumSize(QtCore.QSize(179, 50))
        self.link0_keys.setMaximumSize(QtCore.QSize(179, 50))
        self.link0_keys.setObjectName("link0_keys")
        self.linedit_addkeys = QtWidgets.QLineEdit(self.frame_2)
        self.linedit_addkeys.setGeometry(QtCore.QRect(90, 110, 179, 21))
        self.linedit_addkeys.setMinimumSize(QtCore.QSize(179, 21))
        self.linedit_addkeys.setMaximumSize(QtCore.QSize(179, 21))
        font = QtGui.QFont()
        font.setItalic(True)
        self.linedit_addkeys.setFont(font)
        self.linedit_addkeys.setText("")
        self.linedit_addkeys.setObjectName("linedit_addkeys")
        self.funct_label_4 = QtWidgets.QLabel(self.frame_2)
        self.funct_label_4.setGeometry(QtCore.QRect(10, 10, 70, 26))
        self.funct_label_4.setMinimumSize(QtCore.QSize(70, 0))
        self.funct_label_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.funct_label_4.setObjectName("funct_label_4")
        self.basis2_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.basis2_comboBox.setGeometry(QtCore.QRect(90, 70, 51, 26))
        self.basis2_comboBox.setMinimumSize(QtCore.QSize(51, 0))
        self.basis2_comboBox.setMaximumSize(QtCore.QSize(51, 16777215))
        self.basis2_comboBox.setEditable(True)
        self.basis2_comboBox.setObjectName("basis2_comboBox")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_3.setMinimumSize(QtCore.QSize(319, 150))
        self.frame_3.setMaximumSize(QtCore.QSize(319, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.textbrowser_preview = QtWidgets.QTextBrowser(self.frame_3)
        self.textbrowser_preview.setGeometry(QtCore.QRect(10, 30, 298, 81))
        self.textbrowser_preview.setMinimumSize(QtCore.QSize(298, 0))
        self.textbrowser_preview.setMaximumSize(QtCore.QSize(298, 16777215))
        self.textbrowser_preview.setObjectName("textbrowser_preview")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 10, 60, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.save_button = QtWidgets.QPushButton(self.frame_3)
        self.save_button.setGeometry(QtCore.QRect(220, 120, 85, 25))
        self.save_button.setMinimumSize(QtCore.QSize(85, 25))
        self.save_button.setMaximumSize(QtCore.QSize(85, 25))
        self.save_button.setObjectName("save_button")
        self.cancel_button = QtWidgets.QPushButton(self.frame_3)
        self.cancel_button.setGeometry(QtCore.QRect(130, 120, 85, 25))
        self.cancel_button.setMinimumSize(QtCore.QSize(85, 25))
        self.cancel_button.setMaximumSize(QtCore.QSize(85, 25))
        self.cancel_button.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    /*background-color:rgb(98, 114, 164);*/\n"
"    background-color: rgb(30,30,30);\n"
"    color: rgb(143,23,119);\n"
"    \n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"       background-color: rgb(40, 40, 40);\n"
"    /*color:rgb(20,20,20);*/\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: rgb(143,23,119);\n"
"\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    color: rgb(143, 23, 119);\n"
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"")
        self.cancel_button.setObjectName("cancel_button")
        self.verticalLayout.addWidget(self.frame_3)
        CalcSetupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CalcSetupWindow)
        QtCore.QMetaObject.connectSlotsByName(CalcSetupWindow)

    def retranslateUi(self, CalcSetupWindow):
        _translate = QtCore.QCoreApplication.translate
        CalcSetupWindow.setWindowTitle(_translate("CalcSetupWindow", "Calculation setup"))
        self.label1.setText(_translate("CalcSetupWindow", "Job \n"
"keywords:"))
        self.label0.setText(_translate("CalcSetupWindow", "Job type:"))
        self.label2.setText(_translate("CalcSetupWindow", "Additional \n"
"keywords:"))
        self.label_8.setText(_translate("CalcSetupWindow", " )"))
        self.label4.setText(_translate("CalcSetupWindow", "Basis set:"))
        self.label_9.setText(_translate("CalcSetupWindow", " ,"))
        self.label_10.setText(_translate("CalcSetupWindow", "("))
        self.label3.setText(_translate("CalcSetupWindow", "Link 0 \n"
"commands:"))
        self.funct_label_4.setText(_translate("CalcSetupWindow", "Functional :"))
        self.label.setText(_translate("CalcSetupWindow", "Preview"))
        self.save_button.setText(_translate("CalcSetupWindow", "Save"))
        self.cancel_button.setText(_translate("CalcSetupWindow", "Cancel"))
#import icons_rc
