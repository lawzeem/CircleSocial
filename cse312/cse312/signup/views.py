from django.shortcuts import render

# Create your views here.
def showSignup(request):
    return render(request, 'signup/signup.html');