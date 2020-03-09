from .views import showLogin
from django.urls import path

urlpatterns = [
    path('', showLogin, name='showLogin'),
]