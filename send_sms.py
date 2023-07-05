import africastalking

class SMS:
    def __init__(self):
        self.username = "orchid"
        self.api_key = "6308e6ddc6ce92f958392693e6ebe7223b218bc2b50974337d31688b97774977"

    def send(self):
        recipients = ["+254712227589"]
        message = "Hello, this is Grace"

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
