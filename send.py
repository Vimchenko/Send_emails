from io import BytesIO

from reportlab.pdfgen import canvas
from django.http import HttpResponse
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

sender_mail = 'faefafae@umpa.com'
sender_password = 'qwerty'

target_mail = 'qwdqwdq@klukva.com'

subject = 'STEP'
msg = MIMEMultipart()
msg['From'] = sender_mail
msg['To'] = target_mail
msg.add_header('reply_to', sender_mail)

mailsender = smtplib.SMTP_SSL('smtp.gmail.com', 600)
#mailsender.starttls()
mailsender.login(sender_mail, sender_password)
mail_subject = 'Hi. How are You?'
mail_body_text = 'This is the End'
mail_body_html = '<html><head><body></body><a href="bonk.com"</a></head></html>'
msg = MIMEText(mail_body_html, 'html', 'utf-8')
msg['Subject'] = Header(mail_subject, 'utf-8')
mailsender.sendmail(sender_mail, target_mail, msg.as_string())
mailsender.quit()
