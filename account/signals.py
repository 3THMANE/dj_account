from django.db.models.signals import post_save, post_delete

from django.contrib.auth.models import User
from .models import Profile


def createprofile(sender, instance, created, **kwargs):
    
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            first_name = user.first_name,
            last_name = user.last_name,
            username =user.username,
            email = user.email,

        )

def updateprofile(sender, instance, created, **kwargs):
    
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteuser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass



post_save.connect(createprofile, sender=User)
post_save.connect(updateprofile, sender=Profile)
post_delete.connect(deleteuser, sender=Profile)

