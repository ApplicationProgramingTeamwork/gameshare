# games/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Gamer

@receiver(post_save, sender=User)
def create_gamer_profile(sender, instance, created, **kwargs):
    """Create a Gamer profile when a new User is created."""
    if created:
        Gamer.objects.get_or_create(owner=instance, username=instance.username)
