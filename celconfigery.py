from datetime import timedelta

# Celery configuration
broker_url = 'localhost'
result_backend = 'localhost'
timezone = 'UTC'

# Schedule configuration
beat_schedule = {
    'send_sms_at_end_of_month': {
        'task': 'sms.send',
        'schedule': timedelta(days=1),  # Run the task every day
        'args': (),
    },
}
