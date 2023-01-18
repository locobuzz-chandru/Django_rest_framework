from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True)
def send_mail_func(self):
    mail_subject = 'Celery testing'
    message = 'Testing'
    to_email = settings.EMAIL_HOST_USER
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    return 'Done'
