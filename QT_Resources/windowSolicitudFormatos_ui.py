# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowSolicitudFormatos.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 654)
        MainWindow.setMinimumSize(QSize(1000, 654))
        MainWindow.setMaximumSize(QSize(1000, 654))
        MainWindow.setStyleSheet(u"background-color : rgba(255, 255, 255, 255);\n"
"border-radius:3;\n"
"border:1px solid black;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"border:0px;\n"
"background-color:rgba(0, 0, 0, 0)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(150, 0))
        self.frame_17.setMaximumSize(QSize(150, 16777215))
        self.frame_17.setStyleSheet(u"border:0px;\n"
"background-color:rgba(0, 0, 0, 0)")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_17)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"image: url(:/Images/1_LogoRhelec.png);\n"
"border-color: rgb(255, 255, 255);\n"
"padding: 0 0 3 0")

        self.verticalLayout_2.addWidget(self.label_4)


        self.horizontalLayout_3.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_18)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label = QLabel(self.frame_18)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(100, 0))
        self.frame_19.setMaximumSize(QSize(100, 16777215))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pb_minimized = QPushButton(self.frame_19)
        self.pb_minimized.setObjectName(u"pb_minimized")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_minimized.sizePolicy().hasHeightForWidth())
        self.pb_minimized.setSizePolicy(sizePolicy)
        self.pb_minimized.setMinimumSize(QSize(0, 25))
        self.pb_minimized.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"image: url(:/featherIcons/featherIcons/divide-square.svg);\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(200, 200, 200, 120);\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(180, 180, 180, 150);\n"
"	border-radius: 6px\n"
"}")

        self.horizontalLayout_4.addWidget(self.pb_minimized)

        self.pb_exit = QPushButton(self.frame_19)
        self.pb_exit.setObjectName(u"pb_exit")
        sizePolicy.setHeightForWidth(self.pb_exit.sizePolicy().hasHeightForWidth())
        self.pb_exit.setSizePolicy(sizePolicy)
        self.pb_exit.setMinimumSize(QSize(0, 25))
        self.pb_exit.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	image: url(:/featherIcons/featherIcons/x-square.svg);\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(200, 200, 200, 120);\n"
