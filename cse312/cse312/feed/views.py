from django.shortcuts import render

# Create your views here.
def showFeed(request):
    return render(request, 'feed/feed.html');