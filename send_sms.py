import os
from flask import Flask, request
from send_sms import send_sms

app = Flask(__name__)

# TODO: create incoming messages route

# TODO: create delivery reports route.

#TODO: Initialize the SDK
username = 'orchid'
api_key = 'd354a71adee83ba94a9cb40d6c2f9159a02331d2dbbb95bc8053144b98900a3e'
africastalking.initialize(username, api_key)

if __name__ == "__main__":
    #TODO: Call send message function
    def sending(self):
            # Set the numbers in international format
            recipients = ["+254704469422"]
            # Set your message
            message = "Hey AT Ninja! Good luck today";
            # Set your shortCode or senderId
            sender = "XXYYZZ"
            try:
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Houston, we have a problem: {e}')
    

    app.run(debug=True, port = os.environ.get("PORT"))

#TODO: Call SMS method
send_sms().sending()