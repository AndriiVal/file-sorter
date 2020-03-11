# -*- coding: utf-8 -*-
# Author: Andrii Valchuk

import sys

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from file_sorter import FileSortingUi

if __name__ == "__main__":

    app = QApplication(sys.argv)
    file_sorting = FileSortingUi()
    sys.exit(app.exec_())
