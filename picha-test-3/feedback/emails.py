from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.template import Context
from django.template.loader import render_to_string


def send_feedback_email(email, message):
    c = Context({'email': email, 'message': message})

    email_subject = render_to_string(
        'feedback/email/feedback_email_subject.txt', c).replace('\n', '')
    email_body = render_to_string('feedback/email/feedback_email_body.txt', c)

    email = EmailMessage(
        email_subject, email_body, settings.DEFAULT_FROM_EMAIL,
        [email], [],
        headers={'Reply-To': email}
    )
    # email1 = send_mail(
    #     email_subject,
    #     email_body,
    #     settings.DEFAULT_FROM_EMAIL,
    #     [email],
    #     fail_silently=False,
    # )
    return email.send(fail_silently=False)
    # return email1
