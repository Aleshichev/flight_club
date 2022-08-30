import smtplib

from twilio.rest import Client
import os

TWILIO_SID = os.environ.get('OWM_TWILIO_SID')
TWILIO_AUTH_TOKEN = os.environ.get('OWM_TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.environ.get('OWM_TWILIO_VIRTUAL_NUMBER')
MY_EMAIL = os.environ.get('OWM_MY_EMAIL')
PASSWORD = os.environ.get('OWM_PASSWORD')


class NotificationManager:
    """This class is responsible for sending sms."""
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, phone, message):
        """Send sms if price low. Only my phone works!!!"""
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=phone,
        )
        return print(f"Check your mobile phone")

    def send_emails(self, email, message):
        """Send email if price low."""
        with smtplib.SMTP("outlook.office365.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
            )
        return print(f"Check your email: {email}")
