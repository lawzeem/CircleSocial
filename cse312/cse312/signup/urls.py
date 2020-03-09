from .views import showSignup
from django.urls import path

urlpatterns = [
    path('', showSignup, name='showSignup'),
]