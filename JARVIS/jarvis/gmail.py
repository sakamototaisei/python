import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate


# SMTPのオブジェクト作成。GmailのSMTPポートは587
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)

# メールサーバに対する応答
smtpobj.ehlo()
# 暗号化通信開始
smtpobj.starttls()
smtpobj.ehlo()
# ログイン
smtpobj.login("jarvis.tony.stark.pepper@gmail.com", "jarvistony")


# 送信元、送信先
mail_from = "jarvis.tony.stark.pepper@gmail.com"
mail_to = "taisei0403089@gmail.com"

# 本文
text = "これはテスト用のメールです"

# メッセージのオブジェクト
msg = MIMEText(text)
msg['Subject'] = "テスト送信"
msg['From'] = mail_from
msg['To'] = mail_to
msg['Date'] = formatdate(localtime=True)

# メール送信
smtpobj.sendmail(mail_from, mail_to, msg.as_string())
