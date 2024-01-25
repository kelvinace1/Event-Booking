# signals.py
from django.db.models.signals import post_save
from allauth.account.signals import user_signed_up
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Account, Event
from django.utils import timezone

@receiver(user_signed_up)
def create_user_account(sender, request, user, **kwargs):
    Account.objects.create(account=user, balance = 0.0)

"""@receiver(post_save, sender=Event)
def send_event_notification(sender, instance, created, **kwargs):
    if created:
        # The event is created for the first time

        message = f"New event '{instance.title}' added on {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}."
        users = User.objects.all()
        for user in users:
            Notification.objects.create(user=user, message=message) """
        