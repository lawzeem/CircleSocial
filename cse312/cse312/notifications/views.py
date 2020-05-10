from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cse312.users.models import User
from cse312.message.models import ChatMessage
from cse312.profile.models import Profile
from .models import Notifications
from django.http import Http404, HttpResponseRedirect

def showNotifications(request):
    notifications = Notifications.objects.filter(user=request.user)
    print("------------ All Notifications: ", notifications)
    try:
        messages = notifications
    except:
        messages = ""
    return render(request, 'notifications/notifications.html', {'notifications':messages});

@login_required
def editNotifications(request, messageID, operation):
    owner = request.user
    message = ChatMessage.objects.get(id=messageID)
    if operation == "add":
        Notifications.add(owner, message)
    elif operation == "remove":
        Notifications.remove(owner, message)
    else:
        raise Http404
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
