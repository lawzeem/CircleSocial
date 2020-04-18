from .views import showFeed, MakePostView
from django.urls import path

urlpatterns = [
    path('', showFeed, name='showFeed'),
    path('add', MakePostView, name='makePost'),
]