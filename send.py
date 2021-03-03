import smtplib
from email.mime.multipart import MIMEMultipart

# настройка ключевых переменных: содержание текста, отправитель (мы)
sender_mail = 'myMail@gmail.com'
sender_password = 'PASSWORD_EXAMPLE'
subject = 'MESSAGE!'
mail_body_text = 'What is up?'
# получатель
target_mail = 'hisherMail@gmail.com'

#  email Head: отправитель, получатель, объект
msg = MIMEMultipart('good')
msg['From'] = sender_mail
msg['To'] = target_mail
msg['Subject'] = subject
msg.add_header('reply-to', sender_mail)
# сессия для отправки почтой
mail_sender = smtplib.SMTP('smtp.gmail.com', 587)
mail_sender.starttls()
mail_sender.login(sender_mail, sender_password)
mail_sender.sendmail(sender_mail, target_mail, msg.as_string())
mail_sender.quit()
# уведомить нас об успешной отправке
print('OK!')


''' ПРИМЕЧАНИЕ: 
для корректной работы авторизации через библиотеку smtplib, 
вам нужно разрешить непроверенным сообщениям доступ к почте. Ссылка: 
https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PuXAqdqYZaj1mOzVvrWNSDXDt5yfqFdwWHBvERSOkK0L67GLNj8JOlDwAJFSOkxwYQ9MLy3u0TTMG8UUq-Ifdck7-N1A '''