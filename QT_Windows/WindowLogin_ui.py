# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WindowLogin.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QWidget)
import resources_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.setWindowModality(Qt.NonModal)
        LoginWindow.resize(650, 380)
        LoginWindow.setMinimumSize(QSize(650, 300))
        LoginWindow.setMaximumSize(QSize(650, 400))
        font = QFont()
        font.setFamilies([u"Adobe Devanagari"])
        LoginWindow.setFont(font)
        LoginWindow.setMouseTracking(False)
        LoginWindow.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/Images/ResourcesFolder/Imagenes/Logo_Lineas.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setWindowOpacity(1.000000000000000)
        LoginWindow.setAutoFillBackground(True)
        LoginWindow.setStyleSheet(u"")
        LoginWindow.setInputMethodHints(Qt.ImhNone)
        LoginWindow.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        LoginWindow.setAnimated(True)
        LoginWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"\n"
"background-color : rgba(255, 255, 255, 235);\n"
"border-radius:30;\n"
"border:1px solid gray;\n"
"\n"
"}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(62, 60, 200, 200))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgba(180, 180, 180, 255);\n"
"border-radius:100;\n"
"image: url(:/Images/ResourcesFolder/Logo_Rhelec/Antenna.png);\n"
"border:0px;\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 60, 281, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(27)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border:0px;\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)
        self.txtUsername = QLineEdit(self.centralwidget)
        self.txtUsername.setObjectName(u"txtUsername")
        self.txtUsername.setGeometry(QRect(410, 120, 191, 41))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        font2.setBold(False)
        self.txtUsername.setFont(font2)
        self.txtUsername.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.txtUsername.setMaxLength(16)
        self.txtUsername.setCursorPosition(0)
        self.txtUsername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txtUsername.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lblIconUsername = QLabel(self.centralwidget)
        self.lblIconUsername.setObjectName(u"lblIconUsername")
        self.lblIconUsername.setGeometry(QRect(386, 130, 21, 21))
        self.lblIconUsername.setStyleSheet(u"image: url(:/featherIcons/ResourcesFolder/featherIcons/user.svg);\n"
"background-color: rgb(190, 190, 190);\n"
"border-radius: 10px;\n"
"border:0px;")
        self.frameUsername = QFrame(self.centralwidget)
        self.frameUsername.setObjectName(u"frameUsername")
        self.frameUsername.setGeometry(QRect(380, 120, 221, 41))
        self.frameUsername.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.frameUsername.setFrameShape(QFrame.StyledPanel)
        self.frameUsername.setFrameShadow(QFrame.Raised)
        self.framePassword = QFrame(self.centralwidget)
        self.framePassword.setObjectName(u"framePassword")
        self.framePassword.setGeometry(QRect(380, 190, 221, 41))
        self.framePassword.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.framePassword.setFrameShape(QFrame.StyledPanel)
        self.framePassword.setFrameShadow(QFrame.Raised)
        self.txtPassword = QLineEdit(self.centralwidget)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setGeometry(QRect(410, 190, 191, 41))
        self.txtPassword.setFont(font2)
        self.txtPassword.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(190, 190, 190);\n"
"border:0px;")
        self.txtPassword.setMaxLength(16)
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.txtPassword.setCursorPosition(0)
        self.txtPassword.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txtPassword.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.lblIconPassword = QLabel(self.centralwidget)
        self.lblIconPassword.setObjectName(u"lblIconPassword")
        self.lblIconPassword.setGeometry(QRect(386, 200, 21, 21))
        self.lblIconPassword.setStyleSheet(u"image: url(:/featherIcons/ResourcesFolder/featherIcons/lock.svg);\n"
"background-color: rgb(190, 190, 190);\n"
"border-radius: 10px;\n"
"border:0px;")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(38, 230, 251, 90))
        self.frame_4.setStyleSheet(u"image: url(:/Images/ResourcesFolder/Logo_Rhelec/LetrasRhelec.png);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pbAcceder = QPushButton(self.centralwidget)
        self.pbAcceder.setObjectName(u"pbAcceder")
        self.pbAcceder.setGeometry(QRect(380, 260, 221, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.pbAcceder.setFont(font3)
        self.pbAcceder.setStyleSheet(u"QPushButton{\n"
"	border-radius:15px;\n"
"	color: rgb(0, 0, 0);\n"
"background-color: rgb(154, 192, 213);\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(124, 162, 183);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(154, 192, 213);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 320, 251, 20))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(11)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_webpage = QLabel(self.centralwidget)
        self.lbl_webpage.setObjectName(u"lbl_webpage")
        self.lbl_webpage.setGeometry(QRect(459, 340, 141, 20))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(11)
        font5.setUnderline(True)
        self.lbl_webpage.setFont(font5)
        self.lbl_webpage.setStyleSheet(u"color: rgb(35, 170, 242);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border:0px;")
        self.lbl_webpage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_webpage.setOpenExternalLinks(True)
        self.pbClose = QPushButton(self.centralwidget)
        self.pbClose.setObjectName(u"pbClose")
        self.pbClose.setGeometry(QRect(610, 13, 21, 21))
        self.pbClose.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	image: url(:/featherIcons/ResourcesFolder/featherIcons/x-square.svg);\n"
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
        self.pbMinimize = QPushButton(self.centralwidget)
        self.pbMinimize.setObjectName(u"pbMinimize")
        self.pbMinimize.setGeometry(QRect(580, 13, 21, 21))
        self.pbMinimize.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"	image: url(:/featherIcons/ResourcesFolder/featherIcons/divide-square.svg);\n"
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
        LoginWindow.setCentralWidget(self.centralwidget)
        self.frameUsername.raise_()
        self.label.raise_()
        self.txtUsername.raise_()
        self.lblIconUsername.raise_()
        self.framePassword.raise_()
        self.txtPassword.raise_()
        self.lblIconPassword.raise_()
        self.pbAcceder.raise_()
        self.label_4.raise_()
        self.pbClose.raise_()
        self.pbMinimize.raise_()
        self.lbl_webpage.raise_()
        self.frame.raise_()
        self.frame_4.raise_()

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Iniciar Sesi\u00f3n - RHELEC", None))
#if QT_CONFIG(tooltip)
        LoginWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        LoginWindow.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.frame.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Inicio de Sesi\u00f3n", None))
        self.txtUsername.setText("")
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Usuario", None))
        self.lblIconUsername.setText("")
        self.txtPassword.setText("")
        self.txtPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Contrase\u00f1a", None))
        self.lblIconPassword.setText("")
        self.pbAcceder.setText(QCoreApplication.translate("LoginWindow", u"Acceder", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Grupo Rhelec Ingenier\u00eda Cia. Ltda.", None))
        self.lbl_webpage.setText(QCoreApplication.translate("LoginWindow", u"<a href=\"https://www.rhelec.ec/\">www.rhelec.ec</a>", None))
        self.pbClose.setText("")
        self.pbMinimize.setText("")
    # retranslateUi

