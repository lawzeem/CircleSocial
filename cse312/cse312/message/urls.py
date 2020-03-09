from .views import showMessage
from django.urls import path

urlpatterns = [
    path('', showMessage, name='showMessage'),
]