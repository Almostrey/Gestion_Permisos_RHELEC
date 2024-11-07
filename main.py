from sys import argv, path
from os import getcwd
path.append(getcwd()+'/QT_Resources')
from openpyxl import load_workbook
from datetime import date, timedelta
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from QT_Resources import windowSolicitudFormatos_ui
from QT_Resources import VideoLogoWindow_ui
from PySide6 import QtSvg
from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
from time import sleep
from threading import Timer
from PySide6 import QtMultimedia
from multiprocessing import Process, Queue
import functools

def getDatosRBS(nameRBS:str) -> dict:
    """This Function collect all the data from the RBS (O&M, Supervisor, Team Leader, Cuadrilla, Ubicacion, etc) and returns a dictionary

    Args:
        nameRBS (str): Example: "MILAGRO3", "SALINERITO", etc. Does not matter upper-lowercase

    Returns:
        dict: {nameRBS, OyMOwner, Generator, Region, Zone, Supervisor, Cuadrilla, TeamLeader, Technicians, TelephoneTeamLeader, TelephoneTechnicians}
    """
    RBS = {}
    if nameRBS == "REPNARANCAY":
        RBS = {"nameRBS":"REPNARANCAY", "provinciaRBS" : "Cuenca", "OyMOwner":"Henry Ramos", "eMailOyM":"deguevarab@hotmail.com","Generator":"OLYMPIAN", 
               "Region":"R2", "Zone":"Z2", "Supervisor":"Carlos Bustamante", "Cuadrilla":"CUE02", "TeamLeader":"Pablo Esteban Saca Guaman", 
               "Technicians":["Christian Santiago Saca Guaman", "Andres Esteban Guerrero Zuñiga"], "TelephoneTeamLeader":"0994020739", 
               "TelephoneTechnicians":["0988098112", "-"], "CCTeamLeader" : "105847628", "CCTechnicians" : ["105847644", "107586323"]}
    elif nameRBS == "MILAGROUNI":
        RBS = {"nameRBS" : "MILAGROUNI", "provinciaRBS" : "Guayas", "OyMOwner" : "Fernando Almeida", "eMailOyM" : "deguevarab@hotmail.com", 
               "Generator" : "SIN GENERADOR", "Region" : "R2", "Zone" : "Z1", "Supervisor" : "Carlos Bustamante", "Cuadrilla" : "GYE02", 
               "TeamLeader" : "Carlos Augusto Quiñonez Nazareno", "Technicians" : ["Roberto Alejandro Guilindro Cordova", "Jose Antonio Duarte Caicedo"], 
               "TelephoneTeamLeader" : "0994534040", "TelephoneTechnicians" : ["990328035", "-"], "CCTeamLeader" : "0915855357", 
               "CCTechnicians" : ["0931146500", "0998938604"]}
    else:
        RBS = {"nameRBS" : "", "provinciaRBS" : "", "OyMOwner" : "", "eMailOyM" : "", "Generator" : "", "Region" : "", "Zone" : "", "Supervisor" : "", 
               "Cuadrilla" : "", "TeamLeader" : "", 
               "Technicians" : ["", ""], "TelephoneTeamLeader" : "", 
               "TelephoneTechnicians" : ["", ""], "CCTeamLeader" : "", "CCTechnicians" : ["", ""]}
    return RBS

def createPermisos(nameRBS:str, nameFormato:str, actividad:str, FechaDesde:str, FechaHasta:str, OyMReceiver:str, cuadrilla:str) -> str:
    if nameFormato.upper() == "FINANCIEROS": return modifyPermisosFinancieros(nameRBS, actividad, FechaDesde, FechaHasta, OyMReceiver, cuadrilla)
    elif nameFormato.upper() == "SBA": return modifyPermisosSBA(nameRBS, actividad, FechaDesde, FechaHasta, OyMReceiver, cuadrilla)
    else: return ""

