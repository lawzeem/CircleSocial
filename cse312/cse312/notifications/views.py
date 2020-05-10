from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cse312.users.models import User
from cse312.message.models import ChatMessage
from cse312.profile.models import Profile
from .models import Notifications
from django.http import Http404, HttpResponseRedirect


from django.contrib.sessions.models import Session
from django.utils import timezone


def get_all_logged_in_users():
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))
    return User.objects.filter(id__in=uid_list)


@login_required
def showNotifications(request):
    notifications = Notifications.objects.filter(user=request.user)
    print("---------------------------- notifications: ", notifications.count())
    if notifications.count() > 0:
        messages = list(notifications)
    else:
        messages = None
    return render(request, 'notifications/notifications.html', {'notifications':messages});


@login_required
def editNotifications(request, messageID, operation):
    owner = request.user
    message = ChatMessage.objects.get(id=messageID)
    if operation == "add":
        Notifications.add(owner, message.user, message)
    elif operation == "remove":
        Notifications.remove(owner, message.user, message)
    else:
        raise Http404
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
