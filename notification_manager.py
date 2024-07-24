from twilio.rest import Client
from data_manager import DataManager

account_sid = 'FROM YOUR OWN ACCOUNT'
auth_token = 'FROM YOUR OWN ACCOUNT'

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def sent_sms(self, msg_content):

        message = self.client.messages.create(
            body=msg_content,
            from_="FROM YOUR OWN ACCOUNT",
            to="YOUR OWN NUMBER"
        )
        print(message)


