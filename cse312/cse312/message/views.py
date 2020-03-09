from django.shortcuts import render

# Create your views here.
def showMessage(request):
    return render(request, 'message/message.html');