from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm
from .models import Profile
from cse312.users.models import User
from cse312.feed.models import Post
from cse312.friends.models import Friend
from django.http import Http404
from django.db.models import Q

@login_required
def showProfile(request):
    user = request.user
    posts = Post.objects.filter(user=user).order_by('-id')
    return render(request, 'profile/profile.html', {'user':user, 'posts':posts});

@login_required
def EditProfileView(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('showProfile')
    else:
        user = request.user
        form = ProfileEditForm(instance = request.user.profile)
        args = {'form':form, 'user':user}
        return render(request, 'profile/edit.html', args)

@login_required
def GetProfile(request, username):
    try:
        user = User.objects.get(user_name=username)
        # print("Found User")
        profile = Profile.objects.get(user=user)

        # Use in postgres
        # friends = Friend.objects.filter(current_user=request.user)[0].user.all()
        # Use in sqlite
        friends = Friend.objects.filter(current_user=request.user)

        posts = Post.objects.filter(user=user).order_by('-id')

        if user in friends:
            friends = True
        else:
            friends = False

        args = {'profile':profile, 'friends':friends, 'posts':posts}

    except:
        raise Http404
    return render(request, 'profile/view.html', args)

def SearchProfile(request):
    query = request.GET.get('q')
    if query:
        results = User.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(user_name__icontains=query))
    else:
        results = User.objects.all()
    args = {'users':results}
    return render(request, 'profile/search.html', args)
