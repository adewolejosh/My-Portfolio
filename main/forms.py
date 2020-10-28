from django import forms
from .models import Subscriber
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def sending_mail(email):
    subject = 'Thanks for Subscribing To My NewsLetter'
    message = render_to_string('main/submail.html')
    mail = EmailMessage(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email, 'adewole.josh.mydjangotestmail@gmail.com'],
    )
    mail.send()


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        fields = "__all__"
