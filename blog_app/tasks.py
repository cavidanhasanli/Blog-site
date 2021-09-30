from __future__ import absolute_import, unicode_literals
from django.core.mail import EmailMultiAlternatives
from blog_project.settings import EMAIL_HOST_USER


def send_team_task(to_mail, link):
    subject, from_email, to = 'TexnoEraAcademy', EMAIL_HOST_USER, to_mail
    text_content = 'Click for Verify account'
    link='https://friendofthesea.org/wp-content/uploads/the-test-fun-for-friends-screenshot.png'
    html_content = f'<img src={link}>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()