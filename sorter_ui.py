# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sorter.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QSize(640, 480))
        Form.setMaximumSize(QSize(640, 480))
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 70, 621, 401))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.textBrowser_3 = QTextBrowser(self.tab)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(10, 10, 151, 141))
        self.textBrowser_4 = QTextBrowser(self.tab)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(10, 160, 151, 91))
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 40, 91, 21))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 95, 101, 31))
        self.lineEdit = QLineEdit(self.tab)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 40, 191, 20))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.lineEdit.setFont(font1)
        self.lineEdit_2 = QLineEdit(self.tab)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(280, 100, 191, 20))
        self.lineEdit_2.setFont(font1)
        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(490, 40, 111, 23))
        self.pushButton_2 = QPushButton(self.tab)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(490, 100, 111, 23))
        self.pushButton_3 = QPushButton(self.tab)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(230, 200, 111, 23))
        self.pushButton_4 = QPushButton(self.tab)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(440, 200, 111, 23))
        self.pushButton_5 = QPushButton(self.tab)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(230, 260, 111, 23))
        self.pushButton_6 = QPushButton(self.tab)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(440, 260, 111, 23))
        self.textBrowser_2 = QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(10, 260, 151, 101))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textBrowser_6 = QTextBrowser(self.tab_2)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(10, 10, 151, 151))
        self.textBrowser_7 = QTextBrowser(self.tab_2)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(10, 170, 151, 91))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 10, 91, 21))
        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(270, 10, 201, 20))
        self.lineEdit_3.setFont(font1)
        self.pushButton_7 = QPushButton(self.tab_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(490, 10, 111, 23))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 50, 91, 21))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 80, 91, 21))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(170, 140, 91, 21))
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 170, 91, 21))
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 200, 91, 21))
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 230, 91, 21))
        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(270, 50, 201, 20))
        self.lineEdit_4.setFont(font1)
        self.lineEdit_5 = QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(270, 80, 201, 20))
        self.lineEdit_5.setFont(font1)
        self.lineEdit_6 = QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(270, 140, 201, 20))
        self.lineEdit_6.setFont(font1)
        self.lineEdit_7 = QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(270, 170, 201, 20))
        self.lineEdit_7.setFont(font1)
        self.lineEdit_8 = QLineEdit(self.tab_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(270, 200, 201, 20))
        self.lineEdit_8.setFont(font1)
        self.lineEdit_9 = QLineEdit(self.tab_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(270, 230, 201, 20))
        self.lineEdit_9.setFont(font1)
        self.pushButton_8 = QPushButton(self.tab_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(490, 50, 111, 23))
        self.pushButton_9 = QPushButton(self.tab_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(490, 80, 111, 23))
        self.pushButton_10 = QPushButton(self.tab_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(490, 140, 111, 23))
        self.pushButton_11 = QPushButton(self.tab_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(490, 170, 111, 23))
        self.pushButton_12 = QPushButton(self.tab_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(490, 200, 111, 23))
        self.pushButton_13 = QPushButton(self.tab_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(490, 230, 111, 23))
        self.pushButton_14 = QPushButton(self.tab_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(230, 280, 111, 23))
        self.pushButton_15 = QPushButton(self.tab_2)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(440, 280, 111, 23))
        self.pushButton_31 = QPushButton(self.tab_2)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setGeometry(QRect(230, 330, 111, 23))
        self.pushButton_32 = QPushButton(self.tab_2)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setGeometry(QRect(440, 330, 111, 23))
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(170, 110, 91, 21))
        self.lineEdit_10 = QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(270, 110, 201, 20))
        self.lineEdit_10.setFont(font1)
        self.pushButton_16 = QPushButton(self.tab_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(490, 110, 111, 23))
        self.textBrowser_5 = QTextBrowser(self.tab_2)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(10, 270, 151, 101))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setFont(font)
        self.textBrowser_9 = QTextBrowser(self.tab_3)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(10, 10, 151, 141))
        self.textBrowser_10 = QTextBrowser(self.tab_3)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(10, 160, 151, 91))
        self.label_19 = QLabel(self.tab_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(170, 40, 91, 21))
        self.label_20 = QLabel(self.tab_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(170, 100, 101, 21))
        self.lineEdit_19 = QLineEdit(self.tab_3)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setGeometry(QRect(280, 40, 191, 20))
        self.lineEdit_19.setFont(font1)
        self.lineEdit_20 = QLineEdit(self.tab_3)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(280, 100, 191, 20))
        self.lineEdit_20.setFont(font1)
        self.pushButton_33 = QPushButton(self.tab_3)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setGeometry(QRect(490, 40, 111, 23))
        self.pushButton_34 = QPushButton(self.tab_3)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(490, 100, 111, 23))
        self.pushButton_35 = QPushButton(self.tab_3)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setGeometry(QRect(230, 200, 111, 23))
        self.pushButton_36 = QPushButton(self.tab_3)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setGeometry(QRect(440, 200, 111, 23))
        self.pushButton_37 = QPushButton(self.tab_3)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(230, 260, 111, 23))
        self.pushButton_38 = QPushButton(self.tab_3)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(440, 260, 111, 23))
        self.textBrowser_8 = QTextBrowser(self.tab_3)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(10, 260, 151, 101))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setAutoFillBackground(False)
        self.textBrowser_12 = QTextBrowser(self.tab_4)
        self.textBrowser_12.setObjectName(u"textBrowser_12")
        self.textBrowser_12.setGeometry(QRect(10, 10, 151, 141))
        self.textBrowser_13 = QTextBrowser(self.tab_4)
        self.textBrowser_13.setObjectName(u"textBrowser_13")
        self.textBrowser_13.setGeometry(QRect(10, 160, 151, 91))
        self.label_22 = QLabel(self.tab_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(170, 40, 91, 21))
        self.label_23 = QLabel(self.tab_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(170, 100, 101, 21))
        self.lineEdit_21 = QLineEdit(self.tab_4)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(280, 40, 191, 20))
        self.lineEdit_21.setFont(font1)
        self.lineEdit_22 = QLineEdit(self.tab_4)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setGeometry(QRect(280, 100, 191, 20))
        self.lineEdit_22.setFont(font1)
        self.pushButton_39 = QPushButton(self.tab_4)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setGeometry(QRect(490, 40, 111, 23))
        self.pushButton_40 = QPushButton(self.tab_4)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setGeometry(QRect(490, 100, 111, 23))
        self.pushButton_41 = QPushButton(self.tab_4)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setGeometry(QRect(230, 200, 111, 23))
        self.pushButton_42 = QPushButton(self.tab_4)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setGeometry(QRect(440, 200, 111, 23))
        self.pushButton_43 = QPushButton(self.tab_4)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setGeometry(QRect(230, 260, 111, 23))
        self.pushButton_44 = QPushButton(self.tab_4)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setGeometry(QRect(440, 260, 111, 23))
        self.textBrowser_11 = QTextBrowser(self.tab_4)
        self.textBrowser_11.setObjectName(u"textBrowser_11")
        self.textBrowser_11.setGeometry(QRect(10, 260, 151, 101))
        self.tabWidget.addTab(self.tab_4, "")
        self.label_21 = QLabel(Form)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 20, 41, 31))
        self.label_21.setTextFormat(Qt.AutoText)
        self.textBrowser_20 = QTextBrowser(Form)
        self.textBrowser_20.setObjectName(u"textBrowser_20")
        self.textBrowser_20.setGeometry(QRect(60, 20, 491, 31))
        self.pushButton_17 = QPushButton(Form)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(570, 20, 61, 31))

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"File Sorter", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">This tab lets you sort files into folders:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Pictures</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Music</span></p>\n"
"<p style=\" m"
                        "argin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Videos</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Documents</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Programs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Compressed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#005"
                        "5ff;\">- Others</span></p></body></html>", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">Before starting make sure:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">All files are closed in the folder you want  to sort</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Source folder:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Destination folder:", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Move", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Files info", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">After starting:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">Don't do anything with the files and please wait for the system notification about complete</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Simple sorting", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">This tab lets you sort files into your selected folders by category:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Pictures</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Music</s"
                        "pan></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Videos</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Documents</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Programs</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600; color:#0055ff;\">- Compressed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; f"
                        "ont-weight:600; color:#0055ff;\">- Others</span></p></body></html>", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">Before starting make sure:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">All files are closed in the folder you want  to sort.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Source folder:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Select", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Pictures:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Music:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Documents:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Programs:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Compressed:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Others:", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.lineEdit_6.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.lineEdit_8.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.lineEdit_9.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"Move", None))
        self.pushButton_31.setText(QCoreApplication.translate("Form", u"Files info", None))
        self.pushButton_32.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Videos:", None))
        self.lineEdit_10.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"Select", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">After starting:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">Don't do anything with the files and please wait for the system notification about complete</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Advanced sorting", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0055ff;\">This tab lets you sort files into directory according to their extensions</span></p></body></html>", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">Before starting make sure:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">All files are closed in the folder you want  to sort</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Source folder:", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"Destination folder:", None))
        self.lineEdit_19.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.lineEdit_20.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.pushButton_33.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_34.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_35.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.pushButton_36.setText(QCoreApplication.translate("Form", u"Move", None))
        self.pushButton_37.setText(QCoreApplication.translate("Form", u"Files info", None))
        self.pushButton_38.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">After starting:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">Don't do anything with the files and please wait for the system notification about complete</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Sort by file extensions", None))
        self.textBrowser_12.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#0055ff;\">This tab lets you sort files into directory according to their date</span></p></body></html>", None))
        self.textBrowser_13.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">Before starting make sure:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">All files are closed in the folder you want  to sort</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"Source folder:", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Destination folder:", None))
        self.lineEdit_21.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.lineEdit_22.setText(QCoreApplication.translate("Form", u"Select folder", None))
        self.pushButton_39.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_40.setText(QCoreApplication.translate("Form", u"Select", None))
        self.pushButton_41.setText(QCoreApplication.translate("Form", u"Copy", None))
        self.pushButton_42.setText(QCoreApplication.translate("Form", u"Move", None))
        self.pushButton_43.setText(QCoreApplication.translate("Form", u"Files info", None))
        self.pushButton_44.setText(QCoreApplication.translate("Form", u"Exit", None))
        self.textBrowser_11.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">After starting:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff007f;\">Don't do anything with the files and please wait for the system notification about complete</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Sort by file date", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Status:", None))
        self.textBrowser_20.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select source and destination folders!</p></body></html>", None))
        self.pushButton_17.setText(QCoreApplication.translate("Form", u"About", None))
    # retranslateUi

