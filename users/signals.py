from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name)
        profile.save()
post_save.connect(CreateProfile, sender=User)