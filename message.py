from celery_worker import app


import africastalking

class SMS:
    def __init__(self):
        self.username = "orchid"
        self.api_key = "923b297056fbad50af34924a530f9426038147d90514e215d3c469af8e43aa0a"

    def send(self):
        recipients = ["+254712227"]
        message = "Hello, this is Grace"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        sms = africastalking.SMS

        try:
            response = sms.send(message, recipients)
            print(response)
        except Exception as e:
            print("Oops, the message was not sent")
            print(e)

@app.task()
def send_sms():
    SMS().send()

# Run the task immediatelysend

if __name__ == '__main__':
    send_sms.delay()
