from django.shortcuts import render

# Create your views here.
def showFriends(request):
    return render(request, 'friends/friends.html');