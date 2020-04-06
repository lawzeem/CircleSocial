from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm
from .models import Profile

@login_required
def showProfile(request):
    user = request.user
    return render(request, 'profile/profile.html', {'user':user});

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
