import os
import smtplib  # For sending email
from os.path import basename  # To extract filename from path
from email.mime.application import MIMEApplication  # To attach files
from email.mime.multipart import MIMEMultipart  # To create email with attachments
from email.mime.text import MIMEText  # To add plain text content in email
from email.utils import COMMASPACE, formatdate  # To format email headers
from dotenv import load_dotenv

load_dotenv()

pwd = os.getenv("APP_PASSWORD")
sender = os.getenv("SENDER_ADDRESS")
receiver = os.getenv("RECEIVER_ADDRESS")

def send_email(send_from, send_to, subject, text, files=None):
    # Sends an email with the given subject, body, and optional attachments.

    assert isinstance(send_to, list)

    # Create a multipart email
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    # Attach plain text to the email
    msg.attach(MIMEText(text))

    # Attach files, if any
    for f in files or []:
        with open(f, "rb") as file:
            part = MIMEApplication(file.read(), Name=basename(f))
        part['Content-Disposition'] = f'attachment; filename="{basename(f)}"'
        msg.attach(part)

    # Setup SMTP connection and send email
    smtp = smtplib.SMTP('smtp.gmail.com: 587')
    smtp.starttls()  # Enable TLS
    smtp.login(send_from, pwd)  # Login using provided credentials
    smtp.sendmail(send_from, send_to, msg.as_string())  # Send the email
    smtp.close()  # Close the connection


if __name__ == "__main__":
    # Send the Excel file via email
    send_email(
        sender,
        [receiver],
        'Jobs Postings',
        'Hello This is an automated test mail.',
        files=[]
    )
