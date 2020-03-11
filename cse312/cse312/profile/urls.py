from .views import showProfile
from django.urls import path

urlpatterns = [
    path('', showProfile, name='showProfile'),
]