def modifyPermisosFinancieros(nameRBS:str, actividad:str, FechaDesde:str, FechaHasta:str, OyMReceiver:str, cuadrilla:str):
    book = load_workbook("Formatos/PERMISOS FINANCIEROS.xlsx")
    sheet = book.active
    if nameRBS == "REPNARANCAY":
        provinciaRBS = "Cuenca"
    else:
        provinciaRBS = "Guayas"
    sheet["E9"].value = provinciaRBS
    sheet["E10"].value = date.today()
    sheet["E12"].value = nameRBS
    sheet["E13"].value = FechaDesde
    sheet["E14"].value = FechaHasta
    sheet["E16"].value = actividad
    if cuadrilla == "CUE02":
        teamLeader = "Pablo Esteban Saca Guaman"
        telephoneTeamLeader = "0994020739"
        CCTeamLeader = "105847628"
        technicians = ["Christian Santiago Saca Guaman", "Andres Esteban Guerrero Zuñiga"]
        CCtechnicians = ["105847644", "107586323"]
        telephoneTechnicians = ["0988098112", "-"]
    else:
        teamLeader = "Carlos Augusto Quiñonez Nazareno"
        telephoneTeamLeader = "0994534040"
        CCTeamLeader = "0915855357"
        technicians = ["Roberto Alejandro Guilindro Cordova", "Jose Antonio Duarte Caicedo"]
        CCtechnicians = ["0931146500", "0998938604"]
        telephoneTechnicians = ["990328035", "-"]
    sheet["D20"].value = teamLeader
    sheet["E20"].value = CCTeamLeader
    sheet["F20"].value = "RHELEC"
    for i in range(len(technicians)):
        sheet["D"+str(21+i)].value = technicians[i]
        sheet["E"+str(21+i)].value = CCtechnicians[i]
        sheet["F"+str(21+i)].value = "RHELEC"
    pathOutputFile = "Output/"
    nameOutputFile = "PERMISOS FINANCIEROS - " + nameRBS + ".xlsx"
    book.save(pathOutputFile+nameOutputFile)
    book.close
    return pathOutputFile, nameOutputFile

def modifyPermisosSBA(nameRBS:str, actividad:str, FechaDesde:str, FechaHasta:str, OyMReceiver:str, cuadrilla:str):
    if nameRBS == "REPNARANCAY":
        provinciaRBS = "Cuenca"
    else:
        provinciaRBS = "Guayas"
    if cuadrilla == "CUE02":
        teamLeader = "Pablo Esteban Saca Guaman"
        telephoneTeamLeader = "0994020739"
        CCTeamLeader = "105847628"
        technicians = ["Christian Santiago Saca Guaman", "Andres Esteban Guerrero Zuñiga"]
        CCtechnicians = ["105847644", "107586323"]
        telephoneTechnicians = ["0988098112", "-"]
    else:
        teamLeader = "Carlos Augusto Quiñonez Nazareno"
        telephoneTeamLeader = "0994534040"
        CCTeamLeader = "0915855357"
        technicians = ["Roberto Alejandro Guilindro Cordova", "Jose Antonio Duarte Caicedo"]
        CCtechnicians = ["0931146500", "0998938604"]
        telephoneTechnicians = ["990328035", "-"]
    book = load_workbook("Formatos/FORMATO SITIOS SBA RBS.xlsx")
    sheet = book.active
    sheet["D6"].value = nameRBS
    sheet["E3"].value = date.today()
    sheet["D11"].value = FechaDesde
    sheet["D12"].value = FechaHasta
    sheet["C27"].value = actividad
    sheet["D13"].value = teamLeader
    sheet["D14"].value = telephoneTeamLeader
    sheet["C19"].value = teamLeader
    sheet["D19"].value = CCTeamLeader
    sheet["E19"].value = telephoneTeamLeader
    sheet["F19"].value = "RHELEC"
    for i in range(len(technicians)):
        sheet["C"+str(20+i)].value = technicians[i]
        sheet["D"+str(20+i)].value = CCtechnicians[i]
        sheet["E"+str(20+i)].value = telephoneTechnicians[i]
        sheet["F"+str(20+i)].value = "RHELEC"
    pathOutputFile = "Output/"
    nameOutputFile = "FORMATO SITIOS SBA RBS " + nameRBS + ".xlsx"
    book.save(pathOutputFile+nameOutputFile)
    book.close
    return pathOutputFile, nameOutputFile

class WorkerSignals(QtCore.QObject):
    mem_signal = QtCore.Signal(int)

