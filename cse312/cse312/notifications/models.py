from django.db import models
from cse312.users.models import User
from cse312.message.models import ChatMessage

class Notifications(models.Model):
    user = models.ForeignKey(User, related_name="main_user", null=True, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name="sending_user", null=True, on_delete=models.CASCADE)
    message = models.ManyToManyField(ChatMessage)

    @classmethod
    def add(cls, user, sender, message):
        notifications, created = cls.objects.get_or_create(
            user = user,
            sender = sender
        )
        notifications.message.add(message)

    @classmethod
    def remove(cls, user, sender, message):
        notifications, created = cls.objects.get_or_create(
            user = user,
            sender = sender
        )
        notifications.delete()

    def get_count(self):
        return self.message.all().count()

    def get_message(self):
        if self.get_count() > 0:
            return self.message.all()[0]