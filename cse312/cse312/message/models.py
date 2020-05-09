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

    def get_or_new(self, user, other_username): # get_or_create
        print("-------------------------------- In Get or Create ------------------------")
        # username = user.get_user_name
        # other = User.objects.
        if user == other_username:
            return None
        # qlookup1 = Q(first__user_name__iexact=username) & Q(second__user_name__iexact=other_username)
        # qlookup2 = Q(first__user_name__iexact=other_username) & Q(second__user_name__iexact=username)
        thread = Thread.objects.filter((Q(first=user) & Q(second=other_username)) | (Q(first=other_username) & Q(second=user)))
        print("Threads foundL --------------------------------- : ", thread)
        qs = thread.distinct()
        if qs.count() == 1:
            return qs.first(), False
        elif qs.count() > 1:
            return qs.order_by('timestamp').first(), False
        else:
            # Klass = user.__class__
            # user2 = User.objects.get(user_name=username)
            if user != user_name:
                obj = self.model(
                        first=user,
                        second=user_name
                    )
                obj.save()
                return obj, True
        return None, False


class Thread(models.Model):
    first        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_thread_first')
    second       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_thread_second')
    updated      = models.DateTimeField(auto_now=True)
    timestamp    = models.DateTimeField(auto_now_add=True)

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
    timestamp   = models.DateTimeField(auto_now_add=True)
