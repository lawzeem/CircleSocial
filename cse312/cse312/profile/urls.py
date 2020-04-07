from .views import showProfile, EditProfileView, GetProfile
from django.urls import path

urlpatterns = [
    path('', showProfile, name='showProfile'),
    path('edit', EditProfileView, name='editProfile'),
    path('user/<slug:username>', GetProfile, name='getProfile'),
]