# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowSolicitudPermisosMFVStz.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_SolicitudPermisos(object):
    def setupUi(self, SolicitudPermisos):
        if not SolicitudPermisos.objectName():
            SolicitudPermisos.setObjectName(u"SolicitudPermisos")
        SolicitudPermisos.resize(1000, 730)
        SolicitudPermisos.setMinimumSize(QSize(1000, 654))
        SolicitudPermisos.setMaximumSize(QSize(16777215, 16777215))
        SolicitudPermisos.setStyleSheet(u"background-color : rgba(255, 255, 255, 255);\n"
"border-radius:3;\n"
"border:1px solid black;")
        self.centralwidget = QWidget(SolicitudPermisos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"background-color:rgb(240, 240, 240)")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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
        self.frame_17.setMinimumSize(QSize(0, 45))
        self.frame_17.setStyleSheet(u"background-image: url(:/Images/ResourcesFolder/Logo_Rhelec/Up_Design.jpg);\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(10, 0))
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_18)

        self.label_11 = QLabel(self.frame_17)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 0))
        self.label_11.setStyleSheet(u"background-image: url();\n"
"image: url(:/Images/ResourcesFolder/Logo_Rhelec/Logo_Without_Background.png);\n"
"background-color:rgba(255, 255, 255, 200);\n"
"border-radius:0px;")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.label_12 = QLabel(self.frame_17)
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

        self.frame_19 = QFrame(self.frame_17)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 45))
        self.frame_19.setStyleSheet(u"background-image: url();\n"
"background-color:rgba(91, 133, 150, 200);\n"
"border:0px;\n"
"border-radius:0px;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pbMinimize = QPushButton(self.frame_19)
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

        self.pbMaximize = QPushButton(self.frame_19)
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

        self.pbClose = QPushButton(self.frame_19)
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


        self.horizontalLayout_6.addWidget(self.frame_19)


        self.horizontalLayout_3.addWidget(self.frame_17)


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
"background-color:rgb(240, 240, 240)")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(19)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0px;\n"
"}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0px;\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.cbRBS = QComboBox(self.frame_3)
        self.cbRBS.setObjectName(u"cbRBS")
        self.cbRBS.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbRBS.sizePolicy().hasHeightForWidth())
        self.cbRBS.setSizePolicy(sizePolicy)
        self.cbRBS.setMinimumSize(QSize(215, 35))
        self.cbRBS.setMaximumSize(QSize(400, 35))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(18)
        self.cbRBS.setFont(font2)
        self.cbRBS.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.cbRBS.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"    font-size: 18pt;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"\n"
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
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/ResourcesFolder/featherIcons/ch"
                        "evron-down.svg);\n"
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
"}\n"
"")
        self.cbRBS.setEditable(True)
        self.cbRBS.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.cbRBS.setIconSize(QSize(20, 20))
        self.cbRBS.setFrame(True)

        self.gridLayout.addWidget(self.cbRBS, 1, 0, 1, 1)

        self.lineAlarma = QLineEdit(self.frame_3)
        self.lineAlarma.setObjectName(u"lineAlarma")
        sizePolicy.setHeightForWidth(self.lineAlarma.sizePolicy().hasHeightForWidth())
        self.lineAlarma.setSizePolicy(sizePolicy)
        self.lineAlarma.setMinimumSize(QSize(102, 35))
        self.lineAlarma.setMaximumSize(QSize(16777215, 35))
        font3 = QFont()
        font3.setPointSize(12)
        self.lineAlarma.setFont(font3)
        self.lineAlarma.setStyleSheet(u"QLineEdit{\n"
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

        self.gridLayout.addWidget(self.lineAlarma, 1, 2, 1, 1)


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
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setMaximumSize(QSize(350, 16777215))
        self.frame_5.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"background-color:rgb(240, 240, 240)")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border:0px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignHCenter)

        self.lineRegion = QLineEdit(self.frame_7)
        self.lineRegion.setObjectName(u"lineRegion")
        self.lineRegion.setEnabled(False)
        self.lineRegion.setMinimumSize(QSize(0, 30))
        self.lineRegion.setMaximumSize(QSize(70, 16777215))
        self.lineRegion.setFont(font4)
        self.lineRegion.setStyleSheet(u"border:1px solid black;\n"
"background-color:rgb(255, 255, 255)")
        self.lineRegion.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineRegion, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(70, 16777215))
        self.label_4.setFont(font4)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1, Qt.AlignHCenter)

        self.lineZona = QLineEdit(self.frame_7)
        self.lineZona.setObjectName(u"lineZona")
        self.lineZona.setEnabled(False)
        self.lineZona.setMinimumSize(QSize(0, 30))
        self.lineZona.setMaximumSize(QSize(70, 16777215))
        self.lineZona.setFont(font4)
        self.lineZona.setStyleSheet(u"border:1px solid black;\n"
"background-color:rgb(255, 255, 255)")
        self.lineZona.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineZona, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(100, 16777215))
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1, Qt.AlignHCenter)

        self.lineProvincia = QLineEdit(self.frame_7)
        self.lineProvincia.setObjectName(u"lineProvincia")
        self.lineProvincia.setEnabled(False)
        self.lineProvincia.setMinimumSize(QSize(0, 30))
        self.lineProvincia.setMaximumSize(QSize(150, 16777215))
        self.lineProvincia.setFont(font4)
        self.lineProvincia.setStyleSheet(u"border:1px solid black;\n"
"background-color:rgb(255, 255, 255)")
        self.lineProvincia.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineProvincia, 2, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_7, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pbCopyCorreos = QPushButton(self.frame_5)
        self.pbCopyCorreos.setObjectName(u"pbCopyCorreos")
        self.pbCopyCorreos.setMinimumSize(QSize(240, 25))
        self.pbCopyCorreos.setMaximumSize(QSize(240, 25))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(12)
        font5.setItalic(True)
        self.pbCopyCorreos.setFont(font5)
        self.pbCopyCorreos.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_2.addWidget(self.pbCopyCorreos, 0, Qt.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(15)
        self.label_17.setFont(font6)
        self.label_17.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_17)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"border:0px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.cbOyMs = QComboBox(self.frame_12)
        self.cbOyMs.setObjectName(u"cbOyMs")
        sizePolicy1.setHeightForWidth(self.cbOyMs.sizePolicy().hasHeightForWidth())
        self.cbOyMs.setSizePolicy(sizePolicy1)
        self.cbOyMs.setMinimumSize(QSize(119, 35))
        self.cbOyMs.setMaximumSize(QSize(300, 35))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(16)
        self.cbOyMs.setFont(font7)
        self.cbOyMs.setStyleSheet(u"QComboBox {\n"
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
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: "
                        "solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/ResourcesFolder/featherIcons/chevron-down.svg);\n"
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

        self.verticalLayout_6.addWidget(self.cbOyMs)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"border:0px solid gray;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(10)
        self.label_7.setFont(font8)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.pbCopyOyMCorreo = QPushButton(self.frame_13)
        self.pbCopyOyMCorreo.setObjectName(u"pbCopyOyMCorreo")
        self.pbCopyOyMCorreo.setMinimumSize(QSize(40, 25))
        self.pbCopyOyMCorreo.setMaximumSize(QSize(40, 25))
        self.pbCopyOyMCorreo.setStyleSheet(u"QPushButton{\n"
"image: url(:/featherIcons/ResourcesFolder/featherIcons/at-sign.svg);\n"
"background-color: rgb(154, 192, 213);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-right:1px solid gray;\n"
"padding:3 3 3 3;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(124, 162, 183);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(154, 192, 213);\n"
"}")

        self.horizontalLayout_10.addWidget(self.pbCopyOyMCorreo)

        self.pbCopyOyMTel = QPushButton(self.frame_13)
        self.pbCopyOyMTel.setObjectName(u"pbCopyOyMTel")
        self.pbCopyOyMTel.setMinimumSize(QSize(40, 25))
        self.pbCopyOyMTel.setMaximumSize(QSize(40, 25))
        self.pbCopyOyMTel.setStyleSheet(u"QPushButton{\n"
"image: url(:/featherIcons/ResourcesFolder/featherIcons/phone-call.svg);\n"
"background-color: rgb(154, 192, 213);\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-left:1px solid gray;\n"
"padding:3 3 3 3;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(124, 162, 183);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(154, 192, 213);\n"
"}")

        self.horizontalLayout_10.addWidget(self.pbCopyOyMTel)


        self.verticalLayout_6.addWidget(self.frame_13, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font6)
        self.label_18.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_18)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"border:0px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cbSupervisores = QComboBox(self.frame_10)
        self.cbSupervisores.setObjectName(u"cbSupervisores")
        sizePolicy1.setHeightForWidth(self.cbSupervisores.sizePolicy().hasHeightForWidth())
        self.cbSupervisores.setSizePolicy(sizePolicy1)
        self.cbSupervisores.setMinimumSize(QSize(119, 35))
        self.cbSupervisores.setMaximumSize(QSize(300, 35))
        self.cbSupervisores.setFont(font7)
        self.cbSupervisores.setStyleSheet(u"QComboBox {\n"
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
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: "
                        "solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/ResourcesFolder/featherIcons/chevron-down.svg);\n"
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

        self.verticalLayout_3.addWidget(self.cbSupervisores)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"border:0px solid gray;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.pbCopySupervisorCorreo = QPushButton(self.frame_11)
        self.pbCopySupervisorCorreo.setObjectName(u"pbCopySupervisorCorreo")
        self.pbCopySupervisorCorreo.setMinimumSize(QSize(40, 25))
        self.pbCopySupervisorCorreo.setMaximumSize(QSize(40, 25))
        self.pbCopySupervisorCorreo.setStyleSheet(u"QPushButton{\n"
"image: url(:/featherIcons/ResourcesFolder/featherIcons/at-sign.svg);\n"
"background-color: rgb(154, 192, 213);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-right:1px solid gray;\n"
"padding:3 3 3 3;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(124, 162, 183);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(154, 192, 213);\n"
"}")

        self.horizontalLayout_9.addWidget(self.pbCopySupervisorCorreo)

        self.pbCopySupervisorTel = QPushButton(self.frame_11)
        self.pbCopySupervisorTel.setObjectName(u"pbCopySupervisorTel")
        self.pbCopySupervisorTel.setMinimumSize(QSize(40, 25))
        self.pbCopySupervisorTel.setMaximumSize(QSize(40, 25))
        self.pbCopySupervisorTel.setStyleSheet(u"QPushButton{\n"
"image: url(:/featherIcons/ResourcesFolder/featherIcons/phone-call.svg);\n"
"background-color: rgb(154, 192, 213);\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-left:1px solid gray;\n"
"padding:3 3 3 3;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(124, 162, 183);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(154, 192, 213);\n"
"}")

        self.horizontalLayout_9.addWidget(self.pbCopySupervisorTel)


        self.verticalLayout_3.addWidget(self.frame_11, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font6)
        self.label_19.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_19)

        self.cbCuadrillas = QComboBox(self.frame_5)
        self.cbCuadrillas.setObjectName(u"cbCuadrillas")
        sizePolicy.setHeightForWidth(self.cbCuadrillas.sizePolicy().hasHeightForWidth())
        self.cbCuadrillas.setSizePolicy(sizePolicy)
        self.cbCuadrillas.setMinimumSize(QSize(119, 35))
        self.cbCuadrillas.setMaximumSize(QSize(300, 35))
        self.cbCuadrillas.setFont(font7)
        self.cbCuadrillas.setStyleSheet(u"QComboBox {\n"
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
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: "
                        "solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/ResourcesFolder/featherIcons/chevron-down.svg);\n"
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

        self.verticalLayout_2.addWidget(self.cbCuadrillas)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.cbEliminarFormatos = QCheckBox(self.frame_5)
        self.cbEliminarFormatos.setObjectName(u"cbEliminarFormatos")
        self.cbEliminarFormatos.setMinimumSize(QSize(270, 0))
        self.cbEliminarFormatos.setMaximumSize(QSize(270, 16777215))
        font9 = QFont()
        font9.setFamilies([u"Arial"])
        font9.setPointSize(11)
        font9.setBold(True)
        font9.setItalic(True)
        font9.setUnderline(False)
        font9.setStrikeOut(False)
        font9.setKerning(True)
        self.cbEliminarFormatos.setFont(font9)
        self.cbEliminarFormatos.setStyleSheet(u"border:0px;")
        self.cbEliminarFormatos.setIconSize(QSize(10, 10))
        self.cbEliminarFormatos.setTristate(False)

        self.verticalLayout_2.addWidget(self.cbEliminarFormatos, 0, Qt.AlignHCenter)

        self.pbEnviarFormatos = QPushButton(self.frame_5)
        self.pbEnviarFormatos.setObjectName(u"pbEnviarFormatos")
        self.pbEnviarFormatos.setMinimumSize(QSize(290, 40))
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(True)
        self.pbEnviarFormatos.setFont(font10)
        self.pbEnviarFormatos.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"	color: rgb(0, 0, 0);\n"
"background-color: rgb(154, 192, 213);\n"
"border:0px;\n"
"padding:0 10 0 10;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(184, 222, 243);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(154, 192, 213);\n"
"}\n"
"QPushButton:disabled{\n"
"	background-color: rgba(0, 0, 0, 100);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.pbEnviarFormatos)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.horizontalLayout_2.addWidget(self.frame_5, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u" border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"\n"
"\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"background-color:rgb(240, 240, 240)")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 9)
        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 39))
        self.frame_8.setMaximumSize(QSize(16777215, 39))
        self.frame_8.setStyleSheet(u"border:0px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 9, 0, 0)
        self.label_23 = QLabel(self.frame_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font6)
        self.label_23.setStyleSheet(u"background-color: rgb(172, 172, 172);\n"
"border:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"padding:0 10 0 10;")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_23)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.cbPermisos = QComboBox(self.frame_8)
        self.cbPermisos.setObjectName(u"cbPermisos")
        self.cbPermisos.setMinimumSize(QSize(119, 30))
        self.cbPermisos.setFont(font4)
        self.cbPermisos.setStyleSheet(u"QComboBox {\n"
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
"    width: 25px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: "
                        "solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"	image: url(:/featherIcons/ResourcesFolder/featherIcons/chevron-down.svg);\n"
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

        self.horizontalLayout_4.addWidget(self.cbPermisos)

        self.pbAgregarPermiso = QPushButton(self.frame_8)
        self.pbAgregarPermiso.setObjectName(u"pbAgregarPermiso")
        self.pbAgregarPermiso.setMinimumSize(QSize(0, 30))
        self.pbAgregarPermiso.setMaximumSize(QSize(16777215, 30))
        font11 = QFont()
        font11.setFamilies([u"Arial"])
        font11.setPointSize(12)
        self.pbAgregarPermiso.setFont(font11)
        self.pbAgregarPermiso.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(154, 192, 213);\n"
"border:0px;\n"
"padding:0 10 0 10;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:00px;\n"
"border-bottom-right-radius:00px;\n"
"border-right:1px solid gray;\n"
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

        self.horizontalLayout_4.addWidget(self.pbAgregarPermiso)

        self.pbEliminarPermiso = QPushButton(self.frame_8)
        self.pbEliminarPermiso.setObjectName(u"pbEliminarPermiso")
        self.pbEliminarPermiso.setMinimumSize(QSize(0, 30))
        self.pbEliminarPermiso.setMaximumSize(QSize(16777215, 30))
        self.pbEliminarPermiso.setFont(font11)
        self.pbEliminarPermiso.setStyleSheet(u"QPushButton{\n"
"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(154, 192, 213);\n"
"border:0px;\n"
"padding:0 10 0 10;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
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

        self.horizontalLayout_4.addWidget(self.pbEliminarPermiso)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.tablePermisosNecesarios = QTableWidget(self.frame_9)
        if (self.tablePermisosNecesarios.columnCount() < 5):
            self.tablePermisosNecesarios.setColumnCount(5)
        icon = QIcon()
        icon.addFile(u":/featherIcons/ResourcesFolder/featherIcons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font11);
        __qtablewidgetitem.setIcon(icon);
        self.tablePermisosNecesarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        icon1 = QIcon()
        icon1.addFile(u":/featherIcons/ResourcesFolder/featherIcons/calendar.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font11);
        __qtablewidgetitem1.setIcon(icon1);
        self.tablePermisosNecesarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        icon2 = QIcon()
        icon2.addFile(u":/featherIcons/ResourcesFolder/featherIcons/clock.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font11);
        __qtablewidgetitem2.setIcon(icon2);
        self.tablePermisosNecesarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font11);
        __qtablewidgetitem3.setIcon(icon1);
        self.tablePermisosNecesarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font11);
        __qtablewidgetitem4.setIcon(icon2);
        self.tablePermisosNecesarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tablePermisosNecesarios.setObjectName(u"tablePermisosNecesarios")
        self.tablePermisosNecesarios.setFont(font11)
        self.tablePermisosNecesarios.setStyleSheet(u"QHeaderView:section\n"
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
"border-radius:10px;\n"
"border-top-left-radius:0px;\n"
"}")
        self.tablePermisosNecesarios.horizontalHeader().setHighlightSections(False)
        self.tablePermisosNecesarios.verticalHeader().setVisible(False)
        self.tablePermisosNecesarios.verticalHeader().setHighlightSections(False)

        self.verticalLayout_5.addWidget(self.tablePermisosNecesarios)

        self.frame_20 = QFrame(self.frame_9)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"border:0px;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 9, 0, 0)
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 30))
        self.frame_21.setMaximumSize(QSize(16777215, 30))
        self.frame_21.setStyleSheet(u"border:0px;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.frame_21)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"background-color: rgb(172, 172, 172);\n"
"border:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"padding:0 10 0 10;")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_24)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pbAgregarTecnico = QPushButton(self.frame_21)
        self.pbAgregarTecnico.setObjectName(u"pbAgregarTecnico")
        self.pbAgregarTecnico.setMinimumSize(QSize(0, 30))
        self.pbAgregarTecnico.setMaximumSize(QSize(16777215, 30))
        self.pbAgregarTecnico.setFont(font11)
        self.pbAgregarTecnico.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(154, 192, 213);\n"
"border:0px;\n"
"padding:0 10 0 10;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius:00px;\n"
"border-bottom-right-radius:00px;\n"
"border-right:1px solid gray;\n"
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

        self.horizontalLayout_5.addWidget(self.pbAgregarTecnico)

        self.pbEliminarTecnico = QPushButton(self.frame_21)
        self.pbEliminarTecnico.setObjectName(u"pbEliminarTecnico")
        self.pbEliminarTecnico.setMinimumSize(QSize(0, 30))
        self.pbEliminarTecnico.setMaximumSize(QSize(16777215, 30))
        self.pbEliminarTecnico.setFont(font11)
        self.pbEliminarTecnico.setStyleSheet(u"QPushButton{\n"
"border-radius:5px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(154, 192, 213);\n"
"border:0px;\n"
"padding:0 10 0 10;\n"
"border-top-right-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
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

        self.horizontalLayout_5.addWidget(self.pbEliminarTecnico)


        self.horizontalLayout_8.addWidget(self.frame_21)


        self.verticalLayout_5.addWidget(self.frame_20)

        self.tableTecnicosCuadrilla = QTableWidget(self.frame_9)
        if (self.tableTecnicosCuadrilla.columnCount() < 4):
            self.tableTecnicosCuadrilla.setColumnCount(4)
        icon3 = QIcon()
        icon3.addFile(u":/featherIcons/ResourcesFolder/featherIcons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font12 = QFont()
        font12.setFamilies([u"Arial"])
        font12.setPointSize(12)
        font12.setWeight(QFont.Medium)
        font12.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font12);
        __qtablewidgetitem5.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem5.setForeground(brush);
        __qtablewidgetitem5.setIcon(icon3);
        self.tableTecnicosCuadrilla.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        icon4 = QIcon()
        icon4.addFile(u":/featherIcons/ResourcesFolder/featherIcons/unlock.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font11);
        __qtablewidgetitem6.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem6.setIcon(icon4);
        self.tableTecnicosCuadrilla.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        icon5 = QIcon()
        icon5.addFile(u":/featherIcons/ResourcesFolder/featherIcons/briefcase.svg", QSize(), QIcon.Normal, QIcon.Off)
        font13 = QFont()
        font13.setFamilies([u"Arial"])
        font13.setPointSize(12)
        font13.setBold(False)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font13);
        __qtablewidgetitem7.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem7.setIcon(icon5);
        self.tableTecnicosCuadrilla.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        icon6 = QIcon()
        icon6.addFile(u":/featherIcons/ResourcesFolder/featherIcons/at-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font13);
        __qtablewidgetitem8.setBackground(QColor(217, 225, 243));
        __qtablewidgetitem8.setForeground(brush);
        __qtablewidgetitem8.setIcon(icon6);
        self.tableTecnicosCuadrilla.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.tableTecnicosCuadrilla.setObjectName(u"tableTecnicosCuadrilla")
        sizePolicy.setHeightForWidth(self.tableTecnicosCuadrilla.sizePolicy().hasHeightForWidth())
        self.tableTecnicosCuadrilla.setSizePolicy(sizePolicy)
        font14 = QFont()
        font14.setFamilies([u"Arial"])
        font14.setPointSize(12)
        font14.setWeight(QFont.Medium)
        self.tableTecnicosCuadrilla.setFont(font14)
        self.tableTecnicosCuadrilla.setAutoFillBackground(True)
        self.tableTecnicosCuadrilla.setStyleSheet(u"QHeaderView:section\n"
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
"border-radius:10px;\n"
"border-top-left-radius:0px;\n"
"}")
        self.tableTecnicosCuadrilla.setFrameShape(QFrame.NoFrame)
        self.tableTecnicosCuadrilla.setLineWidth(2)
        self.tableTecnicosCuadrilla.setMidLineWidth(0)
        self.tableTecnicosCuadrilla.setAlternatingRowColors(False)
        self.tableTecnicosCuadrilla.setGridStyle(Qt.SolidLine)
        self.tableTecnicosCuadrilla.setSortingEnabled(False)
        self.tableTecnicosCuadrilla.horizontalHeader().setVisible(True)
        self.tableTecnicosCuadrilla.horizontalHeader().setHighlightSections(False)
        self.tableTecnicosCuadrilla.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableTecnicosCuadrilla.verticalHeader().setVisible(False)
        self.tableTecnicosCuadrilla.verticalHeader().setHighlightSections(False)

        self.verticalLayout_5.addWidget(self.tableTecnicosCuadrilla)


        self.horizontalLayout_2.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        SolicitudPermisos.setCentralWidget(self.centralwidget)

        self.retranslateUi(SolicitudPermisos)

        QMetaObject.connectSlotsByName(SolicitudPermisos)
    # setupUi

    def retranslateUi(self, SolicitudPermisos):
        SolicitudPermisos.setWindowTitle(QCoreApplication.translate("SolicitudPermisos", u"Solicitud de Permisos", None))
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("SolicitudPermisos", u"Gesti\u00f3n de Permisos", None))
        self.pbMinimize.setText("")
        self.pbMaximize.setText("")
        self.pbClose.setText("")
        self.label_2.setText(QCoreApplication.translate("SolicitudPermisos", u"RBS", None))
        self.label_3.setText(QCoreApplication.translate("SolicitudPermisos", u"Alarma", None))
        self.label.setText(QCoreApplication.translate("SolicitudPermisos", u"Regi\u00f3n:", None))
        self.label_4.setText(QCoreApplication.translate("SolicitudPermisos", u"Zona:", None))
        self.label_5.setText(QCoreApplication.translate("SolicitudPermisos", u"Provincia:", None))
        self.pbCopyCorreos.setText(QCoreApplication.translate("SolicitudPermisos", u"Copiar Correos Region/Zona", None))
        self.label_17.setText(QCoreApplication.translate("SolicitudPermisos", u"O&M a enviar", None))
        self.label_7.setText(QCoreApplication.translate("SolicitudPermisos", u"Copiar:", None))
        self.pbCopyOyMCorreo.setText("")
        self.pbCopyOyMTel.setText("")
        self.label_18.setText(QCoreApplication.translate("SolicitudPermisos", u"Supervisor", None))
        self.label_6.setText(QCoreApplication.translate("SolicitudPermisos", u"Copiar:", None))
        self.pbCopySupervisorCorreo.setText("")
        self.pbCopySupervisorTel.setText("")
        self.label_19.setText(QCoreApplication.translate("SolicitudPermisos", u"Cuadrilla", None))
        self.cbEliminarFormatos.setText(QCoreApplication.translate("SolicitudPermisos", u"Eliminar Formatos Anteriores", None))
        self.pbEnviarFormatos.setText(QCoreApplication.translate("SolicitudPermisos", u"Generar Formatos", None))
        self.label_23.setText(QCoreApplication.translate("SolicitudPermisos", u"Permisos Necesarios", None))
        self.pbAgregarPermiso.setText(QCoreApplication.translate("SolicitudPermisos", u"Agregar", None))
        self.pbEliminarPermiso.setText(QCoreApplication.translate("SolicitudPermisos", u"Eliminar", None))
        ___qtablewidgetitem = self.tablePermisosNecesarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SolicitudPermisos", u"Permiso", None));
        ___qtablewidgetitem1 = self.tablePermisosNecesarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SolicitudPermisos", u"Fecha Ingreso", None));
        ___qtablewidgetitem2 = self.tablePermisosNecesarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SolicitudPermisos", u"Hora Ingreso", None));
        ___qtablewidgetitem3 = self.tablePermisosNecesarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SolicitudPermisos", u"Fecha Salida", None));
        ___qtablewidgetitem4 = self.tablePermisosNecesarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SolicitudPermisos", u"Hora Salida", None));
        self.label_24.setText(QCoreApplication.translate("SolicitudPermisos", u"T\u00e9cnicos de la Cuadrilla", None))
        self.pbAgregarTecnico.setText(QCoreApplication.translate("SolicitudPermisos", u"Agregar", None))
        self.pbEliminarTecnico.setText(QCoreApplication.translate("SolicitudPermisos", u"Eliminar", None))
        ___qtablewidgetitem5 = self.tableTecnicosCuadrilla.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SolicitudPermisos", u"Nombre", None));
        ___qtablewidgetitem6 = self.tableTecnicosCuadrilla.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SolicitudPermisos", u"Tel\u00e9fono", None));
        ___qtablewidgetitem7 = self.tableTecnicosCuadrilla.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SolicitudPermisos", u"C\u00e9dula", None));
        ___qtablewidgetitem8 = self.tableTecnicosCuadrilla.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SolicitudPermisos", u"Correo", None));
    # retranslateUi

