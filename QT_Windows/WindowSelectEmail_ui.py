# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowSelectEmail.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_SeleccionCorreo(object):
    def setupUi(self, SeleccionCorreo):
        if not SeleccionCorreo.objectName():
            SeleccionCorreo.setObjectName(u"SeleccionCorreo")
        SeleccionCorreo.resize(1286, 566)
        SeleccionCorreo.setStyleSheet(u"border-radius:7px;\n"
"\n"
"background-color: rgb(240, 240, 240);")
        self.centralwidget = QWidget(SeleccionCorreo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1286, 0))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 45))
        self.frame.setStyleSheet(u"background-image: url(:/Images/ResourcesFolder/Logo_Rhelec/Up_Design.jpg);\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(10, 0))
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_17)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 0))
        self.label_11.setStyleSheet(u"background-image: url();\n"
"image: url(:/Images/ResourcesFolder/Logo_Rhelec/Logo_Without_Background.png);\n"
"background-color:rgba(255, 255, 255, 200);\n"
"border-radius:0px;")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(16)
        font.setBold(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"background-image: url();\n"
"background-color:rgba(255, 255, 255, 200);\n"
"border:0px;\n"
"padding: 0 10 0 10;\n"
"border-radius:0px;")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.frame_16 = QFrame(self.frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 45))
        self.frame_16.setStyleSheet(u"background-image: url();\n"
"background-color:rgba(91, 133, 150, 200);\n"
"border:0px;\n"
"border-radius:0px;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pbMinimize = QPushButton(self.frame_16)
        self.pbMinimize.setObjectName(u"pbMinimize")
        self.pbMinimize.setMinimumSize(QSize(20, 45))
        self.pbMinimize.setMaximumSize(QSize(40, 16777215))
        self.pbMinimize.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton{\n"
"image: url(:/featherIcons/ResourcesFolder/featherIcons/minus.svg);\n"
"padding: 0 10 0 10;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(200, 200, 200, 120);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(180, 180, 180, 150);\n"
"}")
        self.pbMinimize.setIconSize(QSize(15, 15))

        self.horizontalLayout_7.addWidget(self.pbMinimize)

        self.pbMaximize = QPushButton(self.frame_16)
        self.pbMaximize.setObjectName(u"pbMaximize")
        self.pbMaximize.setMinimumSize(QSize(0, 45))
        self.pbMaximize.setMaximumSize(QSize(40, 16777215))
        self.pbMaximize.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton{\n"
"image: url(:/featherIcons/ResourcesFolder/featherIcons/copy.svg);\n"
"padding: 0 10 0 10;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(200, 200, 200, 120);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(180, 180, 180, 150);\n"
"}")
        self.pbMaximize.setIconSize(QSize(15, 15))

        self.horizontalLayout_7.addWidget(self.pbMaximize)

        self.pbClose = QPushButton(self.frame_16)
        self.pbClose.setObjectName(u"pbClose")
        self.pbClose.setMinimumSize(QSize(0, 45))
        self.pbClose.setMaximumSize(QSize(40, 16777215))
        self.pbClose.setStyleSheet(u"\n"
"\n"
"\n"
"QPushButton{\n"
"image: url(:/featherIcons/ResourcesFolder/featherIcons/x.svg);\n"
"padding: 0 10 0 10;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(200, 200, 200, 120);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(180, 180, 180, 150);\n"
"}")

        self.horizontalLayout_7.addWidget(self.pbClose)


        self.horizontalLayout_6.addWidget(self.frame_16)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(500, 16777215))
        self.frame_7.setStyleSheet(u"border:1px solid gray;\n"
"\n"
"background-color: rgb(240, 240, 240)\n"
"")
        self.frame_7.setFrameShape(QFrame.Box)
        self.frame_7.setFrameShadow(QFrame.Sunken)
        self.frame_7.setLineWidth(21)
        self.frame_7.setMidLineWidth(20)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.frame_5 = QFrame(self.frame_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 50))
        self.frame_5.setStyleSheet(u"border:0px;\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(30, 0))
        self.label_7.setMaximumSize(QSize(30, 16777215))
        self.label_7.setStyleSheet(u"image: url(:/featherIcons/ResourcesFolder/featherIcons/user.svg);")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.label_8.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.line = QFrame(self.frame_7)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border-top:1px solid black;\n"
"border-bottom:0px;\n"
"border-radius:0px;\n"
"border-left:0px;\n"
"border-right:0px;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 50))
        self.frame_6.setStyleSheet(u"border:0px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        self.label_9.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.lineBuscar = QLineEdit(self.frame_6)
        self.lineBuscar.setObjectName(u"lineBuscar")
        self.lineBuscar.setEnabled(False)
        self.lineBuscar.setMinimumSize(QSize(0, 30))
        self.lineBuscar.setFont(font2)
        self.lineBuscar.setStyleSheet(u"border:1px solid gray;\n"
"border-radius:10px;\n"
"background-color:rgb(255, 255, 255)")

        self.horizontalLayout_4.addWidget(self.lineBuscar)

        self.cbCorreoNuevo = QCheckBox(self.frame_6)
        self.cbCorreoNuevo.setObjectName(u"cbCorreoNuevo")
        self.cbCorreoNuevo.setEnabled(False)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.cbCorreoNuevo.setFont(font3)

        self.horizontalLayout_4.addWidget(self.cbCorreoNuevo)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(154, 192, 213);\n"
"border:0px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.rbEmail1 = QRadioButton(self.frame_9)
        self.rbEmail1.setObjectName(u"rbEmail1")
        self.rbEmail1.setEnabled(False)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        font4.setUnderline(True)
        self.rbEmail1.setFont(font4)
        self.rbEmail1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.rbEmail1)

        self.lblBodyEmail1 = QLabel(self.frame_9)
        self.lblBodyEmail1.setObjectName(u"lblBodyEmail1")
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        self.lblBodyEmail1.setFont(font5)
        self.lblBodyEmail1.setStyleSheet(u"color:rgba(0, 0, 0, 255)")
        self.lblBodyEmail1.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.lblBodyEmail1)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"border:1px solid gray;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.rbEmail2 = QRadioButton(self.frame_13)
        self.rbEmail2.setObjectName(u"rbEmail2")
        self.rbEmail2.setEnabled(False)
        self.rbEmail2.setFont(font4)
        self.rbEmail2.setCursor(QCursor(Qt.PointingHandCursor))
        self.rbEmail2.setStyleSheet(u"border:0px;")

        self.verticalLayout_6.addWidget(self.rbEmail2)

        self.lblBodyEmail2 = QLabel(self.frame_13)
        self.lblBodyEmail2.setObjectName(u"lblBodyEmail2")
        self.lblBodyEmail2.setFont(font5)
        self.lblBodyEmail2.setStyleSheet(u"color:rgba(0, 0, 0, 255);\n"
"border:0px;")
        self.lblBodyEmail2.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.lblBodyEmail2)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.rbEmail3 = QRadioButton(self.frame_10)
        self.rbEmail3.setObjectName(u"rbEmail3")
        self.rbEmail3.setEnabled(False)
        self.rbEmail3.setFont(font4)
        self.rbEmail3.setCursor(QCursor(Qt.PointingHandCursor))
        self.rbEmail3.setStyleSheet(u"border:0px;")

        self.verticalLayout_7.addWidget(self.rbEmail3)

        self.lblBodyEmail3 = QLabel(self.frame_10)
        self.lblBodyEmail3.setObjectName(u"lblBodyEmail3")
        self.lblBodyEmail3.setFont(font5)
        self.lblBodyEmail3.setStyleSheet(u"color:rgba(0, 0, 0, 255);\n"
"border:0px;")
        self.lblBodyEmail3.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.lblBodyEmail3)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.rbEmail4 = QRadioButton(self.frame_11)
        self.rbEmail4.setObjectName(u"rbEmail4")
        self.rbEmail4.setEnabled(False)
        self.rbEmail4.setFont(font4)
        self.rbEmail4.setCursor(QCursor(Qt.PointingHandCursor))
        self.rbEmail4.setStyleSheet(u"border:0px;")

        self.verticalLayout_8.addWidget(self.rbEmail4)

        self.lblBodyEmail4 = QLabel(self.frame_11)
        self.lblBodyEmail4.setObjectName(u"lblBodyEmail4")
        self.lblBodyEmail4.setFont(font5)
        self.lblBodyEmail4.setStyleSheet(u"color:rgba(0, 0, 0, 255);\n"
"border:0px;")
        self.lblBodyEmail4.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.lblBodyEmail4)


        self.verticalLayout_3.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.rbEmail5 = QRadioButton(self.frame_12)
        self.rbEmail5.setObjectName(u"rbEmail5")
        self.rbEmail5.setEnabled(False)
        self.rbEmail5.setFont(font4)
        self.rbEmail5.setCursor(QCursor(Qt.PointingHandCursor))
        self.rbEmail5.setStyleSheet(u"border:0px;")

        self.verticalLayout_9.addWidget(self.rbEmail5)

        self.lblBodyEmail5 = QLabel(self.frame_12)
        self.lblBodyEmail5.setObjectName(u"lblBodyEmail5")
        self.lblBodyEmail5.setFont(font5)
        self.lblBodyEmail5.setStyleSheet(u"color:rgba(0, 0, 0, 255);\n"
"border:0px;")
        self.lblBodyEmail5.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.lblBodyEmail5)


        self.verticalLayout_3.addWidget(self.frame_12)


        self.horizontalLayout.addWidget(self.frame_7)

        self.frameEditEmail = QFrame(self.frame_3)
        self.frameEditEmail.setObjectName(u"frameEditEmail")
        self.frameEditEmail.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid gray;")
        self.frameEditEmail.setFrameShape(QFrame.StyledPanel)
        self.frameEditEmail.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameEditEmail)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.frame_4 = QFrame(self.frameEditEmail)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setStyleSheet(u"border:0px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(64, 30))
        self.label_6.setMaximumSize(QSize(64, 30))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(True)
        self.label_6.setFont(font6)
        self.label_6.setStyleSheet(u"border-radius:5px;\n"
"border:1px solid gray;\n"
"background-color:rgb(245, 245, 245)")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.linePara = QLineEdit(self.frame_4)
        self.linePara.setObjectName(u"linePara")
        self.linePara.setMinimumSize(QSize(0, 30))
        self.linePara.setMaximumSize(QSize(16777215, 30))
        font7 = QFont()
        font7.setPointSize(10)
        self.linePara.setFont(font7)
        self.linePara.setStyleSheet(u"border-bottom:1px solid gray;\n"
"border-radius:0px;")

        self.horizontalLayout_2.addWidget(self.linePara)

        self.pbEnviar = QPushButton(self.frame_4)
        self.pbEnviar.setObjectName(u"pbEnviar")
        self.pbEnviar.setMinimumSize(QSize(80, 30))
        self.pbEnviar.setMaximumSize(QSize(80, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setItalic(True)
        font8.setUnderline(True)
        self.pbEnviar.setFont(font8)
        self.pbEnviar.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(154, 192, 213);\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(184, 222, 243);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(154, 192, 213);\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(154, 192, 213);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pbEnviar)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_14 = QFrame(self.frameEditEmail)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(16777215, 40))
        self.frame_14.setStyleSheet(u"border:0px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.label_10 = QLabel(self.frame_14)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(64, 30))
        self.label_10.setMaximumSize(QSize(64, 30))
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"border-radius:5px;\n"
"border:1px solid gray;\n"
"background-color:rgb(245, 245, 245)")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.lineCC = QLineEdit(self.frame_14)
        self.lineCC.setObjectName(u"lineCC")
        self.lineCC.setMinimumSize(QSize(0, 30))
        self.lineCC.setMaximumSize(QSize(16777215, 30))
        self.lineCC.setFont(font7)
        self.lineCC.setStyleSheet(u"border-bottom:1px solid gray;\n"
"border-radius:0px;")

        self.horizontalLayout_5.addWidget(self.lineCC)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_8 = QFrame(self.frameEditEmail)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 30))
        self.frame_8.setStyleSheet(u"\n"
"border-radius:0px;\n"
"border:0px;")
        self.frame_8.setInputMethodHints(Qt.ImhHiddenText)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.label_13 = QLabel(self.frame_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(64, 20))
        self.label_13.setMaximumSize(QSize(64, 30))
        self.label_13.setFont(font6)
        self.label_13.setStyleSheet(u"border-radius:5px;\n"
"border:1px solid gray;\n"
"background-color:rgb(245, 245, 245)")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.lineAsunto = QLineEdit(self.frame_8)
        self.lineAsunto.setObjectName(u"lineAsunto")
        self.lineAsunto.setMinimumSize(QSize(0, 20))
        self.lineAsunto.setMaximumSize(QSize(16777215, 30))
        self.lineAsunto.setFont(font1)
        self.lineAsunto.setStyleSheet(u"border-bottom:1px solid gray;\n"
"padding:0 0 0 10;")

        self.horizontalLayout_8.addWidget(self.lineAsunto)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_15 = QFrame(self.frameEditEmail)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border-top:2px solid gray;\n"