class Worker(QtCore.QRunnable):
    
    def __init__(self, nameRBS:str, nameOym:str, namePermiso:str, actividad:str, pathPermisos:str, nameOutputFile:str):
        super().__init__()
        self.signal = WorkerSignals()
        self.nameRBS = nameRBS
        self.nameOym = nameOym
        self.namePermiso = namePermiso
        self.actividad = actividad
        self.pathPermisos = pathPermisos
        self.nameOutputFile = nameOutputFile
        
    @QtCore.Slot()
    def run(self) -> bool:
        print("Haciendo correo"+self.actividad)
        #email_sender = "deguevarab@hotmail.com"
        #password = "ddwyncojorpcgyye"
        email_sender = "deguevarab@gmail.com"
        password = "sfsarwklbezopqct"
        
        email_receivers = ["deguevarab@gmail.com", "deguevarab@outlook.com"]

        subject = "Solicitud de permisos " + self.namePermiso.upper() + " || RBS " + self.nameRBS.upper() + " || " + self.actividad
        text = "Estimado ingeniero @"+self.nameOym+"\n\nPor favor su gentil ayuda con la gestión de los permisos "+self.namePermiso.upper()+" para la RBS "+self.nameRBS.upper()+". Se adjunta el formato en el correo.\n\n Gracias por la atención recibida."
        mensaje = MIMEMultipart()
        mensaje['From'] = email_sender
        mensaje['To'] = ", ".join(email_receivers)
        mensaje['Subject'] = subject

        mensaje.attach(MIMEText(text, 'plain'))
        archivo_adjunto = open(self.pathPermisos+self.nameOutputFile, 'rb')
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        adjunto_MIME.set_payload((archivo_adjunto).read())
        encoders.encode_base64(adjunto_MIME)
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % self.pathPermisos+self.nameOutputFile)
        mensaje.attach(adjunto_MIME)
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        #sesion_smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
        #sesion_smtp = smtplib.SMTP('outlook.office365.com', 587)
        sesion_smtp.ehlo()
        sesion_smtp.starttls()
        sesion_smtp.login(email_sender,password)
        texto = mensaje.as_string()
        sesion_smtp.sendmail(email_sender, email_receivers, texto)
        sesion_smtp.quit()
        self.signal.mem_signal.emit(1)
        print("Correo enviado")

        return True
    
