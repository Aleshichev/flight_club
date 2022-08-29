from twilio.rest import Client
import os

TWILIO_SID = os.environ.get('OWM_TWILIO_SID')
TWILIO_AUTH_TOKEN = os.environ.get('OWM_TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.environ.get('OWM_TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = os.environ.get('OWM_TWILIO_VERIFIED_NUMBER')


class NotificationManager:
    """This class is responsible for sending sms."""
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """Send sms if price low"""
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
