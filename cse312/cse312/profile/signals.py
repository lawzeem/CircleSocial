from django.db.models.signals import post_save
from cse312.users.models import User
from cse312.profile.models import Profile
from django.dispatch import receiver

def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile, sender=User)
