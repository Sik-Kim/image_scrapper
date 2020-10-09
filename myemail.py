import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


# 보내는 사람 정보
me = "summering6@gmail.com"
my_password = "2064872as!"

# 로그인하기
s = smtplib.SMTP_SSL("smtp.gmail.com")
s.login(me, my_password)

# 받는 사람 정보
emails = ["salvame21@naver.com", "salvame21@naver.com"]


for you in emails:
    # 메일 기본 정보 설정
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "[공유] 추석기사"
    msg["From"] = me
    msg["To"] = you

    # 메일 내용 쓰기
    content = "캬캬캿"
    part2 = MIMEText(content, "plain")
    msg.attach(part2)

    part = MIMEBase("application", "octet-stream")
    with open("articles.xlsx", "rb") as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment", filename="추석기사.xlsx")
    msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())  # sendmail에 필요한 변수들 어떤 것들 있는지 이해하기
s.quit()