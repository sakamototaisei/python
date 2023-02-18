"""Eメール送信 Hotmail版"""
from email import message
from email.mime import multipart
from email.mime import text
import smtplib

smtp_host = 'smtp.live.com'
smtp_port = 587
# 送り主
from_email = 'xxx@hotmail.com'
# 送り先
to_email = 'xxx@hotmail.com'
# 送り主
username = 'xxx@hotmail.com'
# ログインパスワード
password = 'hgoahg@oa'

# msg = message.EmailMessage()
# 添付ファイル版
msg = multipart.MIMEMultipart()

# 本文
# msg.set_content('Test Email')
# タイトル
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email
msg.attach(text.MIMEText('Test email', 'plain'))

# 添付ファイルを付け加える
with open('apply_119.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment',
        filename='apply_119.txt'
    )
    msg.attach(attachment)


# 上記の内容をサーバーに送る
server = smtplib.SMTP(smtp_host, smtp_port)
# 初めにサーバーと通信するために必要 ehlo()
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
# ここでメッセージを伝える send_message()
server.send_message(msg)
# 最後にサーバーとの通信を終了する quit()
server.quit()