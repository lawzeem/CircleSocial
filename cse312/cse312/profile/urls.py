from .views import showProfile, EditProfileView, GetProfile, SearchProfile
from django.urls import path

urlpatterns = [
    path('', showProfile, name='showProfile'),
    path('search', SearchProfile, name='searchProfile'),
    path('edit', EditProfileView, name='editProfile'),
    path('user/<slug:username>', GetProfile, name='getProfile'),
]