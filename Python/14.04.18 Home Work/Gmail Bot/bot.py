import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
fromaddr = "mr.roman.gray@gmail.com"
toaddr = "mr.roman.gray@gmail.com"
mypass = "Roman_Gray#1"
 
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от Романа"
 
body = "Это пробное сообщение"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
