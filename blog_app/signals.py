from django.db.models.signals import post_save
from django.dispatch import receiver
from blog_app.tasks import send_team_task
from threading import Thread

print('SIGNAL FOR Team VERIFY')


# @receiver(post_save, sender=TokenModelTeam)
def user_verify(instance, created, **kwargs):
    if created:
        link = 'salam'
        print(instance.user.email)
        background = Thread(target=send_team_task, args=(instance.user.email, link))
        background.start()