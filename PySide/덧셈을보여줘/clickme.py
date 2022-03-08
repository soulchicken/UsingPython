# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '덧셈을보여줘.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_btn_clickme(object):
    def setupUi(self, btn_clickme):
        if not btn_clickme.objectName():
            btn_clickme.setObjectName(u"btn_clickme")
        btn_clickme.resize(519, 425)
        self.centralwidget = QWidget(btn_clickme)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 190, 100, 32))
        btn_clickme.setCentralWidget(self.centralwidget)

        self.retranslateUi(btn_clickme)

        QMetaObject.connectSlotsByName(btn_clickme)
    # setupUi

    def retranslateUi(self, btn_clickme):
        btn_clickme.setWindowTitle(QCoreApplication.translate("btn_clickme", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("btn_clickme", u"\ub20c\ub7ec\ubd10", None))
    # retranslateUi

