from django.db.models.signals import post_save
from django.dispatch import receiver
from Users.models import CustomUser


@receiver(post_save, sender=CustomUser)
def send_new_user_notification(sender, instance, created, **kwargs):
    if created:
        print(f"{instance}  {instance.first_name} {instance.last_name} is created successfully.")
