import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.163.com"  # 设置服务器
mail_user = "akylin4087@163.com"  # 用户名
mail_pass = "FUEALSQBEZCWLUMV"  # 口令

sender = 'akylin4087@163.com'
receivers = ['kylin4087@foxmail.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('<html><body><h1>Hello</h1>' +
                   '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
                   '</body></html>', 'html', 'utf-8')
message['From'] = "akylin4087@163.com"  # 发送者
message['To'] = "kylin4087@foxmail.com"  # 接收者

subject = '收掉信息了吗'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件", smtplib.SMTPException)
