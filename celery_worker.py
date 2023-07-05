import click
import africastalking 

from celery import Celery

app = Celery('sms', include=['sms'])
app.config_from_object('celconfigery')

@click.command()
def celery_worker():
    app.start()
    
if __name__ == '__main__':
    celery_worker()
