# from django.db import models
from cse312.users.models import User
# from django.utils import timezone

# # Create your models here.
# class Message(models.Model):
#     messagetxt = models.CharField('messagetxt', max_length=2000)
#     sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name=('sender'))
#     reciever = models.ForeignKey(User, on_delete = models.CASCADE, related_name=('reciever'))
#     timestamp = models.DateTimeField('timestamp',default=timezone.now)

from django.db import models

from django.conf import settings
from django.db import models
from django.db.models import Q
from cse312.message.utils import broadcast_msg_to_chat
from cse312.users.models import User

class ThreadManager(models.Manager):
    def by_user(self, user):
        qlookup = Q(first=user) | Q(second=user)
        qlookup2 = Q(first=user) & Q(second=user)
        qs = self.get_queryset().filter(qlookup).exclude(qlookup2).distinct()
        return qs

    # Returns the thread between user and other user
    def get_or_new(self, user, other_username):
        if user == other_username:
            return None
        thread = Thread.objects.filter((Q(first=user) & Q(second=other_username)) | (Q(first=other_username) & Q(second=user)))
        qs = thread.distinct()
        if qs.count() == 1:
            return qs.first(), False
        # elif qs.count() > 1:
        #     return qs.order_by('timestamp').first(), False
        else:
            if user != other_username:
                obj = self.model(
                        first=user,
                        second=other_username
                    )
                obj.save()
                return obj, True
        return None, False


class Thread(models.Model):
    first        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_thread_first')
    second       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_thread_second')
    updated      = models.DateTimeField(auto_now=True)
    # timestamp    = models.DateTimeField(auto_now_add=True)

    objects      = ThreadManager()

    @property
    def room_group_name(self):
        return 'message{self.id}'

    def broadcast(self, msg=None):
        if msg is not None:
            broadcast_msg_to_chat(msg, group_name=self.room_group_name, user='admin')
            return True
        return False


class ChatMessage(models.Model):
    thread      = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.SET_NULL)
    user        = models.ForeignKey(User, verbose_name='sender', on_delete=models.CASCADE)
    message     = models.TextField()
    # timestamp   = models.DateTimeField(auto_now_add=True)
