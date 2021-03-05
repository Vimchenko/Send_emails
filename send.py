import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# настройка ключевых переменных: содержание текста, отправитель (мы)
sender_email = 'your.email@gmail.com'
sender_password = 'yourPassword'
subject = 'MESSAGE!'
body = 'How are you?'
# получатель
target_email = 'target.email@gmail.com'
#  email Head: отправитель, получатель, объект
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = target_email
msg['Subject'] = subject
msg.add_header('reply-to', sender_email)
msg.attach(MIMEText(body))
# сессия для отправки почтой
mail_sender = smtplib.SMTP('smtp.gmail.com', 587)
mail_sender.starttls()
mail_sender.login(sender_email, sender_password)
mail_sender.sendmail(sender_email, target_email, msg.as_string())
mail_sender.quit()
# уведомить нас об успешной отправке
print('OK!')


''' ПРИМЕЧАНИЕ: 
для корректной работы авторизации через библиотеку smtplib, 
вам нужно разрешить непроверенным сообщениям доступ к почте. Ссылка: 
https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PuXAqdqYZaj1mOzVvrWNSDXDt5yfqFdwWHBvERSOkK0L67GLNj8JOlDwAJFSOkxwYQ9MLy3u0TTMG8UUq-Ifdck7-N1A '''