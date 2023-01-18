import smtplib, ssl

HOST = "smtp.gmail.com"
PORT = 465


user_name = "Akhmedka1993@gmail.com"
password = "pmdzeyqlyxwtpehr"


recipient = "kodi199312@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Testing Python Script
Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
    server.login(user_name, password)
    server.sendmail(user_name, recipient, message)