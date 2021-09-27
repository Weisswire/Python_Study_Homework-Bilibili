import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg1 = "This is an E-mail."
msg2 = '''
<!DOCTYPE html>
<html>
	<head>
    <h1>...</h1>
    </head>
    <body>
    ...
    </body>
</html>
'''
def send_text(msg:str):
    smtp_obj = smtplib.SMTP("smtp.qq.com")
    smtp_obj.login("username@qq.com","password")
    msg_body = MIMEText(msg,'plain','utf-8')
    msg_body['Subject'] = Header("...",'utf-8')
    msg_body['From'] = Header("...",'utf-8')
    smtp_obj.sendmail('sender@qq.com',['receiver1@qq.com','receiver2@qq.com',],msg_body.as_string())

def send_html(msg:str):
    smtp_obj = smtplib.SMTP("smtp.qq.com")
    smtp_obj.login("username@qq.com","password")
    msg_body = MIMEText(msg,'html','utf-8')
    msg_body['Subject'] = Header("...",'utf-8')
    msg_body['From'] = Header("...",'utf-8')
    smtp_obj.sendmail('sender@qq.com',['receiver1@qq.com','receiver2@qq.com',],msg_body.as_string())

if __name__ == "__main__":
    send_text(msg1)
    send_html(msg2)