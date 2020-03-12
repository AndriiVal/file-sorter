# -*- coding: utf-8 -*-
# Author: Andrii Valchuk

import os
import glob
import shutil
import re
import stat
import threading
import time

from datetime import datetime

from plyer import notification

class SortingFilesUtils(object):

    def __init__(self):
        self.sort_thread = None

    def setHome(self, home):
        self.home = home

    def setNewhome(self, newhome):
        self.newhome = newhome

    def __has_hidden_attribute(self, filepath):
        return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

    def setDestination(self, destination):
        self.destination = destination
    
    def __mascfiles(self, masc):
        mfiles = []
        names = glob.glob(os.path.join(self.home, masc))
        for name in names:
            if os.path.isfile(name) and not self.__has_hidden_attribute(name):
                mfiles.append(name)
        return mfiles

    def __masclist(self, mascs):
        mlist = []
        for masc in mascs:
            mlist = mlist + self.__mascfiles(masc)
        return mlist

    def __sizesortingfiles(self, sfiles):
        sizefiles = 0
        for sf in sfiles:
            size = os.path.getsize(sf)
            sizefiles = sizefiles + size
        return sizefiles

    def allfiles(self):
        sortinglist = []
        names = os.listdir(self.home)
        for name in names:
            fullname = os.path.join(self.home, name)
            if os.path.isfile(fullname) and not self.__has_hidden_attribute(fullname):
                sortinglist.append(fullname)
        return sortinglist

    def audiofiles(self):
        mascs = ['*.aac', '*.aif', '*.aiff', '*.aob', '*.ape', '*.asf', '*.aud', '*.bwg',
                 '*.cdr', '*.flac', '*.ics', '*.iff', '*.m', '*.m4a', '*.m4b', '*.m4p',
                 '*.m4r', '*.mid', '*.midi', '*.mod', '*.mp3', '*.mpa', '*.mpp', '*.msv',
                 '*.mts', '*.nkc', '*.ogg', '*.ps', '*.ra', '*.sdf', '*.sib', '*.sln',
                 '*.spl', '*.srt', '*.vb', '*.wav', '*.wave', '*.wm', '*.wma', '*.wpd']
        return self.__masclist(mascs)

    def documentfiles(self):
        mascs = ['*.gp*', '*.txt', '*.ods', '*.csv', '*.asp', '*.cdd', '*.cpp', '*.djvu',
                 '*.doc', '*.docm', '*.docx', '*.dot', '*.dotm', '*.dotx', '*.epub', '*.fb2',
                 '*.gpx', '*.ibooks', '*.indd', '*.kdc', '*.key', '*.kml', '*.mdb', '*.mdf',
                 '*.mobi', '*.mso', '*.odt', '*.one', '*.oxps', '*.pages', '*.pdf', '*.pkg',
                 '*.pl', '*.pot', '*.potm', '*.potx', '*.pps', '*.ppsm', '*.ppsx', '*.ppt',
                 '*.pptm', '*.pptx', '*.ps', '*.rtf', '*.sdf', '*.snb', '*.wpd', '*.wps',
                 '*.xar', '*.xlr', '*.xls', '*.xlsb', '*.xlsm', '*.xlsx', '*.xlt', '*.xltm',
                 '*.xltx', '*.xps']
        return self.__masclist(mascs)
    
    def imagefiles(self):
        mascs = ['*.svg', '*.webp', '*.skb', '*.skp', '*.apt', '*.bmp', '*.dds', '*.dng',
                 '*.gbr', '*.gif', '*.hta', '*.iff', '*.jpeg', '*.jpg', '*.kdc', '*.mng',
                 '*.png', '*.pot', '*.psd', '*.pspimage', '*.scr', '*.tga', '*.thm', '*.tif',
                 '*.tif', '*.tiff', '*.vst', '*.xcf', '*.yuv']
        return self.__masclist(mascs)

    def videofiles(self):
        mascs = ['*.3g2', '*.3gp', '*.3gp2', '*.3gpp', '*.3gpp2', '*.asf', '*.asx', '*.avi',
                 '*.drv', '*.f4v', '*.flv', '*.gtp', '*.h264', '*.m4v', '*.mkv', '*.mod',
                 '*.moov', '*.mov', '*.mp4', '*.mpeg', '*.mpg', '*.mts', '*.rm', '*.spl',
                 '*.srt', '*.stl', '*.swf', '*.vcd', '*.vid', '*.vob', '*.wm', '*.wmv', '*.yuv']
        return self.__masclist(mascs)

    def arhivefiles(self):
        mascs = ["*.7z", "*.arj", "*.pkg", "*.rar", "*.tar", "*.gz", "*.z", "*.zip"]
        return self.__masclist(mascs)

    def programsfiles(self):
        mascs = ["*.apk", "*.bat", "*.bin", "*.cgi", "*.pl", "*.com", "*.exe", "*.gadget",
                 "*.jar", "*.py", "*.wsf", "*.ino", "*.rpm", "*.deb"]
        return self.__masclist(mascs)

    def othersfiles(self):
        return list(set(self.allfiles()) - set(self.imagefiles()) - set(self.audiofiles()) - set(self.videofiles())
                    - set(self.documentfiles()) - set(self.arhivefiles()) - set(self.programsfiles()))

    def sizeall(self):
        return self.__sizesortingfiles(self.allfiles())

    def sizeaudio(self):
        return self.__sizesortingfiles(self.audiofiles())

    def sizedocument(self):
        return self.__sizesortingfiles(self.documentfiles())

    def sizeimage(self):
        return self.__sizesortingfiles(self.imagefiles())

    def sizevideo(self):
        return self.__sizesortingfiles(self.videofiles())

    def sizearhive(self):
        return self.__sizesortingfiles(self.arhivefiles())

    def sizeprograms(self):
        return self.__sizesortingfiles(self.programsfiles())

    def sizeothers(self):
        return self.__sizesortingfiles(self.othersfiles())

    def list_move(self, myhome, target):
        if not os.path.exists(target):
                os.makedirs(target)
        for homefile in myhome:
            tempfile = os.path.split(homefile)[-1]
            if os.path.exists(os.path.join(target, tempfile)):
                n = 1
                newfile = tempfile
                while os.path.exists(os.path.join(target, newfile)):
                    newfile = os.path.splitext(tempfile)[0] + '(' + str(n) + ')' + os.path.splitext(tempfile)[1]
                    n += 1
                shutil.move(homefile, os.path.join(target, newfile))
            else:
                shutil.move(homefile, target)

    def list_copy(self, myhome, target):
        if not os.path.exists(target):
                os.makedirs(target)
        for homefile in myhome:
            tempfile = os.path.split(homefile)[-1]
            if os.path.exists(os.path.join(target, tempfile)):
                n = 1
                newfile = tempfile
                while os.path.exists(os.path.join(target, newfile)):
                    newfile = os.path.splitext(tempfile)[0] + '(' + str(n) + ')' + os.path.splitext(tempfile)[1]
                    n += 1
                shutil.copy2(homefile, os.path.join(target, newfile))
            else:
                shutil.copy2(homefile, target)

    def move(self):
        try:
            self.list_move(self.imagefiles(), self.newhome[0])
            self.list_move(self.audiofiles(), self.newhome[1])
            self.list_move(self.videofiles(), self.newhome[2])
            self.list_move(self.documentfiles(), self.newhome[3])
            self.list_move(self.programsfiles(), self.newhome[4])
            self.list_move(self.arhivefiles(), self.newhome[5])
            self.list_move(self.othersfiles(), self.newhome[6])
            notification.notify(title='File Sorter: Complete',
                                message='Advanced sorting files is complete',
                                app_icon=None, timeout=60,)
        except Exception as e:
            notification.notify(title='File Sorter: ERROR!',
                                message=str(e),
                                app_icon=None, timeout=60,)

    def move_daemon(self):
        self.sort_thread = threading.Thread(target=self.move)
        self.sort_thread.daemon = True
        self.sort_thread.start()

    def simple_move(self):
        try:
            self.list_move(self.imagefiles(), os.path.join(self.destination, "Pictures"))
            self.list_move(self.audiofiles(), os.path.join(self.destination, "Music"))
            self.list_move(self.videofiles(), os.path.join(self.destination, "Videos"))
            self.list_move(self.documentfiles(), os.path.join(self.destination, "Documents"))
            self.list_move(self.programsfiles(), os.path.join(self.destination, "Programs"))
            self.list_move(self.arhivefiles(), os.path.join(self.destination, "Compressed"))
            self.list_move(self.othersfiles(), os.path.join(self.destination, "Others"))
            notification.notify(title='File Sorter: Complete',
                                message='Simple sorting files is complete',
                                app_icon=None, timeout=60,)
        except Exception as e:
            notification.notify(title='File Sorter: ERROR!',
                                message=str(e),
                                app_icon=None, timeout=60,)
        
    def simple_move_daemon(self):
        self.sort_thread = threading.Thread(target=self.simple_move)
        self.sort_thread.daemon = True
        self.sort_thread.start()

    def move_by_ext(self):
        try:
            for homefile in self.allfiles():
                file_ext = os.path.split(homefile)[-1]
                match = re.search(r'([\w]+)', os.path.splitext(file_ext)[1])
                if match:
                    folder_ext = match.group().upper()
                    target = os.path.join(self.destination, folder_ext)
                    if not os.path.exists(target):
                        os.makedirs(target)
                    if os.path.exists(os.path.join(target, file_ext)):
                        n = 1
                        newfile = file_ext
                        while os.path.exists(os.path.join(target, newfile)):
                            newfile = os.path.splitext(file_ext)[0] + '(' + str(n) + ')' + os.path.splitext(file_ext)[1]
                            n += 1
                        shutil.move(homefile, os.path.join(target, newfile))
                    else:
                        shutil.move(homefile, target)
            notification.notify(title='File Sorter: Complete',
                                message='Sort by file extension is complete',
                                app_icon=None, timeout=60,)
        except Exception as e:
            notification.notify(title='File Sorter: ERROR!',
                                message=str(e),
                                app_icon=None, timeout=60,)

    def move_by_ext_daemon(self):
        self.sort_thread = threading.Thread(target=self.move_by_ext)
        self.sort_thread.daemon = True
        self.sort_thread.start()

    def move_by_date(self):
        try:
            for homefile in self.allfiles():
                file_date = os.path.split(homefile)[-1]
                datestring = time.ctime(os.path.getctime(homefile))
                dt = datetime.strptime(datestring, '%a %b %d %H:%M:%S %Y')
                folder_date = str(dt.day) + '-' + str(dt.month) + '-' + str(dt.year)
                target = os.path.join(self.destination, folder_date)
                if not os.path.exists(target):
                    os.makedirs(target)
                if os.path.exists(os.path.join(target, file_date)):
                    n = 1
                    newfile = file_ext
                    while os.path.exists(os.path.join(target, newfile)):
                        newfile = os.path.splitext(file_ext)[0] + '(' + str(n) + ')' + os.path.splitext(file_ext)[1]
                        n += 1
                    shutil.move(homefile, os.path.join(target, newfile))
                else:
                    shutil.move(homefile, target)
            notification.notify(title='File Sorter: Complete',
                                message='Sort by file date is complete',
                                app_icon=None, timeout=60,)
        except Exception as e:
            notification.notify(title='File Sorter: ERROR!',
                                message=str(e),
                                app_icon=None, timeout=60,)

    def move_by_date_daemon(self):
        self.sort_thread = threading.Thread(target=self.move_by_date)
        self.sort_thread.daemon = True
        self.sort_thread.start()

    def copy(self):
        try:
            self.list_copy(self.imagefiles(), self.newhome[0])
            self.list_copy(self.audiofiles(), self.newhome[1])
            self.list_copy(self.videofiles(), self.newhome[2])
            self.list_copy(self.documentfiles(), self.newhome[3])
            self.list_copy(self.programsfiles(), self.newhome[4])
            self.list_copy(self.arhivefiles(), self.newhome[5])
            self.list_copy(self.othersfiles(), self.newhome[6])
            notification.notify(title='File Sorter: Complete',
                                message='Advanced copy file is complete',
                                app_icon=None, timeout=60,)
        except Exception as e:
            notification.notify(title='File Sorter: ERROR!',
                                message=str(e),
                                app_icon=None, timeout=60,)

    def copy_daemon(self):
        self.sort_thread = threading.Thread(target=self.copy)
        self.sort_thread.daemon = True
        self.sort_thread.start()

    def simple_copy(self):
        try:
            self.list_copy(self.imagefiles(), os.path.join(self.destination, "Pictures"))
            self.list_copy(self.audiofiles(), os.path.join(self.destination, "Music"))
            self.list_copy(self.videofiles(), os.path.join(self.destination, "Videos"))
            self.list_copy(self.documentfiles(), os.path.join(self.destination, "Documents"))
            self.list_copy(self.programsfiles(), os.path.join(self.destination, "Programs"))
            self.list_copy(self.arhivefiles(), os.path.join(self.destination, "Compressed"))
            self.list_copy(self.othersfiles(), os.path.join(self.destination, "Others"))
            notification.notify(title='File Sorter: Complete',
                                message='Simple copy files is complete',
                                app_icon=None, timeout=60,)
        except Exception as e:
            notification.notify(title='File Sorter: ERROR!',
                                message=str(e),
                                app_icon=None, timeout=60,)
        
    def simple_copy_daemon(self):
        self.sort_thread = threading.Thread(target=self.simple_copy)
        self.sort_thread.daemon = True
        self.sort_thread.start()

    def copy_by_ext(self):
        try:
            for homefile in self.allfiles():
                file_ext = os.path.split(homefile)[-1]
                match = re.search(r'([\w]+)', os.path.splitext(file_ext)[1])
                if match:
                    folder_ext = match.group().upper()
                    target = os.path.join(self.destination, folder_ext)
                    if not os.path.exists(target):
                        os.makedirs(target)
                    if os.path.exists(os.path.join(target, file_ext)):
                        n = 1
                        newfile = file_ext
                        while os.path.exists(os.path.join(target, newfile)):
                            newfile = os.path.splitext(file_ext)[0] + '(' + str(n) + ')' + os.path.splitext(file_ext)[1]
                            n += 1
                        shutil.copy2(homefile, os.path.join(target, newfile))
                    else:
                        shutil.copy2(homefile, target)
            notification.notify(title='File Sorter: Complete',
                                message='Copy by file extension is complete',
                                app_icon=None, timeout=60,)
        except Exception as e:
            notification.notify(title='File Sorter: ERROR!',
                                message=str(e),
                                app_icon=None, timeout=60,)

    def copy_by_ext_daemon(self):
        self.sort_thread = threading.Thread(target=self.copy_by_ext)
        self.sort_thread.daemon = True
        self.sort_thread.start()

    def copy_by_date(self):
        try:
            for homefile in self.allfiles():
                file_date = os.path.split(homefile)[-1]
                datestring = time.ctime(os.path.getctime(homefile))
                dt = datetime.strptime(datestring, '%a %b %d %H:%M:%S %Y')
                folder_date = str(dt.day) + '-' + str(dt.month) + '-' + str(dt.year)
                target = os.path.join(self.destination, folder_date)
                if not os.path.exists(target):
                    os.makedirs(target)
                if os.path.exists(os.path.join(target, file_date)):
                    n = 1
                    newfile = file_date
                    while os.path.exists(os.path.join(target, newfile)):
                        newfile = os.path.splitext(file_date)[0] + '(' + str(n) + ')' + os.path.splitext(file_date)[1]
                        n += 1
                    shutil.copy2(homefile, os.path.join(target, newfile))
                else:
                    shutil.copy2(homefile, target)
            notification.notify(title='File Sorter: Complete',
                                message='Copy by file date is complete',
                                app_icon=None, timeout=60,)
        except Exception as e:
            notification.notify(title='File Sorter: ERROR!',
                                message=str(e),
                                app_icon=None, timeout=60,)

    def copy_by_date_daemon(self):
        self.sort_thread = threading.Thread(target=self.copy_by_date)
        self.sort_thread.daemon = True
        self.sort_thread.start()