class mainWindow(QtWidgets.QMainWindow, windowSolicitudFormatos_ui.Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pb_exit.clicked.connect(self.closeWindow)
        self.pb_minimized.clicked.connect(self.minimizeWindow)
        self.pb_Activacion.clicked.connect(self.solicitarActivacion)
        self.setDisableData()
        self.loadRBSs()
        self.cb_RBS.currentIndexChanged.connect(self.loadAllData)
        self.cb_Cuadrillas.currentIndexChanged.connect(self.changeTableCuadrilla)
        #self.cb_OyMs.setMinimumWidth(300)
        #self.cb_Supervisores.setMinimumWidth(300)
        #self.table_TecnicosCuadrilla.setEnabled(False)
    def changeTableCuadrilla(self):
        nameCuadrillas = self.cb_Cuadrillas.currentText()
        if nameCuadrillas == "CUE02":
            RBS = getDatosRBS("REPNARANCAY")
        else:
            RBS = getDatosRBS("MILAGROUNI")
        self.loadTableCuadrilla(RBS)
    def setDisableData(self):
        self.cb_RBS.setCurrentIndex(0)
        self.cb_Formato.addItem("")
        self.cb_Formato.setCurrentIndex(-1)
        self.cb_OyMs.addItem("")
        self.cb_OyMs.setCurrentIndex(-1)
        self.cb_Supervisores.addItem("")
        self.cb_Supervisores.setCurrentIndex(-1)
        self.cb_Cuadrillas.addItem("")
        self.cb_Cuadrillas.setCurrentIndex(-1)
        self.txt_FechaDesde.setText("")
        self.txt_FechaHasta.setText("")
        self.txt_Alarma.setText("")
        self.table_TecnicosCuadrilla.setRowCount(0)
        self.cb_RBS.setEnabled(True)
        self.cb_Formato.setEnabled(False)
        self.cb_OyMs.setEnabled(False)
        self.cb_Supervisores.setEnabled(False)
        self.cb_Cuadrillas.setEnabled(False)
        self.txt_FechaDesde.setEnabled(False)
        self.txt_FechaHasta.setEnabled(False)
        self.txt_Alarma.setEnabled(False)
    def loadRBSs(self):
        self.adjustCuadrillaTable()
        nameRBSs = ["", "REPNARANCAY", "MILAGROUNI"]
        for i in range(len(nameRBSs)):
            if i != 0:
                self.cb_RBS.addItem(QtGui.QIcon("QT_Resources/featherIcons/briefcase.svg"), nameRBSs[i])
            else:
                self.cb_RBS.addItem(nameRBSs[i])
    def adjustCuadrillaTable(self):
        self.table_TecnicosCuadrilla.setColumnWidth(0, 200)
        self.table_TecnicosCuadrilla.setColumnWidth(1, 90)
        self.table_TecnicosCuadrilla.setColumnWidth(2, 90)
        self.table_TecnicosCuadrilla.setColumnWidth(3, 200)
        #self.table_TecnicosCuadrilla.setRowCount(1)
        #self.table_TecnicosCuadrilla.setItem(0, 0, QtWidgets.QTableWidgetItem("Diego Esteban Guevara Bustillos"))
        #self.table_TecnicosCuadrilla.setItem(0, 1, QtWidgets.QTableWidgetItem("0983281925"))
        #self.table_TecnicosCuadrilla.setItem(0, 2, QtWidgets.QTableWidgetItem("1725248775"))
        #self.table_TecnicosCuadrilla.setItem(0, 3, QtWidgets.QTableWidgetItem("deguevarab@hotmail.com"))
    def loadAllData(self):
        if self.cb_RBS.currentText() == "":
            self.setDisableData()
        else:
            self.loadFormatos()
            RBS = getDatosRBS(self.cb_RBS.currentText())
            self.loadcbOyM(RBS)
            self.loadcbSupervisores(RBS)
            self.loadcbCuadrillas(RBS)
            self.loadFechas()
            self.txt_Alarma.setEnabled(True)
            self.loadTableCuadrilla(RBS)
    def loadTableCuadrilla(self, RBS:dict):
        self.table_TecnicosCuadrilla.setEnabled(True)
        nameTecnicos = RBS["Technicians"]
        telephoneTechnicians = RBS["TelephoneTechnicians"]
        ccTechnicians = RBS["CCTechnicians"]
        self.table_TecnicosCuadrilla.setRowCount(len(nameTecnicos)+1)
        
        self.table_TecnicosCuadrilla.setItem(0, 0, QtWidgets.QTableWidgetItem(RBS["TeamLeader"]))
        self.table_TecnicosCuadrilla.setItem(0, 1, QtWidgets.QTableWidgetItem(RBS["TelephoneTeamLeader"]))
        self.table_TecnicosCuadrilla.setItem(0, 2, QtWidgets.QTableWidgetItem(RBS["CCTeamLeader"]))
        self.table_TecnicosCuadrilla.setItem(0, 3, QtWidgets.QTableWidgetItem("example@rhelec.ec"))
        for i in range(len(nameTecnicos)):
            self.table_TecnicosCuadrilla.setItem(i+1, 0, QtWidgets.QTableWidgetItem(nameTecnicos[i]))
            self.table_TecnicosCuadrilla.setItem(i+1, 1, QtWidgets.QTableWidgetItem(telephoneTechnicians[i]))
            self.table_TecnicosCuadrilla.setItem(i+1, 2, QtWidgets.QTableWidgetItem(ccTechnicians[i]))
            self.table_TecnicosCuadrilla.setItem(i+1, 3, QtWidgets.QTableWidgetItem("example@rhelec.ec"))
        pass
    def loadcbOyM(self, RBS:dict):
        self.cb_OyMs.clear()
        self.cb_OyMs.setEnabled(True)
        nameOyMs = [RBS["OyMOwner"], "Pablo Yanez"]
        for i in nameOyMs:
            self.cb_OyMs.addItem(QtGui.QIcon("QT_Resources/featherIcons/user.svg"), i)
    def loadcbSupervisores(self, RBS:dict):
        self.cb_Supervisores.clear()
        self.cb_Supervisores.setEnabled(True)
        nameSupervisores = [RBS["Supervisor"]]
        for i in nameSupervisores:
            self.cb_Supervisores.addItem(QtGui.QIcon("QT_Resources/featherIcons/user.svg"), i)
    def loadcbCuadrillas(self, RBS:dict):
        self.cb_Cuadrillas.clear()
        self.cb_Cuadrillas.setEnabled(True)
        if RBS["nameRBS"] == "REPNARANCAY":
            nameCuadrillas = ["CUE02", "GYE02"]
        else:
            nameCuadrillas = ["GYE02", "CUE02"]
        for i in nameCuadrillas:
            self.cb_Cuadrillas.addItem(QtGui.QIcon("QT_Resources/featherIcons/users.svg"), i)
    def loadFechas(self):
        self.txt_FechaDesde.setEnabled(True)
        self.txt_FechaHasta.setEnabled(True)
        fechaDesde = str(date.today())
        fechaHasta = str(date.today()+ timedelta(days=4))

        self.txt_FechaDesde.setText(fechaDesde)
        self.txt_FechaHasta.setText(fechaHasta)
    def loadFormatos(self):
        self.cb_Formato.clear()
        self.cb_Formato.setEnabled(True)
        nameRBSs = ["FINANCIEROS", "SBA"]
        for i in range(len(nameRBSs)):
            self.cb_Formato.addItem(QtGui.QIcon("QT_Resources/featherIcons/file.svg"), nameRBSs[i])
    def closeWindow(self):
        self.close()
    def minimizeWindow(self):
        pass
    def solicitarActivacion(self):
        if self.txt_Alarma.text() == "":
            self.pb_Activacion.setEnabled(True)
        else:
            [pathPermisos, nameOutputFile] = createPermisos(self.cb_RBS.currentText(), self.cb_Formato.currentText(), self.txt_Alarma.text(), self.txt_FechaDesde.text(), self.txt_FechaHasta.text(), self.cb_OyMs.currentText(), self.cb_Cuadrillas.currentText())
            
            self.threadpool = QtCore.QThreadPool()
            self.worker = Worker(self.cb_RBS.currentText(), self.cb_OyMs.currentText(), self.cb_Formato.currentText(), self.txt_Alarma.text(), pathPermisos, nameOutputFile)
            self.worker.signal.mem_signal.connect(self.test)
            self.threadpool.start(self.worker)
            #self.finished.connect(self.test)
            
            #sendEmail(self.cb_RBS.currentText(), self.cb_OyMs.currentText(), self.cb_Formato.currentText(), self.txt_Alarma.text(), pathPermisos, nameOutputFile)
            self.setDisableData()
    def test(self):
        print("hola")
    def mouseMoveEvent(self, event):
        delta = QtCore.QPoint(event.globalPosition().toPoint() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPosition().toPoint()
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPosition().toPoint()

class Video_Logo_Window(QtWidgets.QMainWindow, VideoLogoWindow_ui.Ui_Video_Logo_Window):
    def __init__(self):
        super(Video_Logo_Window, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(qtc.Qt.WA_TranslucentBackground)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setSource("ResourcesFolder/Logo_Rhelec/Logo_Rhelec.mp4")
        self.player.setVideoOutput(self.VideoPlace)
        self.VideoPlace.show()
        self.player.play()
        self.player.playbackStateChanged.connect(self.paroVideo)
    def paroVideo(self):
        if self.player.isPlaying():
            pass
        else:
            self.close()
            self.w = mainWindow()
            self.w.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    window = Video_Logo_Window()
    window.show()
    app.exec()
    
    
    
    #nameRBS = "REPNARANCAY"
    #RBS = "MILAGROUNI"
    #namePermiso = "financieros"
    #nameFormato = "SBA"
    #actividad = "Caida de RBS y sector U LTE"
    #FechaDesde = "2024/09/25"
    #FechaHasta = "2024/09/27"
    #OyMReceiver = "Fernando Almeida"
    #OyMReceiver = "Henry Ramos"
    #cuadrilla = "CUE02"
    #cuadrilla = "GYE02"
    #[pathPermisos, nameOutputFile] = createPermisos(nameRBS, nameFormato, actividad, FechaDesde, FechaHasta, OyMReceiver, cuadrilla)
    
    #sendEmail(nameRBS, OyMReceiver, nameFormato, actividad, pathPermisos, nameOutputFile)