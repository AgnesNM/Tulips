import africastalking

class SMS:
    def __init__(self):
        self.username = "orchid"
        self.api_key = "6308e6ddc6ce92f958392693e6ebe7223b218bc2b50974337d31688b97774977"

    def send(self):
        recipients = ["+254712227589"]
        message = "Hello, Please remember to pay your Helb loan before the end of the day. Paybill: 200800. Avoid aibu ndogo ndogo" print("\U0001F605")

        #initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        #get the SMS service
        sms = africastalking.SMS

    
        try:
            response = sms.send(message, recipients)
            print(response)
        except Exception as e:
            print("oops, the message was not sent")
            print(e)
            
SMS().send()
