from __future__ import print_function

import africastalking

class SMS:
    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

        africastalking.initialize(username, api_key)
        self.sms = africastalking.SMS
    
    def send(self, recepients_message, message_receiver, sender = None):
        recepients = message_receiver
        message = recepients_message

        try:
            response = self.sms.send(message, recepients, sender)
            print(response)
        except Exception as e:
            print(f"Houston, we have a problem: {e}")