"	border-radius: 6px\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(180, 180, 180, 150);\n"
"	border-radius: 6px\n"
"}")

        self.horizontalLayout_4.addWidget(self.pb_exit)


        self.horizontalLayout_3.addWidget(self.frame_19)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.cb_RBS = QComboBox(self.frame_3)
        self.cb_RBS.setObjectName(u"cb_RBS")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_RBS.sizePolicy().hasHeightForWidth())
        self.cb_RBS.setSizePolicy(sizePolicy1)
        self.cb_RBS.setMinimumSize(QSize(119, 0))
        self.cb_RBS.setMaximumSize(QSize(400, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(18)
        self.cb_RBS.setFont(font1)
        self.cb_RBS.setStyleSheet(u"QComboBox {\n"
"	background-image: url(:/featherIcons/featherIcons/zoom-out.svg);\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width:"
                        " 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/featherIcons/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox::enabled{\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"QComboBox::disabled{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}")

        self.gridLayout.addWidget(self.cb_RBS, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(19)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setKerning(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0px;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0px;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.cb_Formato = QComboBox(self.frame_3)
        self.cb_Formato.setObjectName(u"cb_Formato")
        sizePolicy1.setHeightForWidth(self.cb_Formato.sizePolicy().hasHeightForWidth())
        self.cb_Formato.setSizePolicy(sizePolicy1)
        self.cb_Formato.setMinimumSize(QSize(119, 0))
        self.cb_Formato.setMaximumSize(QSize(400, 16777215))
        self.cb_Formato.setFont(font1)
        self.cb_Formato.setStyleSheet(u"QComboBox {\n"
"	background-image: url(:/featherIcons/featherIcons/zoom-out.svg);\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width:"
                        " 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/featherIcons/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox::enabled{\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"QComboBox::disabled{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}")

        self.gridLayout.addWidget(self.cb_Formato, 1, 2, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setMaximumSize(QSize(350, 16777215))
        self.frame_5.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setStyleSheet(u"border:0px;\n"
"background-color:rgba(0, 0, 0, 0)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border:0px;\n"
"background-color:rgba(0, 0, 0, 0)")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_17 = QLabel(self.frame_11)
        self.label_17.setObjectName(u"label_17")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(15)
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_17)


        self.verticalLayout_3.addWidget(self.frame_11, 0, Qt.AlignHCenter)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setMinimumSize(QSize(300, 0))
        self.frame_12.setMaximumSize(QSize(300, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, -1)
        self.cb_OyMs = QComboBox(self.frame_12)
        self.cb_OyMs.setObjectName(u"cb_OyMs")
        sizePolicy2.setHeightForWidth(self.cb_OyMs.sizePolicy().hasHeightForWidth())
        self.cb_OyMs.setSizePolicy(sizePolicy2)
        self.cb_OyMs.setMinimumSize(QSize(119, 0))
        self.cb_OyMs.setMaximumSize(QSize(300, 16777215))
        self.cb_OyMs.setFont(font1)
        self.cb_OyMs.setStyleSheet(u"QComboBox {\n"
"	background-image: url(:/featherIcons/featherIcons/zoom-out.svg);\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width:"
                        " 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/featherIcons/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox::enabled{\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"QComboBox::disabled{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}")

        self.verticalLayout_9.addWidget(self.cb_OyMs)


        self.verticalLayout_3.addWidget(self.frame_12, 0, Qt.AlignHCenter)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border:0px;\n"
"background-color:rgba(0, 0, 0, 0)")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_18.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_10.addWidget(self.label_18, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_7)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(300, 0))
        self.frame_14.setMaximumSize(QSize(300, 16777215))
        self.frame_14.setStyleSheet(u"border:0px;\n"
"background-color:rgba(0, 0, 0, 0)")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, 0, -1)
        self.cb_Supervisores = QComboBox(self.frame_14)
        self.cb_Supervisores.setObjectName(u"cb_Supervisores")
        sizePolicy2.setHeightForWidth(self.cb_Supervisores.sizePolicy().hasHeightForWidth())
        self.cb_Supervisores.setSizePolicy(sizePolicy2)
        self.cb_Supervisores.setMinimumSize(QSize(300, 0))
        self.cb_Supervisores.setMaximumSize(QSize(300, 16777215))
        self.cb_Supervisores.setFont(font1)
        self.cb_Supervisores.setStyleSheet(u"QComboBox {\n"
"	background-image: url(:/featherIcons/featherIcons/zoom-out.svg);\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width:"
                        " 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/featherIcons/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox::enabled{\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"QComboBox::disabled{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}")

        self.verticalLayout_11.addWidget(self.cb_Supervisores)


        self.verticalLayout_3.addWidget(self.frame_14, 0, Qt.AlignHCenter)

        self.frame_15 = QFrame(self.frame_7)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border:0px;\n"
"background-color:rgba(0, 0, 0, 0)")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_15)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_19)


        self.verticalLayout_3.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_16)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.cb_Cuadrillas = QComboBox(self.frame_16)
        self.cb_Cuadrillas.setObjectName(u"cb_Cuadrillas")
        sizePolicy1.setHeightForWidth(self.cb_Cuadrillas.sizePolicy().hasHeightForWidth())
        self.cb_Cuadrillas.setSizePolicy(sizePolicy1)
        self.cb_Cuadrillas.setMinimumSize(QSize(119, 0))
        self.cb_Cuadrillas.setMaximumSize(QSize(300, 16777215))
        self.cb_Cuadrillas.setFont(font1)
        self.cb_Cuadrillas.setStyleSheet(u"QComboBox {\n"
"	background-image: url(:/featherIcons/featherIcons/zoom-out.svg);\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width:"
                        " 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/featherIcons/chevron-down.svg);\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"QComboBox::enabled{\n"
"	background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"QComboBox::disabled{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,\n"
"                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);\n"
"}")

        self.verticalLayout_13.addWidget(self.cb_Cuadrillas)


        self.verticalLayout_3.addWidget(self.frame_16, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"border:0px;\n"
"background-color:rgba(0, 0, 0, 0)")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1, Qt.AlignHCenter)

        self.label_21 = QLabel(self.frame_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_21, 0, 1, 1, 1, Qt.AlignHCenter)

        self.txt_FechaDesde = QLineEdit(self.frame_8)
        self.txt_FechaDesde.setObjectName(u"txt_FechaDesde")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txt_FechaDesde.sizePolicy().hasHeightForWidth())
        self.txt_FechaDesde.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        self.txt_FechaDesde.setFont(font4)
        self.txt_FechaDesde.setFocusPolicy(Qt.StrongFocus)
        self.txt_FechaDesde.setStyleSheet(u"QLineEdit{\n"
" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 1px 1px 3px;\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"QLineEdit::enabled{\n"
"background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"QLineEdit::disabled{\n"
"background-color:rgba(255, 255, 255, 255);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}")
        self.txt_FechaDesde.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_FechaDesde, 1, 0, 1, 1, Qt.AlignHCenter)

        self.txt_FechaHasta = QLineEdit(self.frame_8)
        self.txt_FechaHasta.setObjectName(u"txt_FechaHasta")
        sizePolicy3.setHeightForWidth(self.txt_FechaHasta.sizePolicy().hasHeightForWidth())
        self.txt_FechaHasta.setSizePolicy(sizePolicy3)
        self.txt_FechaHasta.setFont(font4)
        self.txt_FechaHasta.setFocusPolicy(Qt.StrongFocus)
        self.txt_FechaHasta.setStyleSheet(u"QLineEdit{\n"
" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 1px 1px 3px;\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"QLineEdit::enabled{\n"
"background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"QLineEdit::disabled{\n"
"background-color:rgba(255, 255, 255, 255);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}")
        self.txt_FechaHasta.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_FechaHasta, 1, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_8, 0, Qt.AlignVCenter)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:0px;\n"
"background-color:rgba(0, 0, 0, 0)")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pb_Activacion = QPushButton(self.frame_10)
        self.pb_Activacion.setObjectName(u"pb_Activacion")
        self.pb_Activacion.setMinimumSize(QSize(0, 40))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.pb_Activacion.setFont(font5)
        self.pb_Activacion.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgba(240, 120, 14, 210);\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgba(255, 135, 29, 230);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(255, 135, 29, 255);\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}")

        self.verticalLayout_7.addWidget(self.pb_Activacion)


        self.verticalLayout_6.addWidget(self.frame_10)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 9)
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_23)

        self.txt_Alarma = QLineEdit(self.frame_9)
        self.txt_Alarma.setObjectName(u"txt_Alarma")
        sizePolicy3.setHeightForWidth(self.txt_Alarma.sizePolicy().hasHeightForWidth())
        self.txt_Alarma.setSizePolicy(sizePolicy3)
        self.txt_Alarma.setMinimumSize(QSize(102, 0))
        self.txt_Alarma.setFont(font4)
        self.txt_Alarma.setFocusPolicy(Qt.StrongFocus)
        self.txt_Alarma.setStyleSheet(u"QLineEdit{\n"
" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 1px 1px 3px;\n"
"    min-width: 6em;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}\n"
"QLineEdit::enabled{\n"
"background-color:rgba(255, 255, 255, 255);\n"
"}\n"
"QLineEdit::disabled{\n"
"background-color:rgba(255, 255, 255, 255);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"}")

        self.verticalLayout_5.addWidget(self.txt_Alarma)

        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(15)
        font6.setBold(True)
        self.label_22.setFont(font6)
        self.label_22.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_22)

        self.table_TecnicosCuadrilla = QTableWidget(self.frame_9)
        if (self.table_TecnicosCuadrilla.columnCount() < 4):
            self.table_TecnicosCuadrilla.setColumnCount(4)
        icon = QIcon()
        icon.addFile(u":/featherIcons/featherIcons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(12)
        font7.setWeight(QFont.Medium)
        font7.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font7);
        __qtablewidgetitem.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem.setForeground(brush);
        __qtablewidgetitem.setIcon(icon);
        self.table_TecnicosCuadrilla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon1 = QIcon()
        icon1.addFile(u":/Icons/ResourcesFolder/featherIcons/unlock.svg", QSize(), QIcon.Normal, QIcon.Off)
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(12)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font8);
        __qtablewidgetitem1.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem1.setIcon(icon1);
        self.table_TecnicosCuadrilla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/ResourcesFolder/featherIcons/briefcase.svg", QSize(), QIcon.Normal, QIcon.Off)
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(12)
        font9.setBold(False)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font9);
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem2.setIcon(icon2);
        self.table_TecnicosCuadrilla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/ResourcesFolder/featherIcons/at-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font9);
        __qtablewidgetitem3.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem3.setForeground(brush);
        __qtablewidgetitem3.setIcon(icon3);
        self.table_TecnicosCuadrilla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_TecnicosCuadrilla.setObjectName(u"table_TecnicosCuadrilla")
        sizePolicy1.setHeightForWidth(self.table_TecnicosCuadrilla.sizePolicy().hasHeightForWidth())
        self.table_TecnicosCuadrilla.setSizePolicy(sizePolicy1)
        font10 = QFont()
        font10.setFamilies([u"Arial"])
        font10.setPointSize(10)
        font10.setWeight(QFont.Medium)
        self.table_TecnicosCuadrilla.setFont(font10)
        self.table_TecnicosCuadrilla.setAutoFillBackground(True)
        self.table_TecnicosCuadrilla.setStyleSheet(u"QHeaderView:section\n"
"{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"border:0px;\n"
"border-right:2px solid gray;\n"
"\n"
"}\n"
"QTableWidget{\n"
"background-color: rgba(255, 255, 255, 255);\n"
"border-radius:0px;\n"
"}")
        self.table_TecnicosCuadrilla.setFrameShape(QFrame.NoFrame)
        self.table_TecnicosCuadrilla.setLineWidth(2)
        self.table_TecnicosCuadrilla.setMidLineWidth(0)
        self.table_TecnicosCuadrilla.setAlternatingRowColors(False)
        self.table_TecnicosCuadrilla.setGridStyle(Qt.SolidLine)
        self.table_TecnicosCuadrilla.setSortingEnabled(False)
        self.table_TecnicosCuadrilla.horizontalHeader().setVisible(True)
        self.table_TecnicosCuadrilla.horizontalHeader().setHighlightSections(False)
        self.table_TecnicosCuadrilla.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_TecnicosCuadrilla.verticalHeader().setVisible(False)
        self.table_TecnicosCuadrilla.verticalHeader().setHighlightSections(False)

        self.verticalLayout_5.addWidget(self.table_TecnicosCuadrilla)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Solicitud de Formatos", None))
        self.pb_minimized.setText("")
        self.pb_exit.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RBS", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Formato", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"O&M a enviar", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Supervisor", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Cuadrilla", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Desde", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Hasta", None))
        self.txt_FechaDesde.setInputMask("")
        self.txt_FechaDesde.setText("")
        self.txt_FechaHasta.setInputMask("")
        self.txt_FechaHasta.setText("")
        self.pb_Activacion.setText(QCoreApplication.translate("MainWindow", u"Solicitar activacion de Formato", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Alarma", None))
        self.txt_Alarma.setInputMask("")
        self.txt_Alarma.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"T\u00e9cnicos de Cuadrilla", None))
        ___qtablewidgetitem = self.table_TecnicosCuadrilla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.table_TecnicosCuadrilla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None));
        ___qtablewidgetitem2 = self.table_TecnicosCuadrilla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"C\u00e9dula", None));
        ___qtablewidgetitem3 = self.table_TecnicosCuadrilla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Correo", None));
    # retranslateUi

