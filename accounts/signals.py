import requests
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings

def send_telegram_message(message):
    try:
        url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            'chat_id': settings.TELEGRAM_CHAT_ID,
            'text': message,
            'parse_mode': 'HTML'
        }
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram error: {e}")

@receiver(post_save, sender=User)
def send_admin_alert_on_signup(sender, instance, created, **kwargs):
    if created:
        message = f"🔔 <b>New User Sign-Up!</b>\n\nUsername: {instance.username}\nEmail: {instance.email or 'Not provided'}"
        send_telegram_message(message)
        print(f"Signal triggered for {instance.username}")  # Add this line