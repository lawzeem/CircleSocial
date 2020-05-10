from django.db import models
from cse312.users.models import User
from django.db.models.signals import post_save
from PIL import Image
from cse312.notifications.models import Notifications

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='profile/default.jpg', upload_to='profile')
    bio = models.CharField('bio', max_length=80)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def get_notification_count(self):
        notifications = Notifications.objects.filter(user=self.user)
        return notifications.count()

def create_profile(sender, **kwargs):
    if kwargs['created']:
        profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
