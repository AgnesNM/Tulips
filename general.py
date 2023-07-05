# monthly remider
from celery import Celery
from datetime import timedelta

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def send_reminder():
    # Code to send reminder goes here
    app.conf.beat_schedule = {
    'send-every-30-days': {
        'task': 'tasks.send_reminder',
        'schedule': timedelta(days=30),
    },
}


#make payments
from mpesa_sdk import Mpesa

mpesa = Mpesa(client_key='your_client_key', client_secret='your_client_secret')

def make_payment(amount, phone_number):
    response = mpesa.stk_push(amount, phone_number, 'Account', 'Payment for HELB loan and NHIF')
    return response

#combine the two
# call the make_payment function in the send_reminder task. 
# This way, every time the reminder is sent, the payment is also made.

@app.task
def send_reminder():
    # Code to send reminder goes here
    make_payment(amount, phone_number)
