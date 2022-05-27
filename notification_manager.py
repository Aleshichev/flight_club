from twilio.rest import Client

TWILIO_SID = "AC80549d7af691ed52c46420ba5ba55778"
TWILIO_AUTH_TOKEN = "c69ff4dfb48a1db024f29484f8a29130"
TWILIO_VIRTUAL_NUMBER = "+19362377794"
TWILIO_VERIFIED_NUMBER = "+380989750736"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)