from django.db import models
from cse312.users.models import User
from cse312.message.models import ChatMessage

class Notifications(models.Model):
    user = models.ForeignKey(User, related_name="main_user", null=True, on_delete=models.CASCADE)
    message = models.ManyToManyField(ChatMessage)

    @classmethod
    def add(cls, user, message):
        notifications, created = cls.objects.get_or_create(
            user = user
        )
        notifications.user.remove(message)

    @classmethod
    def remove(cls, message):
        notifications, created = cls.objects.get_or_create(
            user = user
        )
        notifications.user.remove(message)


    def get_message(self):
        return self.message.all()[0]