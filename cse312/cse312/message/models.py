from django.db import models
from cse312.users.models import User
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    messagetxt = models.CharField('messagetxt', max_length=2000)
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name=('sender'))
    reciever = models.ForeignKey(User, on_delete = models.CASCADE, related_name=('reciever'))
    timestamp = models.DateTimeField('timestamp',default=timezone.now)
