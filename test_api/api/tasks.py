from celery import shared_task


@shared_task
def send_feedback_email(name, email, message, image_file=None):
    pass
