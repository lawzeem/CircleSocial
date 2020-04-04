from django.shortcuts import render

# Create your views here.
def showLogin(request):
    return render(request, 'login/login.html');