"border-radius:0px;\n"
"border:0px;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.bodyEmail = QTextEdit(self.frame_15)
        self.bodyEmail.setObjectName(u"bodyEmail")
        self.bodyEmail.setFont(font1)
        self.bodyEmail.setStyleSheet(u"border:0px;")

        self.verticalLayout_4.addWidget(self.bodyEmail)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 30))
        self.frame_18.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"border-radius:10px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, 0)
        self.label_14 = QLabel(self.frame_18)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 30))
        self.label_14.setMaximumSize(QSize(80, 30))
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(10)
        font9.setBold(True)
        self.label_14.setFont(font9)
        self.label_14.setStyleSheet(u"background-color:rgb(220, 220, 220)")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_14)

        self.lineAdjuntos = QLineEdit(self.frame_18)
        self.lineAdjuntos.setObjectName(u"lineAdjuntos")
        self.lineAdjuntos.setEnabled(True)
        self.lineAdjuntos.setFont(font2)
        self.lineAdjuntos.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.lineAdjuntos)


        self.verticalLayout_4.addWidget(self.frame_18)


        self.verticalLayout_2.addWidget(self.frame_15)


        self.horizontalLayout.addWidget(self.frameEditEmail)

        self.horizontalLayout.setStretch(0, 1)

        self.verticalLayout_10.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)

        SeleccionCorreo.setCentralWidget(self.centralwidget)

        self.retranslateUi(SeleccionCorreo)

        QMetaObject.connectSlotsByName(SeleccionCorreo)
    # setupUi

    def retranslateUi(self, SeleccionCorreo):
        SeleccionCorreo.setWindowTitle(QCoreApplication.translate("SeleccionCorreo", u"Seleccion de Cola de Correos", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("SeleccionCorreo", u"Gesti\u00f3n de Permisos", None))
        self.pbMinimize.setText("")
        self.pbMaximize.setText("")
        self.pbClose.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("SeleccionCorreo", u"Nombre Apellido - Operador", None))
        self.label_9.setText(QCoreApplication.translate("SeleccionCorreo", u"Buscar:", None))
        self.cbCorreoNuevo.setText(QCoreApplication.translate("SeleccionCorreo", u"Correo Nuevo", None))
        self.rbEmail1.setText(QCoreApplication.translate("SeleccionCorreo", u"Email 1", None))
        self.lblBodyEmail1.setText(QCoreApplication.translate("SeleccionCorreo", u"Buenos d\u00ecas Estimado Pablo. Envio este mensaje para solicitar de la manera", None))
        self.rbEmail2.setText(QCoreApplication.translate("SeleccionCorreo", u"Email 2", None))
        self.lblBodyEmail2.setText(QCoreApplication.translate("SeleccionCorreo", u"Buenos d\u00ecas Estimado Ing. Envio este mensaje para solicitar de la manera...", None))
        self.rbEmail3.setText(QCoreApplication.translate("SeleccionCorreo", u"Email 3", None))
        self.lblBodyEmail3.setText(QCoreApplication.translate("SeleccionCorreo", u"Buenos d\u00ecas Estimado Ing. Envio este mensaje para solicitar de la manera...", None))
        self.rbEmail4.setText(QCoreApplication.translate("SeleccionCorreo", u"Email 4", None))
        self.lblBodyEmail4.setText(QCoreApplication.translate("SeleccionCorreo", u"Buenos d\u00ecas Estimado Ing. Envio este mensaje para solicitar de la manera...", None))
        self.rbEmail5.setText(QCoreApplication.translate("SeleccionCorreo", u"Email 5", None))
        self.lblBodyEmail5.setText(QCoreApplication.translate("SeleccionCorreo", u"Buenos d\u00ecas Estimado Ing. Envio este mensaje para solicitar de la manera...", None))
        self.label_6.setText(QCoreApplication.translate("SeleccionCorreo", u"Para:", None))
        self.pbEnviar.setText(QCoreApplication.translate("SeleccionCorreo", u"Enviar", None))
        self.label_10.setText(QCoreApplication.translate("SeleccionCorreo", u"CC:", None))
        self.label_13.setText(QCoreApplication.translate("SeleccionCorreo", u"Asunto:", None))
        self.lineAsunto.setText("")
        self.lineAsunto.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("SeleccionCorreo", u"Adjuntos:", None))
        self.lineAdjuntos.setText(QCoreApplication.translate("SeleccionCorreo", u"Solicitud de permisos FINANCIEROS - RBS REPNARANCAY.xlsx", None))
    # retranslateUi

