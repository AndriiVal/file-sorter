#! /usr/bin/python3.7
# -*- coding: utf-8 -*-

# Author: Andrii Valchuk

import sys
import os
import threading

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from sorter_utils import SortingFilesUtils
from sorter_ui import Ui_Form


class FileSortingUi(QMainWindow, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.source)
        self.pushButton_2.clicked.connect(self.destination)
        self.pushButton_7.clicked.connect(self.source)
        self.pushButton_33.clicked.connect(self.source)
        self.pushButton_34.clicked.connect(self.destination)
        self.pushButton_39.clicked.connect(self.source)
        self.pushButton_40.clicked.connect(self.destination)
        self.pushButton_8.clicked.connect(self.pictures)
        self.pushButton_9.clicked.connect(self.music)
        self.pushButton_16.clicked.connect(self.videos)
        self.pushButton_10.clicked.connect(self.documents)
        self.pushButton_11.clicked.connect(self.programs)
        self.pushButton_12.clicked.connect(self.compressed)
        self.pushButton_13.clicked.connect(self.others)
        self.pushButton_6.clicked.connect(self.exit)
        self.pushButton_32.clicked.connect(self.exit)
        self.pushButton_38.clicked.connect(self.exit)
        self.pushButton_44.clicked.connect(self.exit)
        self.pushButton_5.clicked.connect(self.info1)
        self.pushButton_31.clicked.connect(self.info2)
        self.pushButton_37.clicked.connect(self.info3)
        self.pushButton_43.clicked.connect(self.info4)
        self.pushButton_3.clicked.connect(self.copy1)
        self.pushButton_14.clicked.connect(self.copy2)
        self.pushButton_35.clicked.connect(self.copy3)
        self.pushButton_41.clicked.connect(self.copy4)
        self.pushButton_4.clicked.connect(self.move1)
        self.pushButton_15.clicked.connect(self.move2)
        self.pushButton_36.clicked.connect(self.move3)
        self.pushButton_42.clicked.connect(self.move4)
        self.pushButton_17.clicked.connect(self.about)

        self.msgBox = QMessageBox()
        self.msgBox.setWindowTitle("Files information")
        self.msgBox.setIcon(QMessageBox.Information)
        self.warBox = QMessageBox()
        self.warBox.setWindowTitle("Warning!")
        self.warBox.setIcon(QMessageBox.Warning)
        self.warBox.setText("Select source direct!")
        self.warningBox = QMessageBox()
        self.warningBox.setWindowTitle("Warning!")
        self.warningBox.setIcon(QMessageBox.Warning)
        self.warningBox.setText("Select source and destination folders!")
        self.errBox = QMessageBox()
        self.errBox.setWindowTitle("ERROR!")
        self.errBox.setIcon(QMessageBox.Critical)
        self.thrBox = QMessageBox()
        self.thrBox.setWindowTitle("Warning!")
        self.thrBox.setIcon(QMessageBox.Warning)
        self.thrBox.setText("Cannot start because sorting is already in progress!")
        self.thrBox.setInformativeText("Please wait for the system notification about complete")
        self.askBox = QMessageBox()
        self.askBox.setWindowTitle("Confirm sorting")
        self.askBox.setIcon(QMessageBox.Question)
        self.askBox.setInformativeText('If confirm "Run", please wait for the system notification about complete')
        self.okButton = self.askBox.addButton('Ran', QMessageBox.AcceptRole)
        self.askBox.addButton('Cancel', QMessageBox.RejectRole)
        self.aboutBox = QMessageBox()
        self.aboutBox.setWindowTitle("About program")
        self.aboutBox.setIcon(QMessageBox.Information)
        self.aboutBox.setText('Welcome to File Sorter app\n' +
                              'Author: Andrii Valchuk')
        self.aboutBox.setInformativeText('This program lets you sort files by four methods:\n' +
                                         '- Simple sorting: sort files into "Pictures", "Music", "Videos", "Documents", "Programs", "Compressed" and "Others" folders\n' +
                                         '- Advanced sorting: sorts by category into separately selected folders\n' +
                                         '- Sort by file extensions: sort files into directory according to their extensions\n' +
                                         '- Sort by file date: sort files into directory according to their date\n' +
                                         'If the file from the source folder already exists in the destination folder, it will be copied with the copy number name\n' +
                                         'WARNING:\n' + '- Before sorting  make sure all files are closed in the folder you want  to sort\n' +
                                         "- After start sorting don't do anything with the files, don't restart this app and please wait for the system notification about complete")
        
        self.sortmyfiles = SortingFilesUtils()
        self.show()

    def sorting_thread(self):
        try:
            if self.sortmyfiles.sort_thread.isAlive():
                return True
            else:
                return False
        except Exception:
            return False

    def source(self):
        setsource = QFileDialog.getExistingDirectory()
        self.lineEdit.setText(setsource)
        self.lineEdit_3.setText(setsource)
        self.lineEdit_19.setText(setsource)
        self.lineEdit_21.setText(setsource)

    def destination(self):
        setdestination = QFileDialog.getExistingDirectory()
        self.lineEdit_2.setText(setdestination)
        self.lineEdit_20.setText(setdestination)
        self.lineEdit_22.setText(setdestination)

    def pictures(self):
        self.lineEdit_4.setText(QFileDialog.getExistingDirectory())

    def music(self):
        self.lineEdit_5.setText(QFileDialog.getExistingDirectory())

    def videos(self):
        self.lineEdit_10.setText(QFileDialog.getExistingDirectory())

    def documents(self):
        self.lineEdit_6.setText(QFileDialog.getExistingDirectory())

    def programs(self):
        self.lineEdit_7.setText(QFileDialog.getExistingDirectory())

    def compressed(self):
        self.lineEdit_8.setText(QFileDialog.getExistingDirectory())

    def others(self):
        self.lineEdit_9.setText(QFileDialog.getExistingDirectory())

    def exit(self):
        self.close()

    def about(self):
        self.aboutBox.exec_()

    def info1(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if os.path.exists(self.lineEdit.displayText()):
                    self.textBrowser_20.setText("Run info, pleas wait...")
                    self.sortmyfiles.setHome(self.lineEdit.displayText())
                    info_text = ("Count files: " + str(len(self.sortmyfiles.allfiles())) + 
                                 ",   Size: " + str(self.sortmyfiles.sizeall()) + " bytes")
                    self.textBrowser_20.setText(info_text)
                    self.msgBox.setText(info_text)
                    self.msgBox.exec_()
                else:
                    self.textBrowser_20.setText("Select source direct!")
                    self.warBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def info2(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if os.path.exists(self.lineEdit_3.displayText()):
                    self.textBrowser_20.setText("Run info, pleas wait...")
                    self.sortmyfiles.setHome(self.lineEdit_3.displayText())
                    info_text = ("Count files: " + str(len(self.sortmyfiles.allfiles())) +
                                 ",   Size: " + str(self.sortmyfiles.sizeall()) + " bytes")
                    self.textBrowser_20.setText(info_text)
                    self.msgBox.setText(info_text)
                    self.msgBox.exec_()
                else:
                    self.textBrowser_20.setText("Select source direct!")
                    self.warBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def info3(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if os.path.exists(self.lineEdit_19.displayText()):
                    self.textBrowser_20.setText("Run info, pleas wait...")
                    self.sortmyfiles.setHome(self.lineEdit_19.displayText())
                    info_text = ("Count files: " + str(len(self.sortmyfiles.allfiles())) + 
                                 ",   Size: " + str(self.sortmyfiles.sizeall()) + " bytes")
                    self.textBrowser_20.setText(info_text)
                    self.msgBox.setText(info_text)
                    self.msgBox.exec_()
                else:
                    self.textBrowser_20.setText("Select source direct!")
                    self.warBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def info4(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if os.path.exists(self.lineEdit_21.displayText()):
                    self.textBrowser_20.setText("Run info, pleas wait...")
                    self.sortmyfiles.setHome(self.lineEdit_21.displayText())
                    info_text = ("Count files: " + str(len(self.sortmyfiles.allfiles())) + 
                                 ",   Size: " + str(self.sortmyfiles.sizeall()) + " bytes")
                    self.textBrowser_20.setText(info_text)
                    self.msgBox.setText(info_text)
                    self.msgBox.exec_()
                else:
                    self.textBrowser_20.setText("Select source direct!")
                    self.warBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def copy1(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if (os.path.exists(self.lineEdit.displayText()) and
                    os.path.exists(self.lineEdit_2.displayText())):
                    self.askBox.setText("Run simple copy?")
                    self.askBox.exec_()
                    if self.askBox.clickedButton() == self.okButton:
                        self.textBrowser_20.setText("Run simple copy, please wait for the system notification about complete")
                        self.sortmyfiles.setHome(self.lineEdit.displayText())    
                        self.sortmyfiles.setDestination(self.lineEdit_2.displayText())
                        self.sortmyfiles.simple_copy_daemon()
                else:
                    self.textBrowser_20.setText("Select source and destination folders!")
                    self.warningBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def copy2(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if (os.path.exists(self.lineEdit_3.displayText()) and
                    os.path.exists(self.lineEdit_4.displayText()) and
                    os.path.exists(self.lineEdit_5.displayText()) and
                    os.path.exists(self.lineEdit_6.displayText()) and
                    os.path.exists(self.lineEdit_7.displayText()) and
                    os.path.exists(self.lineEdit_8.displayText()) and
                    os.path.exists(self.lineEdit_9.displayText()) and
                    os.path.exists(self.lineEdit_10.displayText())):
                    self.askBox.setText("Run advanced copy?")
                    self.askBox.exec_()
                    if self.askBox.clickedButton() == self.okButton:
                        self.textBrowser_20.setText("Run advanced copy, please wait for the system notification about complete")
                        self.sortmyfiles.setHome(self.lineEdit_3.displayText())
                        target_list = [self.lineEdit_4.displayText(), self.lineEdit_5.displayText(),
                                       self.lineEdit_10.displayText(), self.lineEdit_6.displayText(),
                                       self.lineEdit_7.displayText(), self.lineEdit_8.displayText(),
                                       self.lineEdit_9.displayText()]
                        self.sortmyfiles.setNewhome(target_list)
                        self.sortmyfiles.copy_daemon()
                else:
                    self.textBrowser_20.setText("Select source and destination folders!")
                    self.warningBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def copy3(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if (os.path.exists(self.lineEdit_19.displayText()) and
                    os.path.exists(self.lineEdit_20.displayText())):
                    self.askBox.setText("Run copy by file extension?")
                    self.askBox.exec_()
                    if self.askBox.clickedButton() == self.okButton:
                        self.textBrowser_20.setText("Run copy by file extension, please wait for the system notification about complete")
                        self.sortmyfiles.setHome(self.lineEdit_19.displayText())    
                        self.sortmyfiles.setDestination(self.lineEdit_20.displayText())
                        self.sortmyfiles.copy_by_ext_daemon()
                else:
                    self.textBrowser_20.setText("Select source and destination folders!")
                    self.warningBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def copy4(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if (os.path.exists(self.lineEdit_21.displayText()) and
                    os.path.exists(self.lineEdit_22.displayText())):
                    self.askBox.setText("Run copy by file date?")
                    self.askBox.exec_()
                    if self.askBox.clickedButton() == self.okButton:
                        self.textBrowser_20.setText("Run copy by file date, please wait for the system notification about complete")
                        self.sortmyfiles.setHome(self.lineEdit_21.displayText())    
                        self.sortmyfiles.setDestination(self.lineEdit_22.displayText())
                        self.sortmyfiles.copy_by_date_daemon()
                else:
                    self.textBrowser_20.setText("Select source and destination folders!")
                    self.warningBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def move1(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if (os.path.exists(self.lineEdit.displayText()) and
                    os.path.exists(self.lineEdit_2.displayText())):
                    self.askBox.setText("Run simple sorting?")
                    self.askBox.exec_()
                    if self.askBox.clickedButton() == self.okButton:
                        self.textBrowser_20.setText("Run simple sorting, please wait for the system notification about complete")
                        self.sortmyfiles.setHome(self.lineEdit.displayText())    
                        self.sortmyfiles.setDestination(self.lineEdit_2.displayText())
                        self.sortmyfiles.simple_move_daemon()
                else:
                    self.textBrowser_20.setText("Select source and destination folders!")
                    self.warningBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def move2(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if (os.path.exists(self.lineEdit_3.displayText()) and
                    os.path.exists(self.lineEdit_4.displayText()) and
                    os.path.exists(self.lineEdit_5.displayText()) and
                    os.path.exists(self.lineEdit_6.displayText()) and
                    os.path.exists(self.lineEdit_7.displayText()) and
                    os.path.exists(self.lineEdit_8.displayText()) and
                    os.path.exists(self.lineEdit_9.displayText()) and
                    os.path.exists(self.lineEdit_10.displayText())):
                    self.askBox.setText("Run advanced sorting?")
                    self.askBox.exec_()
                    if self.askBox.clickedButton() == self.okButton:
                        self.textBrowser_20.setText("Run advanced sorting, please wait for the system notification about complete")
                        self.sortmyfiles.setHome(self.lineEdit_3.displayText())
                        target_list = [self.lineEdit_4.displayText(), self.lineEdit_5.displayText(),
                                       self.lineEdit_10.displayText(), self.lineEdit_6.displayText(),
                                       self.lineEdit_7.displayText(), self.lineEdit_8.displayText(),
                                       self.lineEdit_9.displayText()]
                        self.sortmyfiles.setNewhome(target_list)
                        self.sortmyfiles.move_daemon()
                else:
                    self.textBrowser_20.setText("Select source and destination folders!")
                    self.warningBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def move3(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if (os.path.exists(self.lineEdit_19.displayText()) and
                    os.path.exists(self.lineEdit_20.displayText())):
                    self.askBox.setText("Run sort by file extension?")
                    self.askBox.exec_()
                    if self.askBox.clickedButton() == self.okButton:
                        self.textBrowser_20.setText("Run sort by file extension, please wait for the system notification about complete")
                        self.sortmyfiles.setHome(self.lineEdit_19.displayText())    
                        self.sortmyfiles.setDestination(self.lineEdit_20.displayText())
                        self.sortmyfiles.move_by_ext_daemon()
                else:
                    self.textBrowser_20.setText("Select source and destination folders!")
                    self.warningBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()

    def move4(self):
        if  self.sorting_thread():
            self.thrBox.exec_()
        else:
            try:
                if (os.path.exists(self.lineEdit_21.displayText()) and
                    os.path.exists(self.lineEdit_22.displayText())):
                    self.askBox.setText("Run sort by file date?")
                    self.askBox.exec_()
                    if self.askBox.clickedButton() == self.okButton:
                        self.textBrowser_20.setText("Run sort by file date, please wait for the system notification about complete")
                        self.sortmyfiles.setHome(self.lineEdit_21.displayText())    
                        self.sortmyfiles.setDestination(self.lineEdit_22.displayText())
                        self.sortmyfiles.move_by_date_daemon()
                else:
                    self.textBrowser_20.setText("Select source and destination folders!")
                    self.warningBox.exec_()
            except Exception as e:
                self.textBrowser_20.setText("ERROR! " + str(e))
                self.errBox.setText(str(e))
                self.errBox.exec_()
