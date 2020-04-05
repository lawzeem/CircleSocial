from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import ProfileEditForm
from .models import Profile

def showProfile(request):
    user = request.user
    return render(request, 'profile/profile.html', {'user':user});

def editProfile(request):
    user = request.user
    return render(request, 'profile/edit.html', {'user' : user});

def EditProfileView(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('showProfile')
    else:
        # profile = Profile.objects.get(user=request.user.profile)
        form = ProfileEditForm(instance = request.user.profile)
        args = {'form':form}
        return render(request, 'profile/edit.html', args)
