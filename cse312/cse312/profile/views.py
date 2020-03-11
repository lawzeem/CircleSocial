from django.shortcuts import render

# Create your views here.
def showProfile(request):
    return render(request, 'profile/profile.html');
