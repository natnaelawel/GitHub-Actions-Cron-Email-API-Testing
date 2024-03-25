import smtplib
import ssl
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def send_email():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    USERNAME = os.getenv("USER_EMAIL")
    PASSWORD = os.getenv("USER_PASSWORD")

    message = """\
    Subject: Hi there
    
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, USERNAME, message)


send_email()
