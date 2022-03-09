# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.radio_1 = QRadioButton(self.centralwidget)
        self.radio_1.setObjectName(u"radio_1")
        self.radio_1.setGeometry(QRect(310, 220, 99, 20))
        self.radio_2 = QRadioButton(self.centralwidget)
        self.radio_2.setObjectName(u"radio_2")
        self.radio_2.setGeometry(QRect(430, 220, 99, 20))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(370, 180, 100, 32))
        self.chk_1 = QCheckBox(self.centralwidget)
        self.chk_1.setObjectName(u"chk_1")
        self.chk_1.setGeometry(QRect(370, 90, 91, 20))
        self.chk_2 = QCheckBox(self.centralwidget)
        self.chk_2.setObjectName(u"chk_2")
        self.chk_2.setGeometry(QRect(370, 120, 91, 20))
        self.chk_3 = QCheckBox(self.centralwidget)
        self.chk_3.setObjectName(u"chk_3")
        self.chk_3.setGeometry(QRect(370, 150, 91, 20))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radio_1.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radio_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc548\ub155?", None))
        self.chk_1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.chk_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.chk_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
    # retranslateUi

