import smtplib, ssl
from dotenv import load_dotenv


def send_email():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    USERNAME = load_dotenv().get("USER_EMAIL")
    PASSWORD = load_dotenv().get("USER_PASSWORD")

    message = """\
    Subject: Hi there
    
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, USERNAME, message)
        
send_email()