from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cse312.users.models import User
from cse312.profile.models import Profile
from .models import Friend
from django.http import Http404, HttpResponseRedirect

def showFriends(request):
    friend = Friend.objects.get(current_user=request.user)
    friends = friend.user.all()
    return render(request, 'friends/friends.html', {'friends':friends});

@login_required
def editFriends(request, username, operation):
    owner = request.user
    new_friend = User.objects.get(user_name=username)
    profile = Profile.objects.get(user=new_friend)
    if operation == "follow":
        Friend.follow(owner, new_friend)
    elif operation == "unfollow":
        Friend.unfollow(owner, new_friend)
    else:
        raise Http404
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))