import win32com.client
from time import sleep
from docx import Document
import pyperclip
from openpyxl import load_workbook
import csv
from pandas import read_excel

def create_outlook_email(recipient, subject, body):
    outlook = win32com.client.Dispatch("Outlook.Application")
    outlookNS = outlook.GetNameSpace("MAPI")
    mail = outlook.CreateItem(0)
    mail.To = recipient
    mail.Subject = subject
    mail.Body = body
    mail.bodyformat = 3
    mail.Attachments.Add("C:/Users/Diego/OneDrive/Proyectos/Gestion_Permisos_RHELEC/ignore/PERMISOS FINANCIEROS - MILAGROUNI.xlsx")
    mail.Attachments.Add("C:/Users/Diego/OneDrive/Proyectos/Gestion_Permisos_RHELEC/ignore/PERMISOS FINANCIEROS - IMBAMBATO.xlsx")
    mail.Display(False) # Opens the email window
    mail.Save()
    mail.Send()
def readMessages():
    outlook = win32com.client.Dispatch("Outlook.Application")
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    account = outlook.Folders("deguevarab@hotmail.com")

    # this is the main folder that is under your account like Inbox, Draft, sent items, Outbox, etc
    inbox = account.Folders['Inbox']
    #inbox = outlook.GetDefaultFolder(12)
    messages = inbox.Items
    for i in range(len(messages)):
        message = messages.Item(len(messages)-i-1)
        #message = messages.Item(i+1)
        body_content = message.body
        print(message)
        sleep(0.5)
def copyDoc():
    doc_path = "FORMATO SITIOS ETC.docx"
    #doc_path = "../Formatos/Formatos/FORMATO SITIOS ETC.docx"
    template_document = Document(doc_path)
    aux = ""
    for p in template_document.part:
        aux = aux+p.text
    pyperclip.copy(aux)
    
def create_CSV():
    excel = read_excel('C:/Users/Diego/OneDrive/Proyectos/Gestion_Permisos_RHELEC/data/Informacion_RBS_Cuadrillas.xlsx', encoding="utf-8")
    
    

if __name__ == "__main__":
    create_CSV()
    #copyDoc()
    #readMessages()
    #recipient = "deguevarab@gmail.com"
    #subject = "Saludos22"
    #body = "Hola22"
    #create_outlook_email(recipient, subject, body)