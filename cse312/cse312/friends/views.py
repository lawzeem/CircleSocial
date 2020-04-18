from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cse312.users.models import User
from cse312.profile.models import Profile
from .models import Friend
from django.http import Http404, HttpResponseRedirect

def showFriends(request):
    friends = Friend.objects.filter(current_user=request.user)
    try:
        friend = friends[0].user.all()
    except:
        friend = ""
    return render(request, 'friends/friends.html', {'friends':friend});

@login_required
def editFriends(request, username, operation):
    owner = request.user
    new_friend = User.objects.get(user_name=username)
    # new_friend = new_friend[0]
    profile = Profile.objects.filter(user=new_friend)
    if operation == "follow":
        Friend.follow(owner, new_friend)
    elif operation == "unfollow":
        Friend.unfollow(owner, new_friend)
    else:
        raise Http404
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
