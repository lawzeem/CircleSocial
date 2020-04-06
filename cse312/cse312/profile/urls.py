from .views import showProfile, EditProfileView
from django.urls import path

urlpatterns = [
    path('', showProfile, name='showProfile'),
    path('edit', EditProfileView, name='editProfile'),
]