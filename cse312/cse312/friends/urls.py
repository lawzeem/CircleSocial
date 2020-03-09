from .views import showFriends
from django.urls import path

urlpatterns = [
    path('', showFriends, name='showFriends'),
]