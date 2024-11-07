import imaplib
import email
import smtplib
from time import sleep


username = 'deguevarab@gmail.com'
password = 'sfsarwklbezopqct'


imap_server = imaplib.IMAP4_SSL('smtp.gmail.com')
imap_server.login(username, password)

imap_server.select('INBOX')

result, data = imap_server.search(None, '(FROM "deguevarab@gmail.com" Subject "Solicitud de permisos FINANCIEROS || RBS REPNARANCAY || Alarma")')
email_ids = data[0].split()

result, data = imap_server.fetch(email_ids[0], "(RFC822)")

#print(result)
a = data[0][1].split()
for i in a:
    pass
    #print(i)

raw_email = data[0][1]
email_message = email.message_from_bytes(raw_email)




reply = email.message.EmailMessage()
reply['To'] = email_message['From']
reply['Subject'] = "RE:" + email_message['Subject']
reply["In_Reply-To"] = email_message["Message-Id"]
reply["References"] = (email_message["References"] or "") + " " + email_message["Message-Id"]


server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)

server.sendmail(username, reply["In_Reply-To"], 'Subject: Criteria not met\n\Thank you.')
server.sendmail(username, reply["FROM"], reply)
print('Sending email')
server.quit()


imap_server.close()