from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_admin_alert_on_signup(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'New User Sign-Up!',
            f'A new user, {instance.username}, just signed up!',
            'your-email@gmail.com',
            ['your-email@gmail.com'],
            fail_silently=False,
        )